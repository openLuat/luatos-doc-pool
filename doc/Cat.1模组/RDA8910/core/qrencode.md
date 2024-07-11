@[TOC]

# qrencode
二维码生成
## qrencode.encode(data [,version,level])

二维码编码

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|data|string|需要编码的数据|string类型   |
|version|number|二维码版本|可选参数0-40|
|level|number|二维码纠错等级|0-3|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|width|number|生成的二维码信息宽度|   |

**例子**

```lua
 local width, data = qrencode.encode('http://www.openluat.com')
 end

```

---



