
@[TOC]

# sms

模块功能：短信功能

## sms.send(num, data, cbFnc, idx)

发送短信

* 参数

|名称|传入值类型|释义|
|-|-|-|
|num|string|短信接收方号码，ASCII码字符串格式|
|data|string|短信内容，GB2312编码的字符串<br>如果短信内容中只有ascii可见字符，则超过160个字符时，会被拆分为几条长级联短信进行发送<br>如果短信内容中包含除ascii可见字符外的其他字符，例如包含汉字，一个汉字算作一个字符，一个ascii可见字符也算作一个字符，超过70个字符时，会被拆分为几条长级联短信进行发送|
|cbFnc|function|**可选参数，默认为`nil`** 短信发送结果异步返回时的用户回调函数，回调函数的调用形式为：<br>cbFnc(result,num,data)<br>num：短信接收方的号码，ASCII码字符串格式<br>data：短信内容，unicode大端编码的HEX字符串|
|idx|number|**可选参数，默认为`nil`** 插入短信发送缓冲表的位置，默认是插入末尾|

* 返回值

result，true表示调用接口成功（并不是短信发送成功，短信发送结果，通过sendcnf返回，如果有cbFnc，会通知cbFnc函数）；返回false，表示调用接口失败

* 例子

```lua
sms.send("10086","test",cbFnc)
```

---

## sms.setNewSmsCb(cbFnc)

设置新短信的用户处理函数

* 参数

|名称|传入值类型|释义|
|-|-|-|
|cbFnc|function|新短信的用户处理函数|

* 返回值

nil

* 例子

```lua
sms.setNewSmsCb(cbFnc)
```

---
