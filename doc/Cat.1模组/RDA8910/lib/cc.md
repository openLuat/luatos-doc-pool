
@[TOC]

# cc

模块功能：通话管理

## cc.anyCallExist()

是否存在通话

* 参数

无

* 返回值

bool result 存在通话返回true，否则返回false

* 例子

```lua
result = cc.anyCallExist()
```

---

## cc.getState(num)

查询某个号码的通话状态

* 参数

|名称|传入值类型|释义|
|-|-|-|
|num|string|查询号码|

* 返回值

number state 通话状态，状态值参考本模块Fields定义

* 例子

```lua
state = cc.getState('10086')
```

---

## cc.dial(num, delay)

呼出电话

* 参数

|名称|传入值类型|释义|
|-|-|-|
|num|string|呼出号码|
|delay|number|**可选参数，默认为`0`** 延时delay毫秒后，才发起呼叫|

* 返回值

bool result，true表示允许发送at命令拨号并且发送at，false表示不允许at命令拨号

* 例子

```lua
cc.dial('10086')
```

---

## cc.hangUp(num)

挂断通话

* 参数

|名称|传入值类型|释义|
|-|-|-|
|num|string|号码，若指定号码通话状态不对，则直接退出，不会执行挂断，若挂断时会挂断所有电话|

* 返回值

nil

* 例子

```lua
cc.hangUp('10086')
```

---

## cc.accept(num)

接听电话

* 参数

|名称|传入值类型|释义|
|-|-|-|
|num|string|号码，若指定号码通话状态不对，则直接退出，不会接通|

* 返回值

nil

* 例子

```lua
cc.accept('10086')
```

---

## cc.transVoice(data, loop, downLinkPlay)

通话中发送声音到对端,必须是12.2K AMR格式

* 参数

|名称|传入值类型|释义|
|-|-|-|
|data|string|12.2K，AMR格式的数据|
|loop|bool|**可选参数，默认为`nil`** 是否循环发送，true为循环，其余为不循环|
|downLinkPlay|bool|**可选参数，默认为`nil`** 声音是否在本端播放，true为播放，其余为不播放|

* 返回值

bool result true为成功，false为失败

* 例子

```lua
cc.transVoice("#!AMR\010\060*********")
cc.transVoice("#!AMR\010\060*********",true)
cc.transVoice("#!AMR\010\060*********",true,true)
```

---

## cc.dtmfDetect(enable, sens)

设置dtmf检测是否使能以及灵敏度

* 参数

|名称|传入值类型|释义|
|-|-|-|
|enable|bool|**可选参数，默认为`nil`** true使能，false或者nil为不使能|
|sens|number|**可选参数，默认为`3`** 灵敏度，最灵敏为1|

* 返回值

nil

* 例子

```lua
cc.dtmfDetect(true)
```

---

## cc.sendDtmf(str, playtime, intvl)

发送dtmf到对端

* 参数

|名称|传入值类型|释义|
|-|-|-|
|str|string|dtmf字符串，仅支持数字、ABCD*#|
|playtime|number|**可选参数，默认为`100`** 每个dtmf播放时间，单位毫秒|
|intvl|number|**可选参数，默认为`100`** 两个dtmf间隔，单位毫秒|

* 返回值

nil

* 例子

```lua
cc.sendDtmf("123")
```

---
