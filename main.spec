# -*- mode: python ; coding: utf-8 -*-
import os
import glob

APP_NAME = 'pyinstaller-pyarmorpyside-demo'
ICON_PATH = None


def get_all_pyfile():
    pyfile_list = glob.glob('src/*.py')
    pyfile_list.remove('src\\main.py')
    return pyfile_list


block_cipher = pyi_crypto.PyiBlockCipher(key='your key')
# block_cipher = None

# 需要一起打包的资源文件
added_files = [
    # ('src/icon.svg', '.'),
]

a = Analysis(
    [
        # 第一个是入口文件
        os.path.join('src', 'main.py'),
        # 需要把其他代码都加进来
        *get_all_pyfile()
    ],
    pathex=[os.path.join(os.getcwd(), 'src')],
    binaries=[],
    datas=added_files,
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
    # 打包后的文件名称
    name=APP_NAME,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    # 不显示控制台
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    # 图标
    icon=ICON_PATH,
)
