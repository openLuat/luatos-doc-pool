# ICCID介绍

ICCID：Integrate circuit card identity 集成电路卡识别码即 SIM卡号，相当于手机卡的身份证。 ICCID为IC卡的识别号码，共由20位字符组成，其编码格式为：XXXXXX 0MFSS YYGXX XXXX。前六位为运营商代码，用于标识不同的运营商。
例如，中国移动的运营商代码为898600、898602、898604、898607，中国联通的运营商代码为898601、898606、898609，而中国电信的运营商代码为898603、898611。这些代码是ICCID号码的重要组成部分，用于识别SIM卡所属的运营商。

## 获取SIM0接口上 SIM卡的ICCID

**mobile.iccid(id)**

```lua
sys.taskInit(function()
    -- 如果在刚开机就要执行获取，最好先加些延时，防止sim卡刚上电还未准备好，读取失败。
    sys.wait(2000)

    -- 获取ICCID
    local iccid = mobile.iccid()    -- 如果不传入参数 默认获取sim0接口的sim卡，也可以传入0，mobile.iccid(0)
    log.info("sim0_iccid", iccid) -- 例如返回：sim0_iccid 898604981022C0254186
end)
```

## 获取SIM1接口上 SIM卡的ICCID

```lua
sys.taskInit(function()
    -- 如果在刚开机就要执行获取，最好先加些延时，防止sim卡刚上电还未准备好，读取失败。
    sys.wait(2000)

    -- 获取ICCID
    local iccid = mobile.iccid(1)
    log.info("sim1_iccid", iccid) -- 例如返回：sim1_iccid 898600501620F0167894
end)
```

## 当遇到获取ICCID失败

可以按照以下情况排查：

### 硬件排查

1. 是否有查入SIM卡
2. SIM卡插入方向是否正确
3. 如果尝试过有其他卡插入可以读取到，就这张sim卡不行。
    - 可以检查下sim金属面是否比较脏、有刮痕，可以用橡皮擦或者少量酒精擦拭。
    - 卡的厚度相对比较薄，可以尝试垫一点卫生纸，缩短接触距离。
4. SIM卡电路设计有问题。可以进入 air780e.cn 打开硬件设计手册，其中包含SIM卡座的设计电路，作为排查参考。

### 软件排查

1. 是否将接口放在刚开机就立即会执行的位置，并且没有加延时。可能会出现模块开机sim卡还未读取到，软件就走到获取ICCID，这个时候就会获取失败。
2. SIM卡插入的sim硬件接口是否对应mobile.iccid()传入的参数。SIM0 -> mobile.iccid(0)     SIM1 -> mobile.iccid(1)

