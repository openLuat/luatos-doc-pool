@[TOC]

# TTS
语音播报
## ttsply.initEngine()

初始化TTS播报引擎

**参数**

无

**返回值**

无

此API仅推荐给lib脚本使用，不推荐用户应用脚本使用；
用户应用脚本可以直接使用audio API，链接为：[audio](https://doc.openluat.com/wiki/21?wiki_page_id=2266 "audio")

---



## ttsply.setParm(cmd,value)

设置语音播报的参数

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|cmd|number|0/1/2/3 播报速度/音量/声调/文本格式命令|0/1/2/3|
|value|number|对应cmd0/1/2/3 播报速度/音量/声调/文本格式命值|  |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number| 0/1, 失败/成功|0/1|

**例子**

```lua
--[[
    value:
    播报速度值(cmd=0) 0-100
    播报音量值(cmd=1) 0-100
    播报声调值(cmd=2) 0-100
    播报文本格式值(cmd=3):
        0: ASCII
        1: GBK
        2: BIG5
        5: UTF8
        6: UTF16
        7: UNICODE
]]

```
此API仅推荐给lib脚本使用，不推荐用户应用脚本使用；
用户应用脚本可以直接使用audio API，链接为：[audio](https://doc.openluat.com/wiki/21?wiki_page_id=2266 "audio")

---



## ttsply.play(text)

文字播报

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|text|string|待播报的文字|  |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number| 0/1, 失败/成功|0/1|

**例子**

```lua
    ret = ttsply.play(text)

```
此API仅推荐给lib脚本使用，不推荐用户应用脚本使用；
用户应用脚本可以直接使用audio API，链接为：[audio](https://doc.openluat.com/wiki/21?wiki_page_id=2266 "audio")

---



## ttsply.stop()

停止文字播报

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number| 0/1, 失败/成功|0/1|

此API仅推荐给lib脚本使用，不推荐用户应用脚本使用；
用户应用脚本可以直接使用audio API，链接为：[audio](https://doc.openluat.com/wiki/21?wiki_page_id=2266 "audio")

---



