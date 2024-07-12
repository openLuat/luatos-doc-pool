
@[TOC]

# audio

模块功能：音频播放.

支持MP3、amr文件播放；

支持本地TTS播放、通话中TTS播放到对端（需要使用支持TTS功能的core软件）

## audio.play(priority, type, path, vol, cbFnc, dup, dupInterval)

播放音频

* 参数

|名称|传入值类型|释义|
|-|-|-|
|priority|number|音频优先级，数值越大，优先级越高<br>优先级高的播放请求会终止优先级低的播放<br>相同优先级的播放请求，播放策略参考：audio.setStrategy接口|
|type|string|音频类型，目前仅支持"FILE"、"TTS"|
|path|string|音频文件路径，跟typ有关<br>typ为"FILE"时：表示音频文件路径<br>typ为"TTS"时：表示要播放的UTF8编码格式的数据|
|vol|number|**可选参数，默认为`4`** 播放音量，取值范围0到7，0为静音|
|cbFnc|function|**可选参数，默认为`nil`** 音频播放结束时的回调函数，回调函数的调用形式如下：<br>cbFnc(result)<br>result表示播放结果：<br>0-播放成功结束；<br>1-播放出错<br>2-播放优先级不够，没有播放<br>3-传入的参数出错，没有播放<br>4-被新的播放请求中止<br>5-调用audio.stop接口主动停止|
|dup|bool|**可选参数，默认为`nil`** 是否循环播放，true循环，false或者nil不循环|
|dupInterval|number|**可选参数，默认为`0`** 循环播放间隔(单位毫秒)，dup为true时，此值才有意义|

* 返回值

result，bool或者nil类型，同步调用成功返回true，否则返回false

* 例子

```lua
audio.play(0,"FILE","/lua/call.mp3")
audio.play(0,"FILE","/lua/call.mp3",7)
audio.play(0,"FILE","/lua/call.mp3",7,cbFnc)
-- 更多用法参考demo/audio/testAudio.lua
```

---

## audio.stop(cbFnc)

停止音频播放

* 参数

|名称|传入值类型|释义|
|-|-|-|
|cbFnc|function|**可选参数，默认为`nil`** 停止音频播放的回调函数(停止结果通过此函数通知用户)，回调函数的调用形式为：<br>cbFnc(result)<br>result：number类型<br>0表示停止成功|

* 返回值

nil

* 例子

```lua
audio.stop()
```

---

## audio.setVolume(vol)

设置喇叭音量等级

* 参数

|名称|传入值类型|释义|
|-|-|-|
|vol|number|音量值为0-7，0为静音|

* 返回值

bool result，设置成功返回true，失败返回false

* 例子

```lua
audio.setVolume(7)
```

---

## audio.setCallVolume(vol)

设置通话音量等级

* 参数

|名称|传入值类型|释义|
|-|-|-|
|vol|number|音量值为0-7，0为静音|

* 返回值

bool result，设置成功返回true，失败返回false

* 例子

```lua
audio.setCallVolume(7)
```

---

## audio.setMicGain(mode, level)

设置mic增益等级

通话时mic增益在通话建立成功之后设置才有效<br>录音mic增益设置后实时生效

* 参数

|名称|传入值类型|释义|
|-|-|-|
|mode|string|增益类型<br>"call"表示通话中mic增益<br>"record"表示录音mic增益|
|level|number|增益等级，取值为0-7|

* 返回值

bool result，设置成功返回true，失败返回false

* 例子

```lua
audio.setMicGain("record",7)，设置录音时mic增益为7级
```

---

## audio.getVolume()

获取喇叭音量等级

* 参数

无

* 返回值

number vol，喇叭音量等级

* 例子

```lua
audio.getVolume()
```

---

## audio.getCallVolume()

获取通话音量等级

* 参数

无

* 返回值

number vol，通话音量等级

* 例子

```lua
audio.getCallVolume()
```

---

## audio.setStrategy(strategy)

设置优先级相同时的播放策略

* 参数

|名称|传入值类型|释义|
|-|-|-|
|strategy|number|优先级相同时的播放策略；<br>0：表示继续播放正在播放的音频，忽略请求播放的新音频<br>1：表示停止正在播放的音频，播放请求播放的新音频|

* 返回值

nil

* 例子

```lua
audio.setStrategy(0)
audio.setStrategy(1)
```

---

## audio.setTTSSpeed(speed)

设置TTS朗读速度

* 参数

|名称|传入值类型|释义|
|-|-|-|
|speed|number|速度范围为0-100，默认50|

* 返回值

bool result，设置成功返回true，失败返回false

* 例子

```lua
audio.setTTSSpeed(70)
```

---

## audio.setChannel(output, input)

设置音频输入、输出通道

设置后实时生效

* 参数

|名称|传入值类型|释义|
|-|-|-|
|output|number|**可选参数，默认为`2`** 0：earphone听筒，1：headphone耳机，2：speaker喇叭|
|input|number|**可选参数，默认为`0`** 0：主mic，3：耳机mic|

* 返回值

nil

* 例子

```lua
-- 设置为听筒输出：audio.setChannel(0)
-- 设置为耳机输出：audio.setChannel(1)
-- 设置为喇叭输出：audio.setChannel(2)
-- 设置为喇叭输出、耳机mic输入：audio.setChannel(2,3)
```

---
