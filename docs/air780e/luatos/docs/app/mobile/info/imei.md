# IMEI介绍

IMEI（International Mobile Equipment Identity）是国际移动设备识别码的缩写，也被称为手机序列号或手机“串号”。这个号码由15位数字组成，是全球范围内唯一识别每一部移动设备的代码。IMEI号相当于手机的“身份证”，用于在移动通信网络中准确识别每一部手机。

## 获取IMEI

**mobile.imei(index)**

```lua
--4G模组只支持双卡单待/单卡，只有一个IMEI，可以通过mobile.imei()直接获取
sys.taskInit(function()
    -- 获取IMEI
    log.info("imei", mobile.imei())    
    -- 实例输出：imei 866374063853768
end)
```

## 通过IMEI查询模块生产记录

[合宙云平台 (openluat.com)](https://iot.openluat.com/mes/mes-device-info)

