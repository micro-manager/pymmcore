#!/bin/bash

set -e -x

test -n "$BOOST_VERSION" || BOOST_VERSION=1_72_0
test -n "$PARALLEL" || PARALLEL=-j2

cd /


curl -LO https://dl.bintray.com/boostorg/release/${BOOST_VERSION//_/.}/source/boost_$BOOST_VERSION.tar.gz
tar xzf boost_$BOOST_VERSION.tar.gz
pushd boost_$BOOST_VERSION
./bootstrap.sh
./b2 --with-system --with-thread --with-date_time link=static runtime-link=shared cxxflags=-fPIC
popd


git clone https://github.com/swig/swig.git
pushd swig
git checkout rel-4.0.1
curl -LO https://ftp.pcre.org/pub/pcre/pcre-8.44.tar.gz
./Tools/pcre-build.sh
./autogen.sh
./configure
make $PARALLEL
make install
popd


cd /io
export CFLAGS="-Wno-deprecated -Wno-unused-variable"
for PYBIN in /opt/python/cp3*/bin; do
    $PYBIN/pip install --upgrade pip
    $PYBIN/pip install --upgrade setuptools wheel numpy
    rm -rf build
    $PYBIN/python setup.py build_ext -I/boost_$BOOST_VERSION -L/boost_$BOOST_VERSION/stage/lib $PARALLEL
    $PYBIN/python setup.py build
    $PYBIN/python setup.py bdist_wheel
done


# Update ABI tag
cd /io
mkdir -p wheelhouse
for WHL in dist/*.whl; do
    auditwheel show $WHL
    auditwheel repair $WHL -w wheelhouse
done


# Sanity check
cd /
for PYBIN in /opt/python/cp3*/bin; do
    $PYBIN/pip install pymmcore --no-index -f /io/wheelhouse
    $PYBIN/python -m pymmcore
done
