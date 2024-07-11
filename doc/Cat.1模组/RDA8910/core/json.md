@[TOC]

# json
json库
## json.encode(torigin)

json编译

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|torigin|table|待编译的源字符|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|string|json格式字符串|   |

**例子**

```lua
local torigin =
{
    KEY1 = "VALUE1",
    KEY2 = "VALUE2",
    KEY3 = "VALUE3",
    KEY4 = "VALUE4",
    KEY5 = {KEY5_1="VALU5_1",KEY5_2="VALU5_2"},
    KEY6 = {1,2,3},
}

local jsondata = json.encode(torigin)
--[[
{"KEY3":"VALUE3","KEY4":"VALUE4","KEY2":"VALUE2","KEY1":"VALUE1","KEY5":{"KEY5_2":"VALU5_2","KEY5_1":"VALU5_1"}},"KEY6":[1,2,3]}
]]
end

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2315 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2178 "示例")

---



## json.decode(origin)

json解析

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|torigin|table|待解析的json字符串|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|res|string|解析内容，table类型;解析结果，true为成功，false为失败;错误信息|    |

**例子**

```lua
-- 正确json字符串
local wrongOrigin = "{\":\"VALUE3\",\"KEY4\":\"VALUE4\",\"KEY2\":\"VALUE2\",\"KEY1\":\"VALUE1\",\"KEY5\":{\"KEY5_2\":\"VALU5_2\",\"KEY5_1\":\"VALU5_1\"},\"KEY6\":[1,2,3]}"
local origin = "{\"KEY3\":\"VALUE3\",\"KEY4\":\"VALUE4\",\"KEY2\":\"VALUE2\",\"KEY1\":\"VALUE1\",\"KEY5\":{\"KEY5_2\":\"VALU5_2\",\"KEY5_1\":\"VALU5_1\"},\"KEY6\":[1,2,3]}"
local tjsondata,result,errinfo = json.decode(origin)
if result then
    print(tjsondata["KEY1"])
    print(tjsondata["KEY2"])
    print(tjsondata["KEY3"])
    print(tjsondata["KEY4"])
    print(tjsondata["KEY5"]["KEY5_1"],tjsondata["KEY5"]["KEY5_2"])
    print(tjsondata["KEY6"][1],tjsondata["KEY6"][2],tjsondata["KEY6"][3])
else
	print("json.decode error",errinfo)
end
--origin：正确输出
--wrongOrigin：json.decode error	Expected colon but found invalid token at character 5
end

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2315 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2178 "示例")

---



