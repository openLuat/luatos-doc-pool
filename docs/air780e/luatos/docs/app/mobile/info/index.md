# 简介

本资料中心包含Air780E使用LuatOS开发的mobile - 蜂窝网络app的使用和说明。

本库有专属demo，[点此链接查看mobile的demo例子](https://gitee.com/openLuat/LuatOS/tree/master/demo/mobile)

**示例**

```
-- 简单演示

log.info("imei", mobile.imei())
log.info("imsi", mobile.imsi())
local sn = mobile.sn()
if sn then
    log.info("sn",   sn:toHex())
end
log.info("muid", mobile.muid())
log.info("iccid", mobile.iccid())
log.info("csq", mobile.csq())
log.info("rssi", mobile.rssi())
log.info("rsrq", mobile.rsrq())
log.info("rsrp", mobile.rsrp())
log.info("snr", mobile.snr())
log.info("simid", mobile.simid())
```

## 常量

| 常量                                         | 类型   | 解释                                                         |
| -------------------------------------------- | ------ | ------------------------------------------------------------ |
| mobile.UNREGISTER                            | number | 未注册                                                       |
| mobile.REGISTERED                            | number | 已注册                                                       |
| mobile.SEARCH                                | number | 正在搜索中                                                   |
| mobile.DENIED                                | number | 注册被拒绝                                                   |
| mobile.UNKNOW                                | number | 未知                                                         |
| mobile.REGISTERED_ROAMING                    | number | 已注册,漫游                                                  |
| mobile.SMS_ONLY_REGISTERED                   | number | 已注册,仅SMS                                                 |
| mobile.SMS_ONLY_REGISTERED_ROAMING           | number | 已注册,漫游,仅SMS                                            |
| mobile.EMERGENCY_REGISTERED                  | number | 已注册,紧急服务                                              |
| mobile.CSFB_NOT_PREFERRED_REGISTERED         | number | 已注册,非主要服务                                            |
| mobile.CSFB_NOT_PREFERRED_REGISTERED_ROAMING | number | 已注册,非主要服务,漫游                                       |
| mobile.CONF_RESELTOWEAKNCELL                 | number | 小区重选信号差值门限,需要飞行模式设置                        |
| mobile.CONF_STATICCONFIG                     | number | 网络静态模式优化,需要飞行模式设置                            |
| mobile.CONF_QUALITYFIRST                     | number | 网络切换以信号质量优先,需要飞行模式设置,0不开,1开启,2开启并加速切换,功耗会增加 |
| mobile.CONF_USERDRXCYCLE                     | number | LTE跳paging,需要飞行模式设置,谨慎使用,0是不设置,1~7增大或减小DrxCycle周期倍数,1:1/8倍 2:1/4倍 3:1/2倍 4:2倍 5:4倍 6:8倍 7:16倍,8~12配置固定的DrxCycle周期,仅当该周期大于网络分配的DrxCycle周期时该配置才会生效,8:320ms 9:640ms 10:1280ms 11:2560ms 12:5120ms |
| mobile.CONF_T3324MAXVALUE                    | number | PSM模式中的T3324时间,单位S                                   |
| mobile.CONF_PSM_MODE                         | number | PSM模式开关,0关,1开                                          |
| mobile.CONF_CE_MODE                          | number | attach模式，0为EPS ONLY 2为混合，遇到IMSI detach脱网问题，设置为0，注意设置为EPS ONLY时会取消短信功能 |
| mobile.CONF_SIM_WC_MODE                      | number | SIM写入次数的配置和读取                                      |
| mobile.CONF_FAKE_CELL_BARTIME                | number | 伪基站禁止接入的时间，取值为0时取消，0xffff永久              |
| mobile.CONF_RESET_TO_FACTORY                 | number | 删除已保存的协议栈参数，重启后会使用默认配置                 |
| mobile.CONF_USB_ETHERNET                     | number | 蜂窝网络模块的usb以太网卡控制，bit0开关1,开0关，bit1模式1NAT,0独立IP(在usb以太网卡开启前可以修改，开启过就不行)，bit2协议1ECM,0RNDIS，飞行模式里设置 |
| mobile.CONF_DISABLE_NCELL_MEAS               | number | 关闭邻区测量 1关，0开，除了功耗测试外不建议使用              |
| mobile.PIN_VERIFY                            | number | 验证PIN码操作                                                |
| mobile.PIN_CHANGE                            | number | 更换PIN码操作                                                |
| mobile.PIN_ENABLE                            | number | 使能PIN码验证                                                |
| mobile.PIN_DISABLE                           | number | 关闭PIN码验证                                                |
| mobile.PIN_UNBLOCK                           | number | 解锁PIN码                                                    |

- [apn](./info/apn.md) 获取或设置APN
- [iccid](./info/iccid.md) 获取ICCID
- [imei](./info/imei.md) 获取IMEI
- [imsi](./info/imsi.md) 获取IMSI
- [net](./info/net.md) 切换网络
- [net_status](./info/net_status.md) 获取网络状态
- [net_type](./info/net_type.md) 获取网络类型
- [operator](./info/operator.md) 运营商信息
- [rssi](./info/rssi.md) 信号强度包含（csq，rssi，rsrq，rsrp，snr）等信号
- [sim](./info/sim.md) 切换SIM卡，SIM卡状态检测

