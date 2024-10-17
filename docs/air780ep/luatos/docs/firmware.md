# Air780EP LuatOS固件版本

## 最新版本SDK&Demo

### LuatOS固件版本下载地址

[LuatOS-SoC_V2001_Air780EP](https://gitee.com/openLuat/LuatOS/releases/download/v2001.ec7xx.release/LuatOS-SoC_V2001_Air780EP.soc)

### 二次开发demo

[LuatOS-Air780EP](https://gitee.com/openLuat/LuatOS-Air780EP)

## LuatOS固件版本更新说明（最新V1003）

**core_V1003** 2024-09-02

缺陷修复

1：spi table方式发送异常

2：libgnss.clear没有清理干净残留数据

3：gnss定位成功后，执行libgnss.clear，关闭再打开gnss芯片，如果一上电就定位成功，无GNSS_STATE消息

4：mqtt启用后，内存占用过大，导致其他业务逻辑申请不到可用内存

5：http 响应头分包，导致解析失败

6：修复FTP在PASV模式下接受少量数据可能会提示失败

新增功能

add：mqtt添加设置接收缓冲区大小的功能

add：fatfs卸载功能

add：mcu.hardfault新增死机处理模式参数

更新功能

update：限制uart.read单次最大读取量，一次性读取太多数据，容易死机

update：已经释放过的socket ctrl，不再允许其他操作，防止异常死机

update：兼容部分FTP服务器

update：RRC快速释放的优化选项

## 历史版本SDK&Demo

### LuatOS固件版本下载地址

[core_V1003](https://gitee.com/openLuat/LuatOS/releases/download/v1003.ec7xx.release/core_V1003.zip)

[core_V1002](https://gitee.com/openLuat/LuatOS/releases/download/v1002.ec7xx.release/core_V1002.zip)

[core_V1001](https://gitee.com/openLuat/LuatOS/releases/download/v1001.ec7xx.release/core_V1001.zip)

### 二次开发demo

[LuatOS-Air780EP](https://gitee.com/openLuat/LuatOS-Air780EP)


### LuatOS固件版本更新说明（历史版本）


**core_V1002** 2024-07-04

兼容性变化

1：因功能变化较多，FLASH空间不足

(1)LuatOS-SoC_V1001_EC718PV无法远程升级到LuatOS-SoC_V1002_EC718PV

(2)LuatOS-SoC_V1002_EC718PV为正式发行的最后一版EPV固件，后续需要EPV固件请使用云编译或本地自行编译

缺陷修复

fix: 拍照的时候无法选择jpeg编码质量

fix：pwm在没有先close的情况下，既改周期，又改占空比，有可能死机的问题

fix：在使用uart485时，无法设置转向pin为GPIO16和GPIO17的问题

fix：otp功能异常

fix：ota时，在ota完成的最后一刻死机，会导致底层OTA成功，而脚本ota失败

fix：EPV固件，无法进入休眠

fix：socket主动关闭时，回调消息错误

fix：mqtt发送时，一次性将数据发出去，避免被打断

fix：mqttconnect报文长度超过256时，无法连接服务器

fix：ftp异常死机

fix：socket添加防护，防止已释放的资源再次使用

fix：防止可能的时间设置错误

fix：spi table方式发送异常

新增功能

add：audio库添加录音功能

add：agpio在深度休眠唤醒后，依然可以保持休眠前电平的能力

add：重置协议栈参数到默认

add：基站同步时间开关

add：深度休眠定时器回调消息

add：w5500添加DHCP超时消息

add：DHCP重试次数增加，应对运行速度慢的路由器

add：socket查询当前连接状态

add：http自定义header支持自定义大小

add：sfud互斥锁保护

add: 支持外部flash全量升级

add：支持配置codec的工作电压

add：mqtt添加设置缓冲区大小的功能

更新功能

update：当遇到无法解析的NMEA语句时，屏蔽打印


**core_V1001** 2024-03-08

第一次发布


## [Luatools工具使用教程（点击此处，跳转阅读）](https://docs.openluat.com/Luatools/)

## [量产多路下载工具使用教程（点击此处，跳转阅读）](https://docs.openluat.com/multi_download/)