# flake8: noqa

# NOTE: for now this file is manually created (well, a lot of find/replace with a decent
# amount of checking).  As such, it's conceivable that there are errors, so feel free
# to submit PR fixes if you find one.
# See https://github.com/micro-manager/pymmcore/pull/46 for discussion about fully
# autogenerating "good" type hints. (along with a script that might help for anyone
# so inclined)
from __future__ import annotations
from typing import Any, Final, List, Literal, NewType, overload, Sequence, Tuple, Union

import numpy as np
import numpy.typing as npt

__version__: str

MaxStrLength: int

# ActionType
NoAction: Final = 0
BeforeGet: Final = 1
AfterSet: Final = 2
IsSequenceable: Final = 3
AfterLoadSequence: Final = 4
StartSequence: Final = 5
StopSequence: Final = 6

# DeviceType
UnknownType: Final = 0
AnyType: Final = 1
CameraDevice: Final = 2
ShutterDevice: Final = 3
StateDevice: Final = 4
StageDevice: Final = 5
XYStageDevice: Final = 6
SerialDevice: Final = 7
GenericDevice: Final = 8
AutoFocusDevice: Final = 9
CoreDevice: Final = 10
ImageProcessorDevice: Final = 11
SignalIODevice: Final = 12
MagnifierDevice: Final = 13
SLMDevice: Final = 14
HubDevice: Final = 15
GalvoDevice: Final = 16
PressurePumpDevice: Final = 17
VolumetricPumpDevice: Final = 18

# PropertyType
Undef: Final = 0
String: Final = 1
Float: Final = 2
Integer: Final = 3

# PortType
InvalidPort: Final = 0
SerialPort: Final = 1
USBPort: Final = 2
HIDPort: Final = 3

# FocusDirection
FocusDirectionUnknown: Final = 0
FocusDirectionTowardSample: Final = 1
FocusDirectionAwayFromSample: Final = 2

# DeviceNotification
Attention: Final = 0
Done: Final = 1
StatusChanged: Final = 2

# DeviceDetectionStatus
Unimplemented: Final = -2
Misconfigured: Final = -1
CanNotCommunicate: Final = 0
CanCommunicate: Final = 1

# DeviceInitializationState
Uninitialized: Final = 0
InitializedSuccessfully: Final = 1
InitializationFailed: Final = 2

g_CFGCommand_ConfigGroup: Final[Literal["ConfigGroup"]]
g_CFGCommand_ConfigPixelSize: Final[Literal["ConfigPixelSize"]]
g_CFGCommand_Configuration: Final[Literal["Config"]]
g_CFGCommand_Delay: Final[Literal["Delay"]]
g_CFGCommand_Device: Final[Literal["Device"]]
g_CFGCommand_Equipment: Final[Literal["Equipment"]]
g_CFGCommand_FocusDirection: Final[Literal["FocusDirection"]]
g_CFGCommand_ImageSynchro: Final[Literal["ImageSynchro"]]
g_CFGCommand_Label: Final[Literal["Label"]]
g_CFGCommand_ParentID: Final[Literal["Parent"]]
g_CFGCommand_PixelSize_um: Final[Literal["PixelSize_um"]]
g_CFGCommand_PixelSizeAffine: Final[Literal["PixelSizeAffine"]]
g_CFGCommand_PixelSizedxdz: Final[Literal["PixelSizeAngle_dxdz"]]
g_CFGCommand_PixelSizedydz: Final[Literal["PixelSizeAngle_dydz"]]
g_CFGCommand_PixelSizeOptimalZUm: Final[Literal["PixelSizeOptimalZ_Um"]]
g_CFGCommand_Property: Final[Literal["Property"]]

g_CFGGroup_PixelSizeUm: Final[Literal["PixelSize_um"]]
g_CFGGroup_System: Final[Literal["System"]]
g_CFGGroup_System_Shutdown: Final[Literal["Shutdown"]]
g_CFGGroup_System_Startup: Final[Literal["Startup"]]

g_FieldDelimiters: Final[Literal[","]]

g_Keyword_ActualExposure: Final[Literal["ActualExposure"]]
g_Keyword_ActualInterval_ms: Final[Literal["ActualInterval-ms"]]
g_Keyword_AnswerTimeout: Final[Literal["AnswerTimeout"]]
g_Keyword_BaudRate: Final[Literal["BaudRate"]]
g_Keyword_Binning: Final[Literal["Binning"]]
g_Keyword_CameraChannelIndex: Final[Literal["CameraChannelIndex"]]
g_Keyword_CameraChannelName: Final[Literal["CameraChannelName"]]
g_Keyword_CameraID: Final[Literal["CameraID"]]
g_Keyword_CameraName: Final[Literal["CameraName"]]
g_Keyword_CCDTemperature: Final[Literal["CCDTemperature"]]
g_Keyword_CCDTemperatureSetPoint: Final[Literal["CCDTemperatureSetPoint"]]
g_Keyword_Channel: Final[Literal["Channel"]]
g_Keyword_Closed_Position: Final[Literal["ClosedPosition"]]
g_Keyword_ColorMode: Final[Literal["ColorMode"]]
g_Keyword_CoreAutoFocus: Final[Literal["AutoFocus"]]
g_Keyword_CoreAutoShutter: Final[Literal["AutoShutter"]]
g_Keyword_CoreCamera: Final[Literal["Camera"]]
g_Keyword_CoreChannelGroup: Final[Literal["ChannelGroup"]]
g_Keyword_CoreDevice: Final[Literal["Core"]]
g_Keyword_CoreFocus: Final[Literal["Focus"]]
g_Keyword_CoreGalvo: Final[Literal["Galvo"]]
g_Keyword_CoreImageProcessor: Final[Literal["ImageProcessor"]]
g_Keyword_CoreInitialize: Final[Literal["Initialize"]]
g_Keyword_CorePressurePump: Final[Literal["PressurePump"]]
g_Keyword_CoreShutter: Final[Literal["Shutter"]]
g_Keyword_CoreSLM: Final[Literal["SLM"]]
g_Keyword_CoreTimeoutMs: Final[Literal["TimeoutMs"]]
g_Keyword_CoreVolumetricPump: Final[Literal["VolumetricPump"]]
g_Keyword_CoreXYStage: Final[Literal["XYStage"]]
g_Keyword_Current_Volume: Final[Literal["Volume_uL"]]
g_Keyword_DataBits: Final[Literal["DataBits"]]
g_Keyword_Delay: Final[Literal["Delay_ms"]]
g_Keyword_DelayBetweenCharsMs: Final[Literal["DelayBetweenCharsMs"]]
g_Keyword_Description: Final[Literal["Description"]]
g_Keyword_Elapsed_Time_ms: Final[Literal["ElapsedTime-ms"]]
g_Keyword_EMGain: Final[Literal["EMGain"]]
g_Keyword_Exposure: Final[Literal["Exposure"]]
g_Keyword_Flowrate: Final[Literal["Flowrate_uL_per_sec"]]
g_Keyword_Gain: Final[Literal["Gain"]]
g_Keyword_Handshaking: Final[Literal["Handshaking"]]
g_Keyword_HubID: Final[Literal["HubID"]]
g_Keyword_Interval_ms: Final[Literal["Interval-ms"]]
g_Keyword_Label: Final[Literal["Label"]]
g_Keyword_Max_Volume: Final[Literal["Max_Volume_uL"]]
g_Keyword_Meatdata_Exposure: Final[Literal["Exposure-ms"]]
g_Keyword_Metadata_CameraLabel: Final[Literal["Camera"]]
g_Keyword_Metadata_Exposure: Final[Literal["Exposure-ms"]]
g_Keyword_Metadata_Height: Final[Literal["Height"]]
g_Keyword_Metadata_ImageNumber: Final[Literal["ImageNumber"]]
g_Keyword_Metadata_ROI_X: Final[Literal["ROI-X-start"]]
g_Keyword_Metadata_ROI_Y: Final[Literal["ROI-Y-start"]]
g_Keyword_Metadata_Score: Final[Literal["Score"]]
g_Keyword_Metadata_TimeInCore: Final[Literal["TimeReceivedByCore"]]
g_Keyword_Metadata_Width: Final[Literal["Width"]]
g_Keyword_Min_Volume: Final[Literal["Min_Volume_uL"]]
g_Keyword_Name: Final[Literal["Name"]]
g_Keyword_Offset: Final[Literal["Offset"]]
g_Keyword_Parity: Final[Literal["Parity"]]
g_Keyword_PixelType_GRAY16: Final[Literal["GRAY16"]]
g_Keyword_PixelType_GRAY32: Final[Literal["GRAY32"]]
g_Keyword_PixelType_GRAY8: Final[Literal["GRAY8"]]
g_Keyword_PixelType_RGB32: Final[Literal["RGB32"]]
g_Keyword_PixelType_RGB64: Final[Literal["RGB64"]]
g_Keyword_PixelType_Unknown: Final[Literal["Unknown"]]
g_Keyword_PixelType: Final[Literal["PixelType"]]
g_Keyword_Port: Final[Literal["Port"]]
g_Keyword_Position: Final[Literal["Position"]]
g_Keyword_Pressure_Imposed: Final[Literal["Pressure Imposed"]]
g_Keyword_Pressure_Measured: Final[Literal["Pressure Measured"]]
g_Keyword_ReadoutMode: Final[Literal["ReadoutMode"]]
g_Keyword_ReadoutTime: Final[Literal["ReadoutTime"]]
g_Keyword_Speed: Final[Literal["Speed"]]
g_Keyword_State: Final[Literal["State"]]
g_Keyword_StopBits: Final[Literal["StopBits"]]
g_Keyword_Transpose_Correction: Final[Literal["TransposeCorrection"]]
g_Keyword_Transpose_MirrorX: Final[Literal["TransposeMirrorX"]]
g_Keyword_Transpose_MirrorY: Final[Literal["TransposeMirrorY"]]
g_Keyword_Transpose_SwapXY: Final[Literal["TransposeXY"]]
g_Keyword_Type: Final[Literal["Type"]]
g_Keyword_Version: Final[Literal["Version"]]

DEVICE_BUFFER_OVERFLOW: int
DEVICE_CAMERA_BUSY_ACQUIRING: int
DEVICE_CAN_NOT_SET_PROPERTY: int
DEVICE_COMM_HUB_MISSING: int
DEVICE_CORE_CHANNEL_PRESETS_FAILED: int
DEVICE_CORE_CONFIG_FAILED: int
DEVICE_CORE_EXPOSURE_FAILED: int
DEVICE_CORE_FOCUS_STAGE_UNDEF: int
DEVICE_DUPLICATE_LABEL: int
DEVICE_DUPLICATE_LIBRARY: int
DEVICE_DUPLICATE_PROPERTY: int
DEVICE_ERR: int
DEVICE_IMAGE_PARAMS_FAILED: int
DEVICE_INCOMPATIBLE_IMAGE: int
DEVICE_INTERNAL_INCONSISTENCY: int
DEVICE_INVALID_INPUT_PARAM: int
DEVICE_INVALID_PROPERTY_LIMTS: int
DEVICE_INVALID_PROPERTY_TYPE: int
DEVICE_INVALID_PROPERTY_VALUE: int
DEVICE_INVALID_PROPERTY: int
DEVICE_LOCALLY_DEFINED_ERROR: int
DEVICE_NATIVE_MODULE_FAILED: int
DEVICE_NO_CALLBACK_REGISTERED: int
DEVICE_NO_PROPERTY_DATA: int
DEVICE_NONEXISTENT_CHANNEL: int
DEVICE_NOT_CONNECTED: int
DEVICE_NOT_SUPPORTED: int
DEVICE_NOT_YET_IMPLEMENTED: int
DEVICE_OK: int
DEVICE_OUT_OF_MEMORY: int
DEVICE_PROPERTY_NOT_SEQUENCEABLE: int
DEVICE_PUMP_IS_RUNNING: int
DEVICE_SELF_REFERENCE: int
DEVICE_SEQUENCE_TOO_LARGE: int
DEVICE_SERIAL_BUFFER_OVERRUN: int
DEVICE_SERIAL_COMMAND_FAILED: int
DEVICE_SERIAL_INVALID_RESPONSE: int
DEVICE_SERIAL_TIMEOUT: int
DEVICE_SNAP_IMAGE_FAILED: int
DEVICE_UNKNOWN_LABEL: int
DEVICE_UNKNOWN_POSITION: int
DEVICE_UNSUPPORTED_COMMAND: int
DEVICE_UNSUPPORTED_DATA_FORMAT: int
MM_CODE_ERR: int
MM_CODE_OK: int

def CMMCore_noop() -> None: ...
def MetadataTag_ReadLine(jarg: Any) -> str: ...
def PropertySetting_generateKey(device: str, prop: str) -> str: ...

Rectangle = List[int]  # it returns a list of 4 ints... would be nice if it were tuple
DeviceType = int
PropertyType = int
FocusDirection = int
DeviceDetectionStatus = int
DeviceInitializationState = int
AffineTuple = Tuple[float, float, float, float, float, float]

# These are special string types used throughout the API.
# We use NewType() to annotatr *return* values from core (that are guaranteed to be
# valid inputs to other core functions with the same
# type).  However, to remain flexible, we use the fallback `NewType() | str` when
# annotating function inputs.

AdapterName = NewType("AdapterName", str)
"""Name of a device adapter library (discovered in the adapter search path)."""
DeviceLabel = NewType("DeviceLabel", str)
"""User-defined label for a loaded device.
Not to be confused with the `DeviceName`, which is defined by the device adapter.
"""
DeviceName = NewType("DeviceName", str)
"""Name of a Device offered by a device adapter (defined by the device adapter)."""
PropertyName = NewType("PropertyName", str)
"""Name of a device property (defined by the device adapter)."""
ConfigGroupName = NewType("ConfigGroupName", str)
"""User-defined name of a configuration group."""
ConfigPresetName = NewType("ConfigPresetName", str)
"""User-defined name of a preset in a configuration group."""
PixelSizeConfigName = NewType("PixelSizeConfigName", str)
"""User-defined name of a defined pixel size configuration preset"""
StateLabel = NewType("StateLabel", str)
"""User-defined label for a specific state in a state device."""

FeatureFlag = Literal[
    "StrictInitializationChecks",
    "ParallelDeviceInitialization",
]

class CMMCore:
    def __init__(self) -> None: ...
    def addGalvoPolygonVertex(
        self, galvoLabel: str, polygonIndex: int, x: float, y: float
    ) -> None:
        """Add a vertex to a galvo polygon."""
    def clearCircularBuffer(self) -> None:
        """Removes all images from the circular buffer."""
    def clearROI(self) -> None:
        """Set the region of interest of the current camera to the full frame."""
    def debugLogEnabled(self) -> bool:
        """Indicates if logging of debug messages is enabled"""
    @overload
    def defineConfig(self, groupName: str, configName: str) -> None:
        """Defines a configuration.

        If the configuration group/name was not previously defined a new configuration
        will be automatically created; otherwise nothing happens.
        """
    @overload
    def defineConfig(
        self,
        groupName: str,
        configName: str,
        deviceLabel: DeviceLabel | str,
        propName: PropertyName | str,
        value: str,
    ) -> None:
        """Defines a single configuration entry (setting).

        If the configuration group/name was not previously defined a new configuration
        will be automatically created. If the name was previously defined the new
        setting will be added to its list of property settings. The new setting will
        override previously defined ones if it refers to the same property name.
        """
    def defineConfigGroup(self, groupName: str) -> None:
        """Creates an empty configuration group."""
    @overload
    def definePixelSizeConfig(self, resolutionID: str) -> None:
        """Defines an empty pixel size entry."""
    @overload
    def definePixelSizeConfig(
        self,
        resolutionID: str,
        deviceLabel: DeviceLabel | str,
        propName: PropertyName | str,
        value: str,
    ) -> None:
        """Defines a single pixel size entry (setting).

        The system will treat pixel size configurations very similar to configuration
        presets, i.e. it will try to detect if any of the pixel size presets matches the
        current state of the system.

        If the pixel size was previously defined the new setting will be added to its
        list of property settings. The new setting will override previously defined ones
        if it refers to the same property name.
        """
    def defineStateLabel(
        self, stateDeviceLabel: DeviceLabel | str, state: int, stateLabel: str
    ) -> None:
        """Defines a label for the specific state."""
    @overload
    def deleteConfig(
        self, groupName: ConfigGroupName | str, configName: ConfigPresetName | str
    ) -> None:
        """Deletes a configuration from a group."""
    @overload
    def deleteConfig(
        self,
        groupName: ConfigGroupName | str,
        configName: ConfigPresetName | str,
        deviceLabel: DeviceLabel | str,
        propName: PropertyName | str,
    ) -> None: ...
    def deleteConfigGroup(self, groupName: ConfigGroupName | str) -> None:
        """Deletes an entire configuration group."""
    def deleteGalvoPolygons(self, galvoLabel: DeviceLabel | str) -> None:
        """Remove all added polygons"""
    def deletePixelSizeConfig(self, configName: PixelSizeConfigName | str) -> None:
        """Deletes a pixel size configuration."""
    def detectDevice(self, deviceLabel: DeviceLabel | str) -> DeviceDetectionStatus:
        """Tries to communicate to a device through a given serial port Used to automate
        discovery of correct serial port. Also configures the serial port correctly."""
    def deviceBusy(self, label: DeviceLabel | str) -> bool:
        """Checks the busy status of the specific device."""
    def deviceTypeBusy(self, devType: DeviceType) -> bool:
        """Checks the busy status for all devices of the specific type."""
    def displaySLMImage(self, slmLabel: DeviceLabel | str) -> None:
        """Display the waiting image on the SLM."""
    def enableContinuousFocus(self, enable: bool) -> None:
        """Enables or disables the operation of the continuous focusing hardware device."""
    def enableDebugLog(self, enable: bool) -> None:
        """Enable or disable logging of debug messages."""
    # the Literal hint helps people know what the valid options are, but the fallback
    # to str makes it more future proof so that it's still valid to enter any string
    def enableFeature(self, name: FeatureFlag | str, enable: bool) -> None:
        """Enable or disable the given Core feature.

        Core features control whether experimental functionality (which is subject
        to breaking changes) is exposed, or whether stricter API usage is enforced.

        Currently switchable features:

        - "StrictInitializationChecks" (default: disabled) When enabled, an
          exception is thrown when an operation requiring an initialized device is
          attempted on a device that is not successfully initialized. When disabled,
          no exception is thrown and a warning is logged (and the operation may
          potentially cause incorrect behavior or a crash).
        - "ParallelDeviceInitialization" (default: enabled) When enabled, serial ports
          are initialized in serial order, and all other devices are in parallel, using
          multiple threads, one per device module.  Early testing shows this to be
          reliable, but switch this off when issues are encountered during
          device initialization.
        """
    def enableStderrLog(self, enable: bool) -> None:
        """Enables or disables log message display on the standard console."""
    def fullFocus(self) -> None:
        """Performs focus acquisition and lock for the one-shot focusing device."""
    def getAllowedPropertyValues(
        self, label: DeviceLabel | str, propName: PropertyName | str
    ) -> Tuple[str, ...]:
        """Returns all valid values for the specified property."""
    def getAPIVersionInfo(self) -> str:
        """Returns the module and device interface versions."""
    def getAutoFocusDevice(self) -> DeviceLabel | Literal[""]:
        """Returns the label of the currently selected auto-focus device.

        Returns empty string if no auto-focus device is selected.
        """
    def getAutoFocusOffset(self) -> float:
        """Measures offset for the one-shot focusing device."""
    def getAutoShutter(self) -> bool:
        """Returns the current setting of the auto-shutter option."""
    def getAvailableConfigGroups(self) -> Tuple[ConfigGroupName, ...]:
        """Returns the names of all defined configuration groups"""
    def getAvailableConfigs(
        self, configGroup: ConfigGroupName | str
    ) -> Tuple[ConfigPresetName, ...]:
        """Returns all defined configuration (preset) names in a given group"""
    def getAvailableDeviceDescriptions(
        self, library: AdapterName | str
    ) -> Tuple[str, ...]:
        """Get descriptions for available devices from the specified library."""
    def getAvailableDevices(self, library: AdapterName | str) -> Tuple[DeviceName, ...]:
        """Get available devices from the specified device library."""
    def getAvailableDeviceTypes(self, library: AdapterName | str) -> Tuple[int, ...]:
        """Get type information for available devices from the specified library."""
    def getAvailablePixelSizeConfigs(self) -> Tuple[PixelSizeConfigName, ...]:
        """Returns all defined resolution preset names"""
    def getBufferFreeCapacity(self) -> int:
        """Returns the number of images that can be added to the buffer without
        overflowing.
        """
    def getBufferTotalCapacity(self) -> int:
        """Returns the total number of images that can be stored in the buffer"""
    def getBytesPerPixel(self) -> int:
        """How many bytes for each pixel."""
    def getCameraChannelName(self, channelNr: int) -> str:
        """Returns the name of the requested channel as known by the default camera"""
    def getCameraDevice(self) -> DeviceLabel | Literal[""]:
        """Returns the label of the currently selected camera device.

        Returns empty string if no camera device is selected.
        """
    def getChannelGroup(self) -> ConfigGroupName | Literal[""]:
        """Returns the group determining the channel selection.

        Returns empty string if no channel group is selected.
        """
    def getCircularBufferMemoryFootprint(self) -> int:
        """Returns the size of the Circular Buffer in MB"""
    def getConfigData(
        self, configGroup: ConfigGroupName | str, configName: ConfigPresetName | str
    ) -> Configuration:
        """Returns the configuration object for a given group and name."""
    def getConfigGroupState(self, group: ConfigGroupName | str) -> Configuration:
        """Returns the partial state of the system, only for the devices included in the
        specified group."""
    def getConfigGroupStateFromCache(
        self, group: ConfigGroupName | str
    ) -> Configuration:
        """Returns the partial state of the system cache, only for the devices included in
        the specified group."""
    def getConfigState(
        self, group: ConfigGroupName | str, config: ConfigPresetName | str
    ) -> Configuration:
        """Returns a partial state of the system, only for devices included in the
        specified configuration."""
    def getCoreErrorText(self, code: int) -> str:
        """Returns a pre-defined error test with the given error code"""
    def getCurrentConfig(
        self, groupName: ConfigGroupName | str
    ) -> ConfigPresetName | Literal[""]:
        """Returns the current configuration (preset) for a given group.

        Returns empty string if no configuration is selected.
        """
    def getCurrentConfigFromCache(
        self, groupName: ConfigGroupName | str
    ) -> ConfigPresetName | Literal[""]:
        """Returns the configuration for a given group based on the data in the cache."""
    def getCurrentFocusScore(self) -> float:
        """Returns the focus score from the default focusing device measured at the
        current Z position."""
    @overload
    def getCurrentPixelSizeConfig(self) -> PixelSizeConfigName:
        """Get the current pixel configuration name"""
    @overload
    def getCurrentPixelSizeConfig(self, cached: bool) -> PixelSizeConfigName:
        """Get the current pixel configuration name"""
    def getDeviceAdapterNames(self) -> Tuple[AdapterName, ...]:
        """Return the names of discoverable device adapters."""
    def getDeviceAdapterSearchPaths(self) -> Tuple[str, ...]:
        """Return the current device adapter search paths."""
    def getDeviceDelayMs(self, label: DeviceLabel | str) -> float:
        """Reports action delay in milliseconds for the specific device."""
    def getDeviceDescription(self, label: DeviceLabel | str) -> str:
        """Returns description text for a given device label. "Description" is determined
        by the library and is immutable."""
    def getDeviceLibrary(self, label: DeviceLabel | str) -> AdapterName:
        """Returns device library (aka module, device adapter) name."""
    def getDeviceName(self, label: DeviceLabel | str) -> DeviceName:
        """Returns device name for a given device label."""
    def getDevicePropertyNames(
        self, label: DeviceLabel | str
    ) -> Tuple[PropertyName, ...]:
        """Returns all property names supported by the device."""
    def getDeviceType(self, label: DeviceLabel | str) -> DeviceType:
        """Returns device type."""
    @overload
    def getExposure(self) -> float:
        """Returns the current exposure setting of the camera in milliseconds."""
    @overload
    def getExposure(self, label: DeviceLabel | str) -> float:
        """Returns the current exposure setting of the specified camera in milliseconds."""
    def getExposureSequenceMaxLength(self, cameraLabel: DeviceLabel | str) -> int:
        """Gets the maximum length of a camera's exposure sequence."""
    def getFocusDevice(self) -> DeviceLabel | Literal[""]:
        """Returns the label of the currently selected focus device.

        Returns empty string if no focus device is selected.
        """
    def getFocusDirection(self, stageLabel: DeviceLabel | str) -> FocusDirection:
        """Get the focus direction of a stage."""
    def getGalvoChannel(self, galvoLabel: DeviceLabel | str) -> str:
        """Get the name of the active galvo channel (for a multi-laser galvo device)."""
    def getGalvoDevice(self) -> DeviceLabel | Literal[""]:
        """Returns the label of the currently selected Galvo device.

        Returns empty string if no Galvo device is selected.
        """
    @overload
    def getGalvoPosition(self, galvoDevice: DeviceLabel | str) -> List[float]:
        """Get x,y position of the galvo device."""
    @overload
    def getGalvoPosition(
        self,
        galvoLabel: DeviceLabel | str,
        x_stage: Sequence[float],
        y_stage: Sequence[float],
    ) -> None: ...
    def getGalvoXMinimum(self, galvoLabel: DeviceLabel | str) -> float:
        """Get the Galvo x minimum"""
    def getGalvoXRange(self, galvoLabel: DeviceLabel | str) -> float:
        """Get the Galvo x range"""
    def getGalvoYMinimum(self, galvoLabel: DeviceLabel | str) -> float:
        """Get the Galvo y minimum"""
    def getGalvoYRange(self, galvoLabel: DeviceLabel | str) -> float:
        """Get the Galvo y range"""
    @overload
    def getImage(self) -> np.ndarray:
        """Exposes the internal image buffer."""
    @overload
    def getImage(self, numChannel: int) -> np.ndarray:
        """Returns the internal image buffer for a given Camera Channel"""
    def getImageBitDepth(self) -> int:
        """How many bits of dynamic range are to be expected from the camera."""
    def getImageBufferSize(self) -> int:
        """Returns the size of the internal image buffer."""
    def getImageHeight(self) -> int:
        """Vertical dimension of the image buffer in pixels."""
    def getImageProcessorDevice(self) -> DeviceLabel | Literal[""]:
        """Returns the label of the currently selected image processor device.

        Returns empty string if no image processor device is selected.
        """
    def getImageWidth(self) -> int:
        """Horizontal dimension of the image buffer in pixels."""
    def getInstalledDeviceDescription(
        self, hubLabel: DeviceLabel | str, peripheralLabel: DeviceName | str
    ) -> str:
        """Returns description from the specified peripheral on `hubLabel` device."""
    def getInstalledDevices(
        self, hubLabel: DeviceLabel | str
    ) -> Tuple[DeviceName, ...]:
        """Performs auto-detection and loading of child devices that are attached to a
        Hub device.

        Raises RuntimeError if hubLabel is not a hub device.
        """
    def getLastFocusScore(self) -> float:
        """Returns the latest focus score from the focusing device."""
    def getLastImage(self) -> np.ndarray:
        """Gets the last image from the circular buffer."""
    @overload
    def getLastImageMD(self, channel: int, slice: int, md: Metadata) -> np.ndarray: ...
    @overload
    def getLastImageMD(self, md: Metadata) -> np.ndarray:
        """Returns a pointer to the pixels of the image that was last inserted into the
        circular buffer. Also provides all metadata associated with that image"""
    def getLoadedDevices(self) -> Tuple[DeviceLabel, ...]:
        """Returns an array of labels for currently loaded devices."""
    def getLoadedDevicesOfType(self, devType: DeviceType) -> Tuple[DeviceLabel, ...]:
        """Returns an array of labels for currently loaded devices of specific type."""
    def getLoadedPeripheralDevices(
        self, hubLabel: DeviceLabel | str
    ) -> Tuple[DeviceLabel, ...]:
        """Return labels of all loaded peripherals of `hubLabel` device.

        Returns empty tuple if hubLabel is not a hub device, or even if hubLabel is
        not the name of any device.
        """
    def getMagnificationFactor(self) -> float:
        """Returns the product of all Magnifiers in the system or 1.0 when none is found.
        This is used internally by GetPixelSizeUm"""
    # def getMultiROI(self) -> List[Any]: ...  # this overload doesn't seem to be present
    def getMultiROI(
        self,
        xs: Sequence[int],
        ys: Sequence[int],
        widths: Sequence[int],
        heights: Sequence[int],
    ) -> None:
        """Get multiple ROIs from the current camera device.

        Will fail if the camera does not support multiple ROIs. Will return empty
        vectors if multiple ROIs are not currently being used.
        """
    def getNBeforeLastImageMD(self, n: int, md: Metadata) -> np.ndarray:
        """Returns a pointer to the pixels of the image that was inserted n images ago.
        Also provides all metadata associated with that image"""
    def getNumberOfCameraChannels(self) -> int:
        """Returns the number of simultaneous channels the default camera is returning."""
    def getNumberOfComponents(self) -> int:
        """Returns the number of components the default camera is returning."""
    def getNumberOfStates(self, stateDeviceLabel: DeviceLabel | str) -> int:
        """Returns the total number of available positions (states)."""
    def getParentLabel(
        self, peripheralLabel: DeviceLabel | str
    ) -> DeviceLabel | Literal[""]:
        """Returns parent device. Returns empty string if no parent is found."""
    @overload
    def getPixelSizeAffine(self) -> AffineTuple:
        """Returns the current Affine Transform to related camera pixels with
        stage movement."""
    @overload
    def getPixelSizeAffine(self, cached: bool) -> AffineTuple:
        """Returns the current Affine Transform to related camera pixels with
        stage movement."""
    def getPixelSizeAffineByID(
        self, resolutionID: PixelSizeConfigName | str
    ) -> AffineTuple:
        """Returns the Affine Transform to related camera pixels with stage movement for
        the requested pixel size group. The raw affine transform without correction for
        binning and magnification will be returned."""

    @overload
    def getPixelSizedxdz(self) -> float: ...
    @overload
    def getPixelSizedxdz(self, cached: bool) -> float: ...
    @overload
    def getPixelSizedxdz(self, resolutionID: PixelSizeConfigName | str) -> float:
        """Returns the angle between the camera's x axis and the axis (direction) of the z drive.

        This angle is dimensionless (i.e. the ratio of the translation in x caused by a
        translation in z, i.e. dx / dz). This angle can be different for different z
        drives (if there are multiple Z drives in the system, please add the Core-Focus
        device to the pixel size configuration). See:
        https://github.com/micro-manager/micro-manager/issues/1984

        """
    @overload
    def getPixelSizedydz(self) -> float: ...
    @overload
    def getPixelSizedydz(self, cached: bool) -> float: ...
    @overload
    def getPixelSizedydz(self, resolutionID: PixelSizeConfigName | str) -> float:
        """Returns the angle between the camera's y axis and the axis (direction) of the z drive.

        This angle is dimensionless (i.e. the ratio of the translation in x caused by a
        translation in z, i.e. dy / dz). This angle can be different for different z
        drives (if there are multiple Z drives in the system, please add the Core-Focus
        device to the pixel size configuration). See:
        https://github.com/micro-manager/micro-manager/issues/1984

        """
    @overload
    def getPixelSizeOptimalZUm(self) -> float: ...
    @overload
    def getPixelSizeOptimalZUm(self, cached: bool) -> float: ...
    @overload
    def getPixelSizeOptimalZUm(self, resolutionID: PixelSizeConfigName | str) -> float:
        """Returns the optimal z step size in um, optionally using cached pixel configuration.

        There is no magic to this number, but lets the system configuration
        communicate to the end user what the optimal Z step size is for this 
        pixel size configuration
        """
    def setPixelSizedxdz(
        self, resolutionID: PixelSizeConfigName | str, dXdZ: float
    ) -> None:
        """Sets the pixel size in the X direction in microns."""
    def setPixelSizedydz(
        self, resolutionID: PixelSizeConfigName | str, dYdZ: float
    ) -> None:
        """Sets the pixel size in the Y direction in microns."""
    def setPixelSizeOptimalZUm(
        self, resolutionID: PixelSizeConfigName | str, optimalZ: float
    ) -> None:
        """Sets the pixel size in the Z direction in microns."""

    def getPixelSizeConfigData(
        self, configName: PixelSizeConfigName | str
    ) -> Configuration:
        """Returns the configuration object for a give pixel size preset."""
    @overload
    def getPixelSizeUm(self) -> float:
        """Returns the current pixel size in microns."""
    @overload
    def getPixelSizeUm(self, cached: bool) -> float:
        """Returns the current pixel size in microns."""
    def getPixelSizeUmByID(self, resolutionID: PixelSizeConfigName | str) -> float:
        """Returns the pixel size in um for the requested pixel size group"""
    @overload
    def getPosition(self) -> float:
        """Returns the current position of the current FocusDevice in microns."""
    @overload
    def getPosition(self, stageLabel: DeviceLabel | str) -> float:
        """Returns the current position of the stage in microns."""
    def getPrimaryLogFile(self) -> str:
        """Return the name of the primary Core log file."""
    def getProperty(
        self, label: DeviceLabel | str, propName: PropertyName | str
    ) -> str:
        """Returns the property value for the specified device.

        The return value will always be a string.  Use getPropertyType to determine the
        correct type.
        """
    def getPropertyFromCache(
        self, deviceLabel: DeviceLabel | str, propName: PropertyName | str
    ) -> str:
        """Returns the cached property value for the specified device."""
    def getPropertyLowerLimit(
        self, label: DeviceLabel | str, propName: PropertyName | str
    ) -> float:
        """Returns the property lower limit value, if the property has limits - 0
        otherwise."""
    def getPropertySequenceMaxLength(
        self, label: DeviceLabel | str, propName: PropertyName | str
    ) -> int:
        """Queries device property for the maximum number of events that can be put
        in a sequence"""
    def getPropertyType(
        self, label: DeviceLabel | str, propName: PropertyName | str
    ) -> PropertyType:
        """Returns the intrinsic property type."""
    def getPropertyUpperLimit(
        self, label: DeviceLabel | str, propName: PropertyName | str
    ) -> float:
        """Returns the property upper limit value, if the property has limits - 0
        otherwise."""
    def getRemainingImageCount(self) -> int:
        """Returns number ofimages available in the Circular Buffer"""
    @overload
    def getROI(self) -> Rectangle:
        """Return the current hardware region of interest for a camera.

        If multiple ROIs are set, this method instead returns a rectangle that describes
        the image that the camera will generate. The coordinates are in units of binned
        pixels. That is, conceptually, binning is applied before the ROI.

        Returns [0,0,0,0] if no camera is selected.
        """
    @overload
    def getROI(self, label: DeviceLabel | str) -> Rectangle:
        """Return the current hardware region of interest for a specific camera.

        Raises RuntimeError if `label` is not a camera device or does not exist.
        """
    # these overloads don't work for python
    # def getROI(self, x: int, y: int, xSize: int, ySize: int) -> None: ...
    # def getROI(self, label: str, x: int, y: int, xSize: int, ySize: int) -> None: ...
    def getSerialPortAnswer(self, portLabel: str, term: str) -> str:
        """Continuously read from the serial port until the terminating sequence is
        encountered."""
    def getShutterDevice(self) -> DeviceLabel | Literal[""]:
        """Returns the label of the currently selected shutter device.

        Returns empty string if no shutter device is selected.
        """
    @overload
    def getShutterOpen(self) -> bool:
        """Returns the state of the currently selected (default) shutter."""
    @overload
    def getShutterOpen(self, shutterLabel: DeviceLabel | str) -> bool:
        """Returns the state of the specified shutter."""
    def getSLMBytesPerPixel(self, slmLabel: DeviceLabel | str) -> int:
        """Returns the number of bytes per SLM pixel"""
    def getSLMDevice(self) -> DeviceLabel | Literal[""]:
        """Returns the label of the currently selected SLM device.

        Returns empty string if no SLM device is selected.
        """
    def getSLMExposure(self, slmLabel: DeviceLabel | str) -> float:
        """Returns the exposure time that will be used by the SLM for illumination"""
    def getSLMHeight(self, slmLabel: DeviceLabel | str) -> int:
        """Returns the height (in "pixels") of the SLM"""
    def getSLMNumberOfComponents(self, slmLabel: DeviceLabel | str) -> int:
        """Returns the number of components (usually these depict colors) of the SLM.

        For instance, an RGB projector will return 3, but a grey scale SLM returns 1"""
    def getSLMSequenceMaxLength(self, slmLabel: DeviceLabel | str) -> int:
        """For SLMs that support sequences, returns the maximum length of the sequence
        that can be uploaded to the device"""
    def getSLMWidth(self, slmLabel: DeviceLabel | str) -> int:
        """Returns the width (in "pixels") of the SLM"""
    def getStageSequenceMaxLength(self, stageLabel: DeviceLabel | str) -> int:
        """Gets the maximum length of a stage's position sequence."""
    def getState(self, stateDeviceLabel: DeviceLabel | str) -> int:
        """Returns the current state (position) on the specific device."""
    def getStateFromLabel(
        self, stateDeviceLabel: DeviceLabel | str, stateLabel: StateLabel | str
    ) -> int:
        """Obtain the state for a given label."""
    def getStateLabel(self, stateDeviceLabel: DeviceLabel | str) -> StateLabel:
        """Returns the current state as the label (string)."""
    def getStateLabels(
        self, stateDeviceLabel: DeviceLabel | str
    ) -> Tuple[StateLabel, ...]:
        """Return labels for all states"""
    def getSystemState(self) -> Configuration:
        """Returns the entire system state, i.e."""
    def getSystemStateCache(self) -> Configuration:
        """Returns the entire system state, i.e."""
    def getTimeoutMs(self) -> int:
        """Get the timeout for all wait commands.

        (Default is 5000 ms)
        """
    def getVersionInfo(self) -> str:
        """Displays core version."""
    @overload
    def getXPosition(self) -> float:
        """Obtains the current position of the X axis of the XY stage in microns."""
    @overload
    def getXPosition(self, xyStageLabel: DeviceLabel | str) -> float:
        """Obtains the current position of the X axis of the XY stage in microns."""
    @overload
    def getXYPosition(self) -> Sequence[float]:  # always 2-element list, but not tuple
        """Obtains the current position of the XY stage in microns."""
    @overload
    def getXYPosition(self, xyStageLabel: DeviceLabel | str) -> Sequence[float]: ...
    def getXYStageDevice(self) -> DeviceLabel | Literal[""]:
        """Returns the label of the currently selected XYStage device.

        Returns empty string if no XYStage device is selected.
        """
    def getXYStageSequenceMaxLength(self, xyStageLabel: DeviceLabel | str) -> int:
        """Gets the maximum length of an XY stage's position sequence."""
    @overload
    def getYPosition(self) -> float:
        """Obtains the current position of the Y axis of the XY stage in microns."""
    @overload
    def getYPosition(self, xyStageLabel: DeviceLabel | str) -> float:
        """Obtains the current position of the Y axis of the XY stage in microns."""
    def hasProperty(
        self, label: DeviceLabel | str, propName: PropertyName | str
    ) -> bool:
        """Checks if device has a property with a specified name."""
    def hasPropertyLimits(
        self, label: DeviceLabel | str, propName: PropertyName | str
    ) -> bool:
        """Queries device if the specific property has limits."""
    def home(self, xyOrZStageLabel: DeviceLabel | str) -> None:
        """Perform a hardware homing operation for an XY or focus/Z stage."""
    def incrementalFocus(self) -> None:
        """Performs incremental focus for the one-shot focusing device."""
    def initializeAllDevices(self) -> None:
        """Calls Initialize() method for each loaded device.

        See `ParallelDeviceInitialization` feature flag for controlling the order of
        initialization.
        """
    def initializeCircularBuffer(self) -> None:
        """Initialize circular buffer based on the current camera settings."""
    def initializeDevice(self, label: DeviceLabel | str) -> None:
        """Initializes specific device."""
    def getDeviceInitializationState(
        self, label: DeviceLabel | str
    ) -> DeviceInitializationState:
        """Queries the initialization state of the given device."""
    def isBufferOverflowed(self) -> bool:
        """Indicates whether the circular buffer is overflowed"""
    def isConfigDefined(self, groupName: str, configName: str) -> bool:
        """Checks if the configuration already exists within a group.

        If either the groupName or configName are not recognized, returns False.
        """
    def isContinuousFocusDrive(self, stageLabel: DeviceLabel | str) -> bool:
        """Check if a stage has continuous focusing capability.

        (positions can be set while continuous focus runs)."""
    def isContinuousFocusEnabled(self) -> bool:
        """Checks if the continuous focusing hardware device is ON or OFF."""
    def isContinuousFocusLocked(self) -> bool:
        """Returns the lock-in status of the continuous focusing device."""
    def isExposureSequenceable(self, cameraLabel: DeviceLabel | str) -> bool:
        """Queries camera if exposure can be used in a sequence"""
    def isFeatureEnabled(self, name: str) -> bool:
        """Return whether the given Core feature is currently enabled.

        See `enableFeature()` for the available features.

        Raises RuntimeError if the feature name is not recognized.
        """
    def isGroupDefined(self, groupName: str) -> bool:
        """Checks if the group already exists."""
    def isMultiROIEnabled(self) -> bool:
        """Queries the camera to determine if multiple ROIs are currently set."""
    def isMultiROISupported(self) -> bool:
        """Queries the camera to determine if it supports multiple ROIs."""
    def isPixelSizeConfigDefined(self, resolutionID: str) -> bool:
        """Checks if the Pixel Size Resolution already exists"""
    def isPropertyPreInit(
        self, label: DeviceLabel | str, propName: PropertyName | str
    ) -> bool:
        """Tells us whether the property must be defined prior to initialization."""
    def isPropertyReadOnly(
        self, label: DeviceLabel | str, propName: PropertyName | str
    ) -> bool:
        """Tells us whether the property can be modified."""
    def isPropertySequenceable(
        self, label: DeviceLabel | str, propName: PropertyName | str
    ) -> bool:
        """Queries device if the specified property can be used in a sequence"""
    @overload
    def isSequenceRunning(self) -> bool:
        """Check if the current camera is acquiring the sequence.

        Returns false when the sequence is done"""
    @overload
    def isSequenceRunning(self, cameraLabel: DeviceLabel | str) -> bool:
        """Check if the specified camera is acquiring the sequence.

        Returns false when the sequence is done"""
    def isStageLinearSequenceable(self, stageLabel: DeviceLabel | str) -> bool:
        """Queries if the stage can be used in a linear sequence.

        A linear sequence is defined by a stepsize and number of slices"""
    def isStageSequenceable(self, stageLabel: DeviceLabel | str) -> bool:
        """Queries stage if it can be used in a sequence"""
    def isXYStageSequenceable(self, xyStageLabel: DeviceLabel | str) -> bool:
        """Queries XY stage if it can be used in a sequence"""
    def loadDevice(
        self, label: str, moduleName: AdapterName | str, deviceName: DeviceName | str
    ) -> None:
        """Loads a device from the plugin library."""
    def loadExposureSequence(
        self, cameraLabel: DeviceLabel | str, exposureSequence_ms: Sequence[float]
    ) -> None:
        """Transfer a sequence of exposure times to the camera."""
    def loadGalvoPolygons(self, galvoLabel: DeviceLabel | str) -> None:
        """Load a set of galvo polygons to the device"""
    def loadPropertySequence(
        self,
        label: DeviceLabel | str,
        propName: PropertyName | str,
        eventSequence: Sequence[str],
    ) -> None:
        """Transfer a sequence of events/states/whatever to the device.

        This should only be called for device-properties that are sequenceable
        """
    def loadSLMSequence(
        self, slmLabel: DeviceLabel | str, imageSequence: List[bytes]
    ) -> None:
        """Load a sequence of images into the SLM"""
    def loadStageSequence(
        self, stageLabel: DeviceLabel | str, positionSequence: Sequence[float]
    ) -> None:
        """Transfer a sequence of events/states/whatever to the device.

        This should only be called for device-properties that are sequenceable"""
    def loadSystemConfiguration(self, fileName: str) -> None:
        """Loads the system configuration from the text file conforming to the
        MM specific format."""
    def loadSystemState(self, fileName: str) -> None:
        """Loads the system configuration from the text file conforming to the
        MM specific format."""
    def loadXYStageSequence(
        self,
        xyStageLabel: DeviceLabel | str,
        xSequence: Sequence[float],
        ySequence: Sequence[float],
    ) -> None:
        """Transfer a sequence of stage positions to the xy stage.

        xSequence and ySequence must have the same length. This should only be called
        for XY stages that are sequenceable
        """
    @overload
    def logMessage(self, msg: str) -> None:
        """Record text message in the log file."""
    @overload
    def logMessage(self, msg: str, debugOnly: bool) -> None:
        """Record text message in the log file."""
    def noop(self) -> None:
        """A static method that does nothing."""
    def pointGalvoAndFire(
        self, galvoLabel: DeviceLabel | str, x: float, y: float, pulseTime_us: float
    ) -> None:
        """Set the Galvo to an x,y position and fire the laser for a predetermined duration."""
    def popNextImage(self) -> np.ndarray:
        """Gets and removes the next image from the circular buffer."""
    @overload
    def popNextImageMD(self, channel: int, slice: int, md: Metadata) -> np.ndarray: ...
    @overload
    def popNextImageMD(self, md: Metadata) -> np.ndarray:
        """Gets and removes the next image (and metadata) from the circular buffer"""
    def prepareSequenceAcquisition(self, cameraLabel: DeviceLabel | str) -> None:
        """Prepare the camera for the sequence acquisition to save the time in the

        StartSequenceAcqusition() call which is supposed to come next."""
    def readFromSerialPort(self, portLabel: str) -> List[str]:  # charvector
        """Reads the contents of the Rx buffer."""
    def registerCallback(self, cb: MMEventCallback) -> None:
        """Register a callback (listener class)."""
    def renameConfig(
        self,
        groupName: ConfigGroupName | str,
        oldConfigName: ConfigPresetName | str,
        newConfigName: str,
    ) -> None:
        """Renames a configuration within a specified group.

        The command will fail if the configuration was not previously defined.
        """
    def renameConfigGroup(
        self, oldGroupName: ConfigGroupName | str, newGroupName: str
    ) -> None:
        """Renames a configuration group."""
    def renamePixelSizeConfig(
        self, oldConfigName: PixelSizeConfigName | str, newConfigName: str
    ) -> None:
        """Renames a pixel size configuration."""
    def reset(self) -> None:
        """Unloads all devices from the core, clears all configuration data and property
        blocks."""
    def runGalvoPolygons(self, galvoLabel: DeviceLabel | str) -> None:
        """Run a loop of galvo polygons"""
    def runGalvoSequence(self, galvoLabel: DeviceLabel | str) -> None:
        """Run a sequence of galvo positions"""
    def saveSystemConfiguration(self, fileName: str) -> None:
        """Saves the current system configuration to a text file of the MM specific format."""
    def saveSystemState(self, fileName: str) -> None:
        """Saves the current system state to a text file of the MM specific format."""
    @overload
    def setAdapterOrigin(self, newZUm: float) -> None:
        """Enable software translation of coordinates for the current focus/Z stage."""
    @overload
    def setAdapterOrigin(self, stageLabel: DeviceLabel | str, newZUm: float) -> None:
        """Enable software translation of coordinates for the given focus/Z stage."""
    @overload
    def setAdapterOriginXY(self, newXUm: float, newYUm: float) -> None:
        """Enable software translation of coordinates for the current XY stage.

        The current position of the stage becomes (newXUm, newYUm). It is recommended
        that setOriginXY() be used instead where available."""
    @overload
    def setAdapterOriginXY(
        self, xyStageLabel: DeviceLabel | str, newXUm: float, newYUm: float
    ) -> None: ...
    def setAutoFocusDevice(self, focusLabel: DeviceLabel | str) -> None:
        """Sets the current auto-focus device."""
    def setAutoFocusOffset(self, offset: float) -> None:
        """Applies offset the one-shot focusing device."""
    def setAutoShutter(self, state: bool) -> None:
        """If this option is enabled Shutter automatically opens and closes when the
        image is acquired."""
    def setCameraDevice(self, cameraLabel: DeviceLabel | str) -> None:
        """Sets the current camera device."""
    def setChannelGroup(self, channelGroup: ConfigGroupName | str) -> None:
        """Specifies the group determining the channel selection."""
    def setCircularBufferMemoryFootprint(self, sizeMB: int) -> None:
        """Reserve memory for the circular buffer."""
    def setConfig(
        self, groupName: ConfigGroupName | str, configName: ConfigPresetName | str
    ) -> None:
        """Applies a configuration to a group."""
    def setDeviceAdapterSearchPaths(self, paths: Sequence[str]) -> None:
        """Set the device adapter search paths."""
    def setDeviceDelayMs(self, label: DeviceLabel | str, delayMs: float) -> None:
        """Overrides the built-in value for the action delay."""
    @overload
    def setExposure(self, exp: float) -> None:
        """Sets the exposure setting of the current camera in milliseconds."""
    @overload
    def setExposure(self, cameraLabel: DeviceLabel | str, dExp: float) -> None:
        """Sets the exposure setting of the specified camera in milliseconds."""
    def setFocusDevice(self, focusLabel: DeviceLabel | str) -> None:
        """Sets the current focus device."""
    def setFocusDirection(self, stageLabel: DeviceLabel | str, sign: int) -> None:
        """Set the focus direction of a stage."""
    def setGalvoDevice(self, galvoLabel: DeviceLabel | str) -> None:
        """Sets the current galvo device."""
    def setGalvoIlluminationState(
        self, galvoLabel: DeviceLabel | str, on: bool
    ) -> None:
        """Set the galvo's illumination state to on or off"""
    def setGalvoPolygonRepetitions(
        self, galvoLabel: DeviceLabel | str, repetitions: int
    ) -> None:
        """Set the number of times to loop galvo polygons"""
    def setGalvoPosition(
        self, galvoLabel: DeviceLabel | str, x: float, y: float
    ) -> None:
        """Set the Galvo to an x,y position."""
    def setGalvoSpotInterval(
        self, galvoLabel: DeviceLabel | str, pulseTime_us: float
    ) -> None:
        """Set the SpotInterval for the specified galvo device."""
    def setImageProcessorDevice(self, procLabel: DeviceLabel | str) -> None:
        """Sets the current image processor device."""
    # this overload does not appear to be present
    # @overload
    # def setMultiROI(self, rects: List[Any]) -> None: ...
    # @overload
    def setMultiROI(
        self,
        xs: Sequence[int],
        ys: Sequence[int],
        widths: Sequence[int],
        heights: Sequence[int],
    ) -> None:
        """Set multiple ROIs for the current camera device.

        Will fail if the camera does not support multiple ROIs, any widths or heights
        are non-positive, or if the vectors do not all have the same length.
        """
    @overload
    def setOrigin(self) -> None:
        """Zero the current focus/Z stage's coordinates at the current position."""
    @overload
    def setOrigin(self, stageLabel: DeviceLabel | str) -> None:
        """Zero the given focus/Z stage's coordinates at the current position."""
    @overload
    def setOriginX(self) -> None:
        """Zero the given XY stage's X coordinate at the current position."""
    @overload
    def setOriginX(self, xyStageLabel: DeviceLabel | str) -> None:
        """Zero the given XY stage's X coordinate at the current position."""
    @overload
    def setOriginXY(self) -> None:
        """Zero the current XY stage's coordinates at the current position."""
    @overload
    def setOriginXY(self, xyStageLabel: DeviceLabel | str) -> None:
        """Zero the given XY stage's coordinates at the current position."""
    @overload
    def setOriginY(self) -> None:
        """Zero the given XY stage's Y coordinate at the current position."""
    @overload
    def setOriginY(self, xyStageLabel: DeviceLabel | str) -> None:
        """Zero the given XY stage's Y coordinate at the current position."""
    def setParentLabel(
        self, deviceLabel: DeviceLabel | str, parentHubLabel: DeviceLabel | str
    ) -> None:
        """Sets parent device label"""
    def setPixelSizeAffine(
        self, resolutionID: PixelSizeConfigName | str, affine: Sequence[float]
    ) -> None:
        """Sets the raw affine transform for the specific pixel size configuration.

        The affine transform consists of the first two rows of a 3x3 matrix,
        the third row is alsways assumed to be 0.0 0.0 1.0."""
    def setPixelSizeConfig(self, resolutionID: PixelSizeConfigName | str) -> None:
        """Applies a Pixel Size Configuration."""
    def setPixelSizeUm(
        self, resolutionID: PixelSizeConfigName | str, pixSize: float
    ) -> None:
        """Sets pixel size in microns for the specified resolution sensing
        configuration preset."""
    @overload
    def setPosition(self, position: float) -> None:
        """Sets the position of the current FocusDevice in microns."""
    @overload
    def setPosition(self, stageLabel: DeviceLabel | str, position: float) -> None:
        """Sets the position of the stage in microns."""
    @overload
    def setPrimaryLogFile(self, filename: str) -> None: ...
    @overload
    def setPrimaryLogFile(self, filename: str, truncate: bool) -> None:
        """Set the primary Core log file."""
    def setProperty(
        self,
        label: DeviceLabel | str,
        propName: PropertyName | str,
        propValue: Union[bool, float, int, str],
    ) -> None:
        """Changes the value of the device property."""
    @overload
    def setRelativePosition(self, d: float) -> None:
        """Sets the relative position of the stage in microns."""
    @overload
    def setRelativePosition(self, stageLabel: DeviceLabel | str, d: float) -> None:
        """Sets the relative position of the stage in microns."""
    @overload
    def setRelativeXYPosition(self, dx: float, dy: float) -> None:
        """Sets the relative position of the XY stage in microns."""
    @overload
    def setRelativeXYPosition(
        self, xyStageLabel: DeviceLabel | str, dx: float, dy: float
    ) -> None:
        """Sets the relative position of the XY stage in microns."""
    @overload
    def setROI(self, x: int, y: int, xSize: int, ySize: int) -> None:
        """Set the hardware region of interest for the current/specified camera.

        A successful call to this method will clear any images in the sequence buffer,
        even if the ROI does not change.

        If multiple ROIs are set prior to this call, they will be replaced by the new
        single ROI.

        The coordinates are in units of binned pixels. That is, conceptually, binning is
        applied before the ROI.
        """
    @overload
    def setROI(
        self, label: DeviceLabel | str, x: int, y: int, xSize: int, ySize: int
    ) -> None:
        """Set the hardware region of interest for the current camera."""
    def setSerialPortCommand(self, portLabel: str, command: str, term: str) -> None:
        """Send string to the serial device and return an answer."""
    def setSerialProperties(
        self,
        portName: str,
        answerTimeout: str,
        baudRate: str,
        delayBetweenCharsMs: str,
        handshaking: str,
        parity: str,
        stopBits: str,
    ) -> None:
        """Sets all com port properties in a single call."""
    def setShutterDevice(self, shutterLabel: DeviceLabel | str) -> None:
        """the current shutter device."""
    @overload
    def setShutterOpen(self, state: bool) -> None:
        """Opens or closes the currently selected (default) shutter."""
    @overload
    def setShutterOpen(self, shutterLabel: DeviceLabel | str, state: bool) -> None:
        """Opens or closes the specified shutter."""
    def setSLMDevice(self, slmLabel: DeviceLabel | str) -> None:
        """Sets the current slm device."""
    def setSLMExposure(self, slmLabel: DeviceLabel | str, exposure_ms: float) -> None:
        """For SLM devices with build-in light source (such as projectors),
        this will set the exposure time, but not (yet) start the illumination"""
    @overload
    def setSLMImage(
        self, slmLabel: DeviceLabel | str, pixels: npt.NDArray[np.uint8]
    ) -> None:
        """Write an image to the SLM .

        When passing a numpy array, `pixels` must be one of the following:

        - a 2D numpy array [h,w] of uint8s, representing a grayscale image to write
          to the SLM.
        - a 3D numpy array [h,w,3] of uint8s with 3 color channels [R,G,B], representing
          an imgRGB32 image to write to the SLM.

        In both cases, the dimensions of the array should match the width and height
        of the SLM.

        !!! warning

            SLM might convert grayscale to binary internally.
        """
    @overload
    def setSLMImage(self, slmLabel: DeviceLabel | str, pixels: Any) -> None:
        """Write a list of chars to the SLM.

        Length of the list must match the number of pixels (or 4 * number of
        pixels to write an imgRGB32.)
        """
    @overload
    def setSLMPixelsTo(self, slmLabel: DeviceLabel | str, intensity: int) -> None:
        """Set all SLM pixels to a single 8-bit intensity."""
    @overload
    def setSLMPixelsTo(
        self, slmLabel: DeviceLabel | str, red: int, green: int, blue: int
    ) -> None:
        """Set all SLM pixels to an RGB color."""
    def setStageLinearSequence(
        self, stageLabel: DeviceLabel | str, dZ_um: float, nSlices: int
    ) -> None:
        """Loads a linear sequence (defined by stepsize and nr. of steps) into the device."""
    def setState(self, stateDeviceLabel: DeviceLabel | str, state: int) -> None:
        """Sets the state (position) on the specific device."""
    def setStateLabel(
        self, stateDeviceLabel: DeviceLabel | str, stateLabel: StateLabel | str
    ) -> None:
        """Sets device state using the previously assigned label (string)."""
    def setSystemState(self, conf: Configuration) -> None:
        """Sets all properties contained in the Configuration object."""
    def setTimeoutMs(self, timeoutMs: int) -> None:
        """Sets the timeout for all wait commands.

        (Default is 5000 ms)
        """
    @overload
    def setXYPosition(self, x: float, y: float) -> None:
        """Sets the position of the XY stage in microns."""
    @overload
    def setXYPosition(
        self, xyStageLabel: DeviceLabel | str, x: float, y: float
    ) -> None: ...
    def setXYStageDevice(self, xyStageLabel: DeviceLabel | str) -> None:
        """Sets the current XY device."""
    def sleep(self, intervalMs: float) -> None:
        """Waits (blocks the calling thread) for specified time in milliseconds."""
    def snapImage(self) -> None:
        """Acquires a single image with current settings."""
    def startContinuousSequenceAcquisition(self, intervalMs: float) -> None:
        """Starts the continuous camera sequence acquisition."""
    def startExposureSequence(self, cameraLabel: DeviceLabel | str) -> None:
        """Starts an ongoing sequence of triggered exposures in a camera.

        This should only be called for cameras where exposure time is sequenceable"""
    def startPropertySequence(
        self, label: DeviceLabel | str, propName: PropertyName | str
    ) -> None:
        """Starts an ongoing sequence of triggered events in a property of a device.

        This should only be called for device-properties that are sequenceable"""
    @overload
    def startSecondaryLogFile(self, filename: str, enableDebug: bool) -> int:
        """Start capturing logging output into an additional file."""
    @overload
    def startSecondaryLogFile(
        self, filename: str, enableDebug: bool, truncate: bool
    ) -> int: ...
    @overload
    def startSecondaryLogFile(
        self, filename: str, enableDebug: bool, truncate: bool, synchronous: bool
    ) -> int: ...
    @overload
    def startSequenceAcquisition(
        self, numImages: int, intervalMs: float, stopOnOverflow: bool
    ) -> None: ...
    @overload
    def startSequenceAcquisition(
        self,
        cameraLabel: DeviceLabel | str,
        numImages: int,
        intervalMs: float,
        stopOnOverflow: bool,
    ) -> None: ...
    def startSLMSequence(self, slmLabel: DeviceLabel | str) -> None:
        """Starts the sequence previously uploaded to the SLM"""
    def startStageSequence(self, stageLabel: DeviceLabel | str) -> None:
        """Starts an ongoing sequence of triggered events in a stage.

        This should only be called for stages"""
    def startXYStageSequence(self, xyStageLabel: DeviceLabel | str) -> None:
        """Starts an ongoing sequence of triggered events in an XY stage.

        This should only be called for stages"""
    def stderrLogEnabled(self) -> bool:
        """Indicates whether logging output goes to stdErr"""
    def stop(self, xyOrZStageLabel: DeviceLabel | str) -> None:
        """Stop the XY or focus/Z stage motors"""
    def stopExposureSequence(self, cameraLabel: DeviceLabel | str) -> None:
        """Stops an ongoing sequence of triggered exposures in a camera.

        This should only be called for cameras where exposure time is sequenceable"""
    def stopPropertySequence(
        self, label: DeviceLabel | str, propName: PropertyName | str
    ) -> None:
        """Stops an ongoing sequence of triggered events in a property of a device.

        This should only be called for device-properties that are sequenceable"""
    def stopSecondaryLogFile(self, handle: int) -> None:
        """Stop capturing logging output into an additional file."""
    @overload
    def stopSequenceAcquisition(self) -> None:
        """Stops streaming camera sequence acquisition."""
    @overload
    def stopSequenceAcquisition(self, cameraLabel: DeviceLabel | str) -> None:
        """Stops streaming camera sequence acquisition for a specified camera."""
    def stopSLMSequence(self, slmLabel: DeviceLabel | str) -> None:
        """Stops the SLM sequence if previously started"""
    def stopStageSequence(self, stageLabel: DeviceLabel | str) -> None:
        """Stops an ongoing sequence of triggered events in a stage.

        This should only be called for stages that are sequenceable"""
    def stopXYStageSequence(self, xyStageLabel: DeviceLabel | str) -> None:
        """Stops an ongoing sequence of triggered events in an XY stage.

        This should only be called for stages that are sequenceable"""
    def supportsDeviceDetection(self, deviceLabel: DeviceLabel | str) -> bool:
        """Return whether or not the device supports automatic device detection (i.e."""
    def systemBusy(self) -> bool:
        """Checks the busy status of the entire system."""
    def unloadAllDevices(self) -> None:
        """Unloads all devices from the core and resets all configuration data."""
    def unloadDevice(self, label: DeviceLabel | str) -> None:
        """Unloads the device from the core and adjusts all configuration data."""
    def unloadLibrary(self, moduleName: AdapterName | str) -> None:
        """Forcefully unload a library."""
    def updateCoreProperties(self) -> None:
        """Updates CoreProperties (currently all Core properties are devices types) with
        the loaded hardware."""
    def updateSystemStateCache(self) -> None:
        """Updates the state of the entire hardware."""
    def usesDeviceDelay(self, label: DeviceLabel | str) -> bool:
        """Signals if the device will use the delay setting or not."""
    def waitForConfig(
        self, group: ConfigGroupName | str, configName: ConfigPresetName | str
    ) -> None:
        """Blocks until all devices included in the configuration become ready."""
    def waitForDevice(self, label: DeviceLabel | str) -> None:
        """Waits (blocks the calling thread) until the specified device becomes non-busy."""
    def waitForDeviceType(self, devType: DeviceType) -> None:
        """Blocks until all devices of the specific type become ready (not-busy)."""
    def waitForSystem(self) -> None:
        """Blocks until all devices in the system become ready (not-busy)."""
    def writeToSerialPort(self, portLabel: str, data: bytes) -> None:
        """Sends an array of characters to the serial port and returns immediately."""

    def pressurePumpStop(self, pumpLabel: str) -> None:
        """Stops the pressure pump."""
    def pressurePumpCalibrate(self, pumpLabel: str) -> None:
        """Calibrates the pressure pump."""
    def pressurePumpRequiresCalibration(self, pumpLabel: str) -> bool:
        """Return True if pump requires calibration before operation."""
    def setPumpPressureKPa(self, pumpLabel: str, pressure: float) -> None:
        """Sets the pressure of the pump in kPa."""
    def getPumpPressureKPa(self, pumpLabel: str) -> float:
        """Return the pressure of the pump in kPa."""

    def volumetricPumpStop(self, pumpLabel: str) -> None:
        """Stops the volumetric pump."""
    def volumetricPumpHome(self, pumpLabel: str) -> None:
        """Homes the volumetric pump."""
    def volumetricPumpRequiresHoming(self, pumpLabel: str) -> bool:
        """Return True if the volumetric pump requires homing."""
    def invertPumpDirection(self, pumpLabel: str, invert: bool) -> None:
        """Sets whether the pump direction needs to be inverted"""
    def isPumpDirectionInverted(self, pumpLabel: str) -> bool:
        """Return True if pump direction needs to be inverted"""
    def setPumpVolume(self, pumpLabel: str, volume: float) -> None:
        """Sets the volume of fluid in the pump in uL.

        Note it does not withdraw upto this amount. It is merely to inform MM
        of the volume in a prefilled pump.
        """
    def getPumpVolume(self, pumpLabel: str) -> float:
        """Return the fluid volume in the pump in uL"""
    def setPumpMaxVolume(self, pumpLabel: str, volume: float) -> None:
        """Set the max volume of the pump in uL"""
    def getPumpMaxVolume(self, pumpLabel: str) -> float:
        """Return max volume of the pump in uL"""
    def setPumpFlowrate(self, pumpLabel: str, volume: float) -> None:
        """Set the flowrate of the pump in uL per second"""
    def getPumpFlowrate(self, pumpLabel: str) -> float:
        """Return the flowrate of the pump in uL per second"""
    def pumpStart(self, pumpLabel: str) -> None:
        """Start dispensing until syringe is empty, or manually stopped.

        (whichever occurs first).
        """
    def pumpDispenseDurationSeconds(self, pumpLabel: str, seconds: float) -> None:
        """Dispenses for the provided duration (in seconds) at the set flowrate."""
    def pumpDispenseVolumeUl(self, pumpLabel: str, microLiter: float) -> None:
        """Dispenses the provided volume (in uL) at the set flowrate."""

    # These are in MMCoreJ, not pymmcore
    # def getTaggedImage(self) -> TaggedImage: ...
    # def getTaggedImage(self, cameraChannelIndex: int) -> TaggedImage: ...
    # def getNBeforeLastTaggedImage(self, n: int) -> TaggedImage: ...
    # def getLastTaggedImage(self) -> TaggedImage: ...
    # def getLastTaggedImage(self,cameraChannelIndex: int) -> TaggedImage: ...
    # def popNextTaggedImage(self) -> TaggedImage: ...
    # def popNextTaggedImage(self, cameraChannelIndex: int) -> TaggedImage: ...
    # def getPixelSizeAffineAsString(self) -> str:
    # """Convenience function."""
    # https://github.com/micro-manager/pymmcore/issues/65
    # @overload
    # def getXYStagePosition(self) -> List[float]:
    #     """Convenience function: returns the current XY position of the current
    #     XY stage device as a Point2D.Double."""
    # @overload
    # def getXYStagePosition(self, stage: str) -> List[float]: ...

ErrorCode = int

class CMMError:
    @overload
    def __init__(self, msg: str, code: ErrorCode = 1): ...
    @overload
    def __init__(self, msg: str, code: ErrorCode, underlyingError: CMMError): ...
    @overload
    def __init__(self, msg: str, underlyingError: CMMError): ...
    @overload
    def __init__(self, other: CMMError): ...
    def getCode(self) -> ErrorCode: ...
    def getFullMsg(self) -> str: ...
    def getMsg(self) -> str: ...
    def getSpecificCode(self) -> ErrorCode: ...
    def getUnderlyingError(self) -> CMMError: ...
    def what(self) -> str: ...

class Configuration:
    """Encapsulation of the configuration information.

    Designed to be wrapped by SWIG. A collection of configuration settings."""

    def __init__(self) -> None: ...
    def addSetting(self, setting: PropertySetting) -> None:
        """Adds new property setting to the existing contents."""
    def deleteSetting(self, device: str, prop: str) -> None:
        """Removes property setting, specified by device and property names, from the configuration."""
    @overload
    def getSetting(self, index: int) -> PropertySetting:
        """Returns the setting with specified index."""
    @overload
    def getSetting(self, device: str, prop: str) -> PropertySetting:
        """Get the setting with specified device name and property name."""
    def getVerbose(self) -> str:
        """Returns verbose description of the object's contents."""
    def isConfigurationIncluded(self, cfg: Configuration) -> bool:
        """Checks whether a configuration is included.

        Included means that all devices from the operand configuration are included
        and that settings match,"""
    def isPropertyIncluded(self, device: str, prop: str) -> bool:
        """Checks whether the property is included in the configuration."""
    def isSettingIncluded(self, ps: PropertySetting) -> bool:
        """Checks whether the setting is included in the configuration."""
    def size(self) -> int:
        """Returns the number of settings."""

class MetadataTag:
    def Clone(self) -> MetadataTag: ...
    def GetDevice(self) -> str: ...
    def GetName(self) -> str: ...
    def GetQualifiedName(self) -> str: ...
    def IsReadOnly(self) -> bool: ...
    def Restore(self, stream: str) -> bool: ...
    def Serialize(self) -> str: ...
    def SetDevice(self, device: str) -> None: ...
    def SetName(self, name: str) -> None: ...
    def SetReadOnly(self, ro: bool) -> None: ...
    def ToArrayTag(self) -> MetadataArrayTag: ...
    def ToSingleTag(self) -> MetadataSingleTag: ...

class MetadataArrayTag(MetadataTag):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, name: str, device: str, readOnly: bool): ...
    def AddValue(self, val: str): ...
    def GetSize(self) -> int: ...
    def GetValue(self) -> str: ...
    def SetValue(self, val: str, idx: int) -> str: ...

class MetadataSingleTag(MetadataTag):
    @overload
    def __init__(self): ...
    @overload
    def __init__(self, name: str, device: str, readOnly: bool): ...
    def GetValue(self) -> str: ...
    def SetValue(self, val: str) -> str: ...

class Metadata:
    def Clear(self) -> None: ...
    def Dump(self) -> str: ...
    def GetArrayTag(self, key: str) -> MetadataArrayTag: ...
    def GetKeys(self) -> str: ...
    def GetSingleTag(self, key: str) -> MetadataSingleTag: ...
    def HasTag(self, key: str) -> bool: ...
    def Merge(self, newTags: Metadata) -> None: ...
    def RemoveTag(self, key: str) -> None: ...
    def Restore(self, stream: str) -> bool: ...
    def Serialize(self) -> str: ...
    def SetTag(self, tag: MetadataTag) -> None: ...
    def readLine(self, iss) -> str: ...

class MetadataError:
    def __init__(self, msg: str) -> None: ...
    def getMsg(self) -> str: ...

class MetadataKeyError(MetadataError):
    def __init__(self) -> None: ...

class MetadataIndexError(MetadataError):
    def __init__(self) -> None: ...

class MMEventCallback:
    def __init__(self) -> None: ...
    def onChannelGroupChanged(self, newChannelGroupName: str) -> None: ...
    def onConfigGroupChanged(self, groupName: str, newConfigName: str) -> None: ...
    def onExposureChanged(self, name: str, newExposure: float) -> None: ...
    def onPixelSizeAffineChanged(
        self, v0: float, v1: float, v2: float, v3: float, v4: float, v5: float
    ) -> None: ...
    def onPixelSizeChanged(self, newPixelSizeUm: float) -> None: ...
    def onPropertiesChanged(
        self,
    ) -> None: ...
    def onPropertyChanged(self, name: str, propName: str, propValue: str) -> None: ...
    def onSLMExposureChanged(self, name: str, newExposure: float) -> None: ...
    def onStagePositionChanged(self, name: str, pos: float) -> None: ...
    def onSystemConfigurationLoaded(
        self,
    ) -> None: ...
    def onXYStagePositionChanged(self, name: str, xpos: float, ypos: float) -> None: ...

class PropertySetting:
    """Property setting defined as triplet: device - property - value."""

    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, deviceLabel: str, prop: str, value: str) -> None: ...
    @overload
    def __init__(
        self, deviceLabel: str, prop: str, value: str, readOnly: bool
    ) -> None: ...
    @staticmethod
    def generateKey(self, device: str, prop: str) -> str:
        """Returns `{device}-{prop}`."""
    def getDeviceLabel(self) -> DeviceLabel:
        """Returns the device label."""
    def getKey(self) -> str: ...
    def getPropertyName(self) -> PropertyName:
        """Returns the property name."""
    def getPropertyValue(self) -> str:
        """Returns the property value."""
    def getReadOnly(self) -> bool:
        """Returns the read-only status."""
    def getVerbose(self) -> str:
        """Returns verbose description of the object's contents."""
    def isEqualTo(self, ps: PropertySetting) -> bool:
        """Returns true if the settings are equal."""
    def __eq__(self, other: Any) -> bool:
        """prefer isEqualTo()."""
