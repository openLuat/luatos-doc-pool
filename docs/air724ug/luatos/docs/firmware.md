# Air724UG LuatOS固件版本

## 最新版本SDK&Demo

### 1.3底层core下载地址

- [CORE_V4030](https://cdn.openluat-luatcommunity.openluat.com/attachment/20240925115323601_CORE_V4030.rar)

### Luat上层脚本包

- [上层软件LuaTask_V2.4.4（demo+lib）](https://cdn.openluat-luatcommunity.openluat.com/attachment/20230911174858333_script_LuaTask_V2.4.4.zip)

### 1.3底层core固件更新说明（最新V4030）

- **V4030底层固件更新说明**
  
  1：修复℃字符ut8转gb2312不正确
  
  2：新增外挂flash挂载u盘功能
  
  3：rtos.set_trace可修改波特率:
  
  4：保存图片接口增加裁剪图片功能

### 上层脚本更新说明（最新V2.4.4）

- **2.4.4上层脚本更新说明**

  发布时间：2023/8/18 18:01:30

  修改记录

  一：lib脚本修改

  lib脚本版本号：2.4.4

  新增

  （1）gpsHxxt.lua

  510U快速定位

  （2）gpsZkw.lua

  530Z快速定位                                         

  （3）aliyun.lua

  阿里云自定义rrpc主题

  （4）errdump.lua

  支持向https服务器发送错误日志

  （5）socket.lua：

  从lib简单统计数据流量的接口ssl校验时，是否上报域名的参数

  （6）socketESP8266.lua

  外接esp8266 socket框架

  （7）update.lua

  设置升级包下载进度通知回调

  （8）nvm.lua

  出现异常后、自恢复机制

  修复

  （1）update.lua：

  校验失败的情况下还重启的问题

  （2）socketCH395.lua :

  连接不存在的服务器会显示连接成功的问题使用异步收发时，无法发出数据的问题

  （3）audio.lua:

  无法播放wav格式的音频的问题

  （4）aliyun.lua :

  当同时启用阿里云OTA和其他方式OTA时，阿里云消息会打断正常升级的问题

  （5）http.lua:

  http重定向丢失端口信息的问题

  （6）websocket.lua:

  一帧数据过长时，无法接收到完整的数据的问题连接成功后没有立即执行连接成功的回调的

  二：demo脚本修改

  新增

  （1）gps:

  外接Air510U

  （2）mqtt全双工对讲

  （3）ui：

  SH1108单色屏驱动

  ST7735S屏幕驱动

  （4）peripheral

  CH395添加Server端演示

  串口外接esp8266 socket演示

  （5）camera

  gc032a摄像头驱动（配合版本号>=4020的底层使用）

  （6）nvm

  nvm.sett的演示

  （7）阿里云微消息队列MQTT

  修复

  （1）record

  缺少录音质量参数的问题

  （4）peripheral

  sht30，crc等于100的时候被忽略的问题

  （1）qspi

  修改对io.mount返回值的判断

  （4）

  autoGps  当Air820匹配到国科微芯片时，无法工作的问题

## 空间说明

```
Luat二次开发使用的Flash空间有两部分：脚本区和文件系统区

脚本区：
通过Luatools烧写的所有文件，都存放在此区域
非TTS版本为720KB，TTS版本为426KB；如果烧录时，超过此限制，Luatools会报错
不同版本的core可能会有差异，以版本每次的更新记录为准

文件系统区：
程序运行过程中实时创建的文件都会存放在此区域，例如下载的一些音源文件  
总空间为1.3MB 
不同版本的core可能会有差异，可通过rtos.get_fs_free_size()查询剩余的文件系统可用空间
下载的差分升级包也存放在文件系统区，为保证差分升级可以用，建议预留900KB给差分升级使用  
```

```
Luat二次开发可用的ram空间，通用底层固件和定制固件有所不同，详细说明如下：
通用底层固件，分为虚拟机空间和底层空间
虚拟机空间：可用的ram空间有1.36MB可通过collectgarbage("count")查询已经使用的内存空间（返回值单位为KB）,总的1.36MB减去使用的内存，就是当前剩余的Lua运行可用内存
底层可用空间：AT^HEAPINFO查询结果的第3个值

定制固件可用内存空间以定制系统说明为准，剩余可用空间为：AT^HEAPINFO查询结果的第3个值
```

## 底层固件功能列表

| 1.2基线                        | LCD  | 字库 | 图片 | 扫码   | 二维码生成 | 摄像头 | TTS    | WIFI Scan | 蓝牙   | SD卡   | littleVGL | VOLTE  | 脚本文件 | 文件系统空间 | RAM空间 |
| ------------------------------ | ---- | ---- | ---- | ------ | ---------- | ------ | ------ | --------- | ------ | ------ | --------- | ------ | -------- | ------------ | ------- |
| Luat_RDA8910                   | 支持 | 支持 | 支持 | 支持   | 支持       | 支持   | 不支持 | 支持      | 不支持 | 支持   | 支持      | 支持   | 720KB    | 1.3MB        | 1.36MB  |
| Luat_RDA8910_FLOAT             | 支持 | 支持 | 支持 | 支持   | 支持       | 支持   | 不支持 | 支持      | 不支持 | 支持   | 支持      | 支持   | 720KB    | 1.3MB        | 1.36MB  |
| Luat_RDA8910_TTS               | 支持 | 支持 | 支持 | 不支持 | 不支持     | 不支持 | 支持   | 支持      | 不支持 | 不支持 | 支持      | 支持   | 426KB    | 1.3MB        | 1.36MB  |
| Luat_RDA8910_TTS_FLOAT         | 支持 | 支持 | 支持 | 不支持 | 不支持     | 不支持 | 支持   | 支持      | 不支持 | 不支持 | 支持      | 支持   | 426KB    | 1.3MB        | 1.36MB  |
| Luat_RDA8910_TTS_NOLVGL        | 支持 | 支持 | 支持 | 不支持 | 不支持     | 不支持 | 支持   | 支持      | 不支持 | 不支持 | 不支持    | 支持   | 426KB    | 1.3MB        | 1.36MB  |
| Luat_RDA8910_TTS_NOVOLTE_FLOAT | 支持 | 支持 | 支持 | 不支持 | 不支持     | 不支持 | 支持   | 支持      | 不支持 | 不支持 | 支持      | 不支持 | 426KB    | 1.3MB        | 1.36MB  |
| Luat_RDA8910_TTS_NOLVGL_FLOAT  | 支持 | 支持 | 支持 | 不支持 | 不支持     | 不支持 | 支持   | 支持      | 不支持 | 不支持 | 不支持    | 支持   | 426KB    | 1.3MB        | 1.36MB  |
| Luat_RDA8910_BT_FLOAT          | 支持 | 支持 | 支持 | 支持   | 支持       | 支持   | 不支持 | 支持      | 支持   | 支持   | 支持      | 不支持 | 720KB    | 1.3MB        | 1.36MB  |

| 1.3基线                        | LCD  | 字库 | 图片 | 扫码   | 二维码生成 | 摄像头 | TTS    | WIFI Scan | 蓝牙   | SD卡 | littleVGL | VOLTE  | 脚本文件 | 文件系统空间 | RAM空间 |
| ------------------------------ | ---- | ---- | ---- | ------ | ---------- | ------ | ------ | --------- | ------ | ---- | --------- | ------ | -------- | ------------ | ------- |
| Luat_RDA8910                   | 支持 | 支持 | 支持 | 支持   | 支持       | 支持   | 不支持 | 支持      | 不支持 | 支持 | 支持      | 支持   | 704KB    | 1.3MB        | 1.36MB  |
| Luat_RDA8910_BT_FLOAT          | 支持 | 支持 | 支持 | 支持   | 支持       | 支持   | 不支持 | 支持      | 支持   | 支持 | 支持      | 不支持 | 704KB    | 1.3MB        | 1.36MB  |
| Luat_RDA8910_RBTTSQRLLSDFT     | 支持 | 支持 | 支持 | 支持   | 支持       | 支持   | 支持   | 支持      | 支持   | 支持 | 不支持    | 不支持 | 416KB    | 1.3MB        | 1.36MB  |
| Luat_RDA8910_NOVOLTE_FLOAT     | 支持 | 支持 | 支持 | 支持   | 支持       | 支持   | 不支持 | 支持      | 不支持 | 支持 | 支持      | 不支持 | 704KB    | 1.3MB        | 1.36MB  |
| Luat_RDA8910_TTS_NOLVGL_FLOAT  | 支持 | 支持 | 支持 | 不支持 | 不支持     | 不支持 | 支持   | 支持      | 不支持 | 支持 | 不支持    | 支持   | 416KB    | 1.3MB        | 1.36MB  |
| Luat_RDA8910_TTS_NOVOLTE_FLOAT | 支持 | 支持 | 支持 | 支持   | 支持       | 支持   | 支持   | 支持      | 不支持 | 支持 | 支持      | 不支持 | 704KB    | 1.3MB        | 1.36MB  |
| LuatOS-HMI_RDA8910             | 支持 | 支持 | 支持 | 不支持 | 支持       | 不支持 | 不支持 | 支持      | 不支持 | 支持 | 支持      | 不支持 | 1.06MB   | 1.87MB       | 1.36MB  |

**V1.2与V1.3固件的背景和联系：**

V1.3分支是基于V1.2分支厂商平台版本的一次大升级，V1.3在V1.2的基础上新增    蓝牙，超低功耗，SIM卡自动切换功能。V3XXX为V1.3的LUAT版本，V0XXX为V1.2的LUAT版本，如V3027是V1.3的固件，V0030是V1.2的固件。

**Q1: V1.2固件出货的模块能升级到V1.3的版本吗？**
A:   V1.3完全兼容V1.2，故V1.2的版本可以升级到V1.3的版本。（特别注意！！）只支持USB线刷，不能远程升级到V1.3。

**Q2: V1.3固件出货的模块能降级到V1.2的版本吗？**
A:   V1.2版本不支持V1.3版本的校准参数，故V1.3的版本不能降级到V1.2的版本,否则会开不了机。
首推1.3基线版本，支持相同基线版本之间空中升级，不支持跨基线版本间空中升级

## Luat固件在线编译说明

[Luat固件定制系统](https://doc.openluat.com/shareArticle/Vf34iUQh9em7c "Luat固件定制系统")
针对客户不同功能使用场景，提供免费在线定制固件服务。满足客户功能定制化需求，同时也能最大化保留Lua运行和存储空间
`注：  .pac后缀的是本地烧录固件； .bin后缀的是空中升级文件`

## 历史版本SDK&Demo

### 1.3底层core下载地址

- [CORE_V4029](https://cdn.openluat-luatcommunity.openluat.com/attachment/20240925115248809_CORE_V4029.rar)
- [CORE_V4028](https://cdn.openluat-luatcommunity.openluat.com/attachment/20240123153445684_CORE_V4028.rar)
- [CORE_V4027](https://cdn.openluat-luatcommunity.openluat.com/attachment/20240123152853483_CORE_V4027.rar)
- [CORE_V4026](https://cdn.openluat-luatcommunity.openluat.com/attachment/20231218154303212_CORE_V4026.rar)
- [CORE_V4025](https://cdn.openluat-luatcommunity.openluat.com/attachment/20230911173607889_CORE_4025.rar)
- [CORE_V4023](https://cdn.openluat-luatcommunity.openluat.com/attachment/20230720134926678_CORE_4023.rar)
- [CORE_V4022](https://cdn.openluat-luatcommunity.openluat.com/attachment/20230601114442637_CORE_V4022.rar)
- [CORE_V4021](https://cdn.openluat-luatcommunity.openluat.com/attachment/20230206170442898_CORE_V4021.rar)
- [CORE_V4020](https://cdn.openluat-luatcommunity.openluat.com/attachment/20230106110259573_CORE_V4020.rar)
- [CORE_V4018](https://cdn.openluat-luatcommunity.openluat.com/attachment/20221025113556425_CORE_V4018.rar)
- [CORE_V4017](https://cdn.openluat-luatcommunity.openluat.com/attachment/20220920105910726_CORE_V4017.rar)
- [CORE_V4013](https://cdn.openluat-luatcommunity.openluat.com/attachment/20220813150712187_CORE_V4013.rar)
- [CORE_V4003](https://cdn.openluat-luatcommunity.openluat.com/attachment/20220509135412413_LuatOS-Air_V4003_RDA8910.rar)
- [CORE_V4002](https://cdn.openluat-luatcommunity.openluat.com/attachment/20220412224322254_LuatOS-Air_V4002_RDA8910.rar)
- [CORE_V3211](https://cdn.openluat-luatcommunity.openluat.com/attachment/20220224105019684_CORE_V3211.rar)
- [CORE_V3209](https://cdn.openluat-luatcommunity.openluat.com/attachment/20220118195139532_CORE_V3209.rar)
- [CORE_V3205](https://cdn.openluat-luatcommunity.openluat.com/attachment/20211202121015424_CORE_V3205.rar)
- [CORE_V3105](https://cdn.openluat-luatcommunity.openluat.com/attachment/20210924175954802_LuatOS-Air_V3105.rar)
- [CORE_V3037](https://cdn.openluat-luatcommunity.openluat.com/attachment/20210702115356609_V3037.rar)
- [CORE_V3035](https://cdn.openluat-luatcommunity.openluat.com/attachment/20210609131505703_Luat_V3035_RDA8910.rar)
- [CORE_V3032](https://cdn.openluat-luatcommunity.openluat.com/attachment/20220623154957177_CORE_V3032.rar)
- [CORE_V3029](https://cdn.openluat-luatcommunity.openluat.com/attachment/20210326091852273_V3029.zip)
- [CORE_V3028](https://cdn.openluat-luatcommunity.openluat.com/attachment/20210316145120070_V3028.rar)
- [CORE_V3027](https://cdn.openluat-luatcommunity.openluat.com/attachment/20210422171412263_Luat_3027.rar)

### 1.2底层core下载地址

- [CORE_V0034](https://cdn.openluat-luatcommunity.openluat.com/attachment/20210906161937203_CORE_V0034.rar)

- [CORE_V0032](https://cdn.openluat-luatcommunity.openluat.com/attachment/20210624191326612_V0032.rar)
- [CORE_V0031](http://openluat-erp.oss-cn-hangzhou.aliyuncs.com/erp_site_file/product_file/CORE_V0031.zip)
- [CORE_V0030](http://openluat-erp.oss-cn-hangzhou.aliyuncs.com/erp_site_file/product_file/CORE_V0030.zip)
- [CORE_V0022](https://cdn.openluat-luatcommunity.openluat.com/attachment/20210223114918666_CORE_V0022.rar)
- [CORE_V0019](https://cdn.openluat-luatcommunity.openluat.com/attachment/20210113175605790_CORE_V0019.rar)

### Luat上层脚本包

- [上层软件LuaTask_V2.4.3（demo+lib）](https://cdn.openluat-luatcommunity.openluat.com/attachment/20220513211301955_script_LuaTask_V2.4.3.zip)
- [上层软件LuaTask_V2.4.2（demo+lib）](https://cdn.openluat-luatcommunity.openluat.com/attachment/20211211144532571_script_LuaTask_V2.4.2.zip)
- [上层软件LuaTask_V2.4.0（demo+lib)](https://cdn.openluat-luatcommunity.openluat.com/attachment/20210816193152252_script_LuaTask_V2.4.0.zip)
- [上层软件LuaTask_V2.3.9（demo+lib)](https://cdn.openluat-luatcommunity.openluat.com/attachment/20210622180131380_script_LuaTask_V2.3.9.zip)
- [上层软件LuaTask_V2.3.8（demo+lib)](https://cdn.openluat-luatcommunity.openluat.com/attachment/20210622150357405_script_LuaTask_V2.3.8.rar)
- [上层软件LuaTask_V2.3.7（demo+lib)](https://cdn.openluat-luatcommunity.openluat.com/attachment/20210127105045913_script_LuaTask_V2.3.7.zip)
- [上层软件LuaTask_V2.3.6（demo+lib）](https://cdn.openluat-luatcommunity.openluat.com/attachment/20201222164107696_script_LuaTask_V2.3.6.zip)
- [上层软件LuaTask_V2.3.5（demo+lib）](https://cdn.openluat-luatcommunity.openluat.com/attachment/20201030144159021_script_LuaTask_V2.3.5.zip)
- [上层软件LuaTask _V2.3.4  (demo+lib)](https://github.com/openLuat/Luat_4G_RDA_8910/tree/master/script_LuaTask)

---

### 1.3底层core固件更新说明（历史版本）

- **V4029底层固件更新说明**

  1：全双工对讲audiocore.pocstreamplay增加判断流录音播放结束的标志

  2：增加CRC7算法

- **V4028底层固件更新说明**
  
  1：解决经典蓝牙功能在IOS机型无效的问题
  
- **V4027底层固件更新说明**
  
  1：解决收到彩信后接收短信没有CMTI上报问题
  
- **V4026底层固件更新说明**
  
  1：可选编译支持ipv6功能:
  
  2：增加对795的自适应
  
  3：解决移动卡在特定情况下对6F7E写入问题:
  
  4：解决通过audiocore.streamplay播放音频数据，但监听不到语音流结束的问题
  
  5：更新sm2库相关联的文件
  
- **V4025底层固件更新说明**
  
  1：解决当频繁切换小区时产生的大量写卡动作
  
  2：解决bit.bnot接口返回值不对问题
  
  3：增加ds18b20rst指令延迟设置接口
  
  4：解决广电卡获取ip慢的问题
  
- **V4023底层固件更新说明**
  
  1：解决某些蓝牙设备当查询特征时句柄范围异常
  
  2：解决uart485 mode为1时无TX消息上报
  
- **V4022底层固件更新说明**
  
  1：解决蓝牙设置特征描述value后查不到的问题
  
  2：解决调用热插拔接口进出飞行模式异常；（必现）
  
  3：解决pio.pin.plus接口输出方波时无法切换io输出；（必现）
  
  4：解决lvgl触摸事件里加publish，外面subscribe的话响应会很慢
  
  5：audiocore.pocstart增加AMRWB格式；
  
  6：NDK增加信号量接口；
  
- **V4021底层固件更新说明**
  
  1：解决模块进出飞行模式无sim卡状态下，上报+CPIN: READY问题；（必现）
  
  2：解决alipay上报时间未加本地时区的问题；（必现）
  
  3：解决由于CCED获取异常，导致alipay死机问题；（必现）
  
- **V4020底层固件更新说明**
  
  1：默认关闭cp日志
  
  2：解除U盘功能授权
  
  3：解决流录音管道中还有内容时，audiocore.streamrecordread查询为0的问题
  
  4：增加gc032a摄像头驱动,(增加时钟配置键值mClk)
  
- **V4018底层固件更新说明**
  
  1：支持RSA_SHA1私钥签名，新增crypto.rsa_sha1_sign接口；
  
  2：解决TCP 长连接，会因为通话挂断而断开问题；(必现）
  
  3：解决用字库芯片，lvgl显示中文标点死机的问题；必现）
  
  4：解决远程升级过程中概率出现超时，导致升级失败的问题；(概率性）
  
  【问题原因】网络环境较好情况下，底层luatask优先级较低，接收数据不及时导致消息流转机制进入死锁状态。
  
- **V4017底层固件更新说明**
  
  1：解决蓝牙从机接收不到模块主机发的数据的问题，btcore.send增加参数设置发送方式(必现）
  【问题原因】主机发送方式与从机特征写属性不符，模块蓝牙支持的write属性是write without response，从机uuid支持的属性是write
  
  2：解决uart上报消息rtos.MSG_UART_RXDATA慢的问题，uart.setup接口增加priority参数修改task优先级(必现）
  
  3：解决阿里云OTA下载超时问题(概率性）
  
- **V4013底层固件更新说明**
  
  1：解决https下载大文件会超时的问题(概率性）
  
  2：解决pio.pin.pwm关闭后不能重新打开的问题（必现）
  
  3：解决flash硬件不通时，mount死机的问题（必现）
  
  4：解决电池供电时sd卡读写慢的问题（概率性）
  
  5：解决https链接失败的问题（必现）
  
  [问题原因]客户端没有上报服务器域名导致，主要和服务器有关
  
  6：支持目录重命名，新增rtos.rename_dir接口
  
  7：camera预览（disp.camerapreview()）在横屏时会花屏（必现）
  
  8：解决可选编译固件tts播放会存在POP音问题（必现）
  
  9：解决PPP拨号成功后ATO指令无法切换AT/数据模式（必现）
  
  10：解决socket链接中概率出现连接关闭的问题（概率性）
  
  [问题原因]模块socket回调函数进程异常，模块频繁断开和连接socket时，容易出现
  
  11：解决蓝牙设置value值后对端设备读的数据长度有误的问题，btcore.setvalue()添加第三个参数可配置长度（必现）
  
  12：解决spi的cs控制慢的问题（必现）
  
  13：解决SIM卡锁PIN状态下无法读取CCID问题(必现）
  
  14：解决读矢量字体数据时死机的问题（概率性）
  
  15：解决擎亚扫码，codabar和code93码,交叉25码死机的问题（必现）
  
  16：解决BAND34注册不上网络问题（概率性），解决方案和问题原因参考链接https://e3zt58hesn.feishu.cn/docx/doxcnjkoytBMHjMwVsjWShfEn9c
  
- **V4003底层固件更新说明**
  
  1：增加设置BLE蓝牙MTU的功能 ，添加接口btcore.setmtu(size)
  
  2：解决模块BLE主模式连接从模式时，打开通知失败的问题（必现）
  
  3：添加gif播放结束时发送事件和设置gif播放速度接口，分别是lvgl.EVENT_LEAVE和lvgl.gif_set_delay（g,delay）
  
  4：添加擎亚扫码正反色配置的功能，添加接口disp.scantype(value)
  
  5：解决BLE接收数据丢数据问题（必现）
  
  6：解决lvgl qrcode控件显示不正常的问题  (概率性)
  
  7：解决lvgl无法显示SD卡文件的问题（必现）
  
- **4002底层固件更新说明**
  
  1：NDK支持ADC快速读取；
  
  2：解决矢量字库无法使用默认图标的问题；(概率性）
  
  3：增加NDK的math库接口适配；
  
  4：解决图片控件右侧有彩边的问题；(概率性）
  
  5：合宙8910平台全系Cat.1 模块生产出货固件版本升级（升级至V4XXX），不允许版本回退的相关说明；     https://doc.openluat.com/share_article/zH73TFN62lEyw#
  
  6：更新擎亚扫码库，优化识别效果；
  
  7：解决lua版本中不支持绑定本地端口的问题，增加mt:connect接口可选参数local_port 进行本地端口配置；(必现）
  
  8：解决模块蓝牙主模式下，读特征value数据异常的问题；（必现）
  
  9：增加经典蓝牙获取音乐播放状态的接口btcore.getavrcpstate();
  
  10：解决i2c通讯时首字节为双字节不生效问题；（必现）
  
  11：解决lvgl设置png格式的图片时不能正确的显示透明度的问题；（概率性）
  
  12：解决lvgl bin格式图片旋转时显示不正常的问题；（概率性）
  
  13：增加支持oppo sans字体；
  
  14：解决gif和label滚动导致的软狗喂狗超时问题；（概率性）
  
  15：解决设置缩放后，jpg图片无法显示的问题；(概率性）
  
  16：HMI固件增加矢量字库功能；
  
  17：增加擎亚扫码库种类，大于等于V3212之后，擎亚的码种有三种选择：
  
  1）QR+CODE128；
  
  2）QR+CODE128+UPC（包含EAN）；
  
  3）QR+Code128+Code39+EAN13+交叉25码+UPC码+93码+ISBN码+Codabar；
  
- **3211底层固件更新说明**
  
  1：解决擎亚扫码失败时内存泄漏的问题（必现）
  
  2：解决LDO无法配置FLASH_IB引脚（722UG模块 Pin60）的问题，(pmd.LDO_FLASHIB  取值0-15)（必现）
  
  3：解决lvgl.dropdown_get_selected_str不能用的问题（概率性）
  
  4：解决截屏接口disp.screenshots 在LVGL+SPI屏时只能截到空白图片的问题（概率性）
  
  5：解决在disp中使用矢量字库时颜色大小与设置的不一样的问题（概率性）
  
  6：解决lvgl.msgbox_add_btns不能用的问题（必现）
  
  7：解决LVGL横屏设置功能在SPI屏上会死机的问题（概率性）
  
  8：增加LVGL支持播放gif的功能，https://doc.openluat.com/wiki/21?wiki_page_id=2988
  
  9：解决lvgl.gauge_set_needle_count、lvgl.gauge_set_formatter_cb、lvgl.tileview_set_valid_positions、lvgl.calendar_set_highlighted_dates、lvgl.keyboard_set_map、lvgl.keyboard_set_ctrl_map接口不能用的问题
  
  10：解決uart数据写到sd卡，挂测几小时后，lua收不到uart消息的问题（必现）
  
- **3209底层固件更新说明**
  
  1：解决可选编译版本（比如：V3205_RDA8910_RFTLLMPSDZZ），使用MIPI lcd会导致掉卡，无法上网的问题（必现）
  
  【问题原因】可选编译版本打开了平台的sim卡热插拔功能，使用管脚GPIO4与MIPI管脚冲突，使用MIPI会触发热插拔，导致掉卡
  
  2：添加audiocore.pa使能可选参数（audiocore.pa(gpio,devout[,plus_count][,plus_period][,enable][,plus_delay])接口中[,enable]参数）
  
  3：解决SD卡播放音频时计算MD5错误的问题 （概率性）
  
  4：解决lvgl不能在lua协程中调用的问题（必现）
  
  5：解决模块BLE主模式连接蓝牙芯片nordic52832从模式时，打开通知失败的问题（必现）
  
  6：解决lvgl使用大图（比如：图片11KB）时连续内存不足导致死机的问题（概率性）
  
  7：解决lvgl控件创建接口参数值为nil时不能省略的问题（概率性）
  
  8：解决模块BLE蓝牙主模式设置扫描过滤策略为1无效的问题（必现）
  
  9：解决在lvgl中使用样式（style）会死机重启的问题（概率性）
  
  10：解决lvgl中calendar_set_day_names和calendar_set_month_names第二个参数的最后结尾若不是空字符串就无法删除的问题（必现）
  
  11：增加定制固件的矢量字体功能，http://ask.openluat.com/wiki/21?wiki_page_id=2752
  
  12：解决rtmp播放结束后，超时回调上报慢的问题，audiocore.rtmpopen接口第二个参数可设置超时时间（必现）
  
  13：解决RTMP拉流播放音频时卡顿的问题，audiocore.rtmpopen接口第三个参数可设置修改RTMP缓冲区时间（必现）
  
  【问题原因】服务器发送数据过快导致出现零窗口
  
  14：增加获取外挂FLASH空间大小功能，io.unmount接口，http://ask.openluat.com/wiki/21?wiki_page_id=2248
  
  15：增加获取全屏RGB数据接口disp.get_screenrgb（pathname，x1,x2,y1,y2)
  
  16：解决模块作为蓝牙主设备或者从设备时，BLE连接后无法获取对端设备蓝牙MAC地址的问题（概率性）
  
  17：增加NDK功能，支持可选编译，http://ask.openluat.com/wiki/21?wiki_page_id=2768
  
  18：解决概率性文件系统被破坏的问题（概率性）
  【备注】后续音频参数保存与之前固件版本有点不同，需要多重启一次。
  
  19：增加sock_ssl单项认证证书校验失败是否坚持访问参数，sockcore.sock_conn接口，可选参数insist，默认连接，（必现）
  
  20：添加查询ims注册状态的指令AT+CIREG，支持查询sim卡是否开通VOLTE。
  
  21：解决SPI LCD接口，屏幕不亮的问题（特殊硬件环境下必现）
  【问题原因】spi lcd数据只刷新了更新内容，未进行全屏更新
  
  22：解决使用矢量字体后刷屏慢的问题 （概率性）
  
  23：解决lvgl.bar_get_start_value接口获取不到Bar控件起始值的问题（必现）
  
- **3205底层固件更新说明**
  
  1：解决lvgl.table_get_pressed_cell获取不到点击的单元格的问题（必现）
  
  2：解决mipi重复授权导致屏幕不亮的问题（必现）
  
  3：解决windows重启后概率性识别不到模块usb的问题 ，(通过设置AT+SYSNV=1,"usbreboot",1，在usb进入到suspend状态时重新配置usb，规避问题)
  
  4：解决苹果手机部分应用搜索到的蓝牙信号名称错误的问题（概率性复现）
  
  5：解决使用rndis时 tcp链接数量有限制问题（必现）
  
  【问题原因】nat映射表最大为1024
  
  6：解决3105和3201固件版本通话中设置MIC增益失败的问题（必现）
  
  7：解决星舆rtk报错9003，9002之后无法恢复的问题（必现）
  
  【问题原因】报错后状态异常，无nema数据
  
  8：添加lvgl横竖屏转换功能（lvgl.disp_set_rotation(nil, lvgl.DISP_ROT_angle)接口，http://ask.openluat.com/wiki/21?wiki_page_id=2578）
  
  9：添加获取模块硬件版本号的接口rtos.get_hardware()
  
  10：解决U盘在拷贝大文件时，概率性出现软狗重启的问题（概率性复现）
  
  11：解决wav流录音断开和卡顿问题，（必现）
  
  【问题原因】：接收队列太小，消息发送太频繁，优化队列
  
  12：解决经典蓝牙播放音乐暂停后无法快速播放TTS的问题（蓝牙播放音乐暂停后，间隔1S，播放TTS，必现）
  
  13：添加lvgl二维码显示控件的功能，http://ask.openluat.com/wiki/21?wiki_page_id=2723
  
  14：添加擎亚扫码功能（http://ask.openluat.com/wiki/21?wiki_page_id=2670）
  
  15：解决lvgl设置横屏时屏幕底部区域无法刷新的问题（必现）
  
  16：解决主模式打开通知失败的问题（必现）
  
  【问题现象】
  
  1）：从机服务为128位uuid，特征为16位uuid，模块蓝牙主机打开通知失败
  
  2）：从机服务为16位uuid，特征为128位uuid，模块蓝牙主机打开通知失败
  
  17：增加支持镜像扫码设置，disp.scanmode(mode)接口
  
  18：解决蓝牙发现服务包含的特征既有16位uuid又有128位uuid时，主模式无法正常使用的问题（必现）
  
  19：新增”LuatOS-HMI_V3XXX_RDA8910”类型正式版本
  
  20：添加i2c支持16位寄存器配置功能
  
  21：解决 蓝牙打开后，间隔5秒，循环开启关闭蓝牙扫描，出现无扫描结果上报的问题（概率性）
  
  22：解决不插卡情况下，星舆rtk demo测试死机问题（必现）
  
  23：解决rtk接口导致的栈溢出死机的问题（概率性）
  
  24：解决pack.unpack往lua栈里push的值太多，导致内存覆盖的问题（概率性）
  
  25：解决lvgl界面一直无法刷新的问题（必现）
  
  【问题原因】:在没有按键或触摸输入和界面没用到动画的情况下，prvLvTaskHandler更新一次后就只返回0xffffffff，导致没法刷新屏幕
  
  26：解决lvgl不支持按键控制UI的问题（概率性）
  
- **3105底层固件更新说明**
  
  1：外接电源时, i2c接口 自定义波特率失效
  
  【问题原因】:睡眠唤醒时没有重定向clock设置函数
  
  2：解决SIM卡热插拔无+cpin:sim removed上报的问题
  
  【问题原因】:拔卡后缺少上报
  
  3：添加MIPI LCD功能,支持最大分辨率 480X854（目前只有722系列模块支持）
  
  4：支持luaIDE单步调试,  IDE教程链接： https://doc.openluat.com/article/32035：解决未加密脚本空中升级为luae脚本变砖问题（不支持这种升级方式，实际升级不会成功）
  
  6：支持SM3算法（sm3Obj:sm3update()和sm3Obj:sm3finish()接口）
  
  7：支持AT+CDNSCFG指令 设置DNS服务器
  
  8：支持 LVGL7.11
  
  说明1：V30XX版本的LVGL是V6.1版本,V31XX版本之后的LVGL是V7.11版本,2个LVGL版本底层接口不兼容，因此，如果V30XX版本（用了LVGL  V6.1）需要空中升级到V31XX版本(用了LVGL  V7.11)时，V31XX版本 中 上层脚本LVGL部分需要重写，参考https://doc.openluat.com/article/3285  ，生成差分包时，必须包含core和脚本
  
  说明2：如果V30XX版本未用到LVGL功能，可参考教程：https://doc.openluat.com/wiki/21?wiki_page_id=2314,空中升级到V31XX版本
  
  9：提供定时检测脉冲的接口 pio.pin.getval(pin1,pin2,…,pinn)
  
  10：socketcore.sock_conn接口添加可选参数bufferLen配置socket接收buffer的大小(可解决部分中转服务器没有滑窗问题)
  
  11：添加蓝牙BLE特征value的设置接口btcore.setvalue()和读取接口btcore.readvalue()
  
  12：修改蓝牙打开主模式后可以开启广播的问题，默认蓝牙打开主模式后，无法开启广播
  
  13：修改模块RNDIS 断网恢复后概率性PING不通的问题
  
  14：修改485转向延迟导致485帧错误问题
  
  【问题原因】：uart tx优先级太低，被lua task抢占导致485转向延迟
  
  15：[关于V30XX_RDA8910_RBTTSQRLLSDFT 更名为 V31XX_RDA8910_BT_TTS_FLOA说明](https://doc.openluat.com/article/3484 "关于V30XX_RDA8910_RBTTSQRLLSDFT 更名为 V31XX_RDA8910_BT_TTS_FLOA")
  
  16：添加AT*SECUREBOOT指令使能secure boot，功能说明链接：https://doc.openluat.com/wiki/21?wiki_page_id=2538
  
  17：解决长时间播tts（比如：10秒一次，循环播放）会出现再也无法播放的问题
  
  18：新增获取png图片像素内容接口disp.img.convert(org_file,org_format,dest_file,dest_format)
  
  19：解决关闭串口时，串口如果收到数据概率性死机问题
  
  20：修改misc.getVbatt() 必须先设置pmd.init({}) ，获取电压才会变的问题
  
  21：解决使用pbc库（protobuffer2）长时间编解码会死机的问题
  
  22：解决扫码开启时，按键消息的回调函数未触发，扫码结束时，前面的按键回调函数打印的数据会全部吐出来的问题
  
  23：解决低概率性出现打开蓝牙失败的问题
  
  【问题原因】:蓝牙任务优先级低导致被其他任务占用
  
  24：解决lvgl一些接口（比如：lvgl.chart_set_points，lvgl.calendar_set_month_names）无法使用数组数据的问题
  
  25：添加硬件pwm支持周期可设置的功能（pwm.set(id,param1,param2,clk_div)接口中，clk_div参数，https://doc.openluat.com/wiki/21?wiki_page_id=2251）
  
  26：添加变量监视的功能(配合LUA IDE使用）
  
  27：解决下载带有异常脚本，LUA IDE无法下载问题
  
- **3037底层固件更新说明**
  
  1：解除i2c接口波特率限制，i2c_setup接口加入可选参数isbaud实现自定义波特率原因：原先代码里规定i2c速率只有慢速（100k）和快速（400k）
  
  2：增加gpio 模拟io实现多路pwm功能 ，频率范围是1hz-1khz，接口：pio.pin.pwm
  
  3：BLE蓝牙添加白名单功能
  
  4：修改“关闭蓝牙没有消息上报”的问题，添加btcore.MSG_CLOSE_CNF消息上报
  
  5:   添加lua硬流控功能
  
  6：解决btcore.getAddr()获取蓝牙MAC地址接口需要先打开蓝牙的问题（原来从V3027到V3035都存在）
  
  问题现象：没打开蓝牙的情况下，使用btcore.getAddr()获取设置过mac地址的模块蓝牙mac地址，获取到的地址是随机的，但AT指令查询是固定的
  
  7:  新增语音播放的暂停播放接口audiocore.pause()和恢复播放接口audiocore.resume()
  
  8：解决模块作为经典蓝牙与手机连接，播放音乐时，手机端调节音量模块死机的问题
  
  原因：调音量的时候会阻塞音频数据导致死机
  
- **3035底层固件更新说明**
  
  1：去除默认的低电压关机功能，改为开机后可配置，新增AT+CBC?指令， AT+CBC=powerOnVol,powerOffVol 查询和设置开机和关机电压检测
  
  详情参考：https://doc.openluat.com/wiki/21?wiki_page_id=1947   常见问题 3
  
  2：修改crypto.aes_encrypt接口使用NONE填充死机的问题
  
  3：修改数传过程中，较低概率出现memcpy长度不对，访问到了非法地址导致远程升级死机重启问题
  
  4：修改crypto.aes_decrypt解密非加密字符的时候，可能导致设备重启问题
  
  【问题原因】:密文长度不是16的整数倍
  
  5：解决Luatools2.1.14 版本 下载3032，3033版本概率性下载失败问题
  
  【问题原因】:部分文件损坏，删除不了
  
  6：修改DES CBC加密解密16个以上字节出现乱码的问题
  
  7：解决模块循环连接服务器，服务器一直踢掉模块几十秒就会死机的问题
  
  【问题原因】:脚本会循环连接一个服务器，服务器会不断地踢掉模块。然后就会在短时间内创建大量定时器，触发定时器最大50个的阈值导致死机
  
  8：修改域名解析慢和解析失败的问题
  
  【问题原因】:原始UDP包的checksum为0，但是还去校验
  
  9：修改定制版本升级完成后部分版本（比如：Luat_V3032_RDA8910_RBL）重启死机的问题【问题原因】:malloc空间太大导致死机
  
  10：解决蓝牙扫描到的RSSI不稳定的问题
  
- **3032底层固件更新说明**
  
  1:流播放接口audiocore.streamplay添加对端播放的功能
  
  2:解决rtmp服务器主动断开，应用层无消息上报问题:
  
  3:解决当前摄像头拍照时处理不了其他消息问题
  
  4:解决SIM1 无法休眠的问题
  
  5:解决wifi扫描有的时候扫出信号为正数的热点信息问题
  
  6:解决lvgl不支持透明背景问题
  
  7:解决看门狗喂狗优先级低导致重启问题
  
  8:添加经典蓝牙从机功能(音频、电话)
  
- **3029底层固件更新说明**
  
  1:修正“sim.getIccid()接口概率性获取不到iccid”的问题
  
  2:蓝牙添加广播和扫描参数设置接口（btcore.setadvparam和btcore.setscanparam）
  
  3:修改pmd.LDO_VBACKLIGHT_X 调用两遍才生效的问题
  
  6:添加支持int64类型数据的进制转换接口rtos.hextodec
  
  7:修改disp.close后再disp.init会死机的问题
  
  8:删除bootload对GPIO_5的控制，解决GPIO5控制背光时开机白屏问题
  
  9:解决SPEEX流播放时，调节音量会死重启的问题
  
  10:gpio中断，无法检测50us的方波波形，丢部分中断
  
- **3028底层固件更新说明**
  
  1.同时配置所有的gpio为上拉中断，部分gpio无法使用问题
  
  2.第一个GPIO配置是上下拉必现死机
  
  3.修改audiocore.pa功能无法使用问题
  
- **3027底层固件更新说明**
  
  1.增加蓝牙功能
  
  2.增加超低功耗功能
  
  3.SIM卡自动切换
  
  4.LUA: 增加部分固件的大ram 和大文件系统

### 1.2底层core固件更新说明（历史版本）

- **0034底层固件更新说明**

  1：解决特殊国外卡开机后一段时间死机的问题

  【问题原因】:在中断服务程序中调用了rpc的接口

  2：解决DNS查询多次失败的问题

  【问题原因】:原始UDP包的checksum为0，但是还去校验

  3：解决查询空电话本死机的问题

  【问题原因】:log打印访问空指针

  4：解决空中升级大脚本失败问题

  【问题原因】:MD5校验脚本一次性申请空间太多

  5：解决模块循环连接服务器，服务器一直踢掉模块情况下，几十秒就会死机的问题

  【问题原因】:脚本循环连接一个服务器，服务器会不断地踢掉模块，会在短时间内创建大量定时器，触发定时器最大50个的阈值，导致死机

- **0032底层固件更新说明**
  
  1：修改播放音乐时切换音频通道会出现耳机和喇叭同时放音的问题
  
  2：优化部分城市类似“电子围栏的小区，公安系统布的网络”引起的掉线问题（普通的sim卡无法使用）
  
  3：优化网络延时问题，例如：云喇叭播报延迟
  出现概率：概率性的，和网络配置相关
  
  4：解决socket 发送数据失败后，重连https一直失败，模块重启后正常的问题，和网络环境相关，出现概率较低
  
- **0031底层固件更新说明**
  
  1:添加支持int64类型数据的进制转换接口rtos.hextodec
  
  2:gpio中断，无法检测50us的方波波形，丢部分中断
  
  3:同时配置所有的gpio为上拉中断，部分gpio无法使用问题
  
  4:第一个GPIO配置是上下拉必现死机
  
- **0030底层固件更新说明**
  
  1:linux上usb识别完后加载rndis驱动会上不了网
  
  2:解决挂测过程中ssl死机问题
  
  3:vbat电压发生变化时，rtos.MSG_PMD消息不会上报
  
  4:支持DES3加密，解密接口
  
  5:spi dma模式挂测外部flash，概率读写失败导致lua卡主问题
  
  6:Luat_0022版本做socket压力测试发现 socketcore.sock_send() 会断开网络
  
  7:adc open增加scale可选参数，用来增加ADC的精度
  
  8:启动防抖定时器时，close gpio会导致死机
  
  9:mount/umount SD卡，3次后必现死机
  
  10:485存在内存泄漏
  
  11:修改I2C1和I2C3不能用的问题 2. cid值1,2,3对应硬件i2c1,2,3
  
  12:sd卡 fat32 format失败
  
  13:rsa算法内存泄漏问题
  
  14:在Luat版本上开发“设置mic输入通道”的接口
  
  15:解决SSL接收数据过程中突然关闭造成死机的问题
  
  16:增加远程升级lua脚本的校验功能，防止下载错误的脚本导致模块无法开机
  
  17:修改插卡开机同时使用SD卡和SPI概率性死机问题
  
  18:修改keypad按键，多个按键同时抬起，丢中断问题
  
  19:uart.set_rs485_oe添加可选参数,用来配置485转向延迟时间
  
  20:GPIO配置输入中断后， 设置上下拉会触发中断
  
  21:解决电池检测电压不准的问题
  
  22:使用电信卡连接失败问题，改为IPV4优先
  
  23:充电开机，会上报开机按键消息
  
  24:解决调用io.opendir()打开目标文件夹，无论是否存在都会返回true的问题
  
  25:同时配置所有的gpio为上拉中断，部分gpio无法使用问题
  
- **0022底层固件更新说明**
  
  1:添加rtos.setTransData
  
  2:添加Socket Options参数设置接口sock_setopt,lua通过设置opt实现保活功能
  
  3:添加AT+TCPUSERPARAM
  
  4:新增lua otp接口
  
  5:支持关机充电功能 ，lua项目打开充电开机功能
  
  6:添加des_encrypt和des_decrypt接口
  
  7:添加AT*USB=HOTPLUG,0/1
  
- **0019底层固件更新说明**
  
  1:升级到19
  
  2:支持应用层更新audio校准参数
  
  3:开发通用工厂测试
  
  4:同时建大于3路ssl tcp时会死机
  
  5:升级到W20.30.1
  
  6:多中断设置后触发中断会导致死机
  
  7:vbus插入消息上报
  
  8:耳机通道等级3的音量不正常
  
  9:8910平台LUA版本增加读取客户版本号的AT指令，兼容之前1802平台的“AT+LUAINFO?”
  
  10:NAT PPP拨号之后无法PING外网
  
  11:添加GPIO 测试AT 命令
  
  12:阿里云OTA升级失败
  
  13:重启开机原因值不对的问题
  
  14:解决speex流播放出现的死机问题
  
  15:修改注网太快，lua task还没跑起来的时候就已经注册上网，会有很多主动上报丢掉的问题
  
  16:ui字库错位，显示出来的文字不正确
  
  17:ui分辨率设置为320会重启
  
  18:添加camera 预览放缩和反转接口
  
  19:使用充电头供电，1s刷新界面，一段时间后不刷新了
  
  20:mqtt 挂测死机
  
  21:1. 添加VGA拍照功能，不支持VGA扫码
  
  22:无法dhcp 获取IP 问题
  
  23:添加disp.camerawritereg，设置camera sensor的寄存器
  
  24:模块下载断电变砖
  
  25:camera 户外拍照很白的问题
  
  26:添加nv项，控制usbrst中的延时时间，AT*USB=RSTDELAY,xxx
  
  27:有些主控开机太慢导致识别不到模块的usb
  
  28:V0018 wifi扫描得到的ap mac地址有的丢了0
  
  29:fota升级后,升级文件没有清除，导致文件系统空间变少
  
  30:修改反复open / close uart会内存泄漏的问题
  
  31:修改注网太快，lua task还没跑起来的时候就已经注册上网，会有很多主动上报丢掉的问题

---

### 上层脚本更新说明（历史版本）

- **2.4.3上层脚本更新说明**
  
  发布时间：2022/2/17 13:17:00
  
  修改记录：
  
  一：lib脚本修改
  
  lib脚本版本号：2.4.3
  
  （1）新增Air551G配套lib，gps7201.lua，agps9701.lua
  
  （2）ftp.lua：完善异常处理，避免出现socket异常后没有终止，引起多次close的问题
  
  （3）audio.lua：修复setVolume返回值与文档不符的问题
  
  （4）http.lua：修复http连接时超时时间过长的问题
  
  （5）新增socketCh395.lua，spi转以太网
  
  （6）link.lua、socket.lua：现可选择使用4G、SPI转以太网CH395
  
  （7）socket4G：新增、单向认证证书中的域名校验不过时，是否继续访问的参数
  
  （8）sys.lua：版本号修改为2.4.3
  
  二：demo脚本修改
  
  （1）bluetooth：
  
  slave、master：新增蓝牙连接时，获取对方mac地址的演示
  
  beacon:  新增，直接使用广播包接口设置beacon广播
  
  （2）ftp：完善异常处理，避免出现网络异常时，引起多次close的问题
  
  （3）autoGps：解决国科版本gps自适应不匹配的问题
  
  （4）i2c：移至peripheral目录下
  
  （5）lvgl：移至金牛座开发板示例下
  
  （6）peripheral：
  
  新增：
  
  数码管驱动：TM1650
  
  光敏电阻：GM5528
  
  高精度时钟模块：PCF8563T
  
  电子罗盘：HMC5883L
  
  SPI转以太网：CH395
  
  SPI转CAN：SIT2515
  
  ADC数模转换：HX711、ADS1115
  
  MODBUS从机
  
  修改：
  
  ws2801：修复不能用的问题
  
  （7）sms：开机后延时发送短信，解决开机后立即发送短信有可能发送失败的问题
  
  （8）ui：新增MIPI屏幕驱动：HX8379C、ST7701S
  
  （9）gps：新增Air551Gdemo
  
- **2.4.2上层脚本更新说明**
  
  发布时间：2021/12/11 14:38
  
  修改记录：
  
  一：lib脚本修改
  
  lib脚本版本号：2.4.2
  
  (1)sys.lua：修复subscribe消息增删时会引起异常的问题；
  
  例如，在一个task内先用sys.subscribe()订阅一条消息，再sys.waitUntil()一条同样的消息，再
  
  subscribe一条同样的消息，当消息publish过来时，软件会报错
  
  (2)misc.lua：增加获取模块温度的接口——misc.getTemperature()
  
  (3)net.lua：修复网络注册正常状态下，如果主动ril.request("AT+CPIN?"),会导致net.getState()查询网络状态出错的问题
  
  (4)patch.lua、misc.lua:修复未执行pmd.init接口时，调用misc.getVbatt()获取到的电压不会变化的问题
  
  (5)update.lua：新增"当用户使用自定义服务器时，在update.request()内添加的自定义url前增加三个井号"###",脚本内则不会将模块信息与url进行拼接"；默认会将模块信息与url进行拼接
  
  (6)socket.lua：修复UDP连接，一包数据超过1472字节后，数据实际发送失败的问题；
  
  (7)mqtt.lua：修复当packet为空时，mqtt任务终止的问题
  
  (8)websocket.lua：修复：传入的url变为小写的问题，当接收数据长度超过126时解析异常的问题，新增：主动退出一个websocket任务的接口
  
  (9)errDump.lua：新增：当使用合宙调试服务器时，添加上传日志的开关
  
  (10)update.lua：新增：请求升级时，获取服务器返回信息的接口
  
  二：demo脚本修改
  
  (1)bluetooth：新增打开关闭扫描是否成功的消息上报
  
  (2)CPU温度：新增获取模块芯片温度的demo
  
  (3)gps：autoGPS.lua 增加：重启后发送一次指令校验
  
  autoGPS.lua 修改在发生异常后重新激活autotask后重复init()的问题
  
  (4)i2c：修改AHT10demo，将SHT30.lua移至外设传感器目录，新增HDC1000 DEMO
  
  (5)protoBuffer3：新增protoBuffer3 demo
  
  (6)msc：新增u盘测试demo
  
  (7)peripheral：新增支持的外设演示dmeo
  
  DAC数模转换：MCP4725
  
  GPIO扩展模块：MCP23008、MCP23017
  
  触摸屏：GT911
  
  高精度时钟模块：DS3231
  
  光照传感器：BH1750、TCS34725、TSL2561、CJMCU3001
  
  气压传感器：BME280、BME680、BMP180、BMP280
  
  数码管驱动：lcd_1621、TM1637、TM1638、ws2801
  
  温湿度传感器：AHT10、AM2320、DS18B20、HDC1000、HDC1080、HDC2080、LM75B、LM92、SHT20、SHT30、SI7021
  
  重力加速度计：ADXL345、ADXL346、BMA250、DA213B、GY271、KXTJ2-1009、KXTJ3-1057、L3G4200D、MC3416、MPU6XXX、SC7A20、LIS2DH12TR
  
  二氧化碳传感器：CCS811
  
  SPI转CAN：mcp2515
  
  (8)ui：新增st75256屏幕驱动
  
  (9)zlib：新增zlib压缩/解压缩示例
  
  (10)lvgl：新增lvgl7的demo
  
  (11)rtk：新增rtkdemo
  
- **2.4.0上层脚本更新说明**
  
  发布时间：2021/08/02 10:08
  
  修改记录：
  
  一、lib脚本修改
  
  lib脚本版本号：2.4.0
  
  (1)lbsLoc.lua：定位成功时的回调函数cbFnc(result,lat,lng,addr,time,locType)增加一个回调参数locType，表示定位类型，0表示基站定位，255表示WIFI定位
  
  (2)lbsLoc.lua：修正“request接口timeout参数功能不生效”的问题
  
  (3)gps.lua、gpsZkw、gpsHxxt：扩展3款gps芯片功能，支持demo中自适应3款gps芯片功能
  
  (4)misc.lua：新增getModelType()接口，支持获取模块型号
  
  (5)patch.lua：修正“因系统进入休眠状态，导致sd卡挂载概率失败”的问题
  
  (6)cc.lua：支持"通话断开原因值"的功能
  
  二、demo脚本修改
  
  (1)pwm呼吸灯：新增pwm呼吸灯demo
  
  (2)bluetooth：新增“蓝牙关闭消息上报”功能演示
  
  (3)bluetooth：修正“蓝牙数据接收时，因为代码逻辑问题导致的数据接收延迟”的问题
  
  (4)bluetooth：新增“特征值的设置与读取”功能演示【底层固件LuatOS-Air_V3102以及之后的版本才支持此功能】
  
  (5)ui：新增GC9306、ST7789驱动
  
  (6)cc：新增“通话中向对方播放音频”功能演示
  
  (7)cc：新增“基站/WIFI定位成功类型”功能演示
  
  (8)lbsLoc：新增“基站/WIFI定位成功类型”功能演示
  
  (9)gpio：新增“脉冲计数检测”功能演示【底层固件LuatOS-Air_V3102以及之后的版本才支持此功能】
  
  (10)crypt：新增“SM3算法”功能演示【底层固件LuatOS-Air_V3102以及之后的版本才支持此功能】
  
- **2.3.9上层脚本更新说明**
  
  发布时间：2021/05/17 13:27
  
  修改记录：
  
  一、lib脚本修改
  
  lib脚本版本号：2.3.9
  
  (1)websocket.lua：新增websocket功能
  
  二、demo脚本修改
  
  (1)camera：新增gc0130驱动ic拍摄640*480照片的演示功能
  
  (2)websocket：新增websocket演示功能
  
- **2.3.8上层脚本更新说明**
  
  发布时间：2021/04/07 15:41
  
  修改记录：
  
  一、lib脚本修改
  
  lib脚本版本号：2.3.8
  
  (1)socket.lua：新增socket.setLowPower接口，可以设置网络数据传输后，允许进入休眠的延时（配合core V3XXX版本使用才生效）
  
  (2)patch.lua：重定义disp.sleep，在sleep前不允许系统休眠，sleep后，允许系统休眠，修正“系统休眠状态下，disp.sleep功能失效”的问题
  
  (3)ftp.lua：规范ftp api命令格式
  
  二、demo脚本修改
  
  (1)i2c：新增bh1750、ds3231驱动文件
  
  (2)bluetooth：新增经典蓝牙从机功能、ble参数设置功能演示
  
  (3)AM2320、LM75B：新增温湿度传感器功能演示
  
  (4)huaWeiYun：新增华为云功能演示
  
  (5)onenet_studio：修正“onenet订阅主题失败”的问题
  
  (6)ctwing：新增电信云功能演示
  
  (7)所有demo：main.lua中默认关闭rndis网卡功能
  
- **2.3.7上层脚本更新说明**
  
  发布时间：2021/01/27 09:50
  
  修改记录：
  
  一、lib脚本修改
  
  lib脚本版本号：2.3.7
  
  (1)mqtt.lua：修正“subscribe订阅，服务器返回订阅失败时，代码逻辑无法检测到失败”的问题
  
  (2)aLiYun.lua：支持最新的阿里云公共实例和企业版示例的MQTT直连方式
  
  (3)audio.lua：新增“设置mic增益”的功能接口audio.setMicGain
  
  (4)audio.lua：支持“audio.setChannel接口设置输入mic通道”的功能
  
  (5)patch.lua：修正“2.3.6版本中spi.send_recv接口，接收不到数据”的问题
  
  二、demo脚本修改
  
  (1)i2c：新增mpu6xxx、aht10驱动文件
  
  (2)rtmp：新增rtmp demo
  
  (3)aLiYun：公共实例和企业版示例的MQTT直连方式demo
  
  (4)call：新增mic增益设置功能演示
  
  (5)call：新增mic增益设置和mic通道选择功能演示
  
  (6)txiot：新增腾讯云demo
  
  (7)modbus：新增modbus demo
  
  (8)bluetooth：新增beacon功能演示
  
- **2.3.6上层脚本更新说明**
  
  发布时间：2020/12/22 10:45
  
  修改记录：
  
  一、lib脚本修改
  
  lib脚本版本号：2.3.6
  
  (1)audio.lua：支持“多mp3文件拼接播放”功能
  
  (2)http.lua：支持HEAD操作
  
  (3)sys.lua：修正“某个task中如果有sys.waitUntil，并且这个task循环的创建和销毁，造成内存泄漏”的问题
  
  (4)net.lua:修正“core升级为0022之后，2g卡不能上网”的问题
  
  (5)aLiYun.lua：mqtt直连方式，增加获取username和password的函数设置功能
  
  二、demo脚本修改
  
  (1)bluetooth：新增蓝牙demo，需要配合Luat_V3开头的core固件才能使用，此类core固件还没有发布
  
  (2)crypto：新增des和des3功能示例
  
  (3)ftp：新增ftp demo
  
- **2.3.5上层脚本更新说明**
  
  1:aLiYun.lua：新增setConnectMode接口，可设置为MQTT-TCP直连模式、直连域名、直连端口、clientid生成规则
  
  2：aLiYun.lua：新增setRegion接口，可设置地域id
  
  3：aLiYun.lua：支持连接状态下的主题订阅功能
  
  4：audio.lua：play接口支持一次传入多文件连续拼接播放功能
  
  5：nvm.lua：init接口支持“本地烧录软件时是否擦除nvm中已有的参数”功能
  
  6：cc.lua：修正“通话中发送dtmf失败”的问题
  
  7：net.lua：修正“core概率性不上报^MODE: %d,%d，导致网络逻辑异常”的问题
  
  8：gpsZkw.lua、agpsZkw.lua：支持Air820UX系列模块的gps以及agps功能
  
- **2.3.2上层脚本更新说明**
  
  发布时间：2020/05/31 10:10
  
  修改记录：
  
  一、lib脚本修改
  
  lib脚本版本号：2.3.2
  
  (1)scanCode：支持摄像头拍照和扫码功能
  
  (2)record：支持流式录音功能
  
  (3)wifiScan：支持wifi热点扫描功能
  
  (4)audio：支持通话音量调节功能
  
  (5)http：修正“transfer-encoding区分大小写导致的chunk编码数据无法正常解析”的问题
  
  二、demo脚本修改
  
  (1)完善或者支持camera、record、wifi、audio、call demo
  
- **2.3.1上层脚本更新说明**
  
  发布时间：2020/05/04 22:48
  
  修改记录：
  
  一、lib脚本修改
  
  lib脚本版本号：2.3.1
  
  (1)audio.lua：修正“TTS速度设置错误”的问题
  
  (2)record.lua：新增录音功能
  
  二、demo脚本修改
  
  (1)alarm：新增闹钟demo
  
  (2)record：新增录音demo
  
- **2.3.0上层脚本更新说明**
  
  发布时间：2020/04/23 15:03
  
  修改记录：
  
  一、lib脚本修改
  
  lib脚本版本号：2.3.0
  
  (1)audio.lua：新增audio.setChannel接口，可以设置音频输出通道
  
- **2.2.9上层脚本更新说明**
  
  发布时间：2020/04/11 23:43
  
  修改记录：
  
  lib脚本版本号：2.2.9
  
  (1)支持tts、call功能
  
  (2)添加GPIO ldo电压域的控制说明
  
  (3)修改开发板默认netLed的控制方式，ldo电压域的控制放到main.lua去控制，不再写在netLed.lua中去控制
  
- **2.2.8上层脚本更新说明**
  
  发布时间：2020/04/09 23:37
  
  修改记录：
  
  lib脚本版本号：2.2.8
  
  (1)支持ui、audio、qrcode功能
  
  (2)修正“部分sim卡无法触发上网逻辑”的问题
  
  (3)修正“网络指示灯不亮”的问题
