# pyinstaller pyarmor pyside demo

使用pyinstaller和pyarmor打包pyside程序示例。

## 环境

- Windows 10
- python38
- pyinstaller 5.1
- pyarmor 7.5.1
- pyside6 6.3.1

## 说明

使用pyinstaller和pyarmor加密打包python，以pyside6为例。

打包后再使用 pyinstxtractor.py 和 uncompyle6 进行反编译检查是否加密，可以看到反编译出来的pyc文件是加密后的文件。

在 main.spec 中使用下面方式加密方式后，则无法提取部分pyc代码，其后缀为`.pyc.encrypted`

```
block_cipher = pyi_crypto.PyiBlockCipher(key='your key')
```

pyinstxtractor.py 会报错

```
[!] Error: Failed to decompress XXX.pyc, probably encrypted. Extracting as is.
```

## 加密打包

    pyarmor pack -s main.spec src/main.py --clean -x " -r"

## 代码提取

    python pyinstxtractor.py dist\pyinstaller-pyarmorpyside-demo.exe

## 反编译

    uncompyle6 pyinstaller-pyarmorpyside-demo.exe_extracted\main.pyc > main.pyc
