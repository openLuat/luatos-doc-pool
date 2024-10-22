
@[TOC]

# ntp

模块功能：网络授时.

重要提醒！！！！！！

本功能模块采用多个免费公共的NTP服务器来同步时间

并不能保证任何时间任何地点都能百分百同步到正确的时间

所以，如果用户项目中的业务逻辑严格依赖于时间同步功能

则不要使用使用本功能模块，建议使用自己的应用服务器来同步时间

参考 http://ask.openluat.com/article/912 加深对授时功能的理解

## ntp.timeSync(period, fnc, fun)

ntp同步时间任务.

重要提醒！！！！！！<br>本功能模块采用多个免费公共的NTP服务器来同步时间<br>并不能保证任何时间任何地点都能百分百同步到正确的时间<br>所以，如果用户项目中的业务逻辑严格依赖于时间同步功能<br>则不要使用使用本功能模块，建议使用自己的应用服务器来同步时间

* 参数

|名称|传入值类型|释义|
|-|-|-|
|period|number|**可选参数，默认为`nil`** 调用本接口会立即同步一次；每隔period小时再自动同步1次，nil表示仅同步一次|
|fnc|function|**可选参数，默认为`nil`** 同步结束，设置系统时间后的回调函数，回调函数的调用形式为：<br>fnc(time，result)<br>time表示设置之后的系统时间，table类型，例如{year=2017,month=2,day=14,hour=14,min=19,sec=23}<br>result为true表示成功，false或者nil为失败|
|fun|function|**可选参数，默认为`nil`** 同步结束，设置系统时间前的回调函数，回调函数的调用形式为：fun()|

* 返回值

nil<br> 

* 例子

```lua
-- 立即同步一次（仅同步这一次）：
ntp.timeSync()
-- 立即同步一次，之后每隔1小时自动同步一次：
ntp.timeSync(1)
-- 立即同步一次（仅同步这一次），同步结束后执行fnc(time,result)：
ntp.timeSync(nil,fnc)
-- 立即同步一次，之后每隔24小时自动同步一次，每次同步结束后执行fnc(time,result)：
ntp.timeSync(24,fnc)
```

---
