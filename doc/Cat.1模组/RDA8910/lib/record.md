
@[TOC]

# record

模块功能：录音处理

## record.start(seconds, cbFnc, type, quality, rcdType, format, streamRptLen)

开始录音

* 参数

|名称|传入值类型|释义|
|-|-|-|
|seconds|number|录音时长，单位：秒<br>流录音模式下，如果想长时间录音，可以将此参数设置为0x7FFFFFFF，相当于录音2147483647秒=24855天|
|cbFnc|function|**可选参数，默认为`nil`** 录音回调函数：<br>当type参数为"FILE"时，回调函数的调用形式为：<br>cbFnc(result,size)<br>result：录音结果，true表示成功，false或者nil表示失败<br>size：number类型，录音文件的大小，单位是字节，在result为true时才有意义<br>当type参数为"STREAM"时，回调函数的调用形式为：<br>cbFnc(result,size,tag)<br>result：录音结果，true表示成功，false或者nil表示失败<br>size：number类型，每次上报的录音数据流的大小，单位是字节，在result为true时才有意义<br>tag：string类型，"STREAM"表示录音数据流通知，"END"表示录音结束|
|type|string|**可选参数，默认为`"FILE"`** 录音模式<br>"FILE"表示文件录音模式，录音数据自动保存在文件中，录音结束后，执行一次cbFnc函数<br>"STREAM"表示流录音模式，录音数据保存在内存中，每隔一段时间执行一次cbFnc函数去读取录音数据流，录音结束后再执行一次cbFnc函数|
|quality|number|**可选参数，默认为`1`** 录音质量，0：一般质量，1：中等质量，2：高质量，3：无损质量|
|rcdType|number|**可选参数，默认为`2`** 录音类型，n:1:mic(从麦克风录制)，2:voice(录制语音通话，录制的流与上下行通道)，3:voice_dual(在poc模式下从麦克风录制)|
|format|number|**可选参数，默认为`3`** 录音格式，1:pcm，2:wav，3:amrnb，4:speex<br>pcm格式：录音质量参数无效，采样率：8000，单声道，采样精度：16 bit，5秒钟录音80KB左右<br>wav格式：录音质量参数无效，比特率：128kbps，5秒钟录音80KB左右<br>amrnb格式：录音质量参数有效<br>录音质量为0时：比特率：5.15kbps，5秒钟录音3KB多<br>录音质量为1时：比特率：6.70kbps，5秒钟录音4KB多<br>录音质量为2时：比特率：7.95kbps，5秒钟录音4KB多<br>录音质量为3时：比特率：12.2kbps，5秒钟录音7KB多<br>speex格式：录音质量参数无效，pcm格式128kbps后的压缩格式，5秒钟6KB左右|
|streamRptLen|number|**可选参数，默认为`nil`** 流录音时，每次上报的字节阀值|

* 返回值

无

* 例子

```lua
-- 文件录音模式，录音5秒，一般质量，amrnb格式，录音结束后执行cbFnc函数：
record.start(5,cbFnc)
-- 流录音模式，录音5秒，一般质量，amrnb格式，每隔一段时间执行一次cbFnc函数，录音结束后再执行一次cbFnc函数：
record.start(5,cbFnc,"STREAM")
-- 流录音模式，录音5秒，一般质量，amrnb格式，每产生500字节的录音数据执行一次cbFnc函数，录音结束后再执行一次cbFnc函数：
record.start(5,cbFnc,"STREAM",nil,nil,500)
```

---

## record.stop(cbFnc)

停止录音

* 参数

|名称|传入值类型|释义|
|-|-|-|
|cbFnc|function|**可选参数，默认为`nil`** 停止录音的回调函数(停止结果通过此函数通知用户)，回调函数的调用形式为：<br>cbFnc(result)<br>result：number类型<br>0表示停止成功<br>1表示之前已经发送了停止动作，请耐心等待停止结果的回调|

* 返回值

无

* 例子

```lua
record.stop(cb)
```

---

## record.getFilePath()

读取录音文件的完整路径

* 参数

无

* 返回值

string 录音文件的完整路径

* 例子

```lua
filePath = record.getFilePath()
```

---

## record.getData(offset, len)

读取录音数据

* 参数

|名称|传入值类型|释义|
|-|-|-|
|offset|param|偏移位置|
|len|param|长度|

* 返回值

data 录音数据

* 例子

```lua
data = record.getData(0, 1024)
```

---

## record.getSize()

读取录音文件总长度，录音时长

* 参数

无

* 返回值

fileSize 录音文件大小
duration 录音时长

* 例子

```lua
fileSize, duration = record.getSize()
```

---

## record.delete()

删除录音

* 参数

无

* 返回值

无

* 例子

```lua
record.delete()
```

---

## record.exists()

判断是否存在录音

* 参数

无

* 返回值

result true - 有录音 false - 无录音

* 例子

```lua
result = record.exists()
```

---

## record.isBusy()

是否正在处理录音

* 参数

无

* 返回值

result true - 正在处理 false - 空闲

* 例子

```lua
result = record.isBusy()
```

---
