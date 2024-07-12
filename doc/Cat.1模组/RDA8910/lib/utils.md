
@[TOC]

# utils

模块功能：常用工具类接口

## string.toHex(str, separator)

将Lua字符串转成HEX字符串，如"123abc"转为"313233616263"

* 参数

|名称|传入值类型|释义|
|-|-|-|
|str|string|输入字符串|
|separator|string|**可选参数，默认为`""`** 输出的16进制字符串分隔符|

* 返回值

hexstring 16进制组成的串
len 输入的字符串长度

* 例子

```lua
string.toHex("\1\2\3") -> "010203" 3
string.toHex("123abc") -> "313233616263" 6
string.toHex("123abc"," ") -> "31 32 33 61 62 63 " 6
```

---

## string.fromHex(hex)

将HEX字符串转成Lua字符串，如"313233616263"转为"123abc", 函数里加入了过滤分隔符，可以过滤掉大部分分隔符（可参见正则表达式中\s和\p的范围）。

* 参数

|名称|传入值类型|释义|
|-|-|-|
|hex|string|16进制组成的串|

* 返回值

charstring,字符组成的串
len,输出字符串的长度

* 例子

```lua
string.fromHex("010203")       ->  "\1\2\3"
string.fromHex("313233616263:) ->  "123abc"
```

---

## string.utf8Len(str)

返回utf8编码字符串的长度

* 参数

|名称|传入值类型|释义|
|-|-|-|
|str|string|utf8编码的字符串,支持中文|

* 返回值

number,返回字符串长度

* 例子

```lua
local cnt = string.utf8Len("中国a"),cnt == 3
```

---

## string.utf8ToTable(str)

返回utf8编码字符串的单个utf8字符的table

* 参数

|名称|传入值类型|释义|
|-|-|-|
|str|string|utf8编码的字符串,支持中文|

* 返回值

table,utf8字符串的table

* 例子

```lua
local t = string.utf8ToTable("中国2018")
```

---

## string.rawurlEncode(str)

返回字符串的 RFC3986 编码

* 参数

|名称|传入值类型|释义|
|-|-|-|
|str|string|要转换编码的字符串,支持UTF8编码中文|

* 返回值

str, RFC3986 编码的字符串

* 例子

```lua
local str = string.rawurlEncode("####133") ,str == "%23%23%23%23133"
local str = string.rawurlEncode("中国2018") , str == "%e4%b8%ad%e5%9b%bd2018"
```

---

## string.urlEncode(str)

返回字符串的urlEncode编码

* 参数

|名称|传入值类型|释义|
|-|-|-|
|str|string|要转换编码的字符串,支持UTF8编码中文|

* 返回值

str,urlEncode编码的字符串

* 例子

```lua
local str = string.urlEncode("####133") ,str == "%23%23%23%23133"
local str = string.urlEncode("中国2018") , str == "%e4%b8%ad%e5%9b%bd2018"
```

---

## table.gsort(t, f)

返回一个迭代器函数,每次调用函数都会返回hash表的排序后的键值对

* 参数

|名称|传入值类型|释义|
|-|-|-|
|t|table|要排序的hash表|
|f|param|自定义排序函数|

* 返回值

function.

* 例子

```lua
test = {a=1,f=9,d=2,c=8,b=5}
for name,line in pairsByKeys(test) do print(name,line) end
```

---

## table.rconcat(l)

table.concat的增强版，支持嵌套字符串数组

* 参数

|名称|传入值类型|释义|
|-|-|-|
|l|table|嵌套字符串数组|

* 返回值

string

* 例子

```lua
print(table.rconcat({"a",{" nice "}," and ", {{" long "},{" list "}}}))
```

---

## string.formatNumberThousands(num)

返回数字的千位符号格式

* 参数

|名称|传入值类型|释义|
|-|-|-|
|num|number|数字|

* 返回值

string，千位符号的数字字符串

* 例子

```lua
loca s = string.formatNumberThousands(1000) ,s = "1,000"
```

---

## string.split(str, delimiter)

按照指定分隔符分割字符串

* 参数

|名称|传入值类型|释义|
|-|-|-|
|str|string|输入字符串|
|delimiter|string|分隔符|

* 返回值

分割后的字符串列表

* 例子

```lua
"123,456,789":split(',') -> {'123','456','789'}
```

---

## io.exists(path)

判断文件是否存在

* 参数

|名称|传入值类型|释义|
|-|-|-|
|path|string|文件全名，例如："/lua/call.mp3"|

* 返回值

bool,存在为true,不存在为false

* 例子

```lua
local ex = io.exists("/lua/call.mp3")
```

---

## io.readFile(path)

读取文件中的所有内容

* 参数

|名称|传入值类型|释义|
|-|-|-|
|path|string|文件全名，例如："/lua/call.txt"|

* 返回值

string,文件的内容,文件不存在返回nil

* 例子

```lua
local c = io.readFile("/lua/call.txt")
```

---

## io.writeFile(path, content, mode)

写入文件指定的内容,默认为覆盖二进制模式

* 参数

|名称|传入值类型|释义|
|-|-|-|
|path|string|文件全名，例如："/lua/call.txt"|
|content|string|文件内容|
|mode|string|文件写入模式，支持如下几种（默认"w+b"）：<br>"w"或者"w+b"：空文件写入模式，如果文件不存在，则新建文件，然后从起始位置开始写入；如果文件存在，则删除已有内容，然后从起始位置开始写入<br>"a"或者"a+b"：追加写入模式，如果文件不存在，则新建文件，然后从起始位置开始写入；如果文件存在，则从文件末尾开始追加写入|

* 返回值

boolean result,文件写入结果，true表示写入成功；false表示写入失败

* 例子

```lua
local c = io.writeFile("/lua/call.txt","test")
```

---

## io.pathInfo(path)

将文件路径分解为table信息

* 参数

|名称|传入值类型|释义|
|-|-|-|
|path|string|文件路径全名，例如:"/lua/call.txt"|

* 返回值

table,{dirname="/lua/",filename="call.txt",basename="call",extname=".txt"}

* 例子

```lua
loca p = io.pathInfo("/lua/call.txt")
```

---

## io.fileSize(path)

返回文件大小

* 参数

|名称|传入值类型|释义|
|-|-|-|
|path|string|文件路径全名，例如:"/lua/call.txt"|

* 返回值

number ,文件大小

* 例子

```lua
locan cnt = io.fileSize("/lua/call.txt")
```

---

## io.readStream(path, offset, len)

返回指定位置读取的字符串

* 参数

|名称|传入值类型|释义|
|-|-|-|
|path|string|文件路径全名，例如:"/lua/call.txt"|
|offset|number|要读取的指定位置，相对于文件开头的偏移位置|
|len|number|要读取的字节数|

* 返回值

string,返回要读取的数据,读取失败返回nil

* 例子

无

---
