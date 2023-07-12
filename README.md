# pyinstaller pyarmor pyside demo

使用pyinstaller和pyarmor打包pyside程序示例。

## 环境

- Windows 10
- python38
- pyinstaller 5.1
- pyarmor 7.5.1
- pyside6 6.3.1

## 安装

```
pip install pyinstaller[encryption]
pip install pyarmor<8.0
```

## 说明

使用pyinstaller和pyarmor代码混淆打包python，以pyside6为例。


打包后再使用 pyinstxtractor.py 和 uncompyle6 进行反编译检查是否加密，可以看到反编译出来的pyc文件是加密后的文件。

在 main.spec 中使用下面方式加密方式后，则无法提取部分pyc代码，其后缀为`.pyc.encrypted`

```
block_cipher = pyi_crypto.PyiBlockCipher(key='your key')
```

pyinstxtractor.py 会报错

```
[!] Error: Failed to decompress XXX.pyc, probably encrypted. Extracting as is.
```

## 生成.spec文件

    # -F 表示打包成一个文件
    pyinstaller -F src/main.py

## 普通打包

    pyinstaller main.spec --clean

### 创建pyarmor初始化配置

    pyarmor init --src src --entry .\src\main.py

## 加密打包

    # -x " -r" 表示使 pyarmor 递归加密
    pyarmor pack -s main.spec src/main.py --clean -x " -r"

## 代码提取

    python pyinstxtractor.py dist\pyinstaller-pyarmorpyside-demo.exe

## 反编译

    uncompyle6 pyinstaller-pyarmorpyside-demo.exe_extracted\main.pyc > main.pyc

## 注意事项

pyarmor免费版打包有大小限制，文件不能超过32768字节，如果超过则报错：

```
Too big code object, the limitation is 32768 bytes in trial version 
```

参见：https://github.com/dashingsoft/pyarmor/issues/790
