
@[TOC]

# aLiYunOta

模块功能：阿里云物联网套件客户端OTA功能.

目前固件签名算法仅支持MD5

## aLiYunOta.setVer(version)

设置当前的固件版本号

* 参数

|名称|传入值类型|释义|
|-|-|-|
|version|string|当前固件版本号|

* 返回值

nil

* 例子

```lua
aLiYunOta.setVer("MCU_VERSION_1.0.0")
```

---

## aLiYunOta.setName(name)

设置新固件保存的文件名

* 参数

|名称|传入值类型|释义|
|-|-|-|
|name|string|新固件下载后保存的文件名；注意此文件名并不是保存的完整路径，完整路径通过setCb设置的回调函数去获取|

* 返回值

nil

* 例子

```lua
aLiYunOta.setName("MCU_FIRMWARE.bin")
```

---

## aLiYunOta.setCb(cbFnc)

设置新固件下载后的回调函数

* 参数

|名称|传入值类型|释义|
|-|-|-|
|cbFnc|function|新固件下载后的回调函数<br>回调函数的调用形式为：cbFnc(result,filePath)，result为下载结果，true表示成功，false或者nil表示失败；filePath为新固件文件保存的完整路径|

* 返回值

nil

* 例子

```lua
aLiYunOta.setCb(cbFnc)
```

---
