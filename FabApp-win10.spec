# -*- mode: python ; coding: utf-8 -*-
import os
import PyInstaller.config

PyInstaller.config.CONF['distpath'] = './App/app-compile/win-x64/dist'
PyInstaller.config.CONF['workpath'] = './App/app-compile/win-x64/build'

block_cipher = None


a = Analysis(
    ['App/FabApp.py'],
    pathex=[],
    binaries=[],
    datas=[
        ( os.getcwd() + '/App/img/AP_logo.ico', 'dist/img'),
        ( os.getcwd() + '/App/img/AP_logo_256.png', 'dist/img')
        ],
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
    name='FabApp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    icon= os.getcwd() + '/App\\img\\AP_logo.ico',
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
