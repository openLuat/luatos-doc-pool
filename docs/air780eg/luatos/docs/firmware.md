# Air780EG LuatOS固件版本

## 最新版本SDK&Demo

### LuatOS固件版本下载地址

[core_V1112](https://gitee.com/openLuat/LuatOS/releases/download/v1112.ec618.release/core_V1112.zip)

### 二次开发demo

[LuatOS-Air780EG](https://gitee.com/openLuat/LuatOS-Air780EG)

## LuatOS固件版本更新说明（最新V1112）

**core_V1112** 2024-09-03

缺陷修复

1：从hib模式唤醒后死机

## 历史版本SDK&Demo

### LuatOS固件版本下载地址

[core_V1111](https://gitee.com/openLuat/LuatOS/releases/download/v1111.ec618.release/core_V1111.zip)

[core_V1110](https://gitee.com/openLuat/LuatOS/releases/download/v1110.ec618.release/core_V1110.zip)

[core_V1109](https://gitee.com/openLuat/LuatOS/releases/download/v1109.ec618.release/core_V1109.zip)

[core_V1108](https://gitee.com/openLuat/LuatOS/releases/download/v1108.ec618.release/core_V1108.zip)

## 二次开发demo

[LuatOS-Air780EG](https://gitee.com/openLuat/LuatOS-Air780EG)


## LuatOS固件版本更新说明（历史版本）

**core_V1112** 2024-09-03

缺陷修复

1：从hib模式唤醒后死机


**core_V1111** 2024-08-27

缺陷修复

1：软件串口在没有全部发送完前close，出现异常

2：spi table方式发送异常

3：libgnss.clear没有清理干净残留数据

4：gnss定位成功后，执行libgnss.clear，关闭再打开gnss芯片，如果一上电就定位成功，无GNSS_STATE消息

5：mqtt启用后，内存占用过大，导致其他业务逻辑申请不到可用内存

6：http 响应头分包，导致解析失败

7：修复FTP在PASV模式下接受少量数据可能会提示失败

新增功能

add：mqtt添加设置接收缓冲区大小的功能

add：fatfs卸载功能

add：mcu.hardfault新增死机处理模式参数

更新功能

update：限制uart.read单次最大读取量，一次性读取太多数据，容易死机

update：已经释放过的socket ctrl，不再允许其他操作，防止异常死机

update：兼容部分FTP服务器

update：RRC快速释放的优化选项


**core_V1110** 2024-06-07

兼容性变化

1：tts_onchip下关闭websocket和ftp客户端的支持

2：tts_onchip下关闭ftp

3：因空间不足，后续需要tts_onchip的版本可自行云编译或本地编译，本版本不再更新

缺陷修复

1：防止可能的时间设置错误

2：luatos固件读取的luadb分区大小不对

3：wait485时，485转向io控制timer没有停止，导致数据接收出问题

4：当pwm未close，既改周期又改占空比时，可能死机

5：485换向脚用不了GPIO14、GPIO15

6：软件串口无法使用timer1和timer4

7：OTA底层数据写入完成，但脚本数据没完成时，不允许升级

8：uart485无法使用ALT4的GPIO18和GPIO19

9：socket主动关闭时，回调消息错误

10：合入原厂补丁

11：mqtt发送时，一次性将数据发出去，避免被打断

12：mqttconnect报文长度超过256时，无法连接服务器

13：ftp异常死机

14：socket添加防护，防止已释放的资源再次使用

新增功能

add：重置协议栈参数到默认

add：基站同步时间开关

add：深度休眠定时器回调消息

add：深度休眠唤醒时保持休眠前设置的电平

add：w5500添加DHCP超时消息

add：DHCP重试次数增加，应对运行速度慢的路由器

add：socket查询当前连接状态

add：http自定义header支持自定义大小

add：sfud互斥锁保护

更新功能

update：当遇到无法解析的NMEA语句时，屏蔽打印


**core_V1109** 2024-03-06

兼容性变化:

1：tts_onchip下关闭YMODEM 2：tts_onchip 关闭 REPL 3：调整json.encode的浮点数格式化为 %.7f , 更符合实际用途, 不然以为会吃掉浮点精度

缺陷修复:

fix: 合入原厂补丁 修复SWD CP IO遇到异常信号时会死机，修复伪基站防护漏洞

fix: socket.rx接收数据时,如果zbuff扩容失败,先尝试缩小接收长度,如果没有空间就只能返回错误了

fix: u8g2.CopyBuff没有正常工作,原因是判断zbuff长度有错误

fix: ftp login失败后死机

fix: socket.sntp使用自定义域名会报错死机

fix:luatos i2s录音不能配置frame size

fix:修复luatos固件启用tts时报luat_sfud无法链接的问题

fix:websocket心跳包未正常发出

fix:云编译luatos固件选择禁用DTLS时会报mbedtls_ssl_conf_handshake_timeout函数不存在

fix:无法验证pin码

新增功能:

add: sfud支持获取flash容量和page信息

add: adc分压范围添加最大限制

add: pm.dtimerCheck 添加剩余时间

add: http支持大数据上传

add: 伪基站屏蔽时间

add: u8g2支持配置x轴偏移量

add: libgnss.getIntLocation添加速度参数项

add: errdump支持自定义域名和端口

add: crypto.crc16_modbus支持设置初始值,方便进行多段数据连续计算

add: 新增u8g2.SetPowerSave函数

add: pcf8563t时钟模块的驱动及demo

add: luatos固件添加xxtea库的编译

add: luatos添加蚂蚁链的集成

add: luatos固件添加ercoap库

add: 基于ntp的毫秒级时间戳 socket.ntptm()

更新功能:

update: libgnss.casic_aid兼容基站定位返回的字符串坐标值

update:去掉mqtt接收单包4096限制

update: u8g2新增ssd1309 i2c方式的驱动,之前只有SPI的

update:优化w5500的dhcp过程

update:luatos固件I2C默认使用poll模式

update:luatos补充I2S单声道情况下，左右声道选择

update:luatos uart 接收消息不允许过多，防止异常情况下大量uart接收消息死机

update:adc分压范围最大限制


**core_V1108** 2023-11-17

兼容性变化:

修正CPU温度的单位

影响, 之前的版本返回的CPU温度是摄氏度, 其他BSP均为1/1000摄氏度

解决办法: 新数据 //1000 即得到原有的数据值

缺陷修复:

fix: socket close的时候没有清除掉新数据标志 导致SSL有概率重连持续失败

fix: mqtt库某些情况buffer_offset重连不置零 导致MQTT有概率重连持续失败

fix: mqtt心跳定时器计数错误 导致mqtt心跳可能不会发出

fix: CPU温度的单位应该是1/1000摄氏度, 实现错了

fix: 重写sntp函数,并支持自动超时 弱网情况下,sntp可能会耗尽socket连接数

fix: 合入原厂补丁，修复一个因搜索基站引起的死机问题

fix: mqtt库发送包报错的时候应该关闭socket

fix: lvgl反复创建style会死机

fix: fatfs的lsdir扫不出文件夹

fix: 兼容RTC库的mon属性

fix: AES-128-ECB且PKCS7, 解密错误数据不能返回

fix: 修复iotcloud库onenet部分情况数据截断问题

fix: 修复ymodem路径字符串末尾没有0的问题

fix: 64bit的luatos固件,打印print(-1)会输出很大的值

fix: 780E w5500 sntp死机

fix: ftp启动后台线程应判断是否成功,创建失败要走失败流程

fix: errDump手动读文件的open参数不对

fix: libgnss.getIntLocation的speed值异常

fix: sim卡擦写次数统计不对

fix: 64bit固件下audio库播放音频没有结束播放的回调消息.

fix: 修复socket无法连接情况下无法重连问题

fix: vfs_fatfs里的容量计算错误

fix: i2c.createSoft的示例,在Air780E的V1107固件会报错,干脆填上delay值吧

fix: http库的关闭逻辑不完备,并清除编译警告

fix: 在进行DNS过程时，调用network_force_close_socket并且不再进行连接时，DNS完成仍然会回调

fix: crypto.totp函数有内存泄漏问题

fix: gmssl库的sm4加密模式错误

fix: libemqtt中全部大数组改成heap分配

fix: 修复iconv库转换长数据时会丢失后部分字符

fix: http库tls证书相关的属性没有强制初始化为0,有可能出现非法值

fix: fonts库没有正确枚举新的sarasa字体

fix: ssl发送大量数据时，需要分批发送

fix: adc获取标记未更新，导致获取adc值有可能是上一次的

fix: TTS固件未成功挂载SPI FLASH时会死机

fix: tts播放时无法选择i2s1

fix: 云编译的sarasa英文字体不生效

fix: adc选择关闭内部分压模式时没有完全关闭掉

功能新增和更新:

add: iotcloud库支持涂鸦/百度云

add: ftp添加数据端口返回内网ip的兼容

add: 支持获取硬件版本号

add: fskv库添加sett函数

add: 添加fastlz压缩库

add: 补回json.null属性

add: crypto库添加流式hash接口

add: sntp添加适配器选项

add: 添加u8g2.DrawButtonUTF8

add: mobile添加SIM卡写入统计的API

add: lcd库支持屏幕外的坐标进行绘图,例如图片部分在画面外

add: mqtt添加错误返回参数

add: lcd 添加高通字体gbk接口

add: mqtt添加状态获取接口

add: sms.send新增auto_phone_fix,可禁用对应目标号码的自动出来,从而适应国外的复杂号码规则

add: es8311基础循环录音demo

add: 添加crypto.crc7函数

add: u8g2.CopyBuffer函数

add: gmssl.sm2加解密添加网站兼容模式

add: gmssl.sm2加解密支持老国标C1C2C3

add: gmssl库添加sm2签名和验签

add: http库支持URL中的鉴权信息

add: 新增bit64.strtoll函数

add: luatos云编译支持启用LVGL的PNG和BMP解码

update: 完善ymodem接收文件的结尾处理

update: gpio.debounce 模式1下，去除掉一看就是不合理的中断

update: FTP优化等待数据传输流程

update: 更新 ws2812 demo,EC618支持pin直驱

update: ymodem兼容ymodem-1k

update: 优化ftp接收文件的内存分配

update: 优化http回调下载长度值得精确度

update: 优化了辅助内存回收功能，并提供接口

update: 内存不足时不再简单的提示，而是把使用情况打印出来

update: sim卡可能欠费做个提示

update: 执行poweroff前自动关掉wdt,否则会20秒后死机重启


## [Luatools工具使用教程（点击此处，跳转阅读）](https://docs.openluat.com/Luatools/)

## [量产多路下载工具使用教程（点击此处，跳转阅读）](https://docs.openluat.com/multi_download/)