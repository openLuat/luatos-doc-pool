
@[TOC]

# nvm

模块功能：参数管理

## nvm.init(defaultCfgFile, burnSave)

初始化参数存储管理模块

* 参数

|名称|传入值类型|释义|
|-|-|-|
|defaultCfgFile|string|默认参数文件名|
|burnSave|bool|本地烧录时是否保留已有参数，true为保留，false或者nil为清除<br>注意：在同一个项目，不同版本中，此参数必须保持前后版本一致|

* 返回值

boolean result，如果初始化异常，会恢复出厂设置，此时返回false；其余情况返回nil

* 例子

```lua
-- 初始化参数存储管理模块，默认参数文件名为config.lua，本地烧录时清除已有的参数：
nvm.init("config.lua")
-- 初始化参数存储管理模块，默认参数文件名为config.lua，本地烧录时保留已有的参数：
nvm.init("config.lua",true)
```

---

## nvm.set(k, v, r, s)

设置某个参数的值

* 参数

|名称|传入值类型|释义|
|-|-|-|
|k|string|参数名|
|v|param|参数的新值，仅支持number、string、boolean、table类型|
|r|param|设置原因，如果传入了非nil的有效参数，并且v值和旧值相比发生了改变，<br>会产生一个PARA_CHANGED_IND内部消息，携带 k,v,r 3个参数|
|s|param|是否立即写入到文件系统中，false不写入，其余的都写入|

* 返回值

bool或者nil，成功返回true，失败返回nil

* 例子

```lua
-- 参数name赋值为Luat，立即写入文件系统：
nvm.set("name","Luat")
-- 参数age赋值为12，立即写入文件系统：
-- 如果旧值不是12，会产生一个PARA_CHANGED_IND消息，携带 "age",12,"SVR" 3个参数：
nvm.set("age",12,"SVR")
-- 参数class赋值为Class2，不写入文件系统：
nvm.set("class","Class2",nil,false)
-- 参数score赋值为{chinese=100,math=99,english=98}，立即写入文件系统：
nvm.set("score",{chinese=100,math=99,english=98})
-- 连续写入4个参数，前3个不保存到文件系统中，写第4个时，一次性全部保存到文件系统中：
nvm.set("para1",1,nil,false)
nvm.set("para2",2,nil,false)
nvm.set("para3",3,nil,false)
nvm.set("para4",4)
```

---

## nvm.sett(k, kk, v, r, s)

设置某个table类型参数的某一个索引的值

* 参数

|名称|传入值类型|释义|
|-|-|-|
|k|string|table类型的参数名|
|kk|param|table类型参数的某一个索引名|
|v|param|table类型参数的某一个索引的新值|
|r|param|设置原因，如果传入了非nil的有效参数，并且v值和旧值相比发生了改变，会产生一个TPARA_CHANGED_IND消息，携带k,kk,v,r4个参数|
|s|param|是否立即写入到文件系统中，false不写入，其余的都写入|

* 返回值

bool或者nil，成功返回true，失败返回nil

* 例子

```lua
nvm.sett("score","chinese",100)，参数score["chinese"]赋值为100，立即写入文件系统
nvm.sett("score","chinese",100,"SVR")，参数score["chinese"]赋值为100，立即写入文件系统，
-- 如果旧值不是100，会产生一个TPARA_CHANGED_IND消息，携带 "score","chinese",100,"SVR" 4个参数
nvm.sett("score","chinese",100,nil,false)，参数class赋值为Class2，不写入文件系统
```

---

## nvm.flush()

所有参数立即写入文件系统

* 参数

无

* 返回值

nil

* 例子

```lua
nvm.flush()
```

---

## nvm.get(k)

读取某个参数的值

* 参数

|名称|传入值类型|释义|
|-|-|-|
|k|string|参数名|

* 返回值

参数值

* 例子

```lua
-- 读取参数名为name的参数值：
nameValue = nvm.get("name")
```

---

## nvm.gett(k, kk)

读取某个table类型参数的键名对应的值

* 参数

|名称|传入值类型|释义|
|-|-|-|
|k|string|table类型的参数名|
|kk|param|table类型参数的键名|

* 返回值

无

* 例子

```lua
-- 有一个table参数为score，数据如下：
score = {chinese=100, math=100, english=95}
-- 读取score中chinese对应的值：
nvm.gett("score","chinese")
```

---

## nvm.restore()

参数恢复出厂设置

* 参数

无

* 返回值

nil

* 例子

```lua
nvm.restore()
```

---

## nvm.remove()

请求删除参数文件.

此接口一般用在远程升级时，需要用新的config.lua覆盖原来的参数文件的场景，在此场景下，远程升级包下载成功后，在确定要重启前调用此接口<br>下次开机执行nvm.init("config.lua")时，会用新的config.lua文件自动覆盖参数文件；以后再开机就不会自动覆盖了<br>也就是说"nvm.remove()->重启->nvm.init("config.lua")"是一个仅执行一次的完整操作

* 参数

无

* 返回值

nil

* 例子

```lua
nvm.remove()
```

---
