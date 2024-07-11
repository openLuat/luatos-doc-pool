@[TOC]

# audiocore
audio支持库
## audiocore.play(audioFilePath)	

播放音频文件,音频文件格式支持：mp3、wav、amr、pcm

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|audioFilePath|string|音频文件的完整路径|如果是Luatools烧录的音频文件xxx.mp3,则文件完整路径为"lua/xxx.mp3"如果是sd卡中根目录下的音频文件yyy.mp3,则文件完整路径为"sdcard0/yyy.mp3"其余路径根据实际值传入即可|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|bool|result,返回同步播放结果|false表示不允许播放true表示允许播放,并且已经去执行播放动作;异步播放结果通过消息rtos.MSG_AUDIO通知到Lua脚本,消息携带参数msg.play_end_ind，true表示播放成功结束,其余值表示播放失败|

**例子**

```lua
--local function audioMsg(msg)  
    log.info("audio.MSG_AUDIO",msg.play_end_ind)  
    sys.publish("LIB_AUDIO_PLAY_IND","RESULT",msg.play_end_ind)  
end  

--注册core上报的rtos.MSG_AUDIO消息的处理函数  
rtos.on(rtos.MSG_AUDIO,audioMsg)  
audiocore.play("/lua/call.mp3")  

```
此API仅推荐给lib脚本使用，不推荐用户应用脚本使用；
用户应用脚本可以直接使用audio API，链接为：[audio.play](https://doc.openluat.com/wiki/21?wiki_page_id=2266#audioplaypriority_type_path_vol_cbFnc_dup_dupInterval_11 "audio.play")

---


## audiocore.playdata(audioData,audioFormat,[audioLoop])

功能：播放音频数据音频数据格式支持：mp3、wav、amr、pcm、spx

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|audioData|string|音频数据内容|   |
|audioFormat|number|音频数据格式|audiocore.MP3<br/>audiocore.WAV<br/>audiocore.AMR<br/>audiocore.PCM<br/>audiocore.SPX|
|audioLoop|number|是否循环播放|可选参数,默认不循环,1表示循环播放0或者nil表示仅播放一次,不循环播放|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|bool|返回同步播放结果|false表示不允许播放<br/>true表示允许播放，并且已经去执行播放动作；异步播放结果通过消息rtos.MSG_AUDIO通知到Lua脚本，消息携带参数msg.play_end_ind，true表示播放成功结束，其余值表示播放失败|

**例子**

```lua
--local function audioMsg(msg)  
    log.info("audio.MSG_AUDIO",msg.play_end_ind)  
    sys.publish("LIB_AUDIO_PLAY_IND","RESULT",msg.play_end_ind)  
end  
--注册core上报的rtos.MSG_AUDIO消息的处理函数  
rtos.on(rtos.MSG_AUDIO,audioMsg)  
audiocore.play(io.readFile("/lua/call.mp3"),audiocore.MP3)  

```
此API仅推荐给lib脚本使用，不推荐用户应用脚本使用；
用户应用脚本可以直接使用audio API，链接为：[audio.play](https://doc.openluat.com/wiki/21?wiki_page_id=2266#audioplaypriority_type_path_vol_cbFnc_dup_dupInterval_11 "audio.play")

---



## audiocore.stop()

停止音频播放

**参数**

无

**返回值**

无

**例子**

```lua
 --[[
     注意事项：
在音频播放状态下，调用audiocore.stop()后，会有一个异步消息rtos.MSG_AUDIO通知到Lua脚本，
消息携带参数msg.play_end_ind的值为false，表示播放失败；
无音频播放状态下，调用audiocore.stop()后，没有任何消息通知到Lua脚本]]

```
此API仅推荐给lib脚本使用，不推荐用户应用脚本使用；
用户应用脚本可以直接使用audio API，链接为：[audio.stop](https://doc.openluat.com/wiki/21?wiki_page_id=2266#audiostopcbFnc_42 "audio.stop")

---



## audiocore.pause()

暂停播放音频文件

**参数**

无

**返回值**

无

---



## audiocore.resume()

语音播放的恢复播放功能

**参数**

无

**返回值**

无

**例子**

```lua
audiocore.resume()

```

---



## audiocore.record(audioFileName,recordTimeSec [,audioQual] [,audioType] [,audioFormat])

录音接口

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|audioFileName|string|保存录音数据的文件名| |
|recordTimeSec|number|录音时长|取值>0，单位秒/s|
|audioQual|number|录制音频质量|可选参数:<br/>0///< quality low;<br/>1///< quality medium;<br/>2///< quality high;<br/>3///< quality best。|
|audioType|number|录制音频数据类型|可选参数:<br/>audiocore.RECORE_MIC///从麦克风录制;<br/>audiocore.RECORE_VOICE///录制语音通话，录制的流与上下行通道;<br/>audiocore.RECORE_POC///在poc模式下从麦克风录制。|
|audioFormat|number|录制音频数据格式|可选参数:<br/>audiocore.MP3<br/>audiocore.WAV<br/>audiocore.AMR<br/>audiocore.PCM<br/>audiocore.SPX<br/>|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|bool|返回录音结果|TURE:录音成功;<br/>FALSE:录音失败。|

**例子**

```lua
--
audiocore.record("music",10,2,audiocore.RECORE_MIC,audiocore.MP3) 

```
此API仅推荐给lib脚本使用，不推荐用户应用脚本使用；
用户应用脚本可以直接使用record API，链接为：[record.start](https://doc.openluat.com/wiki/21?wiki_page_id=2289#recordstartseconds_cbFnc_type_quality_rcdType_format_streamRptLen_7 "record.start")

---



## audiocore.streamrecord(recordTimeSec [,audioQual] [,audioType] [,audioFormat] [,length]) 

流录音接口

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|recordTimeSec|number|录音时长|取值>0，单位秒/s|
|audioQual|number|录制音频质量|可选参数:<br/>0///< quality low;<br/>1///< quality medium;<br/>2///< quality high;<br/>3///< quality best。|
|audioType|number|录制音频数据类型|可选参数:<br/>audiocore.RECORE_MIC///从麦克风录制;<br/>audiocore.RECORE_VOICE///录制语音通话，录制的流与上下行通道;<br/>audiocore.RECORE_POC///在poc模式下从麦克风录制。|
|audioFormat|number|录制音频数据格式|可选参数:<br/>audiocore.MP3<br/>audiocore.WAV<br/>audiocore.AMR<br/>audiocore.PCM<br/>audiocore.SPX<br/>|
|length|number|触发录音回调的长度阈值|可选参数:取值>0,单位字节|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|bool|返回录音结果|TURE:录音成功;<br/>FALSE:录音失败。|

**例子**

```lua
--
audiocore.streamrecord(10,2,audiocore.RECORE_MIC,audiocore.MP3) 

```
此API仅推荐给lib脚本使用，不推荐用户应用脚本使用；
用户应用脚本可以直接使用record API，链接为：[record.start](https://doc.openluat.com/wiki/21?wiki_page_id=2289#recordstartseconds_cbFnc_type_quality_rcdType_format_streamRptLen_7 "record.start")

---



## audiocore.stoprecord()

停止录音

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|bool|返回录音结果|TURE:停止录音成功;<br/>FALSE:停止录音失败。|

**例子**

```lua
 --
 audiocore.stoprecord() 

```
此API仅推荐给lib脚本使用，不推荐用户应用脚本使用；
用户应用脚本可以直接使用record API，链接为：[record.stop](https://doc.openluat.com/wiki/21?wiki_page_id=2289#recordstopcbFnc_40 "record.stop")

---



## audiocore.deleterecord()

删除录音

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|返回录音结果|取值为1。|

**例子**

```lua
 --
 audiocore.deleterecord() 

```
此API仅推荐给lib脚本使用，不推荐用户应用脚本使用；
用户应用脚本可以直接使用record API，链接为：[record.delete](https://doc.openluat.com/wiki/21?wiki_page_id=2289#recorddelete_126 "record.delete")

---



## audiocore.streamrecordread(size)

读录音数据流数据

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|size|number|录音数据流的大小|单位是字节|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|buf|string|录音数据流数据|   |

---



## audiocore.streamplay(audioFormat,audioData[,audiotype])

功能：流式播放音频数据<br/>音频数据格式支持：mp3、wav、amr、pcm、spx

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|audioFormat|number|音频数据格式|audiocore.MP3<br/>audiocore.WAV<br/>audiocore.AMR<br/>audiocore.PCM<br/>audiocore.SPX<br/>|
|audioData|string|音频数据内容|   |
|audiotype|number|音频播放类型|audiocore.PLAY_LOCAL<br/>audiocore.PLAY_VOLTE<br/>audiocore.PLAY_POC|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|acceptedAudioDataLen|number|接受的音频数据长度|    |

**例子**

```lua
[[注意事项：流式播放音频数据时，在core中有一个4K字节的缓冲区，用来存放音频数据，调用audiocore.streamplay接口时，
音频数据被填充到这个缓冲区内，被填充的最大长度为缓冲区的剩余字节数；例如缓冲区还剩1000字节可以填充，
如果此时调用audiocore.streamplay填充3000字节数据，则实际只能将这3000字节数据的前1000字节填充到缓冲区，
返回值acceptedAudioDataLen的值为1000，表示填充的字节数，剩余的2000字节被丢弃]]
local tBuffer = {}  
local tStreamType  

local function consumer()  
    sys.taskInit(function()  
        audio.setVolume(7)  
        while true do  
            while #tBuffer==0 do  
                sys.waitUntil("DATA_STREAM_IND")  
            end  
            local data = table.remove(tBuffer,1)  
            --log.info("testAudioStream.consumer remove",data:len())  
            local procLen = audiocore.streamplay(tStreamType,data)  
            if procLen<data:len() then  
                --log.warn("produce fast")  
                table.insert(tBuffer,1,data:sub(procLen+1,-1))  
                sys.wait(5)  
            end  
        end  
    end)  
end  

local function producer(streamType)  
    sys.taskInit(function()  
        while true do  
            tStreamType = streamType  
            local tAudioFile =  
            {  
                [audiocore.AMR] = "tip.amr",  
                [audiocore.SPX] = "record.spx",  
                [audiocore.PCM] = "alarm_door.pcm",  
            }  
            local fileHandle = io.open("/lua/"..tAudioFile[streamType],"rb")  
            if not fileHandle then  
                log.error("testAudioStream.producer open file error")  
                return  
            end  
            while true do  
                local data = fileHandle:read(streamType==audiocore.SPX and 1200 or 1024)  
                if not data then fileHandle:close() return end  
                table.insert(tBuffer,data)  
                if #tBuffer==1 then sys.publish("DATA_STREAM_IND") end  
                --log.info("testAudioStream.producer",data:len())  
                sys.wait(10)  
            end   
        end  
    end)  
end  

sys.timerStart(function()  
    --producer(audiocore.AMR)  
    --producer(audiocore.SPX)  
    producer(audiocore.PCM)  
    consumer()  
end,3000)  

```

---



## audiocore.streamremain()	

功能：获取core中流式播放缓冲区剩余未播放的音频流字节数

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|remainLen|number|缓冲区剩余未播放的音频流字节数|   |

**例子**

```lua
 --[[
     注意事项：
    流式播放音频数据时，在core中有一个4K字节的缓冲区，用来存放音频数据，调用audiocore.streamplay接口时，
    音频数据被填充到这个缓冲区内，audiocore.streamreamin接口的返回值是缓冲区内未播放的音频流数据字节数
 ]]
sys.taskInit(function()  
    sys.wait(5000)  
    local audioData = io.readFile("/lua/tip.amr")  
    --此处audiocore.streamremain()返回0  
    log.info("begin streamremain",audiocore.streamremain())  
    audiocore.streamplay(audiocore.AMR,audioData:sub(1,2000))  
    --此处audiocore.streamremain()返回值不定，和core中rtos系统调度有关  
    log.info("after streamplay 2000, streamremain",audiocore.streamremain())  
    sys.wait(2000)  
    --此处audiocore.streamremain()返回0  
    log.info("play done, streamremain",audiocore.streamremain())  
end)  

```

---



## audiocore.setpa(audioClass)

功能：设置音频功放类型

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|audioClass|number|音频功放类型|audiocore.CLASS_AB<br/>audiocore.CLASS_D|

**返回值**

无

示例参考：[testAudio.lua](https://gitee.com/openLuat/Luat_Lua_Air724U/blob/master/script_LuaTask/demo/audio/testAudio.lua "testAudio.lua")

---



## audiocore.getpa()

功能：获取外部pa控制参数

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|audioClass|number|音频功放类型|audiocore.CLASS_AB<br/>audiocore.CLASS_D|

---



## audiocore.pa(gpio,devout[,plus_count][,plus_period][,enable][,plus_delay])

功能：设置外部pa控制参数

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|gpio|number|gpio id|0到31|
|devout|number|音频输出通道|0：RECEIVER<br/>1：HEADPHONE<br/>2：SPEAKER|
|plus_count|number|输出波形个数，默认为3个可选参数|   |
|plus_period|number|输出波形的时间单位us，默认为2us可选参数|   |
|enable|number|外部pa使能控制参数,默认为使能1可选参数|1/0|
|plus_delay|number|打开功放的延时时间单位ms，默认为0 可选参数| |

**返回值**

无

示例参考：[testAudio.lua](https://gitee.com/openLuat/Luat_Lua_Air724U/blob/master/script_LuaTask/demo/audio/testAudio.lua "testAudio.lua")

---



## audiocore.head_plug(type)

功能：耳机配置

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|type|number|耳机动作|0：耳机拔出<br/>1：4段耳机插入<br/>2：3段耳机插入|

**返回值**

无

---



## audiocore.headsetinit(auto)

功能：开启耳机监测功能

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|auto|number|控制模式|0:耳机插拔会有消息上报给脚本应用，脚本根据消息自行处理<br/>1:耳机插拔没有消息上报给脚本应用，音频通道自动切换   |

**返回值**

无

**例子**

```lua
[[
当auto设置为0时，耳机插拔会有消息上报给脚本应用，上报的消息为table类型，具体参数如下：
  参数      类型      释义              取值

   number  msg.type  耳机消息           1：HEADSET_PLUGIN，耳机插入
                                        2：HEADSET_PLUGOUT，耳机拔出
                                        3：HEADSET_BTN_DOWN，耳机按键按下
                                        4：HEADSET_BTN_UP，耳机按键弹起

number  msg.param 当msg.type为1时，      UNKNOWN_MIC_TYPE = 0,
                  携带的参数             HEADSET_TYPE_NO_MIC = 1,
                                        HEADSET_TYPE_4POLE_NORMAL = 2,
                                        HEADSET_TYPE_4POLE_NOT_NORMAL = 3,
                                        HEADSET_TYPE_APPLE = 4,
                                        HEADSET_TYPE_ERR = 5 ，
目前按键功能尚不支持
]]

local function headsetCB(msg)   
    --log.info("audio.MSG_AUDIO",msg.type,msg.param)  
end  
--注册core上报的rtos.MSG_AUDIO消息的处理函数  
rtos.on(rtos.MSG_HEADSET,headsetCB)  
audiocore.headsetinit(0) 

```

---



## audiocore.rtmpopen(url[,timeout][,bufferms])

功能：打开rtmp拉流

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|url|string|rtmp流的url地址|   |
|timeout|number|rtmp拉流超时时间单位s|默认10s|
|bufferms|number|rtmp缓冲区时间单位ms|默认1h|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|boolean|成功/失败|TRUE/FALSE|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2332 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2191 "示例")

---



## audiocore.rtmpclose()

功能：关闭rtmp拉流

**参数**

无

**返回值**

无

**例子**

```lua
注意事项：在音频播放状态下，调用audiocore.rtmpclose()后，会有一个异步消息rtos.MSG_RTMP通知到Lua脚本

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2332 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2191 "示例")

---



## audiocore.pocstart(audioFormat[,audioQual])

功能：打开全双工对讲

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|audioFormat|number|音频数据格式|audiocore.AMR<br/>audiocore.PCM|
|audioQual|number|录制amr音频质量|可选参数:<br/>0///< quality low;<br/>1///< quality medium;<br/>2///< quality high;<br/>3///< quality best。|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|boolean|成功/失败|TRUE/FALSE|

参考示例：[示例](https://doc.openluat.com/wiki/21?wiki_page_id=4561 "示例")

---



## audiocore.pocstop()

功能：关闭全双工对讲

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|boolean|成功/失败|TRUE/FALSE|

参考示例：[示例](https://doc.openluat.com/wiki/21?wiki_page_id=4561 "示例")

---



## audiocore.pocstreamplay(audioData)

功能：全双工对讲流式播放音频数据

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|audioData|string|音频数据内容|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|acceptedAudioDataLen|number|接受的音频数据长度|    |

参考示例：[示例](https://doc.openluat.com/wiki/21?wiki_page_id=4561 "示例")

---



## audiocore.pocstopplay()

功能：全双工对讲停止播放

**参数**

无

**返回值**

无

参考示例：[示例](https://doc.openluat.com/wiki/21?wiki_page_id=4561 "示例")

---



## audiocore.pocrecord(audioFileName,recordTimeSec)

功能：全双工对讲录音接口

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|audioFileName|string|保存录音数据的文件名| |
|recordTimeSec|number|录音时长|取值>0，单位秒/s|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|bool|返回录音结果|TURE:录音成功;<br/>FALSE:录音失败。|

参考示例：[示例](https://doc.openluat.com/wiki/21?wiki_page_id=4561 "示例")

---



## audiocore.pocstreamrecord(recordTimeSec [,length]) 

功能：全双工对讲流录音接口

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|recordTimeSec|number|录音时长|取值>0，单位秒/s|
|length|number|触发录音回调的长度阈值|可选参数:取值>0,单位字节|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|bool|返回录音结果|TURE:录音成功;<br/>FALSE:录音失败。|

参考示例：[示例](https://doc.openluat.com/wiki/21?wiki_page_id=4561 "示例")

---



## audiocore.pocstoprecord()

功能：全双工对讲停止录音

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|bool|返回录音结果|TURE:停止录音成功;<br/>FALSE:停止录音失败。|

参考示例：[示例](https://doc.openluat.com/wiki/21?wiki_page_id=4561 "示例")

---



