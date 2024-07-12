
@[TOC]

# common

模块功能：通用库函数、编码格式转换、时区时间转换

## common.ucs2ToAscii(inNum)

ascii字符串的unicode编码的16进制字符串 转化为 ascii字符串

* 参数

|名称|传入值类型|释义|
|-|-|-|
|inNum|string|待转换字符串|

* 返回值

string data，转换后的字符串

* 例子

```lua
local data = common.ucs2ToAscii("0031003200330034")
data is "1234"
```

---

## common.nstrToUcs2Hex(inNum)

ascii字符串 转化为 ascii字符串的unicode编码的16进制字符串(仅支持数字和+)

* 参数

|名称|传入值类型|释义|
|-|-|-|
|inNum|string|待转换字符串|

* 返回值

string data,转换后的字符串

* 例子

```lua
local data = common.nstrToUcs2Hex("+1234")
data is "002B0031003200330034"
```

---

## common.numToBcdNum(inStr, destLen)

ASCII字符串 转化为 BCD编码格式字符串(仅支持数字)

* 参数

|名称|传入值类型|释义|
|-|-|-|
|inStr|string|待转换字符串|
|destLen|number|转换后的字符串期望长度，如果实际不足，则填充F|

* 返回值

string data,转换后的字符串

* 例子

```lua
local data = common.numToBcdNum("8618126324567")
data is "688121364265f7" （表示第1个字节是0x68，第2个字节为0x81，......）
```

---

## common.bcdNumToNum(num)

BCD编码格式字符串 转化为 号码ASCII字符串(仅支持数字)

* 参数

|名称|传入值类型|释义|
|-|-|-|
|num|string|待转换字符串|

* 返回值

string data,转换后的字符串

* 例子

```lua
local data = common.bcdNumToNum(common.fromHex("688121364265f7")) --表示第1个字节是0x68，第2个字节为0x81，......
data is "8618126324567"
```

---

## common.ucs2ToGb2312(ucs2s)

unicode小端编码 转化为 gb2312编码

* 参数

|名称|传入值类型|释义|
|-|-|-|
|ucs2s|string|unicode小端编码数据|

* 返回值

string data,gb2312编码数据

* 例子

```lua
local data = common.ucs2ToGb2312(ucs2s)
```

---

## common.gb2312ToUcs2(gb2312s)

gb2312编码 转化为 unicode小端编码

* 参数

|名称|传入值类型|释义|
|-|-|-|
|gb2312s|string|gb2312编码数据|

* 返回值

string data,unicode小端编码数据

* 例子

```lua
local data = common.gb2312ToUcs2(gb2312s)
```

---

## common.ucs2beToGb2312(ucs2s)

unicode大端编码 转化为 gb2312编码

* 参数

|名称|传入值类型|释义|
|-|-|-|
|ucs2s|string|unicode大端编码数据|

* 返回值

string data,gb2312编码数据

* 例子

```lua
data = common.ucs2beToGb2312(ucs2s)
```

---

## common.gb2312ToUcs2be(gb2312s)

gb2312编码 转化为 unicode大端编码

* 参数

|名称|传入值类型|释义|
|-|-|-|
|gb2312s|string|gb2312编码数据|

* 返回值

string data,unicode大端编码数据

* 例子

```lua
local data = common.gb2312ToUcs2be(gb2312s)
```

---

## common.ucs2ToUtf8(ucs2s)

unicode小端编码 转化为 utf8编码

* 参数

|名称|传入值类型|释义|
|-|-|-|
|ucs2s|string|unicode小端编码数据|

* 返回值

string data,utf8编码数据

* 例子

```lua
data = common.ucs2ToUtf8(ucs2s)
```

---

## common.utf8ToUcs2(utf8s)

utf8编码 转化为 unicode小端编码

* 参数

|名称|传入值类型|释义|
|-|-|-|
|utf8s|string|utf8编码数据|

* 返回值

string data,unicode小端编码数据

* 例子

```lua
local data = common.utf8ToUcs2(utf8s)
```

---

## common.ucs2beToUtf8(ucs2s)

unicode大端编码 转化为 utf8编码

* 参数

|名称|传入值类型|释义|
|-|-|-|
|ucs2s|string|unicode大端编码数据|

* 返回值

string data,utf8编码数据

* 例子

```lua
data = common.ucs2beToUtf8(ucs2s)
```

---

## common.utf8ToUcs2be(utf8s)

utf8编码 转化为 unicode大端编码

* 参数

|名称|传入值类型|释义|
|-|-|-|
|utf8s|string|utf8编码数据|

* 返回值

string data,unicode大端编码数据

* 例子

```lua
local data = common.utf8ToUcs2be(utf8s)
```

---

## common.utf8ToGb2312(utf8s)

utf8编码 转化为 gb2312编码

* 参数

|名称|传入值类型|释义|
|-|-|-|
|utf8s|string|utf8编码数据|

* 返回值

string data,gb2312编码数据

* 例子

```lua
local data = common.utf8ToGb2312(utf8s)
```

---

## common.gb2312ToUtf8(gb2312s)

gb2312编码 转化为 utf8编码

* 参数

|名称|传入值类型|释义|
|-|-|-|
|gb2312s|string|gb2312编码数据|

* 返回值

string data,utf8编码数据

* 例子

```lua
local data = common.gb2312ToUtf8(gb2312s)
```

---

## common.timeZoneConvert(y, m, d, hh, mm, ss, srcTimeZone, dstTimeZone)

时区时间转换

* 参数

|名称|传入值类型|释义|
|-|-|-|
|y|number|源时区年份|
|m|number|源时区月份|
|d|number|源时区天|
|hh|number|源时区小时|
|mm|number|源时区分|
|ss|number|源时区秒|
|srcTimeZone|number|源时区|
|dstTimeZone|number|目的时区|

* 返回值

table dstZoneTime,返回目的时区对应的时间，{year,month,day,hour,min,sec}

* 例子

```lua
local dstZoneTime = common.timeZoneConvert(2018,1,1,18,00,00,0,8)
dstZoneTime为{year=2018,month=1,day=2,hour=2,min=0,sec=0}
```

---
