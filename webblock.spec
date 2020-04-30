# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['webblock.py'],
             pathex=['/Users/manu/Desktop/WebBlock'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='webblock',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='/Users/manu/Desktop/WebBlock/Cornmanthe3rd-Plex-Other-python.ico')
app = BUNDLE(exe,
             name='webblock.app',
             icon='/Users/manu/Desktop/WebBlock/Cornmanthe3rd-Plex-Other-python.ico',
             bundle_identifier=None)
