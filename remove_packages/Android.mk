LOCAL_PATH := $(call my-dir)
include $(CLEAR_VARS)
LOCAL_MODULE := remove_packages
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_OVERRIDES_PACKAGES := \
    Chrome \
    Chrome-Stub \
    Drive \
    Gmail2 \
    Maps \
    YouTube \
    YouTubeMusic \
    AICorePrebuilt-aicore_20250130.00_RC01 \
    BetterBugStub \
    DeviceIntelligenceNetworkPrebuilt-astrea_20240329.00_RC02 \
    SettingsIntelligenceGooglePrebuilt \
    WellbeingPrebuilt \
    ScribePrebuilt \
    Videos \
    ConfigUpdater \
    FilesPrebuilt \
    arcore-1.48 \
    MeetPrebuilt_20240128 \
    GoogleRestorePrebuilt-v793553 \
    PlayAutoInstallConfig \
    HealthIntelligencePrebuilt \
    GoogleFeedback \
    KidsSupervisionStub \
    SwitchAccessPrebuilt \
    TurboAdapter \
    TurboPrebuilt \
    talkback \
    YouTube \
    GoogleTTS \
    PrebuiltGmail \
    GoogleFeedback \
    TagGoogle \
    StorageManagerGoogle
LOCAL_UNINSTALLABLE_MODULE := true
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_SRC_FILES := /dev/null
include $(BUILD_PREBUILT)
