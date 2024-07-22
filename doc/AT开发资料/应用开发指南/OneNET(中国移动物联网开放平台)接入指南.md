# 应用概述

&emsp;&emsp;使用AT方式通过MQTT协议连接onenet studio。官网地址：https://open.iot.10086.cn/

# 材料准备
1. Air780EP(V)开发板一套，包括天线SIM卡，USB线。

2. PC电脑，串口工具
  ![](../../../image/AT开发资料/应用开发指南/OneNET(中国移动物联网开放平台)接入指南/开发板.png)

3. 在onenet上创建产品

   打开OneNET官网，进入控制台，进入[Onenet Studio](https://open.iot.10086.cn/studio/summary)，选择设备接入与管理，点击产品管理。

   ![](../../../image/AT开发资料/应用开发指南/OneNET(中国移动物联网开放平台)接入指南/图片1.png) 

   点击添加产品

   ![](../../../image/AT开发资料/应用开发指南/OneNET(中国移动物联网开放平台)接入指南/图片2.png) 

   根据自己产品填写，注意：节点类型选择直连设备，接入协议选择MQTT，点击确定

   ![](../../../image/AT开发资料/应用开发指南/OneNET(中国移动物联网开放平台)接入指南/图片3.png) 

   点击详情

   ![](../../../image/AT开发资料/应用开发指南/OneNET(中国移动物联网开放平台)接入指南/图片4.png) 

   将右上角自动注册打开

   ![](../../../image/AT开发资料/应用开发指南/OneNET(中国移动物联网开放平台)接入指南/图片5.png) 

   记住产品ID和产品key


4. 创建设备

   填入设备名，选择产品，这里我使用的是模块的imei来做设备名称

   ![](../../../image/AT开发资料/应用开发指南/OneNET(中国移动物联网开放平台)接入指南/QQ20240722-151053.png)

5. 查看onenet接入协议

   [MQTT设备连接_开发者文档_OneNET (10086.cn)](https://open.iot.10086.cn/doc/v5/fuse/detail/919))
   
   ![](../../../image/AT开发资料/应用开发指南/OneNET(中国移动物联网开放平台)接入指南/20230808174902316_image.png)

   可以看到，登入onenet时，mqtt的clientID、username和password都有指定

   clientId即为刚才创建的设备名称

   username为创建的产品ID

![](../../../image/AT开发资料/应用开发指南/OneNET(中国移动物联网开放平台)接入指南/QQ20240722-152651.png)


   password是需要经过加密计算得来的鉴权token

   计算方法详见如下文章，这篇文章测试时直接使用onenet提供的测试工具来计算鉴权密码，鉴权计算测试工具下面连接中下载

  [接入安全认证_开发者文档_OneNET (10086.cn)](https://open.iot.10086.cn/doc/iot_platform/book/device-connect&manager/device-auth.html)

   

# 连接onenet
## 1.查询卡、网络注册状态


&emsp;&emsp;具体交互流程如下所示

```lua
查询SIM卡状态
AT+CPIN?

+CPIN: READY

OK

查询信号质量
AT+CSQ

+CSQ: 16,0

OK

查询网络附着状态
AT+CGATT?

+CGATT: 1

OK

AT+CGDCONT?

+CGDCONT: 1,"IP","cmiot","10.126.200.230"

OK
```

## 2.MQTT直连onenet
设备注册参数如下：
```lua
mqttClientId: devicename
mqttUsername: productID
mqttPassword: token
```
| 参数                 | 说明                    |
| -------------------- | ----------------------- |
| devicename           | 设备名称                |
| productID            | 平台分配的产品id        |
| token                | 经过鉴权算法得到的token |
| 具体交互流程如下所示 |                         |

下图为工具计算出的token

![](../../../image/AT开发资料/应用开发指南/OneNET(中国移动物联网开放平台)接入指南/QQ20240722-154010.png)

```lua
AT+MCONFIG="868655072230313","Wf5IXIGcZn","version=2018-10-31&res=products%2FWf5IXIGcZn%2Fdevices%2F868655072230313&et=1721630715&method=md5&sign=DPqCcsPQAQok9Gt7mNPTbA%3D%3D"

OK

AT+MIPSTART="studio-mqtt.heclouds.com",1883

OK

CONNECT OK


AT+MCONNECT=1,120

OK

CONNACK OK

```

可以从平台上看到设备已经在线了

![](../../../image/AT开发资料/应用开发指南/OneNET(中国移动物联网开放平台)接入指南/QQ20240722-160748.png)

## 3.发布与订阅消息

onenet studio有固定的通信TOPIC，可以到官网查看，这里演示下设备属性上报与响应的主题

[通信主题_开发者文档_OneNET (10086.cn)](https://open.iot.10086.cn/doc/iot_platform/book/device-connect&manager/MQTT/topic.html)

![](../../../image/AT开发资料/应用开发指南/OneNET(中国移动物联网开放平台)接入指南/20210812151650017_image.png)

### 订阅
```lua
AT+MSUB="$sys/Wf5IXIGcZn/868655072230313/thing/property/post/reply",0

OK

SUBACK
```
### 发布

向设备上报属性的主题发布消息，消息携带设备的属性，不同的产品具有不同的属性，可以在设备物模型处查看

例如：在文章开始创建的产品具有如下图所示的属性

![](../../../image/AT开发资料/应用开发指南/OneNET(中国移动物联网开放平台)接入指南/QQ20240722-162245.png)

```lua
向上报属性的主题发布一条payload格式错误的消息
AT+MPUB="$sys/q23GT8XVOu/868739055238251/thing/property/post",0,0,"{}"

OK

平台返回缺少参数
+MSUB: "$sys/q23GT8XVOu/868739055238251/thing/property/post/reply",47 byte,{"id":null,"code":2403,"msg":"required msg id"}


如下是正常流程
AT+MPUB="$sys/Wf5IXIGcZn/868655072230313/thing/property/post",0,0,"{\22id\22:\22123\22,\22params\22:{\22Capacity\22:{\22value\22:62}}}"

OK

平台返回成功
+MSUB: "$sys/Wf5IXIGcZn/868655072230313/thing/property/post/reply",39 byte,{"id":"123","code":200,"msg":"success"}

```

可以看到平台已经有数据更新

![](../../../image/AT开发资料/应用开发指南/OneNET(中国移动物联网开放平台)接入指南/QQ20240722-163446.png)
