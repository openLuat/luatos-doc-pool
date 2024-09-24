# Air780E模块开发项目遇到的吐血经历-远程升级篇

## 前情提要

最近去年开发的一个项目产品，用的是合宙的Cat.1 Air780E模块，最近陆续有客户反馈在乡村里频繁出现掉线的情况，通过换货、换SIM卡对比排查测试，只有去年5月22号采购的那批模块在客户环境附近会出现掉线的情况，而今年4月份采购的模块批次就不会掉线，很奇怪。

然后就去联系了对应负责的销售，了解到差异就是模块内的固件版本不同，去年采购的那批模块出厂给的版本是**AirM2M_780E_LTE_AT_V1138**，今年4月采购的那批模块版本是**AirM2M_780E_LTE_AT_V1162**，看来是高版本对网络做了优化，但在这个地区出货的也有150多台设备了，不可能每个都单独回收回来给模块用USB烧录成高版本固件，所以不如直接通过OTA远程批量升级。

## 第一次尝试升级，出现失败~

于是从他们的doc社区上找到了[FOTA远程升级的文档](https://doc.openluat.com/wiki/21?wiki_page_id=6048)，参考先用手边的设备用合宙IOT平台做下测试，看能不能升级。

结果什么都配置好了，到最后模块发 **AT+UPGRADE** 触发升级的时候，却老是报错 +UPGRADEIND: -1003 ，通过升级日志查询结果是"正在生成版本"？

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=MTc0ZTUzZjU5YjM1MGM4NzZmMWU5ODFhMjlhMzYyNzNfTkhxem5rT2VGaTJtcjUzaExzM1IzdjJuQlZ6dU1nS3NfVG9rZW46TFdDUWJpTjVnb1d3eTh4SVRoVmNZbG9rbnNtXzE3MjcxNTk2MzM6MTcyNzE2MzIzM19WNA)

在页面右上角看到有个红色的"？"，是IOT平台的帮助中心，往下滑就看到了升级日志返回结果的对应描述。

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=MjRjMGQ4Njg1MzA2OGE2MmE4NzE1MWM1YmJmZGI1NDRfZml5ZFFHb0Q1WWdtRHdIQ0NGcFJMZDg3a1RIWEoxQkRfVG9rZW46S1FhUmJ0b3V5b09WQXp4czY3ZmNieTZYbnRiXzE3MjcxNTk2MzM6MTcyNzE2MzIzM19WNA)

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=NDgxMzQxYWU5YzExZjBkNDM1MTU2MTAxZDAwODc1YmNfVDBXdThsVk5iU0RBSlVsUU9nT1JGSzNjZFVwS1ZDb1dfVG9rZW46TWZwVGJ6VkJRb29URFZ4Tmt5bmNVNHlVbm9mXzE3MjcxNTk2MzM6MTcyNzE2MzIzM19WNA)

正在生成版本，请稍后再次请求 看样子是版本相差太大了，平台内部还在做差分包，那我就等一会儿再请求看看。

## 第二次尝试升级，再次出现失败~

保险起见间隔了30分钟再次请求，以看到已经进入下载了，但是结果却又出现了 +UPGRADEIND: -1003 ！！

这又是什么原因？

```C#
ATi

AirM2M_780E_V1138_LTE_AT

OK

AT+CPIN?

+CSQ:18           // 信号强度

OK

AT+CEREG?

+CEREG:0,1        // 模块要保证已联网

OK

AT+UPGRADE

OK

+UPGRADEIND: -1003    // IOT平台升级日志显示正在生成版本，正在做差分包

--- 间隔了5分钟再次请求升级 ---
AT+UPGRADE

OK

+UPGRADEIND: 10

+UPGRADEIND: 20

+UPGRADEIND: 30

+UPGRADEIND: 40

+UPGRADEIND: 50

+UPGRADEIND: 60

+UPGRADEIND: 70

+UPGRADEIND: 80

+UPGRADEIND: 90

+UPGRADEIND: 100    // 下载完成了

+UPGRADEIND: -1003    // 啊？？ 怎么到这了还报错
```

先去IOT平台上看一下升级日志的结果是什么，查询看到显示的是"成功"，但实际上并没有升级成功啊，反而还报错了。

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=M2NlMDUwNTVmZTRiYjRhZWJlNDJlNDkzNTJhMzgyMjVfVjU5QUZEWVdjNWpXbTZrNWREOWh0NXNONzdHYWVreUlfVG9rZW46UUNNZ2JFM3Nyb3owM3d4Qnpka2NPTEVHbmZmXzE3MjcxNTk2MzM6MTcyNzE2MzIzM19WNA)

紧接着找合宙的技术人员咨询了解到，差分包大小是有限制的，不能大于480KB，否则会升级不成功。至于IOT平台上升级日志却显示"成功"，原因是这个成功代表的意思不是模块升级成功，而是给予模块的升级请求，下发了升级文件成功了。

经过进一步确认，可以通过合宙自己提供的生成差分包工具的网址，把V1138和V1162的dfota.bin文件放上去，制作一个差分包看看，到底有多大。

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=YTJhNjNmMjhiZTc1MTEyMGFjNmYwNDhhZjEzNTNjYTdfcjJqb2RuQldaUmpvY1VkemVlNHlXbndyRm9PdmhVbzFfVG9rZW46S3A3QWI1WWZhb1M4WUV4ek1uNWNOWGlpbkNlXzE3MjcxNTk2MzM6MTcyNzE2MzIzM19WNA)

等了大概3分钟左右，差分包制作出来了，点击下载后，文件大小有550KB，那确实超出了480KB，升不了。

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=YWQ0YTBjZDQyMTg2ZTZkMTcwOGE2MWZkZTc2NWY3M2JfMHJ0Zm82UDJJRmttRTlMN05FMHFRZWxyN056U2RRRzNfVG9rZW46TG9iYmJrdkV1b1h2U3N4djMzbWNreVQybmVnXzE3MjcxNTk2MzM6MTcyNzE2MzIzM19WNA)

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=ZjY0NDVhMWU4ZmJlNjlhZGVlZTEzZTdlNDNiNzg0ZDdfUlhvZnp6cFRpNnhoWHYyRUNCQnJCYlAzMDN6d2VuM2ZfVG9rZW46VFMyRmJ6ZXlhb0c4WGV4andxNmNaZW9tbldLXzE3MjcxNTk2MzM6MTcyNzE2MzIzM19WNA)

从合宙的技术那里还得到了一份AT固件各个版本之间制作差分包的大小，以及是否可以差分升级的表格，这方便多了啊。

（有数字的代表是在480KB以内，可以差分升级的版本。空白的就是不能升级的）

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=ZjEyNWQ4MTI5OWJjYWUxNTVhNDc3NWUyOWIzNjdjZDJfenU3cFJ3Y2JkWjd0R0JXZm5jU3hRdGR4VTRHZGhtOXhfVG9rZW46Q3NHT2JRNDUwb0N4Zkx4d0h3UmMzdUdYblZlXzE3MjcxNTk2MzM6MTcyNzE2MzIzM19WNA)

那么经过这张图 从左列来看，例如我当前的模块版本是V1138，需要升级到1162，对应的交叉格并没有数字，而且V1138升级到1147的差分包就已经到480KB的临界点了，只能先升到v1147，再升到1162。

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=ZmU4NWE3NTA4NDcyYWEwMjU4YTY0ZDQ4M2VmZTIyM2ZfekVDMEl4dWdnY2JoRnBGbWVTdXdyNldxSDJZcVRFM25fVG9rZW46VEdGY2JvOWFYb1ByNkp4d3hVRWNnRVUwbnBiXzE3MjcxNTk2MzM6MTcyNzE2MzIzM19WNA)

## 再一再二不再三，第三次升级，成功！

那么先获取到V1147版本的固件，[780E AT量产固件获取位置](https://doc.openluat.com/article/4922)，然后搜索得到[AirM2M_780E_LTE_AT_V1147](https://cdn.openluat-erp.openluat.com/erp_site_file/product_file/20230802_120755_AirM2M_780E_LTE_AT_V1147.zip)

解压出来找到"AirM2M_780E_V1147_LTE_AT.dfota.bin"文件，放到IOT平台上面。

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=ZDczM2E1NDdmYjA4MmZmZGRkMjk4NTk5Yzk0ZmUzOGRfUzJhRWRpUWw0UU5CZHZCMTlTU2ZWbFJCVjQ4MmgyenVfVG9rZW46UEMwNWI2bDQ1b2gyRkl4dmNVdmN3ZUpmbnZnXzE3MjcxNTk2MzM6MTcyNzE2MzIzM19WNA)

发送AT指令走下升级流程。

```C#
ATi

AirM2M_780E_V1138_LTE_AT

OK

AT+CPIN?

+CSQ:18           // 信号强度

OK

AT+CEREG?

+CEREG:0,1        // 模块要保证已联网

OK

AT+UPGRADE

OK

+UPGRADEIND: -1003    // IOT平台升级日志显示正在生成版本，正在做差分包


--- 间隔了5分钟再次请求升级 ---
AT+UPGRADE

OK

+UPGRADEIND: 10
+UPGRADEIND: 20
+UPGRADEIND: 30
+UPGRADEIND: 40
+UPGRADEIND: 50
+UPGRADEIND: 60
+UPGRADEIND: 70
+UPGRADEIND: 80
+UPGRADEIND: 90
+UPGRADEIND: 100    // 下载完成了

^boot.rom'v'!\n    // 自动重启

+QIND: "FOTA","START"            // 开始写入差分包
+QIND: "FOTA","UPDATING",0
+QIND: "FOTA","UPDATING",2
+QIND: "FOTA","UPDATING",4
+QIND: "FOTA","UPDATING",6
+QIND: "FOTA","UPDATING",9
+QIND: "FOTA","UPDATING",13
+QIND: "FOTA","UPDATING",18
+QIND: "FOTA","UPDATING",20
+QIND: "FOTA","UPDATING",22
+QIND: "FOTA","UPDATING",24
+QIND: "FOTA","UPDATING",27
+QIND: "FOTA","UPDATING",32
+QIND: "FOTA","UPDATING",34
+QIND: "FOTA","UPDATING",36
+QIND: "FOTA","UPDATING",37
+QIND: "FOTA","UPDATING",39
+QIND: "FOTA","UPDATING",41
+QIND: "FOTA","UPDATING",44
+QIND: "FOTA","UPDATING",45
+QIND: "FOTA","UPDATING",48
+QIND: "FOTA","UPDATING",50
+QIND: "FOTA","UPDATING",51
+QIND: "FOTA","UPDATING",52
+QIND: "FOTA","UPDATING",55
+QIND: "FOTA","UPDATING",57
+QIND: "FOTA","UPDATING",59
+QIND: "FOTA","UPDATING",62
+QIND: "FOTA","UPDATING",64
+QIND: "FOTA","UPDATING",68
+QIND: "FOTA","UPDATING",73
+QIND: "FOTA","UPDATING",78
+QIND: "FOTA","UPDATING",79
+QIND: "FOTA","UPDATING",82
+QIND: "FOTA","UPDATING",85
+QIND: "FOTA","UPDATING",93
+QIND: "FOTA","UPDATING",97
+QIND: "FOTA","UPDATING",100    // 写入成功
+QIND: "FOTA","END",0           // 写入结束

RDY                 // 开机的URC上报

^MODE: 17,17        // 一些注网相关的URC

+E_UTRAN Service

+CGEV: ME PDN ACT 1

+NITZ: 2024/08/23,06:52:50+32,0

ATI                // 发送ATI 查询下版本

AirM2M_780E_V1147_LTE_AT    // 升级成功了！

OK
```

成功从 **AirM2M_780E_V1138_LTE_AT** 升级到了 **AirM2M_780E_V1147_LTE_AT。**接下来就是按照的步骤，再升级到 **AirM2M_780E_V1162_LTE_AT** 版本。

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=Yzk1ZjJmZGMwMjhlZGYyOTRiMWU0M2IyMmZlMzYyMDNfZFFKOWJDakxHTmZ5cU1mWWFxbHlucmw3UG5SUWpIcXBfVG9rZW46RmJTcWJBeDJBb1NzYzZ4R2hjRmM4YlRMbjZmXzE3MjcxNTk2MzM6MTcyNzE2MzIzM19WNA)

```C#
ATi

AirM2M_780E_V1147_LTE_AT

OK


AT+UPGRADE

OK

+UPGRADEIND: -1003    // IOT平台升级日志显示正在生成版本，正在做差分包


--- 间隔了5分钟再次请求升级 ---
AT+UPGRADE

OK

+UPGRADEIND: 10
+UPGRADEIND: 20
+UPGRADEIND: 30
+UPGRADEIND: 40
+UPGRADEIND: 50
+UPGRADEIND: 60
+UPGRADEIND: 70
+UPGRADEIND: 80
+UPGRADEIND: 90
+UPGRADEIND: 100    // 下载完成了

^boot.rom'v'!\n    // 自动重启

+QIND: "FOTA","START"            // 开始写入差分包
+QIND: "FOTA","UPDATING",0
+QIND: "FOTA","UPDATING",2
+QIND: "FOTA","UPDATING",4
+QIND: "FOTA","UPDATING",6
+QIND: "FOTA","UPDATING",9
+QIND: "FOTA","UPDATING",13
+QIND: "FOTA","UPDATING",18
+QIND: "FOTA","UPDATING",20
+QIND: "FOTA","UPDATING",22
+QIND: "FOTA","UPDATING",24
+QIND: "FOTA","UPDATING",27
+QIND: "FOTA","UPDATING",32
+QIND: "FOTA","UPDATING",34
+QIND: "FOTA","UPDATING",36
+QIND: "FOTA","UPDATING",37
+QIND: "FOTA","UPDATING",39
+QIND: "FOTA","UPDATING",41
+QIND: "FOTA","UPDATING",44
+QIND: "FOTA","UPDATING",45
+QIND: "FOTA","UPDATING",48
+QIND: "FOTA","UPDATING",50
+QIND: "FOTA","UPDATING",51
+QIND: "FOTA","UPDATING",52
+QIND: "FOTA","UPDATING",55
+QIND: "FOTA","UPDATING",57
+QIND: "FOTA","UPDATING",59
+QIND: "FOTA","UPDATING",62
+QIND: "FOTA","UPDATING",64
+QIND: "FOTA","UPDATING",68
+QIND: "FOTA","UPDATING",73
+QIND: "FOTA","UPDATING",78
+QIND: "FOTA","UPDATING",79
+QIND: "FOTA","UPDATING",82
+QIND: "FOTA","UPDATING",85
+QIND: "FOTA","UPDATING",93
+QIND: "FOTA","UPDATING",97
+QIND: "FOTA","UPDATING",100    // 写入成功
+QIND: "FOTA","END",0           // 写入结束

RDY                 // 开机的URC上报

^MODE: 17,17        // 一些注网相关的URC

+E_UTRAN Service

+CGEV: ME PDN ACT 1

+NITZ: 2024/08/23,06:52:50+32,0

ATI                // 发送ATI 查询下版本

AirM2M_780E_V1162_LTE_AT    // ok，终于达到目的了！

OK
```

## 总结

从以前的老固件做升级，还要考虑到模块内部对差分升级所分配的FOTA分区有多少，如果差分包超过了分区（Air780E模块的FOTA分区看来就是480KB了），超出肯定是升级不了的。

紧接着和领导做了汇报，在本地测试了Air780E OTA升级可以了，流程也写好了，先找了5台在外的设备远程升级，测试一下看升级后掉线的现象也确实减少了，那说明固件没问题。掉线的麻烦事也完美解决了！
