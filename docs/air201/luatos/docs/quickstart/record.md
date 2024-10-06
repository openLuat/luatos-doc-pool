# 使用Air201做录音和播放录音的功能
Air201可以支持本地的录音功能，并且将录音保存的数据进行播放，下面我们将开始帮助您如何从零上手，实现录音和播放的功能。

## 1, 搭建环境

此时也可以在Luatools项目管理中新建一个项目，重新选择底层CORE和脚本

或者在原有项目的基础上，不更换CORE，将原来的脚本删除，添加为demo/record的脚本。

### 1.1 **获取软件资料**

   固件链接：https://gitee.com/openLuat/LuatOS-Air201/tree/master/core

   脚本链接：https://gitee.com/openLuat/LuatOS-Air201/tree/master/demo/record

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=NDQ3YzkyMDg0NmQ5Mjk5YmMyYzQ4Y2QxY2FkZmMxZDlfbERrVXFjUGNGM2dmU2Z4UHFMSHBoa0RsdElEMTNFYmRfVG9rZW46R1FaUWJaOHRIb1NycXR4Mjl0QmN3NGx6bmxmXzE3MjgxMzcwMzM6MTcyODE0MDYzM19WNA)

### 1.2 连接喇叭

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=MjhhMjQ0YWFmNTUxZDE3ZjQyMjZmMzgxNmVhZWQ4MDZfZHVYbWJQSFgwV2dSN05Zb0ZSV0tvU0NqQ3hPemdQY3ZfVG9rZW46STlmMWJmWTdIb1JUbXh4ekd6UGN0ZDJtbkNiXzE3MjgxMzcwMzM6MTcyODE0MDYzM19WNA)

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=Mjk5M2Y0YmIzZTI2YzQ1ZTA1YWIzNWFkYThmZGQxNmZfVFR1VkJkRHNQcUpYODdOZmpHWTlhMW8xaW14dEZYQlNfVG9rZW46QTc2UmI0RDhCb0RTMDB4eFhsc2M2RHZXbjNpXzE3MjgxMzcwMzM6MTcyODE0MDYzM19WNA)![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=Zjk0OTE0NWUyMTQwYTZmYjM4NGUxMDAyMTA0Y2UwOTNfTWlTbzFYM0Z3QkdGaHFMb2VmUmdUMEhTWldFdkNOeDBfVG9rZW46U3R5NWI1V3R6b0hrWVd4N2NoSmNxOW83bkZnXzE3MjgxMzcwMzM6MTcyODE0MDYzM19WNA)

## 2, 调试代码

> **使用克隆的代码中 LuatOS-Air201\demo\record 的代码测试**

###  2.1 初始化驱动es8311

Air201板子自带了es8311音频解码芯片（audio codec），所以硬件配置参数是固定的。

- es8311使用了I2C0，电源脚为GPIO2，pa控制脚为GPIO23

```Lua
local es8311i2cId = 0       -- I2CID
local es8311PowerPin = 2    -- ES8311电源控制引脚
local paPin = 23            -- PA放大器控制引脚

mcu.altfun(mcu.I2C, es8311i2cId, 13, 2, 0)
mcu.altfun(mcu.I2C, es8311i2cId, 14, 2, 0)

i2c.setup(es8311i2cId, i2c.SLOW)
i2s.setup(0, 0, 16000, 16, i2s.MONO_R, i2s.MODE_LSB, 16)

audio.config(0, paPin, 1, 3, 100, es8311PowerPin, 1, 100)
audio.setBus(0, audio.BUS_I2S, {
    chip = "es8311",
    i2cid = es8311i2cId,
    i2sid = 0,
    voltage = audio.VOLTAGE_1800
}) -- 通道0的硬件输出通道设置为I2S

audio.vol(0, 80)        -- 喇叭输出音量
audio.micVol(0, 80)     -- mic输入音量
audio.pm(0, audio.POWEROFF)
```

### 2.2 注册音频事件回调函数

```Lua
-- @param id 通道id
-- @param event 事件类型，可以是以下之一：
--               0 开始解码文件
--               1 开始输出解码后的音数据
--               2 MORE_DATA: 底层驱动播放播放完一部分数据，需要更多数据
--               3 AUDIO_DONE: 底层驱动播放完全部数据了
--               4 DONE: 音频解码完成
--               5 TTS做完了必要的初始化，用户可以通过audio_play_tts_set_param做个性化配置
--               6 TTS编码完成了。注意不是播放完成
--               7 RECORD_DATA: 录音数据
--               8 RECORD_DONE: 录音完成
-- @param buff 事件相关的数据缓冲区
audio.on(0, function(id, event, buff)
    log.info("audio.on", id, event)
    -- 使用play来播放文件时只有播放完成回调
    if event == audio.RECORD_DATA then -- 录音数据

    elseif event == audio.RECORD_DONE then -- 录音完成
        sys.publish("AUDIO_RECORD_DONE")
    elseif event == audio.DONE or event == audio.MORE_DATA then -- 播放音频的事件
        local succ, stop, file_cnt = audio.getError(0)
        if not succ then
            if stop then
                log.info("用户停止播放")
            else
                log.info("第", file_cnt, "个文件解码失败")
            end
        end
        log.info("播放完成一个音频")
        sys.publish("AUDIO_PLAY_DONE")
    end
end)
```

### 2.3 准备录音

**录音****API****说明**

audio.record(id, record_type, record_time, amr_quailty, path, record_callback_time)

id：多媒体播放通道号

record_type：录音音频格式，支持audio.AMR和audio.PCM

record_time：录制时长 单位秒，可选参数，默认为0 则表示一直录制

amr_quailty：录音质量，只有在音频格式为audio.AMR的情况下此参数有效。

path：录音文件路径，可选参数，不指定则不保存，可以再audio.on回调函数中处理原始PCM数据

record_callback_time：单次录音回调时长，单位100ms 默认1，既100ms。在不指定录音文件路径时，此参数有效。

```Lua
-- 开始录音
log.info("准备开始录音")
audio.pm(0, audio.RESUME)   -- 工作模式
local err = audio.record(0, audio.AMR, 5, 7, recordPath)    -- 录制AMR格式，时长为5s的录音数据
result = sys.waitUntil("AUDIO_RECORD_DONE", 10000)  -- 等待录音结束，并设置10s超时（超时时间要设置的比录制时间长 否则会还没录完就被当做超时强制结束了）
log.info("录音结束")
audio.pm(0, audio.POWEROFF) -- 断电模式，工作结束后就休息，节省功耗
```

### 2.4 播放录音

播放录音需要使用 audio.play() 接口，需要将录音文件的存放路径（path），作为第二个参数传入，就可以将刚刚录音的文件，进行播放。

```Lua
-- 播放录音
log.info("准备播放录音")
local err = audio.play(0, recordPath)
result = sys.waitUntil("AUDIO_PLAY_DONE", 10000)    -- 等待录音文件播放结束，并设置10s超时（超时时间要设置的比录制时间长 否则会还没播放完就被当做超时强制结束了）
log.info("录音播放完成")
audio.pm(0, audio.POWEROFF) -- 断电模式，工作结束后就休息，节省功耗
```

## 3, 展示效果

将demo烧录至Air201开机后，等待蓝灯亮起后对着mic麦克说话

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=MTU3YmMxZjM3OTgwZmQ5NTljOTk0MjA1YWJmZWRiMDZfa0JmUjZQeklHeUVkYmlmY2wzWTRHRTU3Y1c5b24zTlVfVG9rZW46VE5MU2JJMGJ2b1g3Nzl4bUpaRWNmRjhMblRmXzE3MjgxMzcwMzM6MTcyODE0MDYzM19WNA)

经过5s后，蓝灯灭掉，会自动结束录音。随后间隔2s，红灯亮起，开始播放录音文件。

<video data-lark-video-uri="drivetoken://B8nTb4ltEojZUZxiHbGcaa5Fn9c" data-lark-video-mime="video/mp4" data-lark-video-size="5145384" data-lark-video-duration="0" data-lark-video-name="d3e50ea050fdf61bb8d688242b1e10d6.mp4" data-lark-video-width="720" data-lark-video-height="1280"></video>
