[app]
title = Изолинии
package.name = isolines
package.domain = org.geology

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf

version = 1.0
requirements = python3,kivy

orientation = portrait

presplash.filename = %(source.dir)s/presplash.png
icon.filename = %(source.dir)s/icon.png

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.sdk = 28
android.ndk = 25b

[buildozer]
log_level = 2
