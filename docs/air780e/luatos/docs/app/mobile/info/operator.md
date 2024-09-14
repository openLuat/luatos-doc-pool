# 运营商信息

可以通过查询卡的IMSI和MNC来判断
IMSI共有15位，其结构如下：
MCC+MNC+MSIN ，(MNC+MSIN=NMSI)
MCC：Mobile Country Code，移动国家码，MCC的资源由国际电联(ITU)统一分配和管理，唯一识别移动用户所属的国家，共3位，中国为460;
MNC:Mobile Network Code，移动网络码，共2位，中国移动00、02、04、07、08，中国联通01、09，中国电信03、05、11
MSIN:Mobile Subscriber Identification Number共有10位

## mobile.imsi(index)

获取IMSI

**参数**

| 传入值类型 | 解释                                             |
| ---------- | ------------------------------------------------ |
| int        | 编号,默认0. 在支持双卡的模块上才会出现0或1的情况 |

**返回值**

| 返回值类型 | 解释                       |
| ---------- | -------------------------- |
| string     | 当前的IMSI值,若失败返回nil |

**例子**

```
log.info("imsi", mobile.imsi()) --460081899904186，MNC：08说明是移动卡
```
