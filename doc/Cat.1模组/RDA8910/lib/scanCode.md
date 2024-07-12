
@[TOC]

# scanCode

模块功能：扫码.

支持二维码、条形码扫描

## scanCode.request(cbFnc, timeout)

设置扫码请求

* 参数

|名称|传入值类型|释义|
|-|-|-|
|cbFnc|function|扫码返回或者超时未返回的回调函数，回调函数的调用形式为：<br>cbFnc(result,type,str)<br>result：true或者false，true表示扫码成功，false表示超时失败<br>type：string或者nil类型，result为true时，表示扫码类型；result为false时，为nil；支持QR-Code和CODE-128<br>str：string或者nil类型，result为true时，表示扫码结果的字符串；result为false时，为nil|
|timeout|number|**可选参数，默认为`10000`** 设置请求后，等待扫码结果返回的超时时间，单位毫秒，默认为10秒|

* 返回值

无

* 例子

```lua
scanCode.request(cbFnc)
scanCode.request(cbFnc,5000)
```

---
