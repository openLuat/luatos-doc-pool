
@[TOC]

# wifiScan

模块功能：wifi扫描功能

支持wifi热点扫描

## wifiScan.request(cbFnc, timeout)

wifi扫描热点请求

* 参数

|名称|传入值类型|释义|
|-|-|-|
|cbFnc|function|扫描到热点返回或者超时未返回的回调函数，回调函数的调用形式为：<br>cbFnc(result,cnt,info)<br>result：true或者false，true表示扫描成功，false表示扫描失败或者超时失败<br>cnt：number类型，表示扫描到的热点个数<br>info：table或者nil类型；result为false时，为nil；result为true时，表示扫码到的热点mac和信号信息，table类型，例如：<br>{<br>["1a:fe:34:9e:a1:77"] = -63,<br>["8c:be:be:2d:cd:e9"] = -81,<br>["20:4e:7f:82:c2:c4"] = -70,<br>}|
|timeout|number|**可选参数，默认为`10000`** 等待扫描热点返回的超时时间，单位毫秒，默认为10秒|

* 返回值

无

* 例子

```lua
wifiScan.request(cbFnc)
wifiScan.request(cbFnc,5000)
```

---
