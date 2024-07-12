
@[TOC]

# pb

模块功能：电话簿管理

## pb.setStorage(storage, cb)

设置电话本存储区域

* 参数

|名称|传入值类型|释义|
|-|-|-|
|storage|string|存储区域字符串，仅支持"SM"|
|cb|param|设置后的回调函数<br><br>回调方式为cb(result)，result为true表示成功，false或者nil表示失败|

* 返回值

无

* 例子

```lua
pb.setStorage(storage,cb)
```

---

## pb.read(index, cb)

读取一条电话本记录

* 参数

|名称|传入值类型|释义|
|-|-|-|
|index|number|电话本在存储区的位置|
|cb|function|function类型，读取后的回调函数<br><br>回调方式为cb(result,name,number)：result为true表示成功，false或者nil表示失败；name为姓名；number为号码|

* 返回值

无

* 例子

```lua
pb.read(1,cb)
```

---

## pb.write(index, name, num, cb)

写入一条电话本记录

* 参数

|名称|传入值类型|释义|
|-|-|-|
|index|number|电话本在存储区的位置|
|name|string|姓名|
|num|string|号码|
|cb|function|functionl类型，写入后的回调函数<br><br>回调方式为cb(result)：result为true表示成功，false或者nil表示失败|

* 返回值

无

* 例子

```lua
pb.write(1,"zhangsan","13233334444",cb)
```

---

## pb.delete(index, cb)

删除一条电话本记录

* 参数

|名称|传入值类型|释义|
|-|-|-|
|index|number|电话本在存储区的位置|
|cb|function|function类型，删除后的回调函数<br><br>回调方式为cb(result)：result为true表示成功，false或者nil表示失败|

* 返回值

无

* 例子

```lua
pb.delete(1,cb)
```

---
