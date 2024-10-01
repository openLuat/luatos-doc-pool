# 常驻GPIO

## 常驻GPIO介绍

常      驻GPIO，即AGPIO。

1、AONGPIO管脚休眠模式下可保持，保持高或低。

2、AONGPIO输出驱动能力单管脚：可以复用为WAKEUP3/WAKEUP4/WAKEUP5的前三个AONGPIO<=30uA，其余AONGPIO<=5mA；所有AONGPIO驱动电流总和也不能超过5mA

3、AGPIO3 芯片内部本身是默认拉低的，AT固件当前是通过软件开机初始改为拉高

## 常驻GPIO示例

        该示例可以对比进入休眠模式前后，普通GPIO和AGPIO的区别。

```lua
-- LuaTools需要PROJECT和VERSION这两个信息
PROJECT = "gpio2demo"
VERSION = "1.0.0"

log.info("main", PROJECT, VERSION)

-- sys库是标配
_G.sys = require("sys")

if wdt then
    --添加硬狗防止程序卡死，在支持的设备上启用这个功能
    wdt.init(9000)--初始化watchdog设置为9s
    sys.timerLoopStart(wdt.feed, 3000)--3s喂一次狗
end

sys.taskInit(function ()
    sys.wait(8000)
    --关闭USB电源
    pm.power(pm.USB, false)
    --进入低功耗模式
    pm.power(pm.WORK_MODE,3)
    
end)

-- 用户代码已结束---------------------------------------------
-- 结尾总是这一句
sys.run()
-- sys.run()之后后面不要加任何语句!!!!!

```
## 示例效果展示

        进入低功耗模式前，普通GPIO和AGPIO都可以保持电平，进入低功耗模式后，只有AGPIO可以保持电平。

![dd](./image/retentionResultDisplay1.gif)