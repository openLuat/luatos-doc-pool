@[TOC]

# pwm
脉冲输出接口
## pwm.open(id)

打开pwm

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|id|number|PWM硬件编号|0(gpio5管脚),1(gpio13管脚)|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number| 1：表示成功，0：表示失败|1/0 |

---



## pwm.close(id)

关闭脉冲输出

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|id|number|PWM硬件编号|0(gpio5管脚),1(gpio13管脚)|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number| 1：表示成功，0：表示失败|1/0 |

---



## pwm.set(id,param1,param2,clk_div)

设置脉冲参数，并输出脉冲

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|id|number|PWM硬件编号|0(gpio5管脚),1(gpio13管脚)|
|param1|number|周期分频系数/周期|(id=0时取值范围1-2047)/(id=1时取值范围0-7)|
|param2|number|占空比计算系数/高电平时间|(id=0时取值范围1-1023)/(id=1时取值范围0-15) |
|clk_div(可选)|number|PWM分频模式|0(200M),1(25M),2(12.5M),3(6.25M)|

**返回值**

无

**例子**

```lua
[[
    0 ：代表PWM0(gpio5管脚)   
	1 ：代表PWM1(gpio13管脚) 

当id为0吋: PWM0(gpio5管脚)
    param1:周期分频系数( 最大值为2047)，对应关系为：
    clk_div默认为0
        当clk_div为0吋:PWM0周期（45ns--82us） 
            PWM0周期 = (param1*8+1)/200000000 (s)
            PWM0周期范围：（45ns--82us）
            PWM0频率 = 200000000/(param1*8+1) (HZ)
            PWM0频率范围：（12.2KHZ--22.2MHZ）

        当clk_div为1吋: PWM0周期（360ns--655us）
            PWM0周期 = (param1*8+1)/25000000 (s)
            PWM0周期范围：（360ns--655us）
            PWM0频率 = 25000000/(param1*8+1) (HZ)
            PWM0频率范围：（1.52KHZ--2.78MHZ）

        当clk_div为2吋: PWM0周期（720ns--1300us）
            PWM0周期 = (param1*8+1)/12500000 (s)
            PWM0周期范围：（720ns--1.3ms）
            PWM0频率 = 12500000/(param1*8+1) (HZ)
            PWM0频率范围：（763HZ--1.39MHZ）

        当clk_div为3吋: PWM0周期（1440ns--2625us）
            PWM0周期 = (param1*8+1)/6250000 (s)
            PWM0周期范围：（1440ns--2625us）
            PWM0频率 = 6250000/(param1*8+1) (HZ)
            PWM0频率范围：（381HZ--694KHZ）

    param2:占空比计算系数( 最大值为1023)，对应关系为：
        PWM0占空比 = param2/ param1
        PWM0占空比范围：（0--100）

当id为1吋: PWM1(gpio13管脚)，PWM分频模式为0.
    param1:代表周期，对应关系为：
    0   --   LPG_PER_125MS
    1   --   LPG_PER_250MS
    2   --   LPG_PER_500MS
    3   --   LPG_PER_1000MS
    4   --   LPG_PER_1500MS
    5   --   LPG_PER_2000MS
    6   --   LPG_PER_2500MS
    7   --   LPG_PER_3000MS
   param2:代表高电平时间，对应关系为：
    0   --   LPG_ONTIME_UNDEFINE
    1   --   LPG_ONTIME_15_6MS
    2   --   LPG_ONTIME_31_2MS
    3   --   LPG_ONTIME_46_8MS
    4   --   LPG_ONTIME_62MS
    5   --   LPG_ONTIME_78MS
    6   --   LPG_ONTIME_94MS
    7   --   LPG_ONTIME_110MS
    8   --   LPG_ONTIME_125MS
    9   --   LPG_ONTIME_140MS
    10  --   LPG_ONTIME_156MS
    11  --   LPG_ONTIME_172MS
    12  --   LPG_ONTIME_188MS
    13  --   LPG_ONTIME_200MS
    14  --   LPG_ONTIME_218MS
    15  --   LPG_ONTIME_234MS

示例：
module(..., package.seeall)
function openPwm(id, para1, para2)
    pwm.open(id)
    pwm.set(id,para1,para2)
end

sys.taskInit(
    function ()
        -- 通道0，周期为45ns,频率为22.2MHZ
        misc.openPwm(0, 1，1)
        -- 通道0，PWM分频模式为1，周期为360ns,频率为2.78MHZ
        --misc.openPwm(0, 1，1, 1)
        -- 通道1，频率为2Hz，周期为500ms
        misc.openPwm(1, 2, 8)
        sys.wait(5000)
        end
    )

]]    

```

---



