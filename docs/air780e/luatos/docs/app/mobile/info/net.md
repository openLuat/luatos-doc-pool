# 切换网络

网络切换可以通过进出飞行模式，锁定band，重启协议栈，配置小区重选信号差值门限来进行切换网络。

## mobile.flymode(index, enable)

进出飞行模式

**参数**

| 传入值类型 | 解释                                             |
| ---------- | ------------------------------------------------ |
| int        | 编号,默认0. 在支持双卡的模块上才会出现0或1的情况 |
| bool       | 是否设置为飞行模式,true为设置, false为退出,可选  |

**返回值**

| 返回值类型 | 解释             |
| ---------- | ---------------- |
| bool       | 原飞行模式的状态 |

**例子**

mobile.flymode(0,true)   --进入飞行模式

mobile.flymode(0,false)  --退出飞行模式

## mobile.getCellInfo()

获取基站信息

**参数**

无

**返回值**

| 返回值类型 | 解释               |
| ---------- | ------------------ |
| table      | 包含基站数据的数组 |

**例子**

```
-- 注意: 从2023.06.20开始, 需要主动请求一次reqCellInfo才会有基站数据.

--示例输出(原始数据是table, 下面是json格式化后的内容)
--[[
[
    {"rsrq":-10,"rssi":-55,"cid":124045360,"mnc":17,"pci":115,"earfcn":1850,"snr":15,"rsrp":-85,"mcc":1120,"tdd":0},
    {"pci":388,"rsrq":-11,"mnc":17,"earfcn":2452,"snr":5,"rsrp":-67,"mcc":1120,"cid":124045331},
    {"pci":100,"rsrq":-9,"mnc":17,"earfcn":75,"snr":17,"rsrp":-109,"mcc":1120,"cid":227096712}
]
]]

mobile.reqCellInfo(60)
-- 订阅
sys.subscribe("CELL_INFO_UPDATE", function()
    log.info("cell", json.encode(mobile.getCellInfo()))
end)

-- 定期轮训式
sys.taskInit(function()
    sys.wait(3000)
    while 1 do
        mobile.reqCellInfo(15)
        sys.waitUntil("CELL_INFO_UPDATE", 15000)
        log.info("cell", json.encode(mobile.getCellInfo()))
    end
end)
```

## mobile.reqCellInfo(timeout)

发起基站信息查询,含临近小区

**参数**

| 传入值类型 | 解释                                  |
| ---------- | ------------------------------------- |
| int        | 超时时长,单位秒,默认15. 最少5, 最高60 |

**返回值**

| 返回值类型 | 解释     |
| ---------- | -------- |
| nil        | 无返回值 |

**例子**

```
-- 参考 mobile.getCellInfo 函数
```

## mobile.reset()

重启协议栈

**参数**

无

**返回值**

| 返回值类型 | 解释     |
| ---------- | -------- |
| nil        | 无返回值 |

**例子**

```
-- 重启LTE协议栈
mobile.reset()
```

## mobile.dataTraffic(clearUplink, clearDownlink)

数据量流量处理

**参数**

| 传入值类型 | 解释                                   |
| ---------- | -------------------------------------- |
| boolean    | 清空上行流量累计值，true清空，其他忽略 |
| boolean    | 清空下行流量累计值，true清空，其他忽略 |

**返回值**

| 返回值类型 | 解释       |
| ---------- | ---------- |
| int        | 上行流量GB |
| int        | 上行流量B  |
| int        | 下行流量GB |
| int        | 下行流量B  |

**例子**

```
-- 获取上下行流量累计值
-- 上行流量值Byte = uplinkGB * 1024 * 1024 * 1024 + uplinkB
-- 下行流量值Byte = downlinkGB * 1024 * 1024 * 1024 + downlinkB
local uplinkGB, uplinkB, downlinkGB, downlinkB = mobile.dataTraffic()

-- 清空上下行流量累计值
mobile.dataTraffic(true, true)

-- 仅记录开机后的流量,复位/重启会归零
```

## mobile.config(item, value)

网络特殊配置

**参数**

| 传入值类型 | 解释                          |
| ---------- | ----------------------------- |
| int        | 配置项目，看mobile.CONF_XXX   |
| int        | 配置值,根据具体配置的item决定 |

**返回值**

| 返回值类型 | 解释     |
| ---------- | -------- |
| boolean    | 是否成功 |

**例子**

```
--针对不同平台有不同的配置，谨慎使用，目前只有EC618/EC718系列

-- EC618配置小区重选信号差值门限，不能大于15dbm，必须在飞行模式下才能用
mobile.flymode(0,true)
mobile.config(mobile.CONF_RESELTOWEAKNCELL, 15)
mobile.config(mobile.CONF_STATICCONFIG, 1) --开启网络静态优化
mobile.flymode(0,false)

-- EC618设置SIM写入次数的统计
-- 关闭统计
mobile.config(mobile.CONF_SIM_WC_MODE, 0)
-- 开启统计, 默认也是开启的.
mobile.config(mobile.CONF_SIM_WC_MODE, 1)
-- 读取统计值,异步, 需要通过系统消息SIM_IND获取
sys.subscribe("SIM_IND", function(stats, value)
    log.info("SIM_IND", stats)
    if stats == "SIM_WC" then
        log.info("sim", "write counter", value)
    end
end)
mobile.config(mobile.CONF_SIM_WC_MODE, 2)
-- 清空统计值
mobile.config(mobile.CONF_SIM_WC_MODE, 3)
```

## mobile.getBand(band, is_default)

获取当前使用/支持的band

**参数**

| 传入值类型 | 解释                                                         |
| ---------- | ------------------------------------------------------------ |
| zbuff      | 输出band                                                     |
| boolean    | true默认支持，false当前支持的，默认是false，当前是预留功能，不要写true |

**返回值**

| 返回值类型 | 解释                        |
| ---------- | --------------------------- |
| boolean    | 成功返回true，失败放回false |

**例子**

```
local buff = zbuff.create(40)
mobile.getBand(buff) --输出当前使用的band，band号放在buff内，buff[0]，buff[1]，buff[2] .. buff[buff:used() - 1]
```



------

## mobile.setBand(band, num)

设置使用的band

**参数**

| 传入值类型 | 解释           |
| ---------- | -------------- |
| zbuff      | 输入使用的band |
| int        | band数量       |

**返回值**

| 返回值类型 | 解释                        |
| ---------- | --------------------------- |
| boolean    | 成功返回true，失败放回false |

**例子**

```
local buff = zbuff.create(40)
buff[0] = 3
buff[1] = 5
buff[2] = 8
buff[3] = 40
mobile.setBand(buff, 4) --设置使用的band一共4个，为3,5,8,40
```

------

