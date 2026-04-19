# These and other macros are documented in ../droid-configs-device/droid-configs.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device surya
%define vendor xiaomi

%define vendor_pretty Xiaomi
%define device_pretty Poco X3 NFC

# Community HW adaptations need this
%define community_adaptation 1

# Device-specific ofono configuration
Provides: ofono-configs
Obsoletes: ofono-configs-mer
Obsoletes: ofono-configs-binder

#Device-specific usb-moded configuration
Provides: usb-moded-configs
Obsoletes: usb-moded-defaults

# Pixel ratio 1.0 was originally jolla phone with 245ppi, and the devices
# should roughly have their ppi compared to that. Large displays can use
# bigger ratio if seen fit. Values are with 0.25 increments.
%define pixel_ratio 1.0

%include droid-configs-device/droid-configs.inc
%include patterns/patterns-sailfish-device-adaptation-surya.inc
%include patterns/patterns-sailfish-device-configuration-surya.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

