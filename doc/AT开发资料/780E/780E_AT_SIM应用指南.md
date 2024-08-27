# 780E模块SIM应用指南

# 简介

> - 文档和工具
>   - AT指令手册：[Luat4G模块EC618&EC716&EC718系列AT命令手册](https://doc.openluat.com/article/4985)
>   - 780E模块AT固件：[合宙Air780E&600E AT固件更新说明](https://doc.openluat.com/article/4922)
>   - 本示例所烧录的AT固件版本： **AirM2M_780E_LTE_AT_V1165**
>   - 如果不会烧录，可参考 [烧录教程](https://doc.openluat.com/wiki/21?wiki_page_id=6072)
>   - 如果没有串口工具，推荐 [LLCOM | 能跑Lua代码的串口调试工具！](https://llcom.papapoi.com/index.html)

# 简介

SIM( Subscriber Identity Module)卡为用户识别模块，内部使用新式单片机及存储器管理结构，包含了大规模的集成电路，同时也称为用户识别卡。通信设备通过SIM卡来识别其用户，只有设备插入SIM卡后才能入网使用。SIM卡接口用于和SIM卡进行通信。

# 准备工作

1. 780E全IO开发板一套，包括天线、数据线和SIM卡，并烧录AT固件

   ![780E](image/Air780E.jpg)

2. PC电脑，串口工具

# 示例

> 下面是AT命令序列，如果不理解AT命令含义，请自行参考AT手册。

## 查询SIM是否在位示例

```LUA
[14:34:12.900]发→◇AT+CPIN?  //查询SIM卡是否在位，READY说明检查到SIM卡
□
[14:34:12.904]收←◆AT+CPIN?

+CPIN: READY

OK

[14:34:17.764]发→◇AT+ICCID  //查询SIM卡ICCID
□
[14:34:17.767]收←◆AT+ICCID

+ICCID: 898604981022C0254186

OK
```

## SIM卡热插拔示例

AT+CSDT该命令的设置命令可以开启 USIMDET这个引脚的功能。当 AT+CSDT=1 的时候，使能该引脚。此时配合 SIM 卡外围。

检测电路就能检测 SIM 卡在位状态，即插卡或掉卡。

如果需要关机保存，请输入AT+CSDT=;&W 

AT+CSDT=1：默认上升沿触发，不插卡是低，插入卡是高电平 

AT+CSDT=1,0：可以配置下降沿触发，不插卡是高，插入卡是低电平 

AT+CSDT=1,1：可以配置上升沿触发，不插卡是低，插入卡是高电平

```LUA
[14:35:27.671]发→◇AT+CSDT=1  //使能热插拔功能(默认上升沿触发，不插卡是低，插入卡是高电平)
□
[14:35:27.674]收←◆AT+CSDT=1

OK

[14:36:26.927]收←◆  //USIMDET与GND短接
^MODE: 0,0

+NO Service

+CGEV: NW PDN DEACT 1

+CGEV: ME DETACH

[14:36:27.750]收←◆+CPIN: SIM REMOVED 0

[14:36:38.159]收←◆
+CGEV: ME DETACH

[14:36:39.298]收←◆  //USIMDET与GND断开
^MODE: 17,17

+E_UTRAN Service

+CGEV: ME PDN ACT 1,0

[14:36:39.373]收←◆
+NITZ: 2024/08/27,06:36:38+0, 

[14:36:39.938]收←◆+CPIN: READY 0
```

## SIM卡手动切换示例

**单卡状态**：

如果只有 SIM0 接口上插入 SIM 卡时，模块会去读取 SIM0 接口的卡信息去注册网络。

如果只有 SIM1 接口上插入 SIM 卡时，需要通过手动输入 AT+SIMCROSS 这个指令将位置切换为 SIM1 后，

模块才能读取到 SIM1 接口的卡信息然后去注册网络。

**双卡状态**：

如果 SIM0 接口和 SIM1 接口如果同时插入了 SIM 卡，默认会使用 SIM0 接口上的 SIM 卡，此时可通过

AT+SIMCROSS 这个指令切换为 SIM1 接口上的 SIM 卡。

**注意：**

需要进飞行模式下进行卡切换（进入飞行模式（AT+CFUN=0），切换卡，退出飞行模式 AT+CFUN=1），否则指令会报错。

这里的SIM0对应开发板上的SIM1，SIM1对应开发板上的SIM2。

以下为只有 SIM1 接口上插入 SIM 卡时，通过手动输入 AT+SIMCROSS 这个指令将位置切换为 SIM1 后，模块才能读取到 SIM1 接口的卡信息然后去注册网络的示例：

```LUA
[14:43:16.109]发→◇AT+CPIN?  //查询卡状态为+CME ERROR: 10 说明未检查到卡
□
[14:43:16.112]收←◆AT+CPIN?

+CME ERROR: 10

[14:43:28.483]发→◇AT+CFUN=0  //进入飞行模式
□
[14:43:28.488]收←◆AT+CFUN=0

OK

+CGEV: ME DETACH

[14:43:29.772]发→◇AT+SIMCROSS=1  //切换成SIM1卡
□
[14:43:29.775]收←◆AT+SIMCROSS=1

+SIMCROSS:1

OK

[14:43:35.434]发→◇AT+CFUN=1  //退出飞行模式
□
[14:43:35.438]收←◆AT+CFUN=1

[14:43:35.579]收←◆
OK

[14:43:37.110]收←◆  //卡注册网络成功后上报信息
^MODE: 17,17

+E_UTRAN Service

+CGEV: ME PDN ACT 1,0

[14:43:37.181]收←◆
+NITZ: 2024/08/27,06:43:36+0, 

[14:43:46.683]发→◇AT+CPIN?
□
[14:43:46.686]收←◆AT+CPIN?  //查询卡状态为READY，说明成功检查到卡

+CPIN: READY

OK

```

## SIM卡自动切换示例

**关机前设置使用的SIM0:**

1. 只有SIM0卡：不用切换直接使用(切换次数0)

2. 只有SIM1卡：检测SIM1不在切换到SIM2(切换次数1)

3. SIM0和SIM1都在：不用切换直接使用(切换次数0)

**关机前设置使用的SIM1:**

1. 只有SIM0卡：切换到SIM0使用(切换次数1)

2. 只有SIM1卡：切换到SIM0检测不在，再切换回SIM1(切换次数2)

3. SIM0和SIM1都在：切换到SIM1使用(切换次数1)

可根据 AT+ECSIMCFG? 返回值中的 simSlot 来判断使用哪个卡进行网络通信。

```LUA

[14:48:03.802]发→◇AT*SIMAUTO=1  //打开SIM自动切换功能
□
[14:48:03.805]收←◆AT*SIMAUTO=1

[14:48:03.926]收←◆
OK

[14:48:09.097]发→◇AT+ECSIMCFG?
□
[14:48:09.102]收←◆AT+ECSIMCFG?

+ECSIMCFG: "SimSimulator",0
+ECSIMCFG: "SimPowerSave",1
+ECSIMCFG: "SimPresenceDetect",1
+ECSIMCFG: "SimSlot",0         //使用SIM0卡进行网络通信
+ECSIMCFG: "SoftSim",0

OK

[14:49:04.690]发→◇AT+RESET  //卡插入SIM1，重启模块
□
[14:49:04.693]收←◆AT+RESET

OK

[14:49:12.466]收←◆
+CGEV: ME DETACH

+CGEV: ME DETACH

^MODE: 17,17      //重启后成功注册网卡

+E_UTRAN Service

+CGEV: ME PDN ACT 1,0

+NITZ: 2024/08/27,06:49:09+0, 

[14:49:20.913]发→◇AT+ECSIMCFG?
□
[14:49:20.918]收←◆AT+ECSIMCFG?

+ECSIMCFG: "SimSimulator",0
+ECSIMCFG: "SimPowerSave",1
+ECSIMCFG: "SimPresenceDetect",1
+ECSIMCFG: "SimSlot",1        //使用SIM1卡进行网络通信
+ECSIMCFG: "SoftSim",0

OK
```

# 常见问题

### sim卡不识别问题？

sim卡不识别按以下步骤进行：
1：看模块开机没？at指令能不能用？at+cpin?返回ready,代表读到卡，如果返回error,按以下几点排查：
2：sim卡是不是Ok？sim卡方向有没反。
3：每个脚对地用万用表，打到二级管档位量下，红接地，黑接每个管脚，值是400-500之间正常。
4：看模块与卡座之间连线有没有问题，引脚对地阻值是不是正常，引脚间有没短路，
原理图和Pcb网络名与sim卡座实物对不对，卡座是否接触良好，如果sim卡一插入，vdd和clk就对地短路，一般是卡座问题。
5：示波器测试下sim_vdd波形，有个1.8-3.3v的高电平跳变，如果波形正常，一般是卡座和模块引脚之间问题，要识别到卡，才会有电压输出。
6：如果是贴片卡，可以先拆下贴片卡，飞线到一个可以识别到卡的卡座到模块管脚，看下是否贴片卡问题

### 专网卡访问白名单

用定向Ip的物联网卡，需要把域名或IP加入白名单才能使用，下面列出模块会访问的域名或IP服务器。
AT版本
DNS服务器，可以通过AT+CDNSCFG?查询默认的服务器，如果需要修改，可以通过AT+CDNSCFG=ip1,ip2进行修改。

|     功能     |                          地址                          | 端口  | 协议 |
| :----------: | :----------------------------------------------------: | :---: | :--: |
|   远程升级   |      [iot.openluat.com](http://iot.openluat.com/)      |  80   | http |
| 基站WIFI定位 |       [bs.openluat.com](http://bs.openluat.com/)       | 12412 | http |
| AGPS星历下载 | [download.openluat.com](http://download.openluat.com/) |  80   | http |
| NTP时间同步  |       [ntp1.aliyun.com](http://ntp1.aliyun.com/)       |  123  | udp  |

### 怎么判断sim卡是移动，联通还是电信？

可以通过查询卡的IMSI来判断
IMSI共有15位，其结构如下：
MCC+MNC+MSIN ，(MNC+MSIN=NMSI)
MCC：Mobile Country Code，移动国家码，MCC的资源由国际电联(ITU)统一分配和管理，唯一识别移动用户所属的国家，共3位，中国为460;
MNC:Mobile Network Code，移动网络码，共2位，中国移动00、02、04、07，08，中国联通01，中国电信03，11
MSIN:Mobile Subscriber Identification Number共有10位
AT命令获取IMSI方法

```lua
AT+CIMI
460081899904186 --MNC为08说明是中国移动卡
OK
```

> 合宙支持AT功能的模组型号，除本文介绍的Air780E外，
> 还有Air780EPA、Air780EP、Air780EX、Air201、Air780EQ、Air780EPT、Air780EPS等型号，
> 本文介绍的SIM应用应用指南的AT流程，同样也适用于这些型号。

![选型手册简洁版01](image/1.jpg)


![2](image/2.jpg)