[app]

# (str) Title of your application
title = Kivy App

# (str) Package name
package.name = kivyapp

# (str) Package domain
package.domain = org.test

# (str) Source code folder
source.dir = main.py

# (list) Source files to include
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,json

# (list) Files to exclude
source.exclude_exts = spec

# (list) Excluded directories
source.exclude_dirs = tests, bin, venv, .git

# (str) Application version
version = 1.0

# (list) Application requirements
requirements = python3==3.10.11,kivy==2.2.1

# (str) Orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 1

# (int) Supported Android API
android.api = 33

# (int) Minimum API
android.minapi = 21

# (int) Android SDK version
android.sdk = 33

# (int) Android NDK version
android.ndk = 25b

# (str) Android NDK API
android.ndk_api = 21

# Accept licenses automatically
android.accept_sdk_license = True

# (list) Android architectures
android.archs = arm64-v8a, armeabi-v7a

# (bool) Use AndroidX
android.enable_androidx = True

# (str) Presplash image
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon
# icon.filename = %(source.dir)s/data/icon.png

# Permissions
android.permissions = INTERNET

# (bool) Accept SDK license
android.accept_sdk_license = True

# Log level
log_level = 2

# Enable backup
android.allow_backup = True

# Window size
window.width = 720
window.height = 1280

# (bool) Wake lock
android.wakelock = False

# (bool) Private storage
android.private_storage = True

# (str) Entry point
entrypoint = org.kivy.android.PythonActivity

# (str) Theme
android.apptheme = "@android:style/Theme.NoTitleBar"

# (bool) Skip update
android.skip_update = False

# (str) Bootstrap
p4a.bootstrap = sdl2

# (list) Extra arguments to p4a
p4a.extra_args = --copy-libs

# (bool) Copy libs
android.copy_libs = 1

# (str) Application category
category = Utility

# (str) Application author
author = Developer

# (str) Author email
author_email = example@email.com

# (str) Description
description = My Kivy Android Application

# (list) Services
# services =

# (bool) Debuggable
android.debug = True

# (bool) Release artifact
android.release_artifact = apk

# (str) Presplash color
android.presplash_color = #FFFFFF

# (bool) Numeric version

# Include patterns
source.include_patterns = assets/*,images/*

# Exclude patterns
source.exclude_patterns = README.md,*.pyc,__pycache__/*

# Kivy version
osx.kivy_version = 2.2.1

# Build mode
build_dir = .buildozer

# ---------------------------------------------------------------- #

[buildozer]

# (int) Log level
log_level = 2

# (int) Warn on root
warn_on_root = 1
