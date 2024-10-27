# 009：Air724UG-LuatOS-软件 demo-音频应用-音频录制

## **一、音频应用-音频录制概述**

音频录制应用是指利用 Air724UG 模块的音频输入功能，通过 MIC 捕捉声音信号，并将其转换为数字音频数据进行存储或传输的应用。除了 MIC 输入外，Air724UG 还支持扬声器（SPK）输出、耳机（HP）输出和听筒（RECEIVER）输出等多种音频输出模式，方便用户在不同场景下进行音频录制和播放。这一应用广泛适用于物联网设备中的语音交互、语音记录等场景。

## 二、准备硬件环境

“古人云：‘工欲善其事，必先利其器。’在深入介绍本功能示例之前，我们首先需要确保以下硬件环境的准备工作已经完成。”

### 2.1  Air724UG 开发板

本 demo 使用的是 Air724UG_A14 开发板，如下图所示：

![](static/O3fXb76ato6ZSCxxdjDcAogsn1f.png)

点击链接购买：[EVB_Air724UG_A14 开发板淘宝购买链接](https://item.taobao.com/item.htm?spm=a1z10.1-c-s.w5003-23813349255.25.43af346aVmYQNY&id=614125604268&scene=taobao_shop) ；

此开发板的详细使用说明参考：[Air724UG 产品手册](https://docs.openluat.com/air724ug/product/)中的开发板硬件资料中《EVB_Air724UG_A14 开发板使用说明.pdf》；开发板使用过程中遇到任何问题，可以直接参考这份使用说明 pdf 文档。

### 2.2 SIM 卡

请准备一张可正常上网的 SIM 卡，该卡可以是物联网卡或您的个人手机卡。

**特别提醒：**请确保 SIM 卡未欠费且网络功能正常，以便顺利进行后续操作。

### 2.3 PC 电脑

请准备一台配备 USB 接口且能够正常上网的电脑。

### 2.4 数据通信线

请准备一根用于连接 EVB_Air724UG_A14 开发板和 PC 电脑的数据线，该数据线将实现业务逻辑的控制与交互。

- USB 数据线：此数据线不仅用于为测试板供电，还用于查看数据日志。其一端为 Micro-B 接口（俗称老安卓口），用于连接 EVB_Air724UG_A14 开发板；另一端为标准 USB 接口，连接 PC 电脑。

![](static/FwY6bvFgtoOkYsxwrjJcGVvTnld.png)

### 2.5 组装硬件环境

#### 2.5.1 请按 SIM 卡槽指示方向正确插入 SIM 卡，避免插反损坏

通常，插入 SIM 卡的步骤如下：

- 将 SIM 卡的金属卡槽下滑打开。
- 平稳地将 SIM 卡放入卡槽。
- 上滑关闭卡槽。

![](static/LW51buLF8oHz6mxbDZHcTEnFn5d.png)
![](static/ZbUCbfTwPo3vsmx20wLcy9DOnkh.png)

#### 2.5.2 USB 数据线，连接电脑和 EVB_Air724UG_A14 开发板，如下图所示：

![](static/LHUfbBmfOoct5LxorJ3csBOznJd.png)

## 三、准备软件环境

“凡事预则立，不预则废。”在详细阐述本功能示例之前，我们需先精心筹备好以下软件环境。

### 3.1 Luatools 工具

要想烧录 AT 固件到 4G 模组中，需要用到合宙的强大的调试工具：Luatools；

下载地址：[Luatools v3 下载调试工具](https://luatos.com/luatools/download/last)。

Luatools 工具集具备以下几大核心功能：

- 一键获取最新固件：自动连接合宙服务器，轻松下载最新的合宙模组固件。
- 固件与脚本烧录：便捷地将固件及脚本文件烧录至目标模组中。
- 串口日志管理：实时查看模组通过串口输出的日志信息，并支持保存功能。
- 串口调试助手：提供简洁的串口调试界面，满足基本的串口通信测试需求。

Luatools 下载之后， 无需安装， 解压到你的硬盘，点击 Luatools_v3.exe 运行，出现如下界面，就代表 Luatools 安装成功了：

![](static/DmsMbL64aorKnlx31DJc4e5Gnwd.png)

### 3.2 烧录代码

首先要说明一点： 脚本代码， 要和固件的 LuatOS-Air_V4030_RDA8910_BT_TTS_FLOAT.pac（注：此固件支持 LCD,字库，图片，扫码，生成二维码，摄像头，TTS,WIFI Scan，蓝牙，SD 卡，FLOAT） 文件一起烧录。

**整体压缩文件：内含有 二个文件，一个演示视频，如图所示。**

![](static/OlOhbnJKFogzbsxKzbMcv159nbc.png)

#### 3.2.1 **压缩文件：完整文件包**

#### 3.2.2 **找到烧录的固件文件**

官网下载,底层 core 下载地址：[LuatOS 底层 core](https://docs.openluat.com/air724ug/luatos/firmware/)     **注：**本 demo 使用如图所示固件

![](static/JBw7bKtzco4hcfxTQ7DcaeeGnLh.png)

![](static/Emt9b5AcfoSoxFxrjkBcbBeynAc.png)

#### 3.2.3 **正确连接电脑和 4G 模组电路板**

使用带有数据通信功能的数据线，不要使用仅有充电功能的数据线；

#### 3.2.4 **识别 4G 模组的 boot 引脚**

在下载之前，要用模组的 boot 引脚触发下载， 也就是说，要把 4G 模组的 boot 引脚拉到 1.8v，或者直接把 boot 引脚和 VDD_EXT 引脚相连。我们要在按下 BOOT 按键时让模块开机，就可以进入下载模式了。

具体到 EVB_Air724UG_A14 开发板，

- 当我们模块没开机时，按着下载模式键然后长按开机键开机。
- 当我们模块开机时，按着下载模式键然后点按重启键即可。

![](static/DuZCbWChkobWBTxEOfycsjIYn2e.png)

#### 3.2.5 **识别电脑的正确端口**

判断是否进入 BOOT 模式：

- 模块上电，此时在电脑的设备管理器中，查看串口设备，如下图：

![](static/EswabnR3ooPCPxx4i7Rcs5EInoc.png)

- 先按下载模式在按一下重启，会出现一个端口表示进入了 boot 下载模式，如下图所示：

![](static/SmBTb61GDoCrT2xyILnclVsKnFf.png)

- 这时候， 硬件连接上就绪状态，恭喜你，可以进行烧录了！

#### 3.2.6 **新建项目**

首先，确保你的 Luatools 的版本大于或者等于 3.0.6 版本.

在 Luatools 的左上角上有版本显示的，如图所示：

![](static/KyWgb3Eh2oAvYjxXDPscOJ6wnRh.png)

Luatools 版本没问题的话， 就点击 Luatools 右上角的“项目管理测试”按钮，如下图所示：

![](static/K7MbbeETboBHGyxYWB5cIP5fnKb.png)

这时会弹出项目管理和烧录管理的对话框，如下图：

![](static/CmifbIMbHo8iDTxmZtbcvoCfnjh.png)

#### 3.2.7 **开始烧录**

- 选择 Air724ug 开发板对应的底层 core 和刚改的 main.lua 脚本文件。下载到板子中。

![](static/FjDxbMkH3obY1Dx93BYcL3j0nhd.png)

- 一直按下载模式按键，在按一下重启，然后点击下载底层和脚本，如图所示：

![](static/Z1YqbcSRQoPEi0x4wh6covKHnMg.png)

- 出现如图所示，表示已进入 boot 模式，可以松开下载模式按键，等待下载完成。

![](static/RbCebHXDGoLMFRxTJ4ZczQiznRe.png)

- 下载完成，如图所示

![](static/W7XVbbQP0oLOIUxv62mcSbBun3m.png)

## 四、音频应用-录音基本用法

### 4.1 本教程实现的功能定义：

- record 库在 EVB_Air724UG_A14-LuatOS 系统中提供了一种强大、灵活且易用的音频录制解决方案。此次说明旨在帮助开发者快速熟悉并掌握 record 库的 API 接口，以便进行高效的音频录制和管理操作。

### 4.2 文章内容引用

- EVB_Air724UG_A14 开发板软硬件资料 ： [EVB_Air724UG_A14 产品手册 ](https://docs.openluat.com/air724ug/product/)
- 以下接口函数不做详细介绍，可通过此链接查看具体介绍：[record_API](https://doc.openluat.com/wiki/21?wiki_page_id=2289)

### 4.3 API 接口详解

#### 4.3.1 `record.start(seconds, cbFnc, type, quality, rcdType, format, streamRptLen)`

参数讲解：

`seconds`：

录音时长，单位：秒

流录音模式下，如果想长时间录音，可以将此参数设置为 0x7FFFFFFF，相当于录音 2147483647 秒=24855 天。

`cbFnc`：

- **可选参数，默认为****nil** 录音回调函数：
  当 type 参数为"FILE"时，回调函数的调用形式为：
  cbFnc(result,size)
  result：录音结果，true 表示成功，false 或者 nil 表示失败
  size：number 类型，录音文件的大小，单位是字节，在 result 为 true 时才有意义
  当 type 参数为"STREAM"时，回调函数的调用形式为：
  cbFnc(result,size,tag)
  result：录音结果，true 表示成功，false 或者 nil 表示失败
  size：number 类型，每次上报的录音数据流的大小，单位是字节，在 result 为 true 时才有意义
  tag：string 类型，"STREAM"表示录音数据流通知，"END"表示录音结束

`type`：

- **可选参数，默认为****"FILE"** 录音模式
  "FILE"表示文件录音模式，录音数据自动保存在文件中，录音结束后，执行一次 cbFnc 函数
  "STREAM"表示流录音模式，录音数据保存在内存中，每隔一段时间执行一次 cbFnc 函数去读取录音数据流，录音结束后再执行一次 cbFnc 函数

`quality`：

- **可选参数，默认为****1** 录音质量，0：一般质量，1：中等质量，2：高质量，3：无损质量

`rcdType`：

- **可选参数，默认为****2** 录音类型，n:1:mic(从麦克风录制)，2:voice(录制语音通话，录制的流与上下行通道)，3:voice_dual(在 poc 模式下从麦克风录制)

`format`：

- **可选参数，默认为****3** 录音格式，1:pcm，2:wav，3:amrnb，4:speex
  pcm 格式：录音质量参数无效，采样率：8000，单声道，采样精度：16 bit，5 秒钟录音 80KB 左右
  wav 格式：录音质量参数无效，比特率：128kbps，5 秒钟录音 80KB 左右
  amrnb 格式：录音质量参数有效
  录音质量为 0 时：比特率：5.15kbps，5 秒钟录音 3KB 多
  录音质量为 1 时：比特率：6.70kbps，5 秒钟录音 4KB 多
  录音质量为 2 时：比特率：7.95kbps，5 秒钟录音 4KB 多
  录音质量为 3 时：比特率：12.2kbps，5 秒钟录音 7KB 多
  speex 格式：录音质量参数无效，pcm 格式 128kbps 后的压缩格式，5 秒钟 6KB 左右

`streamRptLen`：

- **可选参数，默认为****nil** 流录音时，每次上报的字节阀值

返回值：

- 无返回值。

举例：

```lua
--[[
函数名：rcdcb
功能  ：录音结束后的回调函数
参数  ：
        result：录音结果，true表示成功，false或者nil表示失败
        size：number类型，录音文件的大小，单位是字节，在result为true时才有意义
返回值：无
]]
function rcdcb(result,size)
    log.info("testRecord.rcdcb",result,size) 
end

--5秒后，开始录音
sys.timerStart(record.start,5000,5,rcdcb)
```

总结：

`record.start函数用于启动录音，支持多种参数配置。通过回调函数，用户可以处理录音过程中的各种事件。`

#### 4.3.2 `record.stop(cbFnc)`

参数讲解：

- `cbFnc`：
- **可选参数，默认为****nil** 停止录音的回调函数(停止结果通过此函数通知用户)，回调函数的调用形式为：
  cbFnc(result)
  result：number 类型
  0 表示停止成功
  1 表示之前已经发送了停止动作，请耐心等待停止结果的回调

返回值：

- 无返回值

举例：

```lua
local function stopCallback(errCode)  
    if errCode == 0 then  
        print("录音已停止")  
    else  
        print("停止录音失败，错误码：" .. errCode)  
    end  
end  
  
-- 停止当前正在进行的录音  
record.stop(stopCallback)
```

总结：

`record.stop` 函数用于停止录音，并通过回调函数通知用户停止的结果。

#### 4.3.3 `record.getFilePath()`

参数讲解：

- 无参数。

返回值：

- 返回一个字符串，表示最近一次录音生成的文件路径。

举例：

```lua
-- 获取最近一次录音的文件路径  
local filePath = record.getFilePath()  
print("录音文件路径：" .. filePath)
```

总结：

`record.getFilePath函数提供了一种便捷的方式来获取录音文件的路径。`

#### 4.3.4 `record.getData(offset, len)`

参数讲解：

- `offset`：从哪个字节开始读取数据。
- `len`：要读取的数据长度（字节）。

返回值：

- 从指定位置读取的录音数据。

举例：注：这里的例子和开始的录音例子相结合，此处只做单独解说（完整 demo,请看最后的完整实例）

```lua
--[[
函数名：readrcd
功能  ：读取录音文件内容
参数  ：无
返回值：无
]]
local function readrcd()    
    local s = record.getData(rcdoffset,RCD_READ_UNIT)
    log.info("testRecord.readrcd",rcdoffset,rcdcnt,string.len(s))
    rcdcnt = rcdcnt-1
    --录音文件内容已经全部读取出来
    if rcdcnt<=0 then
        sys.timerStop(readrcd)
        --播放录音内容
        audio.play(0,"FILE",record.getFilePath(),7,playcb)
    --还没有全部读取出来
    else
        rcdoffset = rcdoffset+RCD_READ_UNIT
    end
end
```

总结：

`record.getData函数用于从录音文件中读取数据`

#### 4.3.5 `record.getSize()`

参数讲解：

- 无参数。

返回值：

- 返回一个表，包含两个元素：文件大小（字节）和录音时长（秒）。

举例：

```lua
-- 获取录音文件的大小和时长
local fileSize, duration = record.getSize()  
print("录音文件大小：" .. fileSize .. " 字节，时长：" .. duration .. " 秒")
```

总结：

`record.getSize函数提供了一种便捷的方式来获取录音文件的大小和时长`

#### 4.3.6 `record.delete()`

参数讲解：

- 无参数。

返回值：

- 无返回值。

举例：

```lua
-- 删除最近一次录音的文件  
record.delete()  
print("录音文件已删除")
```

总结：

`record.delete` 函数用于删除最近一次录音生成的文件，从而释放存储空间。

#### 4.3.7 `record.exists()`

参数讲解：

- 无参数。

返回值：

- 返回一个布尔值，表示最近一次录音生成的文件是否存在。

举例：

```lua
-- 检查录音文件是否存在  
local fileExists = record.exists()  
if fileExists then  
    print("录音文件存在")  
else  
    print("录音文件不存在")  
end
```

总结：

`record.exists函数提供了一种检查录音文件是否存在的方法，这对于避免重复录音或处理不存在的文件非常有用。`

#### 4.3.8 `record.isBusy()`

参数讲解：

- 无参数。

返回值：

- 返回一个布尔值，表示录音模块是否正在处理录音操作

举例

```lua
-- 检查录音模块是否忙碌  
local isBusy = record.isBusy()  
if isBusy then  
    print("录音模块正在忙碌")  
else  
    print("录音模块空闲")  
end
```

总结：

`record.isBusy` 函数提供了一种检查录音模块状态的方法，这对于避免在录音过程中进行其他冲突操作非常有用。通过检查模块状态，用户可以确保在合适的时机启动或停止录音。

## 五、音频应用整体演示

### 5.1 音频应用-录音**成果演示与深度解析：视频 + 图文全面展示**

![](static/GRncb0issoXxs1x3Ooncdko7nkg.png)

#### 5.1.1 **成果运行精彩呈现**

#### 5.1.2 **完整实例深度剖析**

```lua
--- 模块功能：录音功能测试.
-- LuaTools需要PROJECT和VERSION这两个信息
PROJECT = "record_demo"
VERSION = "1.0.0"

require"record"
require"audio"
require"sys"

--每次读取的录音文件长度
local RCD_READ_UNIT = 1024
--rcdoffset：当前读取的录音文件内容起始位置
--rcdsize：录音文件总长度
--rcdcnt：当前需要读取多少次录音文件，才能全部读取
local rcdoffset,rcdsize,rcdcnt
--设置为spk播放，耳机mic输入
--audio.setChannel(2, 3)
--设置录音时mic增益为7级
--audio.setMicGain("record",7)
--[[
函数名：playcb
功能  ：播放录音结束后的回调函数
参数  ：无
返回值：无
]]
local function playcb(r)
    log.info("testRecord.playcb",r)
    --删除录音文件
    record.delete()
    record.start(5,rcdcb)
    sys.timerStart(record.stop,3000)
end

--[[
函数名：readrcd
功能  ：读取录音文件内容
参数  ：无
返回值：无
]]
local function readrcd()    
    local s = record.getData(rcdoffset,RCD_READ_UNIT)
    log.info("testRecord.readrcd",rcdoffset,rcdcnt,string.len(s))
    rcdcnt = rcdcnt-1
    --录音文件内容已经全部读取出来
    if rcdcnt<=0 then
        sys.timerStop(readrcd)
        --播放录音内容
        audio.play(0,"FILE",record.getFilePath(),7,playcb)
    --还没有全部读取出来
    else
        rcdoffset = rcdoffset+RCD_READ_UNIT
    end
end

--[[
函数名：rcdcb
功能  ：录音结束后的回调函数
参数  ：
        result：录音结果，true表示成功，false或者nil表示失败
        size：number类型，录音文件的大小，单位是字节，在result为true时才有意义
返回值：无
]]
function rcdcb(result,size)
    log.info("testRecord.rcdcb",result,size)
    if result then
        rcdoffset,rcdsize,rcdcnt = 0,size,(size-1)/RCD_READ_UNIT+1
        sys.timerLoopStart(readrcd,1000)
    end    
end

--5秒后，开始录音
sys.timerStart(record.start,5000,5,rcdcb)

-- 用户代码已结束---------------------------------------------
-- 结尾总是这一句
sys.run()
-- sys.run()之后后面不要加任何语句!!!!!
```

## 六、总结

record 库的音频录制 API 接口共同构成了音频录制的核心功能，使开发者能够高效地管理录音的启动、停止、参数配置、文件管理以及附加的音频处理功能。通过合理利用这些接口，开发者可以构建出具备出色录音体验的应用程序，满足用户在多种场景下的录音需求。同时，也需关注接口之间的协同配合，以确保录音功能的流畅性和可靠性

## 七、常见问题

- **为什么设置通道没用？**
  1、通道设置是否正确
  2、看 mic ,喇叭，耳机是否损坏，固件是否选对

## 八、扩展

如果想使用外接的 mic ，请接开发板的 MIC_P、MIC_N 的管脚上。注：函数接口配置请阅读 API 接口详解。

![](static/GlDhbe0dwoPs2HxY5j0cC1iGnKh.png)
