# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['app.py'],
             pathex=['wvenv\\Lib\\site-packages', 'C:\\Users\\elvis\\Desktop\\Tronco', 'scripts'],
             binaries=[],
             datas=[('templates', 'templates'), ('static', 'static'), ('udpipe', 'udpipe'), ('scripts', 'scripts')],
             hiddenimports=['pkg_resources.py2_warn'],
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
          [],
          exclude_binaries=True,
          name='Tronco',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          icon='static/favicon.ico',
          console=False, uac_admin=True)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Tronco-Windows')
