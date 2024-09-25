
# 合宙DTU资料中心

TODO
# IRTU 固件参考手册 -- V3.9

## 一 、DTU 常见问题

- 1.1、 DTU版本默认上电是透传模式还是非透传模式，两个模式间如何转换?

    答：默认只配置了串口115200,8位数据模式，1个停止位，无校验，通道默认关闭。

- 1.2、是否有可能让在第一次去连接server时上报自己ID(可以自定义)功能?

    答：支持自定义，详见“配置保存指令”的register字段。

- 1.3、在非透传模式报文也是发的AT命令格式吗?

    答：不用AT,非透传模式参考指令“多通道通信报文

- 1.4、 恢复默认设置有条件吗？比如低电平保持多长时间？上电前拉低?

    答：拉低25mS以上即可，不需要上电前拉低。使用云参数的话，基本上不会用到这个脚

- 1.5、心跳包是否支持自定义，有没有长度限制？

    答：心跳包支持自定义，默认是字符串“ping”,长度最大1460字节

- 1.6、 是否可以指定透传模式下每次上报添加ID

    答: 支持,详见“配置保存指令”的plate字段。

- 1.7、如果连上server后MCU如何知道已经连上？会不会有字符串提示?

    答：连上server后，透传模式下相当于一条网线，不会有字符提示，MCU不用去维护DTU的状态。

- 1.8、可否设置如果一定时间内收不到server的心跳包，dtu自动掉电重连?

    答：内部有自动重连，开关飞行模式，重启模式，线程守护来保证DTU的网络链接正常，用户不需要干预。

- 1.9、 是否支持定时采集功能?

    答：支持，以后升级会逐渐支持更多的RTU的功能，比如定时采集，定时任务预置指令采集等。

- 1.10、 如何知道是SIM卡是否欠费，是否连上服务器?

    答：有两个办法：
    	 看指示灯，心跳灯（100ms亮，1900毫秒灭表示脸上服务器），快闪通常表示卡不良或欠费，慢闪表示GSM正常但是网络附着不成功。
    	 读取RDY信号（net ready信号），高电平是服务器链接成功，低电平是未连接。

- 1.11、 串口是否支持流量控制？

    答：支持，在保存参数配置的“flow"参数设置每分钟最大流量值,如果流量超过，则数据丢弃。

- 1.12、 是否发送完成返回标志给MCU？

    答：支持,在MCU控制模式的时候，发送数据成功后会返回"SEND_OK"给MCU,方便MCU关闭模块。

- 1.13、 网络是否连接能不能通知MCU？

    答：支持
    	AIR202U的RDY信号--第6脚(GPIO_3)上电输出低电平，网络链接成功后输出高电平。
    	AIR720 的RDY信号--第5脚（GPIO_65）上电输出低电平，网络链接成功后输出高电平。

- 1.14、 定时采集功能支持透传和非透传模式吗？

    答：定时采集功能只有透传模式才能支持，支持串口1和2单独设置。

## 二、DTU功能说明

AIR202U 是上海合宙出品的一款功能强大使用极其简单的DTU模块，借助不到10条交互指令，就可以实现绝大部分物联网的通讯需求，极大简化用户开发物联网产品的步骤，大幅度减少开发时间

- [x] 支持 MQTT/TCP/UDP 双通道透传（串口1和串口2分别对应两个透传通道）
- [x] 支持 MQTT/TCP/UDP 透传模式添加 IMEI 设备识别码(15个字节)
- [x] 支持 MQTT/TCP/UDP 多通道传输模式（非透传模式）
- [x] 支持 数据中心服务器设置，最多支持7个通道，每个通道可以任意指定串口（1,2）和协议
- [x] 支持 Luat云批量初始化配置，实现全自动无人操作自动配置DTU
- [x] 支持 Luat云远程升级固件，也就是FOAT功能，可以满足用户在某些新增功能需求的时候免现场维护
- [x] 支持 透传/非透传 模式软件恢复出厂默认值
- [x] 支持 硬件恢复出厂默认值
- [x] 支持 NET 指示灯，方便用户显示各种工作状态
- [x] 支持 登陆上传DTU模块状态，方便用户获得模块信息以及登陆鉴权
- [x] 支持 DTU配置程序读取
- [x] 支持 HTTP 的GET 和 POST 请求方法
- [x] 支持 获取网络时间
- [x] 支持 获取基站定位返回的当前模块坐标







## 四、发送数据说明：

### 4.1、透传通道报文

- 直接发送即可,串口1对应通道ID1，串口2对应通道ID2

### 4.2、多通道通信报文

- cmd ："send,id,data"

- code："send,1,data"


| 字段 | 值     | 含义                                            |
| ---- | ------ | ----------------------------------------------- |
| send | send   | 发送数据的标志位                                |
| id   | 1-7    | 通信使用的通道ID,串口通道会自动和对应的通道捆绑 |
| data | string | 要上传的串口数据                                |

### 4.3、单次 HTTP 指令

- cmd："http,method,url,timeout,body,type,basic"

- code："http,get,www.openluat.com,30"

| 字段    | 值        | 含义                                            |
| ------- | --------- | ----------------------------------------------- |
| HTTP    | http      | 通信方式http                                    |
| METHOD  | get-post  | 提交请求的方法                                  |
| URL     | 域名/参数 | HTTP请求的地址和参数,参数需要自己urlencode处理  |
| TIEMOUT | 30        | HTTP请求最长等待时间,超过这个时间,HTTP将返回    |
| BODY    | string    | get或者post提交的body内容，只能是字符串         |
| TYPE    | 1,2,3     | body的提交类型，1是urlencode,2是json，3是stream |
| BASIC   | usr:pwd   | HTTP的BASIC验证,注意账号密码之间用:连接         |
| HEAD    | string    | 自定义head部分, urlencode后的字符串             |

返回:	HTTP服务器返回的正文(body)透传该指令串口 

### 4.4、单次 SOCKET 指令

- cmd："tcp,host,port,ssl,timeout,data"

- code："tcp,180.97.80.55,12415,nossl,30,1122334455667788"

| 字段    | 值       | 含义                            |
| ------- | -------- | ------------------------------- |
| PROT    | TCP\|DUP | 通信协议,必填TCP或者UDP         |
| HOST    | 域名\|IP | SOCKET服务器地址                |
| PORT    | 1-65535  | SOCKET服务器端口号              |
| SSL     | ssl      | 是否ssl端口,默认空              |
| TIMEOUT | 30       | SOCKET服务器超时断开时间,单位秒 |
| DATA    | string   | 发给SOCKET服务器的数据          |

返回数据到对应串口:	

​	数据发送成功返回:	"SEND_OK\r\n"

​	数据发送失败返回:	"SEND_ERR\r\n"

​	数据接收成功返回:	透传服务器返回的数据

### 4.5、恢复出厂默认值指令

- - demo："+++"

- 重启模块并恢复出厂默认值

- 当串口配置错误的时候，可以用另外一个串口配置,也可以云端配置

### 4.6、读取DTU的参数配置

- demo："config,readconfig"
- demo :  "config,readconfig,1234567890"

## 五、API 指令功能说明：

### 5.1、基站定位功能：

- 发送："rrpc,getlocation"
- 返回："rrpc,location,lat,lng"
- 失败： ”ERROR"

### 5.2、实时基站定位功能

- 发送："rrpc,getreallocation"
- 返回："rrpc,getreallocation,lat,lng"
- 失败： ”rrpc,getreallocation,error"
### 5.3、NTP 对时功能：

​	此功能远程不可用

- 发送： "rrpc,gettime"
- 返回： "rrpc,nettime,year,month,day,hour,min,sec"
- 失败： “rrpc,nettime,error"

### 5.4、获取IMEI

- 发送： "rrpc,getimei"
- 返回:  "rrpc,getimei,123456789012345"
- 失败:  "ERROR"
  
### 5.5、获取ICCID

- 发送： "rrpc,geticcid"
- 返回：  "rrpc,geticcid,1234567890123456789"
- 失败： "ERROR"

### 5.6、获取CSQ

- 发送： "rrpc,getcsq"
- 返回： "rrpc,getcsq,17"
- 失败： "ERROR"

### 5,7、获取ADC的值

- 发送： "rrpc,getadc,id" 
- 例子： "rrpc,getadc,0" 
- 返回： "rrpc,getadc,1848"
- 失败： "ERROR"

### 5.8、获取GPIO的值

- 发送： "rrpc,getpio,pin"
- 例子： "rrpc,getpio,8"
- 返回： "rrpc,getpio8,1"
- 失败： "ERROR"
- 可用 GPIO 见手册底部GPIO列表

### 5.9、设置GPIO的值

- 发送： "rrpc,setpio,pin,val"
- 例子： "rrpc,setpio,8,1"
- 返回： "OK"
- 失败： "ERROR"
- 可用 GPIO 见手册底部GPIO列表

### 5.10、远程编程指令下发

- 发送： "rrpc,function,cmdString"
- 例子： "rrpc,function,print(1) return 'ok'"
- 返回： "rrpc,function,'ok"
- 失败： 返回错误代码

### 5.11、远程获取I2C温湿度传感器数据

- 发送： "rrpc,getSensor,addr"
- 例子： "rrpc,getam2320" 或 "rrpc,getam2320,0x5C"
- 例子： "rrpc,getsht" 或 "rrpc,getsht,0x40"
- 返回： "rrpc,getam2320,25.3,64.1"
- 注意：780e系列不支持该指令

### 5.12、远程唤醒GPS

- 发送： "rrpc,gps_wakeup"
- 返回： "rrpc,gps_wakeup,OK"

### 5.13、远程获取GPS设备信息

- 发送： "rrpc,gps_getsta,format"

- 例子： "rrpc,gps_getsta,json" 或 "rrpc,gps_getsta,hex"

- 返回： "rrpc,gps_getsta,{"sta":[true,false,false,false,false,false,65535,4113,15]}"

### 5.14、远程获取GPS定位信息

- 发送： "rrpc,getSensor,format"
- 例子： "rrpc,gps_getmsg,json" 或 "rrpc,gps_getmsg,hex"
- 返回： "rrpc, gps_getmsg, {"msg":[true,1547272715,1136036500,348579350,133,42,1,43,4]}"

### 5.15、远程重启模块

- 发送： "rrpc,reboot"

### 5.16、远程更新参数

- 发送： "rrpc,upconfig"
- 返回： "rrpc,upconfig,OK"

### 5.17、获取固件版本

- 发送： "rrpc,getver"
- 返回： "rrpc,getver,1.5.3"

### 5.18、获取项目名称

- 发送： "rrpc,getproject"
- 返回： "rrpc,getproject,DTU-AIR720-MODUL"

### 5.19、获取VBATT电压

- 发送： "rrpc,getvbatt"
- 返回： "rrpc,getvbatt,4200"

### 5.20、 播放TTS语音

- 发送： "rrpc,tts_play,gb2312,继电器被打开 请注意安全, 7"
- 返回： "rrpc,tts_play,OK"
- 注意：gb2312可选utf8,要播放的语音不能包含","(半角逗号),7可选1-7(TTS音量),780e系列不支持该指令

### 5.21、查询与服务器的链接状态

- 发送： "rrpc,netstatus"
- 返回1： "rrpc,netstatus,RDY"
- 返回2： "rrpc,netstatus,NORDY"
- 注释：返回1 表示与服务器连接成功，返回2表示与服务器连接断开

### 5.22、获取固件完整版本号(固件名称)
- 发送： "rrpc,getfwver"
- 返回： "rrpc,getver,iRTU_1.8.16_Luat_V0032_ASR1802_FLOAT_720"

### 5.23、获取当前4G网络状态
- 发送： "rrpc,getnetmode"
- 返回： "rrpc,getnetmode,"
- 返回值解释：
    - 0：未注册
    - 1：2G GSM网络
    - 2：2.5G EDGE数据网络
    - 3：3G TD网络
    - 4：4G LTE网络
    - 5：3G WCDMA网络

    EC618和EC718的返回内容为：
    - 0：未注册
    - 1：网络已注册
    - 2：正在搜网中
    - 3：网络注册被拒绝


### 5.24、查询与多个服务器的链接状态
- 发送 "rrpc,netstatus,1"
- 返回1： "rrpc,netstatus,RDY" 
- 返回2： "rrpc,netstatus,NORDY"

### 5.25、查询当前设备SN号
- 发送： "rrpc,getSN"
- 返回： "rrpc,getSN,123"
- 返回值解释： 123为设备的SN号

### 5.26、设置SN号
- 发送： "rrpc,setSN"
- 返回： "OK"
- 返回值解释：

### 5.27、关闭GPS
- 发送： "rrpc,gps_close" 
- 返回："rrpc,gps_close,ok"
- 返回值解释：

### 5.28、设置RNDIS状态
- 发送： "rrpc,setRNDIS,1"
- 1是打开，0是关闭
- 返回："OK"
- 返回值解释：
- 注意：780e系列不支持该命令

### 5.29、设置守护机制状态
- 发送： "rrpc,setchannel,1,2,3,4,5,6,7"
- 需要守护几路就填几路，守护全部可以直接rrpc,setchannel,all
- 返回："rrpc,setchannel,OK"
- 返回值解释：

### 5.30、切换SIM卡
- 发送： "rrpc,simcross,1"
- SIM卡为0就填0为1就填1，填2自动切换，该命令重启生效
- 返回："rrpc,setchannel,OK"
- 返回值解释：OK为正常，error为错误

### 5.31、发送短信
- 发送： "rrpc,sms_send,你好"
- 输入内容是发送信息内容
- 返回："ok"
- 返回值解释：ok为接收到串口指令返回的内容，后续信息发送成功会返回sms,ok，失败返回sms,error
- 注意：780e系列不支持该命令

### 5.32、关闭i2c
- 发送： "rrpc,iic_close,1"
- 1是i2c的接口id
- 返回："iic_close,ok,1"
- 返回值解释：ok为正常，error为错误
- 注意：780e系列不支持该命令

### 5.32、打开i2c
- 发送： "rrpc,iic_open,1,10000,0,1,1"
- 内容解释：1：i2c接口id,10000:时钟频率,0:可选,i2c外设地址,1:可选自定义波特率开关 0/1-关闭/开启,1：双字节寄存器配置开关 0/1-关闭/开启
- 返回："iic_open,ok,1"
- 返回值解释：ok为正常，error为错误
- 注意：780e系列不支持该命令

## 六、自动采集任务可用API

### 6.1、Luat API

- 参考 https://doc.openluat.com/wiki/21?wiki_page_id=2068

### 6.2、create库API

#### 6.2.1、实时查询基站定位

- local lat,lng = create.getRealLocation()
#### 6.2.2、获取纬度

- local lat = create.getLat()
#### 6.2.3、获取经度

- local lng = create.getLng()
#### 6.2.4、获取ADC的电压值

- local val = create.getADC(adcid)

### 6.3、tracker库的api

#### 6.3.1、 获取GPS的设备信息

- local str = tracker.locateMessage(format)
- format 为“json” or "hex"
#### 6.3.2、获取GPS设备信息

- local str = tracker.deviceMessage(format)
- format 为“json” or "hex"

## 七、Luat云功能说明

- 地址：<http://dtu.openluat.com>
- 借助Luat云可以实现远程FOTA和自动参数配置，用户无需用上位机配置程序来逐个配置DTU，此方式可以极大减少人工费用和时间。使用远程固件更新和远程参数下发需要用户注册Luat云,用户注册自己的IMEI到云端，指定不同的IMEI到对应的参数版本，DTU模块自动请求参数并保存到到DTU模块中存储。

- 远程固件更新

- 远程参数下发

## 八、硬件说明

### 8.1、Air202/208/800 硬件说明

#### 8.1.1、AIR202-GPIO

- 看门狗：
  - WDI —— 10脚 ( GPIO_31 )
  - RWD —— 11脚 ( GPIO_30 )

- NET_LED：
  - NET_LED —— 13脚 ( GPIO_33 )

- 重置参数：
  - RSP —— 12 脚（GPIO_29)

- 网络连接通知：
  - RDY —— 6脚（GPIO_3）

#### 8.1.2、485 控制脚 (UART1)

    RXD —— 9脚 (GPIO_0)
    TXD —— 8脚 (GPIO_1)
    DIR —— 7脚 (GPIO_2)

### 8.2、AIR720(S)/H/D/M/T/U 硬件说明

#### 8.2.1、AIR720-GPIO

- NET_LED：
  - NET_LED ——  PIN6 ( GPIO_64 )

- 重置参数：
  - RSP —— PIN4（GPIO_68）

- 网络连接通知：
  - RDY —— PIN5 （GPIO_65）


### 780E-GPIO
- NET_LED：
  - NET_LED —— 16脚 ( GPIO_27 )

- 重置参数：
  - RSP —— 78 脚（GPIO_28)

- 网络连接通知：
  - RDY —— 25脚（GPIO_26）

#### 8.2.2、 TTL 输出脚

    UART1_RXD —— PIN11 （GPIO_51）
    UART1_TXD —— PIN12 （GPIO_52）
    UART2_RXD —— PIN68 （GPIO_57）
    UART2_TXD —— PIN67 （GPIO_58）

    780E:TTL 输出脚

    UART1_RXD —— PIN17 （GPIO_18）
    UART1_TXD —— PIN18 （GPIO_19）
    UART2_RXD —— PIN28 （GPIO_10）
    UART2_TXD —— PIN29 （GPIO_11）

#### 8.2.3、 485 控制脚

    UART1_DIR —— PIN13 （GPIO_23） -- 720
    UART1_DIR —— PIN13 （GPIO_61） -- 720S
    
    UART2_DIR —— PIN64 （GPIO_59）-- 720
    UART2_DIR —— PIN64 （GPIO_31）-- 720S

### 8.3  720U/724U（RDA8910）硬件说明

#### 8.3.1、AIR720u-GPIO

- NET_LED：
  - NET_LED ——  ( GPIO_01 )

- 重置参数：
  - RSP —— （GPIO_3）

- 网络连接通知：
  - RDY —— （GPIO_04）

#### 8.3.2、 TTL 输出脚

    UART1_RXD 
    UART1_TXD
    UART2_RXD 
    UART2_TXD

#### 8.3.3、 485 控制脚

    UART1_DIR ——  （GPIO_18）
    UART2_DIR ——  （GPIO_23）

### 8.4、 LED 闪烁规则

    100ms 闪烁 —— 注册GSM
    500ms 闪烁 —— 附着GPRS
    100ms 亮, 1900ms 灭 —— 已连接到服务器

## 九、 附表可远程控制GPIO表

### 9.1、Air202表

| PIN | GPIO    | PIN | GPIO    |
| --- | ------- | --- | ------- |
| 29  | GPIO_6  | 5   | GPIO_12 |
| 30  | GPIO_7  | 11  | GPIO_30 |
| 3   | GPIO_8  | 10  | GPIO_31 |
| 2   | GPIO_10 | 4   | GPIO_11 |

### 9.2、Air800表

| PIN | GPIO    | PIN | GPIO    |
| --- | ------- | --- | ------- |
| 4   | GPIO_6  | 21  | GPIO_11 |
| 3   | GPIO_7  | 22  | GPIO_12 |
| 19  | GPIO_8  | 28  | GPIO_31 |
| 20  | GPIO_10 | 27  | GPIO_30 |
| 18  | GPIO_9  | 29  | GPIO_29 |
| 17  | GPIO_13 | 41  | GPIO_18 |
| 37  | GPIO_14 | 47  | GPIO_34 |
| 38  | GPIO_15 | 40  | GPIO_17 |
| 39  | GPIO_16 |     |         |

### 9.3、Air720系列表

| PIN | GPIO  | PIN | GPIO  |
| --- | ----- | --- | ----- |
| 26  | pio26 | 23  | pio70 |
| 25  | pio27 | 29  | pio71 |
| 24  | pio28 | 28  | pio72 |
| 39  | pio33 | 33  | pio73 |
| 40  | pio34 | 32  | pio74 |
| 38  | pio35 | 30  | pio75 |
| 37  | pio36 | 31  | pio76 |
| 65  | pio55 | 66  | pio77 |
| 62  | pio56 | 63  | pio78 |
| 1   | pio62 | 61  | pio79 |
| 2   | pio63 | 113 | pio80 |
| 115 | pio69 | 114 | pio81 |

## 9.3、Air 724表

| PIN  | GPIO   | PIN  | GPIO            |
| ---- | ------ | ---- | --------------- |
| 52   | GPIO9  | 43   | GPIO13          |
| 54   | GPIO10 | 32   | GPIO14(I2C_SCL) |
| 53   | GPIO12 | 31   | GPIO15(I2C_SDA) |
| 50   | GPIO17 | 38   | GPIO18          |
| 37   | GPIO19 |      |                 |

### **Air780系列表**

| PIN  | GPIO  | PIN  | GPIO  |
| ---- | ----- | ---- | ----- |
| 49   | pio1  | 107  | pio21 |
| 21   | pio2  | 19   | pio22 |
| 54   | pio3  | 99   | pio23 |
| 80   | pio4  | 20   | pio24 |
| 81   | pio5  | 106  | pio25 |
| 55   | pio6  | 25   | pio26 |
| 56   | pio7  | 16   | pio27 |
| 52   | pio8  | 78   | pio28 |
| 50   | pio9  | 30   | pio29 |
| 22   | pio16 | 31   | pio30 |
| 23   | pio17 | 32   | pio31 |
| 102  | pio20 |      |       |
