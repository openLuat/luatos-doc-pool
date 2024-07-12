
@[TOC]

# misc

模块功能：配置管理-序列号、IMEI、底层软件版本号、时钟、是否校准、飞行模式、查询电池电量等功能

## misc.getVersion()

获取core固件名

* 参数

无

* 返回值

string version，core固件名

* 例子

```lua
local version = misc.getVersion()
-- 如果core为Luat_V0026_RDA8910_TTS_FLOAT，则version为string类型的"Luat_V0026_RDA8910_TTS_FLOAT"
```

---

## misc.setClock(t, cbFnc)

设置系统时间

* 参数

|名称|传入值类型|释义|
|-|-|-|
|t|table|系统时间，格式参考：{year=2017,month=2,day=14,hour=14,min=2,sec=58}|
|cbFnc|function|**可选参数，默认为`nil`** 设置结果回调函数，回调函数的调用形式为：<br>cbFnc(time，result)<br>result为true表示成功，false或者nil为失败<br>time表示设置之后的系统时间，table类型，例如{year=2017,month=2,day=14,hour=14,min=19,sec=23}|

* 返回值

nil

* 例子

```lua
misc.setClock({year=2017,month=2,day=14,hour=14,min=2,sec=58})
```

---

## misc.getClock()

获取系统时间

* 参数

无

* 返回值

table time,{year=2017,month=2,day=14,hour=14,min=19,sec=23}

* 例子

```lua
time = getClock()
```

---

## misc.getWeek()

获取星期

* 参数

无

* 返回值

number week，1-7分别对应周一到周日

* 例子

```lua
week = misc.getWeek()
```

---

## misc.getCalib()

获取校准标志

* 参数

无

* 返回值

bool calib, true表示已校准，false或者nil表示未校准

* 例子

```lua
calib = misc.getCalib()
```

---

## misc.getAnt()

获取耦合测试标志

* 参数

无

* 返回值

bool ant, true表示已耦合测试，false或者nil表示未耦合测试

* 例子

```lua
ant = misc.getAnt()
```

---

## misc.setSn(s, cbFnc)

设置SN

* 参数

|名称|传入值类型|释义|
|-|-|-|
|s|string|新sn的字符串|
|cbFnc|function|**可选参数，默认为`nil`** 设置结果回调函数，回调函数的调用形式为：<br>cnFnc(result)，result为true表示成功，false或者nil为失败|

* 返回值

nil

* 例子

```lua
misc.setSn("1234567890")
misc.setSn("1234567890",cbFnc)
```

---

## misc.getSn()

获取模块序列号

* 参数

无

* 返回值

string sn,序列号，如果未获取到返回""<br>注意：开机lua脚本运行之后，会发送at命令去查询sn，所以需要一定时间才能获取到sn。开机后立即调用此接口，基本上返回""

* 例子

```lua
sn = misc.getSn()
```

---

## misc.setImei(s, cbFnc)

设置IMEI

* 参数

|名称|传入值类型|释义|
|-|-|-|
|s|string|新IMEI字符串|
|cbFnc|function|**可选参数，默认为`nil`** 设置结果回调函数，回调函数的调用形式为：<br>cnFnc(result)，result为true表示成功，false或者nil为失败|

* 返回值

nil

* 例子

```lua
misc.setImei(”359759002514931”)
```

---

## misc.getImei()

获取模块IMEI

* 参数

无

* 返回值

string,IMEI号，如果未获取到返回""<br>注意：开机lua脚本运行之后，会发送at命令去查询imei，所以需要一定时间才能获取到imei。开机后立即调用此接口，基本上返回""

* 例子

```lua
imei = misc.getImei()
```

---

## misc.getModelType()

获取模块型号

* 参数

无

* 返回值

string,模块型号，如果未获取到返回""<br>例如：模块型号为724UG,则返回值为Air724UG;模块型号为722UG,则返回值为Air722UG;模块型号为820UG,则返回值为Air820UG<br>注意：开机lua脚本运行之后，会发送at命令去查询模块型号，所以需要一定时间才能获取到模块型号。开机后立即调用此接口，基本上返回""

* 例子

```lua
modeltype = getModelType()
```

---

## misc.getVbatt()

获取VBAT的电池电压

* 参数

无

* 返回值

number,电池电压,单位mv

* 例子

```lua
vb = getVbatt()
```

---

## misc.getVbus()

获取VBUS连接状态

* 参数

无

* 返回值

boolean，true表示VBUS连接，false表示未连接

* 例子

```lua
vbus = getVbus()
```

---

## misc.getMuid()

获取模块MUID

* 参数

无

* 返回值

string,MUID号，如果未获取到返回""<br>注意：开机lua脚本运行之后，会发送at命令去查询muid，所以需要一定时间才能获取到muid。开机后立即调用此接口，基本上返回""

* 例子

```lua
muid = misc.getMuid()
```

---

## misc.openPwm(id, para1, para2)

打开并且配置PWM(支持2路PWM，仅支持输出)

* 参数

|名称|传入值类型|释义|
|-|-|-|
|id|number|PWM输出通道，仅支持0和1<br>0使用MODULE_STATUS/GPIO_5引脚<br>1使用GPIO_13引脚，注意：上电的时候不要把 GPIO_13 拉高到V_GLOBAL_1V8，否则模块会进入校准模式，不正常开机|
|para1|number|当id为0时，para1表示分频系数，最大值为2047；分频系数和频率的换算关系为：频率=25000000/para1（Hz）；例如para1为500时，频率为50000Hz<br>分频系数和周期的换算关系为：周期=para1/25000000（ｓ）；例如para1为500时，周期为20ｕｓ<br>当id为1时，para1表示时钟周期，取值范围为0-7，仅支持整数<br>0-7分别对应125、250、500、1000、1500、2000、2500、3000毫秒|
|para2|number|当id为0时，para2表示占空比计算系数，最大值为1023；占空比计算系数和占空比的计算关系为：占空比=para2/para1<br>当id为1时，para2表示一个时钟周期内的高电平时间，取值范围为1-15，仅支持整数<br>1-15分别对应15.6、31.2、46.8、62、78、94、110、125、140、156、172、188、200、218、234毫秒|

* 返回值

nil

* 例子

```lua
-- 通道0，频率为50000Hz，占空比为0.2：
-- 频率为50000Hz，表示时钟周期为1/50000=0.00002秒=0.02毫秒=20微秒  
-- 占空比表示在一个时钟周期内，高电平的时长/时钟周期的时长，本例子中的0.2就表示，高电平时长为4微秒，低电平时长为16微秒
misc.openPwm(0,500,100)
-- 通道1，时钟周期为500ms，高电平时间为125毫秒：
misc.openPwm(1,2,8)
```

---

## misc.closePwm(id)

关闭PWM

* 参数

|名称|传入值类型|释义|
|-|-|-|
|id|number|PWM输出通道，仅支持0和1<br>0使用MODULE_STATUS/GPIO_5引脚<br>1使用GPIO_13引脚，注意：上电的时候不要把 GPIO_13 拉高到V_GLOBAL_1V8，否则模块会进入校准模式，不正常开机|

* 返回值

nil

* 例子

无

---
