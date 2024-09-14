# APN介绍

APN，全称Access Point Name，即接入点名称。它是移动设备在连接移动网络时，用于指示数据连接的网络接入点的一个标识符。简单来说，APN就是告诉手机或其他移动设备，应该通过哪个“门”来访问互联网或其他外部网络。

如果是公网SIM卡，不需要用户主动设置APN，软件自动去网络端查询APN进行设置。

如果是专网SIM卡，首先咨询SIM卡提供商APN参数，设置APN必须在入网前就设置好，比如在SIM卡识别完成前就设置好。

## 获取当前SIM卡的apn

**mobile.apn()**

```lua
sys.taskInit(function()
    -- 如果在刚开机就要执行获取，最好先加些延时，防止sim卡刚上电还未准备好，读取失败。
    sys.wait(2000)

    -- 获取apn
    -- 对于双卡单待的设备来说,只能获取当前SIM卡的apn
    local apn = mobile.apn()
    log.info("sim_apn", apn)
    -- 实例输出：sim_apn cmnet.mnc008.mcc460.gprs
end)
```

## 设置当前SIM卡的apn

**mobile.apn(index, cid, new_apn_name, user_name, password, ip_type, protocol)**

获取或设置APN，设置APN必须在入网前就设置好，比如在SIM卡识别完成前就设置好

```lua
sys.taskInit(function()
    -- 移动公网卡设置APN为cmiot,一般不用设置
	mobile.apn(0,1,"cmiot","","",nil,0) 
    -- 专网卡设置的demo，name，user，password联系卡商获取
	mobile.apn(0,1,"name","user","password",nil,3) 
end)
```

## 如何区分专网卡

```
根据使用的网络类型来分，sim卡可以分为公网卡和专网卡两种
如何判断sim卡是公网卡还是专网卡，可按照如下顺序确认：
1. 咨询sim卡供应商
2. 如果apn有账号、或者有密码、或者有加密类型，则可以认为是专网卡
```

## 专网卡访问白名单

用定向Ip的物联网卡，需要把域名或IP加入白名单才能使用，下面列出模块会访问的域名或IP服务器。

| 功能         | 地址                  | 端口  | 协议 |
| ------------ | --------------------- | ----- | ---- |
| 远程升级     | iot.openluat.com      | 80    | http |
| 日志服务     | dev_msg1.openluat.com | 12425 | udp  |
| 基站WIFI定位 | bs.openluat.com       | 12411 | udp  |
| AGPS星历下载 | download.openluat.com | 80    | http |
| NTP时间同步  | ntp.aliyun.com        | 123   | udp  |
