# 设置APN

如果是公网SIM卡，不需要用户主动设置APN，软件自动去网络端查询APN进行设置。

如果是专网SIM卡，首先咨询SIM卡提供商APN参数，设置APN必须在入网前就设置好，比如在SIM卡识别完成前就设置好mobile.apn（）。

## mobile.apn(index, cid, new_apn_name, user_name, password, ip_type, protocol)

获取或设置APN，设置APN必须在入网前就设置好，比如在SIM卡识别完成前就设置好

**参数**

| 传入值类型 | 解释                                                         |
| ---------- | ------------------------------------------------------------ |
| int        | 编号,默认0. 在支持双卡的模块上才会出现0或1的情况             |
| int        | cid, 默认0，如果要用非默认APN来激活，必须>0                  |
| string     | 新的APN,不填就是获取APN, 填了就是设置APN, 是否支持设置取决于底层实现 |
| string     | 新的APN的username,如果APN不是空,那必须填写,如果没有留个空字符串””。如果APN是空的，那可以nil |
| string     | 新的APN的password,如果APN不是空,那必须填写,如果没有留个空字符串””。如果APN是空的，那可以nil |
| int        | 激活APN时的IP TYPE,1=IPV4 2=IPV6 3=IPV4V6,默认是1            |
| int        | 激活APN时,如果需要username和password,就要写鉴权协议类型,1~3,默认3,代表1和2都尝试一下。不需要鉴权的写0 |
| boolean    | 是否删除APN,true是,其他都否,只有参数3新的APN不是string的时候才有效果 |

**返回值**

| 返回值类型 | 解释                          |
| ---------- | ----------------------------- |
| string     | 获取到的默认APN值,失败返回nil |

**例子**

```
mobile.apn(0,1,"cmiot","","",nil,0) -- 移动公网卡设置APN为cmiot,一般不用设置
mobile.apn(0,1,"name","user","password",nil,3) -- 专网卡设置的demo，name，user，password
```

## mobile.ipv6(onff)

是否默认开启IPV6功能，必须在LTE网络连接前就设置好

**参数**

| 传入值类型 | 解释                     |
| ---------- | ------------------------ |
| boolean    | 开关 true开启 false 关闭 |

**返回值**

| 返回值类型 | 解释                                  |
| ---------- | ------------------------------------- |
| boolean    | true 当前是开启的，false 当前是关闭的 |

**例子**

```
-- 注意, 开启ipv6后, 开机联网会慢2~3秒
```
