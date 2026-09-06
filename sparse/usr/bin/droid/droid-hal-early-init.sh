#!/bin/sh

touch /odm/lib64/libselinux_stubs.so; mount -o bind /usr/libexec/droid-hybris/system/lib64/libselinux_stubs.so /odm/lib64/libselinux_stubs.so
touch /product/lib64/libselinux_stubs.so; mount -o bind /usr/libexec/droid-hybris/system/lib64/libselinux_stubs.so /product/lib64/libselinux_stubs.so
