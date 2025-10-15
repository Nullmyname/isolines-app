[app]
title = Изолинии
package.name = isolines
package.domain = org.geology

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf

version = 1.0
requirements = python3,kivy

orientation = portrait

[buildozer]
log_level = 2

[app]
presplash.filename = %(source.dir)s/presplash.png
icon.filename = %(source.dir)s/icon.png

[app]
android.permissions =
android.api = 33
android.minapi = 21

