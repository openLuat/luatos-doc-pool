@[TOC]

# iconv
字符编码转换
## iconv.open(tocode, fromcode) 

打开相应字符编码转换函数

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|tocode|string|目标编码格式|gb2312/ucs2/ucs2be/utf8|
|fromcode|string|源编码格式|gb2312/ucs2/ucs2be/utf8|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|cd|table|编码转换函数的转换句柄| |

**例子**

```lua
--unicode大端编码 转化为 utf8编码
local cd = iconv.open("utf8", "ucs2be")

```
用户应用脚本可以直接使用common API，链接为：[common](https://doc.openluat.com/wiki/21?wiki_page_id=2269 "common")

---



## cd:iconv(inbuf) 

字符编码转换

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|inbuf|string|输入字符串|例如:ucs2s |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|返回编码转换后的结果|0成功,-1失败|

**例子**

```lua
--unicode大端编码 转化为 utf8编码
function ucs2beToUtf8(ucs2s)
    local cd = iconv.open("utf8", "ucs2be")
    return cd:iconv(ucs2s)
end

```
用户应用脚本可以直接使用common API，链接为：[common](https://doc.openluat.com/wiki/21?wiki_page_id=2269 "common")

---



## iconv.close(cd) 

关闭字符编码转换

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|cd|string|iconv.open返回的句柄| |

**返回值**

无

**例子**

```lua
--关闭字符编码转换
local cd = iconv.open("utf8", "ucs2be")
iconv.close(cd)

```

---



