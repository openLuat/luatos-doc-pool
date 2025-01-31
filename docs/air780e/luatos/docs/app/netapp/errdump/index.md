## 一、errDump 功能概述

LuatOS-Air 错误日志上报功能模块名叫：errDump，errDump 对“量产投放市场的设备，远程调试初步定位问题”至关重要， 强烈建议客户一定要使用此功能

errDump 就是将模块运行过程中产生的错误信息或者应用日志通过 TCP/UDP 上报到互联网上的指定服务器，技术人员可以在服务器上查阅日志，协助远程了解设备运行情况，或者故障诊断。

使用合宙云服务器时，迫于服务器压力，只有手动打开 debug 开关（见后面第六节代码示例介绍），才有日志上报（当使用合宙调试服务器时，开机前先检查一下 log 开关，每 2 小时查询一次 log 开关，如果开关未开启，则不允许上传调试日志），打开方式见《三、实例介绍》

## 二、演示功能概述

本示例将演示上报错误日志的功能。

## 三、准备硬件环境

### 3.1 780E 开发板一套

淘宝购买链接：[Air780E 核心板淘宝购买链接](https://item.taobao.com/item.htm?id=693774140934&pisk=f1eiwOqL25l1_HYiV6D1ize3wN5d5FMjRrpxkx3VT2uIHCCskWm4kysffAEqor4KRRIskGT0ooqi_coq7DWE000qbVr2mmzKQjNtkV3mnoalvaBRelZshA7RyTFdpD4xQco2_VS2Tcnvc89h5lZshq-pu_FUfEDVVdOmgrkET0ir3mkq_MDEmmM2QjJaY2uI0UGAoNueWRjiw4YTC-_opNr-zluaXleFpfR_X2fhTJVn94W--KJ4KcqQreCDEs3zNVh-DyWpIxqEmyc8savgoor7gX2D7GUzmW4jBJS2_4PTWjestFRZqA0iaRlwjdkIgW2nBR7XNkEn7bDL96_tMA4gN4GNOwa0xVU4IX8G4iReapZyhDSYLIOj_DinyhbSB2IHjbEhxMA51foIXaIhxItMPKJlyMjHNEGZAcQR.&spm=a1z10.5-c-s.w4002-24045920841.33.639f1fd1YrS4b6&skuId=5098266470883) ；

此核心板的详细使用说明参考：[Air780E 产品手册](https://docs.openluat.com/air780e/product/) 中的 << 开发板Core_Air780E使用说明V1.0.5.pdf>>。

![](image/HwHIbALQuohZ8BxyRHmcy0vbn1b.png)

### 3.2 SIM 卡

请准备一张可正常上网的 SIM 卡，该卡可以是物联网卡或您的个人手机卡。

**特别提醒：**请确保 SIM 卡未欠费且网络功能正常，以便顺利进行后续操作。

### 3.3 数据通信线

typec 接口 USB 数据线即可。

### 3.4 PC 电脑

WINDOWS 系统。

## 四、准备软件环境

### 2.1 基本的下载调试工具

使用说明参考：[Luatools 下载和详细使用](https://docs.openluat.com/Luatools/) ；

## 五、errDump 软硬件资料

本文通过 demo 演示来说明本章节内容的基本用法。

### 5.1 源码和工具

- 780E 模块使用固件：[SDK& Demo - 合宙文档中心](https://docs.openluat.com/air780e/luatos/firmware/)，本 demo 使用的固件版本是：LuatOS-SoC_V1112_EC618_FULL.soc
- 本教程使用的 demo：[https://gitee.com/openLuat/LuatOS-Air780E/tree/master/demo/errDump](https://gitee.com/openLuat/LuatOS-Air780E/tree/master/demo/errDump)
- 将固件和脚本烧录到模块中，使用说明参考：[Luatools 下载和详细使用](https://docs.openluat.com/Luatools/)
- 合宙云平台：[https://iot.openluat.com](https://iot.openluat.com)
- 源码和固件已打包，如下所示：
[点我,下载完整压缩文件包](file/完整文件包.zip){:target="_blank"}
- [errDump-全部api地址](https://docs.openluat.com/air780e/luatos/api/core/errDump/)，如果只看本demo的api直接看下面的`5.2 demo使用api介绍`即可。

### 5.2 demo使用api介绍

#### errDump.config(enable, period, user_flag, custom_id, host, port)

作用：配置关键日志上传至 IOT 平台，包括引起 Lua VM 异常退出的日志和用户通过 record 写入的日志，类似于 Air 的 errDump。

**参数**

| **参数**      | **传入值类型** | **解释**                                                                                                                                                                                    |
| ------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enable        | boolean        | 是否启用记录功能，false 时不记录任何日志                                                                                                                                                |
| period        | int            | 定时上传周期，单位秒，默认 600 秒。此为自动上传后的重试时间，开机或 record 操作后会尝试快速上传至 IOT 平台。如果为 0，则不自动上传，由用户 dump 后上传至自己的平台 |
| user_flag     | string         | 用户的特殊标识，可为空                                                                                                                                                                        |
| custom_id     | string         | 设备识别号，4G 设备默认是 IMEI，其他设备默认是 mcu.unique_id                                                                                                                                    |
| host          | string         | 服务器域名，默认 dev_msg1.openluat.com                                                                                                                                                        |
| port          | int            | 服务器端口，默认 12425，为合宙云平台默认端口                                                                                                                                                      |

**返回值**

| **返回值类型** | **解释**       |
| -------------- | -------------- |
| nil            | 无返回值       |

---

#### errDump.dump(zbuff, type, isDelete)

作用：手动读取异常日志，用于将日志发送至用户自有服务器而非 IOT 平台。如果在 errDump.config 中配置了周期上传，则不可使用本函数。

**参数**

| **参数**  | **传入值类型** | **解释**                                             |
| --------- | -------------- | ---------------------------------------------------- |
| zbuff     | zbuff          | 日志信息缓存，若为 nil 则不会读取日志                 |
| type      | int            | 日志类型，目前支持 errDump.TYPE_SYS 和 errDump.TYPE_USR |
| isDelete  | boolean        | 是否删除日志                                         |

**返回值**

| **返回值类型** | **解释**                                                                                              |
| -------------- | ----------------------------------------------------------------------------------------------------- |
| boolean        | true 表示在本次读取前无数据写入，false 表示有数据写入。删除日志前建议再次读取以确保无新数据写入       |

---

#### errDump.record(msg)

作用：写入用户异常日志，注意最大仅为 4KB，超过部分会覆盖旧数据。开启自动上传后会上传至 IOT 平台。

**参数**

| **参数** | **传入值类型** | **解释**       |
| -------- | -------------- | -------------- |
| msg      | string         | 用户日志       |

**返回值**

| **返回值类型** | **解释**       |
| -------------- | -------------- |
| nil            | 无返回值       |


## 六、代码示例介绍

### 6.1  上传错误日志到合宙云平台

#### 6.1.1  云平台配置

合宙云平台：[https://iot.openluat.com](https://iot.openluat.com)

##### 6.1.1.1  打开 IoT 平台

![](image/EIB8bPUpeo80lDxnl2Cc90opnVV.png)

##### 6.1.1.2  新建一个项目

![](image/HhsnbEd7sodHMrxNtQccCk6qn2A.png)

##### 6.1.1.3  将你自己建的项目 key 复制到 demo 中

![](image/OS1mbN90jobxF9xbtv5cHgBunJd.png)

##### 6.1.1.4 打开设备 DEBUG 开关

![](image/ML3lbuOXEoh3v6xUAvmczI48nhU.png)

![](image/BJ9GbxcqcoZKG2xhHWKcmV76ndX.png)

#### 6.1.2 demo 介绍

这里测试用的是合宙云平台上报。

demo 程序中打开自动上报合宙云平台部分，注释掉手动获取信息部分。

使用合宙云平台查看上报错误信息的话，代码更改如下：

```lua
PROJECT = "errdump_test"
VERSION = "1.0"
PRODUCT_KEY = "s1uUnY6KA06ifIjcutm5oNbG3MZf5aUv" --换成自己的
-- sys库是标配
_G.sys = require("sys")
_G.sysplus = require("sysplus")
log.style(1)

--下面演示自动发送
errDump.config(true, 600, "user_id")    -- 默认是关闭，用这个可以额外添加用户标识，比如用户自定义的ID之类

local function test_user_log()
    while true do
        sys.wait(15000)
        errDump.record("测试一下用户的记录功能")
    end
end

local function test_error_log()
    sys.wait(60000)
    lllllllllog.record("测试一下用户的记录功能") --默认写错代码死机
end

-- -- 下面演示手动获取信息
-- errDump.config(true, 0)
-- local function test_user_log()
--  local buff = zbuff.create(4096)
--  local new_flag = errDump.dump(buff, errDump.TYPE_SYS)       -- 开机手动读取一次异常日志
--  if buff:used() > 0 then
--      log.info(buff:toStr(0, buff:used()))    -- 打印出异常日志
--  end
--  new_flag = errDump.dump(buff, errDump.TYPE_SYS)
--  if not new_flag then
--      log.info("没有新数据了，删除系统错误日志")
--      errDump.dump(nil, errDump.TYPE_SYS, true)
--  end
--  while true do
--      sys.wait(15000)
--      errDump.record("测试一下用户的记录功能")
--      local new_flag = errDump.dump(buff, errDump.TYPE_USR)
--      if new_flag then
--          log.info("errBuff", buff:toStr(0, buff:used()))
--      end
--      new_flag = errDump.dump(buff, errDump.TYPE_USR)
--      if not new_flag then
--          log.info("没有新数据了，删除用户错误日志")
--          errDump.dump(nil, errDump.TYPE_USR, true)
--      end

--  end
-- end

-- local function test_error_log()
--  sys.wait(60000)
--  lllllllllog.record("测试一下用户的记录功能") --默认写错代码死机
-- end

sys.taskInit(test_user_log)
sys.taskInit(test_error_log)
sys.run()
```

## 七、功能验证

### 7.1 Luatools 日志打印

![](image/Sx8HbDQ9zoDmKUxNLODc4czwnfb.png)

### 7.2 云平台查看错误上报

![](image/A9tSbg3pYo6sQAx0z2Wc9EDKnwe.png)

## 八、总结

本示例介绍了将错误日志上报到合宙云平台的功能。

## 扩展



## 常见问题



## 给读者的话

> 本篇文章由`Linden`开发；
>
> 本篇文章描述的内容，如果有错误、细节缺失、细节不清晰或者其他任何问题，总之就是无法解决您遇到的问题；
>
> 请登录[合宙技术交流论坛](https://chat.openluat.com/)，点击[文档找错赢奖金-Air780E-LuatOS-软件指南-网络应用-errDump](https://chat.openluat.com/#/page/matter?125=1846802109790552065&126=%E6%96%87%E6%A1%A3%E6%89%BE%E9%94%99%E8%B5%A2%E5%A5%96%E9%87%91-Air780E-LuatOS-%E8%BD%AF%E4%BB%B6%E6%8C%87%E5%8D%97-%E7%BD%91%E7%BB%9C%E5%BA%94%E7%94%A8-errDump&askid=1846802109790552065)；
>
> 用截图标注+文字描述的方式跟帖回复，记录清楚您发现的问题；
>
> 我们会迅速核实并且修改文档；
>
> 同时也会为您累计找错积分，您还可能赢取月度找错奖金！
