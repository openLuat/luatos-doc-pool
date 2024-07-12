
@[TOC]

# gpsZkw

模块功能：GPS模块管理

注意：此功能模块中的功能接口可以分为四大类：

1、GPS开启

2、GPS关闭

3、GPS定位数据读取

4、GPS参数和功能设置

1、2、3是通用功能，除了支持合宙的Air530Z和Air82X系列模块，理论上也支持其他厂家的串口GPS模块

4是专用功能，仅支持合宙的Air530Z和Air82X系列模块

### gpsZkw.DEFAULT

常量值，GPS应用模式1.



打开GPS后，GPS定位成功时，如果有回调函数，会调用回调函数



使用此应用模式调用gpsZkw.open打开的“GPS应用”，必须主动调用gpsZkw.close或者gpsZkw.closeAll才能关闭此“GPS应用”,主动关闭时，即使有回调函数，也不会调用回调函数

---

### gpsZkw.TIMERORSUC

常量值，GPS应用模式2.



打开GPS后，如果在GPS开启最大时长到达时，没有定位成功，如果有回调函数，会调用回调函数，然后自动关闭此“GPS应用”



打开GPS后，如果在GPS开启最大时长内，定位成功，如果有回调函数，会调用回调函数，然后自动关闭此“GPS应用”



打开GPS后，在自动关闭此“GPS应用”前，可以调用gpsZkw.close或者gpsZkw.closeAll主动关闭此“GPS应用”，主动关闭时，即使有回调函数，也不会调用回调函数

---

### gpsZkw.TIMER

常量值，GPS应用模式3.



打开GPS后，在GPS开启最大时长时间到达时，无论是否定位成功，如果有回调函数，会调用回调函数，然后自动关闭此“GPS应用”



打开GPS后，在自动关闭此“GPS应用”前，可以调用gpsZkw.close或者gpsZkw.closeAll主动关闭此“GPS应用”，主动关闭时，即使有回调函数，也不会调用回调函数

---

## gpsZkw.open(mode, para)

打开一个“GPS应用”

“GPS应用”：指的是使用GPS功能的一个应用<br>例如，假设有如下3种需求，要打开GPS，则一共有3个“GPS应用”：<br>“GPS应用1”：每隔1分钟打开一次GPS<br>“GPS应用2”：设备发生震动时打开GPS<br>“GPS应用3”：收到一条特殊短信时打开GPS<br>只有所有“GPS应用”都关闭了，才会去真正关闭GPS<br>每个“GPS应用”打开或者关闭GPS时，最多有4个参数，其中 GPS应用模式和GPS应用标记 共同决定了一个唯一的“GPS应用”：<br>1、GPS应用模式(必选)<br>2、GPS应用标记(必选)<br>3、GPS开启最大时长[可选]<br>4、回调函数[可选]<br>例如gpsZkw.open(gpsZkw.TIMERORSUC,{tag="TEST",val=120,cb=testGpsCb})<br>gpsZkw.TIMERORSUC为GPS应用模式，"TEST"为GPS应用标记，120秒为GPS开启最大时长，testGpsCb为回调函数

* 参数

|名称|传入值类型|释义|
|-|-|-|
|mode|number|GPS应用模式，支持gpsZkw.DEFAULT，gpsZkw.TIMERORSUC，gpsZkw.TIMER三种|
|para|param|table类型，GPS应用参数<br>para.tag：string类型，GPS应用标记<br>para.val：number类型，GPS应用开启最大时长，mode参数为gpsZkw.TIMERORSUC或者gpsZkw.TIMER时，此值才有意义<br>para.cb：GPS应用结束时的回调函数，回调函数的调用形式为para.cb(para.tag)|

* 返回值

nil

* 例子

```lua
gpsZkw.open(gpsZkw.DEFAULT,{tag="TEST1",cb=test1Cb})
gpsZkw.open(gpsZkw.TIMERORSUC,{tag="TEST2",val=60,cb=test2Cb})
gpsZkw.open(gpsZkw.TIMER,{tag="TEST3",val=120,cb=test3Cb})
--另见：DEFAULT,TIMERORSUC,TIMER
```

---

## gpsZkw.close(mode, para)

关闭一个“GPS应用”

只是从逻辑上关闭一个GPS应用，并不一定真正关闭GPS，是有所有的GPS应用都处于关闭状态，才会去真正关闭GPS

* 参数

|名称|传入值类型|释义|
|-|-|-|
|mode|number|GPS应用模式，支持gps.DEFAULT，gps.TIMERORSUC，gps.TIMER三种|
|para|param|table类型，GPS应用参数<br>para.tag：string类型，GPS应用标记<br>para.val：number类型，GPS应用开启最大时长，mode参数为gps.TIMERORSUC或者gps.TIMER时，此值才有意义；使用close接口时，不需要传入此参数<br>para.cb：GPS应用结束时的回调函数，回调函数的调用形式为para.cb(para.tag)；使用close接口时，不需要传入此参数|

* 返回值

nil

* 例子

```lua
GPS应用模式和GPS应用标记唯一确定一个“GPS应用”，调用本接口关闭时，mode和para.tag要和gpsZkw.open打开一个“GPS应用”时传入的mode和para.tag保持一致
gpsZkw.close(gpsZkw.DEFAULT,{tag="TEST1"})
gpsZkw.close(gpsZkw.TIMERORSUC,{tag="TEST2"})
gpsZkw.close(gpsZkw.TIMER,{tag="TEST3"})
--另见：open,DEFAULT,TIMERORSUC,TIMER
```

---

## gpsZkw.closeAll()

关闭所有“GPS应用”

* 参数

无

* 返回值

nil

* 例子

```lua
gpsZkw.closeAll()
--另见：open,DEFAULT,TIMERORSUC,TIMER
```

---

## gpsZkw.isActive(mode, para)

判断一个“GPS应用”是否处于激活状态

* 参数

|名称|传入值类型|释义|
|-|-|-|
|mode|number|GPS应用模式，支持gps.DEFAULT，gps.TIMERORSUC，gps.TIMER三种|
|para|param|table类型，GPS应用参数<br>para.tag：string类型，GPS应用标记<br>para.val：number类型，GPS应用开启最大时长，mode参数为gpsZkw.TIMERORSUC或者gpsZkw.TIMER时，此值才有意义；使用isActive接口时，不需要传入此参数<br>para.cb：GPS应用结束时的回调函数，回调函数的调用形式为para.cb(para.tag)；使用isActive接口时，不需要传入此参数|

* 返回值

bool result，处于激活状态返回true，否则返回nil

* 例子

```lua
GPS应用模式和GPS应用标记唯一确定一个“GPS应用”，调用本接口查询状态时，mode和para.tag要和gpsZkw.open打开一个“GPS应用”时传入的mode和para.tag保持一致
gpsZkw.isActive(gpsZkw.DEFAULT,{tag="TEST1"})
gpsZkw.isActive(gpsZkw.TIMERORSUC,{tag="TEST2"})
gpsZkw.isActive(gpsZkw.TIMER,{tag="TEST3"})
--另见：open,DEFAULT,TIMERORSUC,TIMER
```

---

## gpsZkw.setPowerCbFnc(cbFnc)

设置GPS模块供电控制的回调函数

如果使用的是Air800，或者供电控制使用的是LDO_VCAM，则打开GPS应用前不需要调用此接口进行设置<br>否则在调用gpsZkw.open前，使用此接口，传入自定义的供电控制函数cbFnc，GPS开启时，gpsZkw.lua自动执行cbFnc(true)，GPS关闭时，gpsZkw.lua自动执行cbFnc(false)

* 参数

|名称|传入值类型|释义|
|-|-|-|
|cbFnc|param|function类型，用户自定义的GPS供电控制函数|

* 返回值

nil

* 例子

```lua
gpsZkw.setPowerCbFnc(cbFnc)
```

---

## gpsZkw.setUart(id, baudrate, databits, parity, stopbits)

设置GPS模块和GSM模块之间数据通信的串口参数

如果使用的是Air800，或者使用的UART2(波特率115200，数据位8，无检验位，停止位1)，则打开GPS应用前不需要调用此接口进行设置<br>否则在调用gpsZkw.open前，使用此接口，传入UART参数

* 参数

|名称|传入值类型|释义|
|-|-|-|
|id UART|number|ID，支持1和2，1表示UART1，2表示UART2|
|baudrate|number|波特率，支持1200,2400,4800,9600,10400,14400,19200,28800,38400,57600,76800,115200,230400,460800,576000,921600,1152000,4000000|
|databits|number|数据位，支持7,8|
|parity|number|校验位，支持uart.PAR_NONE,uart.PAR_EVEN,uart.PAR_ODD|
|stopbits|number|停止位，支持uart.STOP_1,uart.STOP_2|

* 返回值

nil

* 例子

```lua
gpsZkw.setUart(2,115200,8,uart.PAR_NONE,uart.STOP_1)
```

---

## gpsZkw.setAerialMode(gps, beidou, glonass)

设置GPS模块搜星模式.

如果使用的是Air820，不调用此接口配置，则默认同时开启GPS、北斗和glonass定位

* 参数

|名称|传入值类型|释义|
|-|-|-|
|gps|number|GPS定位系统，1是打开，0是关闭|
|beidou|number|中国北斗定位系统，1是打开，0是关闭|
|glonass|number|俄罗斯Glonass定位系统，1是打开，0是关闭|

* 返回值

nil

* 例子

```lua
gpsZkw.setAeriaMode(1,1,0)
```

---

## gpsZkw.setNmeaMode(mode, cbFnc)

设置NMEA数据处理模式.

如果不调用此接口配置，则默认仅gpsZkw.lua内部处理NMEA数据

* 参数

|名称|传入值类型|释义|
|-|-|-|
|mode|number|NMEA数据处理模式，0表示仅gpsZkw.lua内部处理，1表示仅用户自己处理，2表示gpsZkw.lua和用户同时处理|
|cbFnc|param|function类型，用户处理一条NMEA数据的回调函数，mode为1和2时，此值才有意义|

* 返回值

nil

* 例子

```lua
gpsZkw.setNmeaMode(0)
gpsZkw.setNmeaMode(1,cbFnc)
gpsZkw.setNmeaMode(2,cbFnc)
```

---

## gpsZkw.setNemaReportFreq(rmc, gga, gsa, gsv, vtg, gll)

设置NEMA语句的输出频率.

* 参数

|名称|传入值类型|释义|
|-|-|-|
|rmc|number|**可选参数，默认为`1`** 单位秒，RMC语句输出频率，取值范围0到9之间的整数，0表示不输出|
|gga|number|**可选参数，默认为`1`** 单位秒，GGA语句输出频率，取值范围0到9之间的整数，0表示不输出|
|gsa|number|**可选参数，默认为`1`** 单位秒，GSA语句输出频率，取值范围0到9之间的整数，0表示不输出|
|gsv|number|**可选参数，默认为`1`** 单位秒，GSV语句输出频率，取值范围0到9之间的整数，0表示不输出|
|vtg|number|**可选参数，默认为`0`** 单位秒，VTG语句输出频率，取值范围0到9之间的整数，0表示不输出|
|gll|number|**可选参数，默认为`0`** 单位秒，GLL语句输出频率，取值范围0到9之间的整数，0表示不输出|

* 返回值

nil

* 例子

```lua
gpsZkw.setNemaReportFreq(5,0,0,0,0,0)
```

---

## gpsZkw.setLocationFilter(seconds)

设置GPS定位成功后经纬度的过滤时间.

* 参数

|名称|传入值类型|释义|
|-|-|-|
|seconds|number|**可选参数，默认为`0`** 单位秒，GPS定位成功后，丢弃前seconds秒的位置信息|

* 返回值

nil

* 例子

```lua
gpsZkw.setLocationFilter(2)
```

---

## gpsZkw.isOpen()

获取GPS模块是否处于开启状态

* 参数

无

* 返回值

bool result，true表示开启状态，false或者nil表示关闭状态

* 例子

```lua
gpsZkw.isOpen()
```

---

## gpsZkw.isFix()

获取GPS模块是否定位成功

* 参数

无

* 返回值

bool result，true表示定位成功，false或者nil表示定位失败

* 例子

```lua
gpsZkw.isFix()
```

---

## gpsZkw.isOnece()

获取GPS模块是否首次定位成功过

* 参数

无

* 返回值

bool result，true表示曾经定位成功

* 例子

```lua
gpsZkw.isOnece()
```

---

## gpsZkw.getLocation(typ)

获取度格式的经纬度信息

* 参数

|名称|传入值类型|释义|
|-|-|-|
|typ|string|**可选参数，默认为`nil`** 返回的经纬度格式，typ为"DEGREE_MINUTE"时表示返回度分格式，其余表示返回度格式|

* 返回值

table location<br>例如typ为"DEGREE_MINUTE"时返回{lngType="E",lng="12128.44954",latType="N",lat="3114.50931"}<br>例如typ不是"DEGREE_MINUTE"时返回{lngType="E",lng="121.123456",latType="N",lat="31.123456"}<br>lngType：string类型，表示经度类型，取值"E"，"W"<br>lng：string类型，表示度格式的经度值，无效时为""<br>latType：string类型，表示纬度类型，取值"N"，"S"<br>lat：string类型，表示度格式的纬度值，无效时为""

* 例子

```lua
gpsZkw.getLocation()
```

---

## gpsZkw.getAltitude()

获取海拔

* 参数

无

* 返回值

number altitude，海拔，单位米

* 例子

```lua
gpsZkw.getAltitude()
```

---

## gpsZkw.getSpeed()

获取速度

* 参数

无

* 返回值

number kmSpeed，第一个返回值为公里每小时的速度
number nmSpeed，第二个返回值为海里每小时的速度

* 例子

```lua
gpsZkw.getSpeed()
```

---

## gpsZkw.getOrgSpeed()

获取原始速度,字符串带浮点

* 参数

无

* 返回值

number speed 海里每小时的速度

* 例子

```lua
gpsZkw.getOrgSpeed()
```

---

## gpsZkw.getCourse()

获取方向角

* 参数

无

* 返回值

number course，方向角

* 例子

```lua
gpsZkw.getCourse()
```

---

## gpsZkw.getViewedSateCnt()

获取可见卫星的个数

* 参数

无

* 返回值

number count，可见卫星的个数

* 例子

```lua
gpsZkw.getViewedSateCnt()
```

---

## gpsZkw.getUsedSateCnt()

获取定位使用的卫星个数

* 参数

无

* 返回值

number count，定位使用的卫星个数

* 例子

```lua
gpsZkw.getUsedSateCnt()
```

---

## gpsZkw.getGgaloc()

获取GGA语句中度分格式的经纬度信息

* 参数

无

* 返回值

string lng，度分格式的经度值(dddmm.mmmm)，西经会添加一个-前缀，无效时为""；例如"12112.3456"表示东经121度12.3456分，"-12112.3456"表示西经121度12.3456分
string lat，度分格式的纬度值(ddmm.mmmm)，南纬会添加一个-前缀，无效时为""；例如"3112.3456"表示北纬31度12.3456分，"-3112.3456"表示南纬31度12.3456分

* 例子

```lua
gpsZkw.getGgaloc()
```

---

## gpsZkw.getUtcTime()

获取RMC语句中的UTC时间

只有同时满足如下两个条件，返回值才有效<br>1、开启了GPS，并且定位成功<br>2、调用setParseItem接口，第一个参数设置为true

* 参数

无

* 返回值

table utcTime，UTC时间，nil表示无效，例如{year=2018,month=4,day=24,hour=11,min=52,sec=10}

* 例子

```lua
gpsZkw.getUtcTime()
```

---

## gpsZkw.getSep()

获取定位使用的大地高

* 参数

无

* 返回值

number sep，大地高

* 例子

```lua
gpsZkw.getSep()
```

---

## gpsZkw.getSateSn()

获取GSA语句中的可见卫星号

只有同时满足如下两个条件，返回值才有效<br>1、开启了GPS，并且定位成功<br>2、调用setParseItem接口，第三个参数设置为true

* 参数

无

* 返回值

string viewedSateId，可用卫星号，""表示无效

* 例子

```lua
gpsZkw.getSateSn()
```

---

## gpsZkw.getGsv()

获取GSV语句中的可见卫星的信噪比

只有同时满足如下两个条件，返回值才有效<br>1、开启了GPS，并且定位成功<br>2、调用setParseItem接口，第二个参数设置为true

* 参数

无

* 返回值

string gsv，信噪比

* 例子

```lua
gpsZkw.getGsv()
```

---

## gpsZkw.setParseItem(utcTime, gsv, gsaId)

设置是否需要解析的字段

* 参数

|名称|传入值类型|释义|
|-|-|-|
|utcTime|bool|**可选参数，默认为`nil`** 是否解析RMC语句中的UTC时间，true表示解析，false或者nil不解析|
|gsv|bool|**可选参数，默认为`nil`** 是否解析GSV语句，true表示解析，false或者nil不解析|
|gsaId|bool|**可选参数，默认为`nil`** 是否解析GSA语句中的卫星ID，true表示解析，false或者nil不解析|

* 返回值

无

* 例子

```lua
gpsZkw.setParseItem(true,true,true)
```

---
