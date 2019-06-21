# -*- mode: python -*-

block_cipher = None


a = Analysis(['pdfConverterGui.py'],
             pathex=['/Users/eliavicentini/pdfconverter-dataanalyzer/Debug'],
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
          [],
          exclude_binaries=True,
          name='PdfConverter-DataAnalyzer',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='app.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='PdfConverter-DataAnalyzer')
app = BUNDLE(coll,
             name='PdfConverter-DataAnalyzer.app',
             icon='app.ico',
             bundle_identifier=None)