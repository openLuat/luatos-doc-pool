@[TOC]

# pmd
电源管理接口 ldo 控制,省电管理
## pmd.init({})

pmd初始化

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|{}|table|初始化配置，参数直接传入一个空表{}|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|1/0 1：表示成功，0：表示失败|  |

**例子**

```lua
    rtos.on(rtos.MSG_PMD,function(msg)
    if msg then
        --msg.voltage：number类型，vbat端的电池电压，单位毫伏
        --msg.level：vbat端电池电量百分比，core按照线性比例，计算出来的一个百分比，值为(msg.voltage-3400)*100/(4200-3400)
        --           如果满足不了自己的需求，可以根据msg.voltage自行计算百分比
        --msg.charger：usb vbus连接状态，true为连接，false为未连接
        --msg.state：充电状态，因Cat.1模块内部不支持充电管理功能，故此值无意义
        log.info("rtos.MSG_PMD",msg.level,msg.voltage,msg.charger,msg.state)
        
        --当level为255时，表示此条消息无意义，直接丢弃，不要做任何处理
        if msg.level==255 then return end
        
        --TODO：此处添加自己的业务逻辑代码
        
    end
end)
--初始化配置，参数直接传入一个空表{}
pmd.init({})

```

---



## pmd.ldoset(level,id1,[id2],...[idn])

ldo控制

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|level|number|ldo 亮度|取值范围0-15|
|id1|number|要设置的第一个 ldo|取值pmd.LDO_VLCD/pmd.LDO_VMMC/pmd.LDO_VSIM1/pmd.LDO_VCAMA/pmd.LDO_VCAMD/pmd.LDO_VBACKLIGHT_R/pmd.LDO_VBACKLIGHT_G/pmd.LDO_VBACKLIGHT_B/pmd.LDO_VBACKLIGHT_W/pmd.LDO_HMICBIAS/pmd.LDO_FLASHIB|
|id2|number|要设置的第二个 ldo|取值pmd.LDO_VLCD/pmd.LDO_VMMC/pmd.LDO_VSIM1/pmd.LDO_VCAMA/pmd.LDO_VCAMD/pmd.LDO_VBACKLIGHT_R/pmd.LDO_VBACKLIGHT_G/pmd.LDO_VBACKLIGHT_B/pmd.LDO_VBACKLIGHT_W/pmd.LDO_HMICBIAS/pmd.LDO_FLASHIB|
|idn|number|要设置的第一个 ldo|取值pmd.LDO_VLCD/pmd.LDO_VMMC/pmd.LDO_VSIM1/pmd.LDO_VCAMA/pmd.LDO_VCAMD/pmd.LDO_VBACKLIGHT_R/pmd.LDO_VBACKLIGHT_G/pmd.LDO_VBACKLIGHT_B/pmd.LDO_VBACKLIGHT_W/pmd.LDO_HMICBIAS/pmd.LDO_FLASHIB|

**返回值**

无

**例子**

```lua
--[[ 
一旦设置了某一个电压域的电压等级，受该电压域控制的所有GPIO的高电平都与设置的电压等级一致
LDO_VLCD
LDO_VSIM1
LDO_VCAMA	
level范围0-15 其中0表示关闭其余值满足下面公式
step=9*level 当step大于127时为127
level对应的电压=1612.5mv+step*12.5mv
------------------------------------------------------------
LDO_VMMC	
level范围0-15 其中0表示关闭其余值满足下面公式
step=9*level 当step大于127时为127
level对应的电压=1612.5mv+step*12.5mv
------------------------------------------------------------
LDO_VCAMD	
level范围0-15 其中0表示关闭其余值满足下面公式
step=9*level 当step大于127时为127
level对应的电压=1400mv+step*12.5mv
------------------------------------------------------------
LDO_HMICBIAS	
level范围0-15 其中0表示关闭,其余值对应的电压如下所示
1 = 2.2V
2 = 2.4V
3 = 2.5V
4 = 2.6V
5 = 2.7V
6 = 2.8V
7 = 2.9V
8 = 3.0V
>8=3.0V
------------------------------------------------------------
LDO_VBACKLIGHT_R --> 对应硬件手册管脚名RGB_IB0
LDO_VBACKLIGHT_G --> 对应硬件手册管脚名RGB_IB1
LDO_VBACKLIGHT_B --> 对应硬件手册管脚名RGB_IB2
LDO_VBACKLIGHT_W --> 对应硬件手册管脚名RGB_IB3	
level范围0-15 其中0表示关闭其余值满足下面公式
step=4*level+3
level对应的电流=1.68mA+step*0.84mA
------------------------------------------------------------
LDO_FLASHIB
level范围0-15
level对应的电流=15mA+level*15mA
------------------------------------------------------------
]]
pmd.ldoset(7,pmd.VSIM1) 


```
详细指南：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2037 "指南")

---



## pmd.sleep(value)

省电控制

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|value|number|1 - 进入睡眠，0 - 退出睡眠|1/0|

**返回值**

无

此API仅推荐给lib脚本使用，不推荐用户应用脚本使用；
用户应用脚本可以直接使用pm API，链接为：[pm.sleep](https://doc.openluat.com/wiki/21?wiki_page_id=2287#pmsleeptag_29 "pm.sleep")

---



## pmd.param_get()

电池状态查询

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|battStatus|bool|电池是否在位|true：在位 false：不在位|
|battVolt|number|电池电压|单位mv|
|battLevel|number|电池电压|百分比|
|chargerStatus|bool|是否在充电|true:在充电 false:不在充电|
|chargeState|number|充电状态|1:正在充电 2:充电结束|

此API仅推荐给lib脚本使用，不推荐用户应用脚本使用；
用户应用脚本可以直接使用miscAPI，链接为：[misc.getVbatt](https://doc.openluat.com/wiki/21?wiki_page_id=2279#miscgetVbatt_238 "misc.getVbatt")

---



