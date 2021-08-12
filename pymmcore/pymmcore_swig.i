// SWIG interface file for MMCore Python bindings
//
// Copyright (C) 2006-2021 Regents of the University of California
//           (C) 2020-2021 Board of Regents of the University of Wisconsin
//                         System
//
// This library is free software; you can redistribute it and/or modify it
// under the terms of the GNU Lesser General Public License, version 2.1, as
// published by the Free Software Foundation.
//
// This library is distributed in the hope that it will be useful, but WITHOUT
// ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
// FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License
// for more details.
//
// You should have received a copy of the GNU Lesser General Public License
// along with this library; if not, write to the Free Software Foundation,
// Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
//
// Author:  Arthur Edelstein, arthuredelstein@gmail.com, 2009.08.11,
//          based on the Java wrapper code by
//          Nenad Amodaj, nenad@amodaj.com, 06/07/2005, and
//          Micro-Manager team and contributors.
//
// History: This file used to be part of the micro-manager source tree; then
//          part of the mmCoreAndDevices source tree. It was moved to this
//          source tree (pymmcore) after mmCoreAndDevices commit
//          5fbfe334730583fc5bd86af875f278f76f88b34d (2021-05-06).

%module (package="pymmcore", directors="1", threads="1") pymmcore_swig

%feature("director") MMEventCallback;
%feature("autodoc", "3");

%include exception.i
%include std_string.i
%include std_vector.i
%include std_map.i
%include std_pair.i
%include "typemaps.i"

%{
#define SWIG_FILE_WITH_INIT
%}

%init %{
import_array();
%}

%{
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include "numpy/arrayobject.h"
#include "string.h"
%}

%typemap(out) void*
{
    npy_intp dims[2];
    dims[0] = (arg1)->getImageHeight();
    dims[1] = (arg1)->getImageWidth();
    npy_intp pixelCount = dims[0] * dims[1];

    if ((arg1)->getBytesPerPixel() == 1)
    {
        PyObject * numpyArray = PyArray_SimpleNew(2, dims, NPY_UINT8);
        memcpy(PyArray_DATA((PyArrayObject *) numpyArray), result, pixelCount);
        $result = numpyArray;
    }
    else if ((arg1)->getBytesPerPixel() == 2)
    {
        PyObject * numpyArray = PyArray_SimpleNew(2, dims, NPY_UINT16);
        memcpy(PyArray_DATA((PyArrayObject *) numpyArray), result, pixelCount * 2);
        $result = numpyArray;
    }
    else if ((arg1)->getBytesPerPixel() == 4)
    {
        PyObject * numpyArray = PyArray_SimpleNew(2, dims, NPY_UINT32);
        memcpy(PyArray_DATA((PyArrayObject *) numpyArray), result, pixelCount * 4);
        $result = numpyArray;
    }
    else if ((arg1)->getBytesPerPixel() == 8)
    {
        PyObject * numpyArray = PyArray_SimpleNew(2, dims, NPY_UINT64);
        memcpy(PyArray_DATA((PyArrayObject *) numpyArray), result, pixelCount * 8);
        $result = numpyArray;
    }
    else
    {
        // don't know how to map
        // TODO: thow exception?
        // XXX Must do something, as returning NULL without setting error results
        // in an opaque error.
        $result = 0;
    }
}


%typemap(out) unsigned int*
{
    //Here we assume we are getting RGBA (32 bits).
    npy_intp dims[3];
    dims[0] = (arg1)->getImageHeight();
    dims[1] = (arg1)->getImageWidth();
    dims[2] = 3; // RGB
    unsigned numChannels = (arg1)->getNumberOfComponents();
    unsigned char * pyBuf;
    unsigned char * coreBuf = (unsigned char *) result;

    if ((arg1)->getBytesPerPixel() == 4 && numChannels == 1)
    {

        // create new numpy array object
        PyObject * numpyArray = PyArray_SimpleNew(3, dims, NPY_UINT8);

        // get a pointer to the data buffer
        pyBuf = (unsigned char *) PyArray_DATA((PyArrayObject *) numpyArray);

        // copy R,G,B but leave out A in RGBA to return a WxHx3-dimensional array

        long pixelCount = dims[0] * dims[1];

        for (long i=0; i<pixelCount; ++i)
        {
            *pyBuf++ = *coreBuf++; //R
            *pyBuf++ = *coreBuf++; //G
            *pyBuf++ = *coreBuf++; //B

            ++coreBuf; // Skip the empty byte
        }

        // Return the numpy array object

        $result = numpyArray;

    }
    else
    {
        // don't know how to map
        // TODO: thow exception?
        $result = 0;
    }
}

/* tell SWIG to treat char ** as a list of strings */
/* From https://stackoverflow.com/questions/3494598/passing-a-list-of-strings-to-from-python-ctypes-to-c-function-expecting-char */
/* XXX No need to freearg the vector, right? */
%typemap(in) std::vector<unsigned char *> {
    // check if is a list
    if(PyList_Check($input))
    {
        long expectedLength = (arg1)->getSLMWidth(arg2) * (arg1)->getSLMHeight(arg2);

        Py_ssize_t size = PyList_Size($input);
        std::vector<unsigned char*> inputVector;

        for(Py_ssize_t i = 0; i < size; i++)
        {
            //printf("Pushing %d\n",  i);
            PyObject * o = PyList_GetItem($input, i);
            if(PyString_Check(o))
            {
                if (PyString_Size(o) != expectedLength)
                {
                    PyErr_SetString(PyExc_TypeError, "One of the Image strings is the wrong length for this SLM.");
                    return NULL;
                }

                inputVector.push_back((unsigned char *)PyString_AsString(o));
            }
            else
            {
                PyErr_SetString(PyExc_TypeError, "list must contain strings");
                return NULL;
            }
        }
        $1 = inputVector;
    }
    else
    {
        PyErr_SetString(PyExc_TypeError, "not a list");
        return NULL;
    }
}

%rename(setSLMImage) setSLMImage_pywrap;
%apply (char *STRING, int LENGTH) { (char *pixels, int receivedLength) };
%extend CMMCore {
PyObject *setSLMImage_pywrap(const char* slmLabel, char *pixels, int receivedLength)
{
    long expectedLength = self->getSLMWidth(slmLabel) * self->getSLMHeight(slmLabel);
    //printf("expected: %d -- received: %d\n",expectedLength,receivedLength);

    if (receivedLength == expectedLength)
    {
        self->setSLMImage(slmLabel, (unsigned char *)pixels);
    }
    else if (receivedLength == 4*expectedLength)
    {
        self->setSLMImage(slmLabel, (imgRGB32)pixels);
    }
    else
    {
        PyErr_SetString(PyExc_TypeError, "Image dimensions are wrong for this SLM.");
        return (PyObject *) NULL;
    }
    return PyInt_FromLong(0);
}
}
%ignore setSLMImage;

%{
#define SWIG_FILE_WITH_INIT
#include "../mmCoreAndDevices/MMDevice/MMDeviceConstants.h"
#include "../mmCoreAndDevices/MMCore/Error.h"
#include "../mmCoreAndDevices/MMCore/Configuration.h"
#include "../mmCoreAndDevices/MMDevice/ImageMetadata.h"
#include "../mmCoreAndDevices/MMCore/MMEventCallback.h"
#include "../mmCoreAndDevices/MMCore/MMCore.h"
%}

// Exception handling. Tranditionally, MMCore uses exception specifications
// (throw(CMMError)) to tell SWIG to generate exception handling code. This is
// handled by the %typemap(throws) below.
// However, C++ exception specifications are deprecated since C++11 and removed
// in C++17. So in order to future-proof this interface, we also specify a
// general exception handler using %exception. The latter applies to all
// functions that do not have an exception specification (or, in the future,
// noexcept).

%{
static int cmmerror_swig_exception_code(const CMMError& e) {
    switch (e.getCode())
    {
        case MMERR_BadAffineTransform:
        case MMERR_BadConfigName:
        case MMERR_DuplicateConfigGroup:
        case MMERR_DuplicateLabel:
        case MMERR_InvalidContents:
        case MMERR_InvalidCoreProperty:
        case MMERR_InvalidCoreValue:
        case MMERR_InvalidLabel:
        case MMERR_InvalidPropertyBlock:
        case MMERR_InvalidSerialDevice:
        case MMERR_InvalidShutterDevice:
        case MMERR_InvalidSpecificDevice:
        case MMERR_InvalidStageDevice:
        case MMERR_InvalidStateDevice:
        case MMERR_InvalidXYStageDevice:
        case MMERR_NoConfigGroup:
        case MMERR_NoConfiguration:
        case MMERR_NullPointerException:
        case MMERR_PropertyNotInCache:
        case MMERR_SetPropertyFailed:
        case MMERR_UnexpectedDevice:
            return SWIG_ValueError;
        case MMERR_FileOpenFailed:
        case MMERR_InvalidCFGEntry:
        case MMERR_InvalidConfigurationFile:
        case MMERR_LoadLibraryFailed:
            return SWIG_IOError;
        case MMERR_CircularBufferEmpty:
        case MMERR_InvalidConfigurationIndex:
            return SWIG_IndexError;
        case MMERR_CircularBufferFailedToInitialize:
        case MMERR_OutOfMemory:
            return SWIG_MemoryError;
        case MMERR_CameraBufferReadFailed:
        case MMERR_CircularBufferIncompatibleImage:
        case MMERR_UnhandledException:
        case MMERR_UnknownModule:
        case MMERR_OK: // Shouldn't get here with MMERR_OK
        default:
            return SWIG_RuntimeError;
    }
}
%}

// Applies to functions with C++ exception specification (to be retired when
// C++ exception specifications retired)
%typemap(throws) CMMError %{
    SWIG_exception(cmmerror_swig_exception_code($1), ($1).getMsg().c_str());
%}
%typemap(throws) MetadataKeyError %{
    SWIG_exception(SWIG_ValueError, ($1).getMsg().c_str());
%}
%typemap(throws) MetadataIndexError %{
    SWIG_exception(SWIG_IndexError, ($1).getMsg().c_str());
%}

// Applies to functions without exception specification
%exception {
    try {
        $action
    }
    catch (const CMMError& e) {
        SWIG_exception(cmmerror_swig_exception_code(e), e.getMsg().c_str());
    }
    catch (MetadataKeyError& e) {
        SWIG_exception(SWIG_ValueError, e.getMsg().c_str());
    }
    catch (MetadataIndexError& e) {
        SWIG_exception(SWIG_IndexError, e.getMsg().c_str());
    }
}


// instantiate STL mappings
namespace std {
    %template(CharVector)   vector<char>;
    %template(LongVector)   vector<long>;
    %template(DoubleVector) vector<double>;
    %template(StrVector)    vector<string>;
    %template(pair_ss)      pair<string, string>;
    %template(StrMap)       map<string, string>;
}

// output arguments
%apply double &OUTPUT { double &x_stage };
%apply double &OUTPUT { double &y_stage };
%apply int &OUTPUT { int &x };
%apply int &OUTPUT { int &y };
%apply int &OUTPUT { int &xSize };
%apply int &OUTPUT { int &ySize };

%include "../mmCoreAndDevices/MMDevice/MMDeviceConstants.h"
%include "../mmCoreAndDevices/MMCore/Error.h"
%include "../mmCoreAndDevices/MMCore/Configuration.h"
%include "../mmCoreAndDevices/MMCore/MMCore.h"
%include "../mmCoreAndDevices/MMDevice/ImageMetadata.h"
%include "../mmCoreAndDevices/MMCore/MMEventCallback.h"
