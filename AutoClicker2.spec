# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['AutoClicker2.py'],
    pathex=[],
    binaries=[],
    datas=[],
hiddenimports=[
    'pynput',  # Include the main pynput module
],

    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
excludes=[
    'Xlib', 'Xlib.protocol', 'Xlib.X', 'Xlib.ext', 'Xlib.display', 
    'Xlib.keysymdef', 'Xlib.XK', 'evdev', 'evdev.events', 
    'AppKit', 'Quartz', 'CoreFoundation', 'HIServices', 'objc', 'posix', 
    'grp', 'pwd', 'fcntl', '_posixsubprocess', 'resource', 'StringIO', 'pep517'
],
    noarchive=True,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [('v', None, 'OPTION')],
    name='AutoClicker2',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
