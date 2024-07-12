@[TOC](目录名称)

## aLiYun


| 消息ID | 消息参数 | 消息说明 |
| --- | --- |--- |
| "GetDeviceSecretEnd"| 无 |一型一密模式下，注册获取到设备密钥 |
| "ALIYUN_AUTH_IND"|1、result：bool类型，true表示收到了完整的鉴权应答；false或者nil表示没有收到<br/>2、statusCode：string类型，鉴权应答的http状态码<br/>3、body：string类型，鉴权应答的http body数据  | 一型一密或者一机一密模式下，http鉴权请求的应答结果消息|



## aLiYunOta


| 消息ID | 消息参数 | 消息说明 |
| --- | --- |--- |
| "LIB_ALIYUN_OTA_DOWNLOAD_BEGIN"| 1、ver：string类型，差分包的版本号 |开始下载差分包 |
| "ALIYUN_OTA_DOWNLOAD_IND"| 1、result：bool类型，true表示下载成功；false或者nil表示下载失败 |差分包下载结束通知 |




## cc
| 消息ID | 消息参数 | 消息说明 |
| --- | --- |--- |
| "CALL_READY"| 无 |通话环境准备就绪，可以发起通话了|
| "CALL_INCOMING"| 1、num：string类型，呼入号码 |来电呼入|
| "CALL_CONNECTED"| 1、num：string类型，建立通话的对方号码 |通话已建立|
| "CALL_DTMF_DETECT"| 1、dtmf：string类型，dtmf字符 |检测到DTMF字符|
| "CALL_DISCONNECTED"|1、disconnecReason：string类型，通话断开原因，取值如下：<br>"CHUP"表示本端调用cc.hungUp()接口主动挂断<br>"NO ANSWER"表示呼出后，到达对方，对方无应答，通话超时断开 or data=="BUSY"<br>"BUSY"表示呼出后，到达对方，对方主动挂断<br>"NO CARRIER"表示通话未建立或者其他未知原因的断开<br>nil表示没有检测到原因值|通话已断开|


## gps
| 消息ID | 消息参数 | 消息说明 |
| --- | --- |--- |
| "GPS_STATE"|1、state：string类型，gps状态"<br/>"OPEN"：gps开启<br/>"CLOSE"：gps关闭 <br/>"LOCATION_SUCCESS"：定位成功<br/>"LOCATION_FAIL"：定位失败<br/>"LOCATION_FILTER"：定位成功前过滤位置点 | gps状态消息|




## gpsZkw
| 消息ID | 消息参数 | 消息说明 |
| --- | --- |--- |
| "GPS_STATE"|1、state：string类型，gps状态"<br/>"OPEN"：gps开启<br/>"CLOSE"：gps关闭 <br/>"LOCATION_SUCCESS"：定位成功<br/>"LOCATION_FAIL"：定位失败<br/>"LOCATION_FILTER"：定位成功前过滤位置点 | gps状态消息|





## link
| 消息ID | 消息参数 | 消息说明 |
| --- | --- |--- |
| "GPRS_ATTACH"| 1、state：bool类型，true表示附着成功；false或者nil表示附着失败 |数据网络附着|
| "IP_READY_IND"| 无 |PDP激活成功，IP网络准备就绪|
| "IP_ERROR_IND"| 无 |IP网络异常|


## misc
| 消息ID | 消息参数 | 消息说明 |
| --- | --- |--- |
| "IMEI_READY_IND"|无 |IMEI初始化完成|
| "SN_RAEDY_IND"| 无 |SN初始化完成|
| "TIME_UPDATE_IND"| 无 |模块时间更新|


## net
| 消息ID | 消息参数 | 消息说明 |
| --- | --- |--- |
| "NET_STATE_REGISTERED"|无 |网络注册成功|
| "NET_STATE_UNREGISTER"| 无 |网络注册失败|
| "NET_CELL_CHANGED"| 无 |驻留的小区发生变化|
| "NET_UPD_NET_MODE"| 无 |网络模式发生变化；例如从2G切换为4G，从4G切换为2G|
| "FLYMODE"| 1、flyMode：bool类型，true表示进入飞行模式；false或者nil表示退出飞行模式 |飞行模式发生变化|



## ntp
| 消息ID | 消息参数 | 消息说明 |
| --- | --- |--- |
| "NTP_SUCCEED"|无 |ntp时间同步成功|


## nvm
| 消息ID | 消息参数 | 消息说明 |
| --- | --- |--- |
| "PARA_CHANGED_IND"|1、k：string类型，nvm存储参数的key值<br/>2、v：nvm存储参数的value值<br/>3、r：nvm存储参数发生改变的原因值 |nvm中存储的某一个非table类型的参数发生改变|
| "TPARA_CHANGED_IND"|1、k：string类型，nvm存储参数的key值<br/>2、kk：nvm存储参数的key值中对应的索引<br/>3、v：nvm存储参数的value值<br/>4、r：nvm存储参数发生改变的原因值 |nvm中存储的某一个table类型的参数发生改变|



## sim
| 消息ID | 消息参数 | 消息说明 |
| --- | --- |--- |
| "SIM_IND"|1、state：string类型，sim卡状态<br/>"RDY"：正常就绪<br/>"NIST"：未检测到 <br/>"SIM_PIN"：锁PIN码<br/>"NORDY"：其他异常 | sim状态发生改变|



## update
| 消息ID | 消息参数 | 消息说明 |
| --- | --- |--- |
| "LIB_UPDATE_OTA_DOWNLOAD_BEGIN"|无 |开始下载差分升级包|
| "LIB_UPDATE_OTA_DOWNLOAD_END"| 1、result：bool类型，true表示下载成功；false或者nil表示下载失败 |差分升级包下载结束|

## socket

|消息ID|消息参数|消息说明|
|---| --- | --- |
|SOCKET_ACTIVE|1、connected：bool类型，true表示有socket整处在连接，false代表没有socket处于连接|是否有socket正处在链接|
|LIB_SOCKET_CONNECT_FAIL_IND|1、ssl：bool类型，true代表是ssl，false代表不是。2、protocol：string类型，代表是什么连接，"UDP","TCP","TCPSSL"。3、address：string类型，服务器地址。4、port int类型：服务器端口|连接失败主动上报|
|LIB_SOCKET_CLOSE_IND|1、ssl：bool类型，true代表是ssl，false代表不是。2、protocol：string类型，代表是什么连接，"UDP","TCP","TCPSSL"。3、address：string类型，服务器地址。4、port int类型：服务器端口|主动关闭上报|
|SOCKET_ASYNC_SEND|1、result：bool类型 异步发送结果|异步发送接口上报|
|LIB_SOCKET_SEND_FAIL_IND|1、ssl：bool类型，true代表是ssl，false代表不是。2、protocol：string类型，代表是什么连接，"UDP","TCP","TCPSSL"。3、address：string类型，服务器地址。4、port int类型：服务器端口|lib库发送结果主动上报|
|SOCKET_RECV|1、socket_index：int类型，socket的索引|收到数据异步通知|
|SOCKET_SEND|1、sockek_id：int类型，socket的发送通道|异步发送上报|

