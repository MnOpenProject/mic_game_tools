# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['start.py'],
    pathex=[],
    binaries=[],
    datas=[('templates', 'templates'), ('static', 'static'), ('auto_data_remember', 'auto_data_remember'), ('data_remember', 'data_remember'), ('common_util.py', '.'), ('config.py', '.'), ('eldenring_steam_copydata.py', '.'), ('eldenring_steam_deletecopydata.py', '.'), ('eldenring_steam_replacedata.py', '.'), ('eldenring_steam_replacedata_fromauto.py', '.'), ('flask_app.py', '.'), ('install_libs.py', '.'), ('main_func.py', '.'), ('route.py', '.'), ('start.py', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='start',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.ico'],
)