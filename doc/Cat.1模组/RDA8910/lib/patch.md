
@[TOC]

# patch

模块功能：Lua补丁

## patch.safeJsonDecode(s) (local函数 无法被外部调用)

封装自定义的json.decode接口

* 参数

|名称|传入值类型|释义|
|-|-|-|
|s|string|json格式的字符串|

* 返回值

table,第一个返回值为解析json字符串后的table
boole,第二个返回值为解析结果(true表示成功，false失败)
string,第三个返回值可选（只有第二个返回值为false时，才有意义），表示出错信息

* 例子

无

---
