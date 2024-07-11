@[TOC]

# lua_protobuf
protobuffer库
## lua_protobuf.state(newstate||nil)

设置新的pb状态或者获取当前pb状态

**历史记录**

|修改时间|修改内容|版本要求|备注|
|-|-|-|-|
|2021.09.06|新接口|>LuatOS-Air_V3104|pb状态|

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|newstate|string|新状态|可选nil|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|status|string|pb状态|状态值|

**例子**

```lua
 --获取当前pb状态值
 local statu = lua_protobuf.state()
 print(statu)

```
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/protoBuffer3 "示例")

---



## pb.conv.encode_int32(value)

将数值转换为int32类型

**历史记录**

|修改时间|修改内容|版本要求|备注|
|-|-|-|-|
|2021.09.06|新接口|>LuatOS-Air_V3104|数值编码|

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|value|number|数值|不限|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|int32数值|-(2e31-1)~(2e31-1)|

**例子**

```lua
 --打印转换后的值
 print(pb.conv.encode_int32(32))

```
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/protoBuffer3 "示例")

---



## pb.conv.encode_uint32(value)

将数值转换为unsigned int32类型

**历史记录**

|修改时间|修改内容|版本要求|备注|
|-|-|-|-|
|2021.09.06|新接口|>LuatOS-Air_V3104|数值编码|

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|value|number|数值|不限|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|uint32数值|0~(2e32-1)|

**例子**

```lua
 --打印转换后的值
 print(pb.conv.encode_uint32(64))

```
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/protoBuffer3 "示例")

---



## pb.conv.encode_sint32(value)

将数值按signed int32类型进行编码

**历史记录**

|修改时间|修改内容|版本要求|备注|
|-|-|-|-|
|2021.09.06|新接口|>LuatOS-Air_V3104|数值编码|

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|value|number|数值|不限|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|sint32编码数值|编码值|

**例子**

```lua
 --编码后解码可得原来的值
 local s32 = pb.conv.encode_sint32(-100)
 print(pb.conv.decode_sint32(s32))

```
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/protoBuffer3 "示例")

---



## pb.conv.decode_sint32(data)

将sint32类型的编码数值解码

**历史记录**

|修改时间|修改内容|版本要求|备注|
|-|-|-|-|
|2021.09.06|新接口|>LuatOS-Air_V3104|数值解码|

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|data|number|编码数值|不限|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|sint32类型的数值|-(2e31-1)~(2e31-1)|

**例子**

```lua
 --详见encode_sint32

```
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/protoBuffer3 "示例")

---



## pb.conv.encode_sint64(value)

将数值按signed int64类型进行编码

**历史记录**

|修改时间|修改内容|版本要求|备注|
|-|-|-|-|
|2021.09.06|新接口|>LuatOS-Air_V3104|数值编码|

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|value|number|数值|不限|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|sint64类型的编码数值|编码值|

**例子**

```lua
  --编码后解码可得原来的值
 local s64 = pb.conv.encode_sint64(-1000000000000)
 print(pb.conv.decode_sint64(s64))

```
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/protoBuffer3 "示例")

---



## pb.conv.decode_sint64(data)

将sint64类型的编码数值解码

**历史记录**

|修改时间|修改内容|版本要求|备注|
|-|-|-|-|
|2021.09.06|新接口|>LuatOS-Air_V3104|数值解码|

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|data|number|编码数值|不限|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|sint64类型的数值|-(2e63-1)~(2e63-1) |

**例子**

```lua
 --详见encode_sint64

```
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/protoBuffer3 "示例")

---



## pb.conv.encode_float(value)

将数值按float类型进行编码

**历史记录**

|修改时间|修改内容|版本要求|备注|
|-|-|-|-|
|2021.09.06|新接口|>LuatOS-Air_V3104|数值编码|

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|value|number|数值|不限|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|float类型的编码数值|编码值|

**例子**

```lua
 --编码后解码可得原来的值
 local flo = pb.conv.encode_float(10.55)
 print(pb.conv.decode_float(flo))

```
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/protoBuffer3 "示例")

---



## pb.conv.decode_float(data)

将float类型的编码数值解码

**历史记录**

|修改时间|修改内容|版本要求|备注|
|-|-|-|-|
|2021.09.06|新接口|>LuatOS-Air_V3104|数值解码|

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|data|number|编码数值|不限|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|float类型的数值|float数值|

**例子**

```lua
 --详见encode_float

```
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/protoBuffer3 "示例")

---



## pb.conv.encode_double(value)

将数值按double类型进行编码

**历史记录**

|修改时间|修改内容|版本要求|备注|
|-|-|-|-|
|2021.09.06|新接口|>LuatOS-Air_V3104|数值编码|

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|value|number|数值|不限|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|double类型的编码数值|编码值|

**例子**

```lua
 --编码后解码可得原来的值
 local doubl = pb.conv.encode_double(10.55)
 print(pb.conv.decode_double(doubl))

```
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/protoBuffer3 "示例")

---



## pb.conv.decode_double(data)

将double类型的编码数值解码

**历史记录**

|修改时间|修改内容|版本要求|备注|
|-|-|-|-|
|2021.09.06|新接口|>LuatOS-Air_V3104|数值解码|

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|data|number|编码数值|不限|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|double类型的数值|double数值|

**例子**

```lua
 --详见encode_double

```
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/protoBuffer3 "示例")

---



## lua_protobuf.load(data)

将二进制模式数据加载到Pb模块

**历史记录**

|修改时间|修改内容|版本要求|备注|
|-|-|-|-|
|2021.09.06|新接口|>LuatOS-Air_V3104|数据加载|

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|data|string|二进制数据|不限|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result1|boolean|导入结果|0 or 1|
|result2|number|pb的地址|地址范围|

**例子**

```lua
 --加载二进制的数据
 print(lua_protobuf.load(data))

```
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/protoBuffer3 "示例")

---



## lua_protobuf.loadfile(filename)

将pb文件加载到Pb模块

**历史记录**

|修改时间|修改内容|版本要求|备注|
|-|-|-|-|
|2021.09.06|新接口|>LuatOS-Air_V3104|文件加载|

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|filename|string|pb文件名|不限|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result1|boolean|导入结果|0 or 1  |
|result2|number|pb的地址|地址范围|

**例子**

```lua
 --加载pb文件
 print(lua_protobuf.loadfile("/lua/tracker.pb"))

```
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/protoBuffer3 "示例")

---



## lua_protobuf.types()

迭代检索模块中的所有类型的信息

**历史记录**

|修改时间|修改内容|版本要求|备注|
|-|-|-|-|
|2021.09.06|新接口|>LuatOS-Air_V3104|类型获取|

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|iterator(迭代)|返回所有类型的信息|信息:name,basename,type|

**例子**

```lua
 --结合pb.type的代码
 for name, basename, type in lua_protobuf.types() do
	 print(name, basename, type)
 end

```
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/protoBuffer3 "示例")

---



## lua_protobuf.fields(type)

迭代检索模块中的指定类型的所有字段的信息

**历史记录**

|修改时间|修改内容|版本要求|备注|
|-|-|-|-|
|2021.09.06|新接口|>LuatOS-Air_V3104|类型字段获取|

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|type|string|指定类型，范围:消息//映射//枚举|message(table)//map//enum|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|iterator(迭代)|迭代返回指定类型所有字段信息|字段信息:name,number,type|

**例子**

```lua
 --结合pb.field的代码
 for name, number, type in lua_protobuf.fields "tracker.SearchRequest" do
     print(name, number, type)
 end

```
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/protoBuffer3 "示例")

---



## lua_protobuf.type(type)

检索指定类型的信息

**历史记录**

|修改时间|修改内容|版本要求|备注|
|-|-|-|-|
|2021.09.06|新接口|>LuatOS-Air_V3104|类型获取|

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|type|string|类型名，范围:消息//映射//枚举|message(table)//map//enum|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|name|string|类型名|不限|
|basename|string|隶属的类型|例:SearchRequest|
|type|string|类型|message//map//enum|

**例子**

```lua
 local tracker = {
	 query = "www",
	 page_number = 8,
	 result_per_page = 100,
 }
 lua_protobuf.loadfile("/lua/tracker.pb")
 print(lua_protobuf.type("tracker.SearchRequest"))

```
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/protoBuffer3 "示例")

---



## lua_protobuf.field(type,string)

检索指定类型指定字段的信息

**历史记录**

|修改时间|修改内容|版本要求|备注|
|-|-|-|-|
|2021.09.06|新接口|>LuatOS-Air_V3104|类型字段获取|

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|type|string|指定类型，范围:消息//映射//枚举|message//map//enum|
|string|string|指定字段|指定类型的成员字段|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|name|string|成员字段名|指定字段|
|number|number|成员字段索引值|例:1,2,3...|
|type|string|成员字段类型|string//number//table|

**例子**

```lua
 local tracker = {
	 query = "www",
	 page_number = 8,
	 result_per_page = 100,
 }
 lua_protobuf.loadfile("/lua/tracker.pb")
 print(lua_protobuf.field("tracker.SearchRequest", "query"))

```
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/protoBuffer3 "示例")

---



## lua_protobuf.defaults(type)

获取类型的默认表

**历史记录**

|修改时间|修改内容|版本要求|备注|
|-|-|-|-|
|2021.09.06|新接口|>LuatOS-Air_V3104|默认表获取|

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|type|string|指定类型|例:tracker.SearchRequest|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|table|默认表及其地址|地址范围|

**例子**

```lua
 --获取类型的默认表
 local tracker = {
	 query = "www",
	 page_number = 8,
	 result_per_page = 100,
 }
 print(lua_protobuf.defaults("tracker.SearchRequest"))

```
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/protoBuffer3 "示例")

---



## lua_protobuf.hook(type)

设置解码挂钩函数

**历史记录**

|修改时间|修改内容|版本要求|备注|
|-|-|-|-|
|2021.09.06|新接口|>LuatOS-Air_V3104|挂钩函数|

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|type|string|指定类型|不限|

**返回值**

无

**例子**

```lua
 --解码时候打印decode sucess
 local tracker = {
	 query = "www",
	 page_number = 8,
	 result_per_page = 100,
 }
 print(lua_protobuf.option("enable_hooks"))
 lua_protobuf.hook("tracker.SearchRequest", function()
     print("decode sucess")
 end)

```
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/protoBuffer3 "示例")

---



## lua_protobuf.encode_hook(type)

设置编码挂钩函数

**历史记录**

|修改时间|修改内容|版本要求|备注|
|-|-|-|-|
|2021.09.06|新接口|>LuatOS-Air_V3104|挂钩函数|

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|type|string|指定类型|不限|

**返回值**

无

**例子**

```lua
 --编码时候打印encode sucess
 local tracker = {
	 query = "www",
	 page_number = 8,
	 result_per_page = 100,
 }
 print(lua_protobuf.option("enable_hooks"))
 lua_protobuf.encode_hook("tracker.SearchRequest", function()
     print("encode sucess")
 end)

```
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/protoBuffer3 "示例")

---



## lua_protobuf.clear()

清除之前注册的所有消息

**历史记录**

|修改时间|修改内容|版本要求|备注|
|-|-|-|-|
|2021.09.06|新接口|>LuatOS-Air_V3104|清除|

**参数**

无

**返回值**

无

**例子**

```lua
 lua_protobuf.clear()

```
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/protoBuffer3 "示例")

---



## lua_protobuf.typefmt(type)

将字段的类型名称转换为打包/解包格式化程序

**历史记录**

|修改时间|修改内容|版本要求|备注|
|-|-|-|-|
|2021.09.06|新接口|>LuatOS-Air_V3104|类型打包|

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|type|string|指定类型，范围:消息//映射//枚举|message//map//enum|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|string|类型|例:message/map/enum|

**例子**

```lua
 --将字段的类型名转换为打包/解包格式化程序
 local tracker = {
 	query = "www",
    page_number = 8,
    result_per_page = 100,
 }
 print(lua_protobuf.typefmt("tracker.SearchRequest"))

```
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/protoBuffer3 "示例")

---



## lua_protobuf.encode(table)

将消息表编码为二进制形式

**历史记录**

|修改时间|修改内容|版本要求|备注|
|-|-|-|-|
|2021.09.06|新接口|>LuatOS-Air_V3104|序列编码|

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|table|table|消息表|按照pb模型|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|string|序列化编码数据|二进制数据|

**例子**

```lua
 local tracker = {
 	query = "www",
    page_number = 8,
    result_per_page = 100,
 }
 lua_protobuf.loadfile("/lua/tracker.pb")
 -- 序列化成二进制数据
 local data = lua_protobuf.encode("tracker.SearchRequest", tracker)
 log.info("protobuf.encode",data:toHex())
 -- 从二进制数据解析出实际消息 

```
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/protoBuffer3 "示例")

---



## lua_protobuf.decode(data)

将二进制消息解码到Lua表中

**历史记录**

|修改时间|修改内容|版本要求|备注|
|-|-|-|-|
|2021.09.06|新接口|>LuatOS-Air_V3104|序列解码|

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|data|string|二进制数据|不限|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|table|解码后的表|table数据|

**例子**

```lua
 --结合encode相关代码
 local msg = lua_protobuf.decode("tracker.SearchRequest", data)
 -- 这里调用了serpent库，用于序列化打印table数据，实际生产可不包含
 print(require "serpent".block(msg))

```
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/protoBuffer3 "示例")

---



## lua_protobuf.option(string)

设置decoder/encoder的选项

**历史记录**

|修改时间|修改内容|版本要求|备注|
|-|-|-|-|
|2021.09.06|新接口|>LuatOS-Air_V3104|选项设置|

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|string|string|选项|例:enable_hooks|

**返回值**

无

**例子**

```lua
 --启用hook函数选项
 lua_protobuf.option("enable_hooks")

```
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/protoBuffer3 "示例")

---



