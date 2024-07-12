
@[TOC]

# net

模块功能：网络管理、信号查询、GSM网络状态查询、网络指示灯控制、临近小区信息查询

## net.switchFly(mode)

设置飞行模式

注意：如果要测试飞行模式的功耗，开机后不要立即调用此接口进入飞行模式<br>在模块注册上网络之前，调用此接口进入飞行模式不仅无效，还会导致功耗数据异常<br>详情参考：http://doc.openluat.com/article/488/0

* 参数

|名称|传入值类型|释义|
|-|-|-|
|mode|bool|true:飞行模式开，false:飞行模式关|

* 返回值

nil

* 例子

```lua
net.switchFly(mode)
```

---

## net.getNetMode()

获取netmode

* 参数

无

* 返回值

number netMode,注册的网络类型<br>0：未注册<br>1：2G GSM网络<br>2：2.5G EDGE数据网络<br>3：3G TD网络<br>4：4G LTE网络<br>5：3G WCDMA网络

* 例子

```lua
net.getNetMode()
```

---

## net.getState()

获取网络注册状态

* 参数

无

* 返回值

string state,GSM网络注册状态，<br>"INIT"表示正在初始化<br>"REGISTERED"表示已注册<br>"UNREGISTER"表示未注册

* 例子

```lua
net.getState()
```

---

## net.getMcc()

获取当前小区的mcc

* 参数

无

* 返回值

string mcc,当前小区的mcc，如果还没有注册GSM网络，则返回sim卡的mcc

* 例子

```lua
net.getMcc()
```

---

## net.getMnc()

获取当前小区的mnc

* 参数

无

* 返回值

string mcn,当前小区的mnc，如果还没有注册GSM网络，则返回sim卡的mnc

* 例子

```lua
net.getMnc()
```

---

## net.getLac()

获取当前位置区ID

* 参数

无

* 返回值

string lac,当前位置区ID(16进制字符串，例如"18be")，如果还没有注册GSM网络，则返回""

* 例子

```lua
net.getLac()
```

---

## net.getBand()

获取当前注册的网络频段

* 参数

无

* 返回值

string band,当前注册的网络频段，如果还没有注册网络，则返回""

* 例子

```lua
net.getBand()
```

---

## net.getCi()

获取当前小区ID

* 参数

无

* 返回值

string ci,当前小区ID(16进制字符串，例如"93e1")，如果还没有注册GSM网络，则返回""

* 例子

```lua
net.getCi()
```

---

## net.getRssi()

获取信号强度

当前注册的是2G网络，就是2G网络的信号强度<br>当前注册的是4G网络，就是4G网络的信号强度

* 参数

无

* 返回值

number rssi,当前信号强度(取值范围0-31)

* 例子

```lua
net.getRssi()
```

---

## net.getRsrp()

4G网络信号接收功率

* 参数

无

* 返回值

number rsrp,当前信号接收功率(取值范围-140 - -40)

* 例子

```lua
net.getRsrp()
```

---

## net.getCellInfo()

获取当前和临近位置区、小区以及信号强度的拼接字符串

* 参数

无

* 返回值

string cellInfo,当前和临近位置区、小区以及信号强度的拼接字符串，例如："6311.49234.30;6311.49233.23;6322.49232.18;"

* 例子

```lua
net.getCellInfo()
```

---

## net.getCellInfoExt(rssi)

获取当前和临近位置区、小区、mcc、mnc、以及信号的拼接字符串

* 参数

|名称|传入值类型|释义|
|-|-|-|
|rssi|bool|**可选参数，默认为`nil`** 信号是否拼接功率，true表示功率，false或者nil表示强度<br>表示强度时，信号的取值范围是0到31<br>表示功率时，信号的计算公式为 强度*2-113，取值范围为-113dB到-51dB|

* 返回值

string cellInfo,当前和临近位置区、小区、mcc、mnc、以及信号的拼接字符串，例如：<br>当rssi参数为true时，"460.01.6311.49234.-73;460.01.6311.49233.-67;460.02.6322.49232.-77;"<br>当rssi参数为false或者nil时，"460.01.6311.49234.30;460.01.6311.49233.23;460.02.6322.49232.18;"

* 例子

```lua
net.getCellInfoExt()
```

---

## net.getTa()

获取TA值

* 参数

无

* 返回值

number ta,TA值

* 例子

```lua
net.getTa()
```

---

## net.getMultiCell(cbFnc)

实时读取“当前和临近小区信息”

* 参数

|名称|传入值类型|释义|
|-|-|-|
|cbFnc|function|回调函数，当读取到小区信息后，会调用此回调函数，回调函数的调用形式为：<br>cbFnc(cells)，其中cells为string类型，格式为：当前和临近位置区、小区、mcc、mnc、以及信号强度的拼接字符串，例如："460.01.6311.49234.30;460.01.6311.49233.23;460.02.6322.49232.18;"|

* 返回值

nil

* 例子

无

---

## net.cengQueryPoll(period)

发起查询基站信息(当前和临近小区信息)的请求

* 参数

|名称|传入值类型|释义|
|-|-|-|
|period|number|查询间隔，单位毫秒|

* 返回值

bool result, true:查询成功，false:查询失败

* 例子

```lua
net.cengQueryPoll() --查询1次
net.cengQueryPoll(60000) --每分钟查询1次
```

---

## net.csqQueryPoll(period)

发起查询信号强度的请求

* 参数

|名称|传入值类型|释义|
|-|-|-|
|period|number|查询间隔，单位毫秒|

* 返回值

bool , true:查询成功，false:查询停止

* 例子

```lua
net.csqQueryPoll() --查询1次
net.csqQueryPoll(60000) --每分钟查询1次
```

---

## net.startQueryAll(...)

设置查询信号强度和基站信息的间隔

* 参数

|名称|传入值类型|释义|
|-|-|-|
|...|number|查询周期,参数可变，参数为nil只查询1次，参数1是信号强度查询周期，参数2是基站查询周期|

* 返回值

bool ，true：设置成功，false：设置失败

* 例子

```lua
net.startQueryAll()
net.startQueryAll(60000) -- 1分钟查询1次信号强度，只立即查询1次基站信息
net.startQueryAll(60000,600000) -- 1分钟查询1次信号强度，10分钟查询1次基站信息
```

---

## net.stopQueryAll()

停止查询信号强度和基站信息

* 参数

无

* 返回值

无

* 例子

```lua
net.stopQueryAll()
```

---

## net.setEngMode(mode)

设置工程模式

* 参数

|名称|传入值类型|释义|
|-|-|-|
|mode|number|**可选参数，默认为`1`** 工程模式，目前仅支持0和1<br>mode为0时，不支持临近小区查询，休眠时功耗较低<br>mode为1时，支持临近小区查询，但是休眠时功耗较高|

* 返回值

nil

* 例子

```lua
net.setEngMode(0)
```

---
