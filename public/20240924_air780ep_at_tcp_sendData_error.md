# Air780EP模块开发项目遇到的的吐血经历-异常断链篇

## 前情提要

我最近被老板驱使，要用780EP做几个紧急项目，由于时间紧任务重，不出所料的遇到了一些棘手问题，可把我给折腾死了，这里把遇到的问题，排查记录下来，看能不能帮到因遇到类似的问题，并且一直没找到原因，而被老板要求加班解决的兄弟们。

不知道各位在用Cat.1模块的时候，会不会遇到收不到网络数据的问题呢，比如"用TCP做长链接，在进入休眠场景后进行保活，但时常出现丢包的现象，应该怎么分析呢"、"MQTT服务器下行数据，模块有概率接收不到，服务器也有遇到收不到模块的上行数据，到底是什么情况"等等类似的问题。

但单纯通过模块这边的看到的现象，也不能断定就是模块这边出了问题。要想准确的找出这个“罪犯”，这种时候就需要通过抓网络包来分析排查出是以下哪种原因：

（1）模块有发出数据->但服务器没收到

（2）模块未发出数据->导致服务器没收到

（3）服务器有发出数据->但模块没收到

（4）服务器未发出数据->导致模块没收到

**以下通过最近遇到的一个实例给各位提供个分析思路。**

目前其中有个项目用的是AT开发，大致应用场景为TCP长链接，要求定时上报GPS/基站/wifi的定位数据，没有休眠需求，但时不时在发送数据的时候，会出现**AT+CIPSEND**发数据发着发着出现返回 **+CME: ERROR 3**的问题。

基本情况解析：

- 使用的数据传输协议为TCP
- 问题现象为偶先，小概率出现
- 从模块查看到的异常情况为**AT+CIPSEND**发送TCP数据的指令出现了 **+CME: ERROR 3**的错误码

首先按照 **+CME: ERROR 3**这个错误码出现的条件，筛选一下可能出现的有哪些情况

1. 最先想到的就是TCP链接已经不存在，断开了，导致发送数据时检测TCP通道关闭，而出现**AT+CIPSEND**命令返回错误。
2. 发送的**AT+CIPSEND**命令前后携带了其他的字符，一起作为一整条指令发送给了模块，导致模块解析出错。

**AT+CIPSEND**这条指令会出现 **+CME: ERROR 3**基本上就是以上两种情况了。

那么先尝试排除下第二条，我在偶现第一次**AT+CIPSEND**出现错误之后，后面也尝试发送了的多条**AT+CIPSEND**命令发现也都会出错，但中间穿插发送的**AT+CEREG?**、**AT+CGATT?**、**AT+CSQ** 查网络状态、信号强度的命令返回都正常，也没有报错。而且把发送的整条数据转为以HEX格式来看，指令前后也没有多余的字符出现，那可以排除第二种情况了。

接下来这个时候为了印证第一条的猜想，就需要排查下问题是否为TCP链接已经断开了，在挂测了一段时间再次复现问题的时候 加一条**AT+CIPSTATUS**的命令查一下连接状态，结果不出所料，返回的结果是**STATE: TCP CLOSED**，TCP链接是断开的状态！已经锁定问题原因是有概率出现TCP突然断链的现象。

由于目前条件抓不了服务器端的网络日志，只能暂且想办法从模块端排查问题。

出现断链也可以分为 模块端发起断开连接 和 服务器端发起断开连接，如果为模块端断接，可以看下是否有主动发送**AT+CIPCL**

**OSE**去断开连接，但我从AT流程的日志来看，明显程序中还没有走到**AT+CIPCLOSE**这一步，问题就已经复现了。 模块端如果没有主动通过指令断开连接，那么在遇到网络波动、信号差、卡没流量等等，会影响网络的事件时，模块也可能会发起断开连接的请求。但上面也已经排查过，在出现**AT+CIPSEND**返回ERROR之后，也发送了**AT+CEREG?**、**AT+CGATT?**、**AT+CSQ**这三条指令，返回结果依次为**+CEREG: 0,1**、**+CGATT: 1**、**+CSQ: 25**，可以从CEREG和CGATT的返回结果看出，网络状态是正常已成功注册网络的，CSQ信号值为25，也很正常。

那这到底是怎么回事呢，这下不得不通过网络抓包来进一步分析了。

## 准备工作

> - 自制板子需要引出USB或者DBG_UART串口，二选一。但如果问题是只有在休眠环境下才能复现的，那么只能使用DBG_UART串口，进入休眠后USB要断开 会导致抓不到休眠中的日志。
> - 如果使用DBG_UART串口，还需要准备一个高速串口工具（能支持6M波特率，例如ch343、ft4232）
> - 合宙开发板默认有引出USB和DBG_UART串口，可以直接接线使用。
> - [EPAT log工具 EPAT_V1.3.262.573](https://cdn.openluat-luatcommunity.openluat.com/attachment/20240204134335482_EPAT_V1.3.262.573.zip)，使用方式本文章也会简单说明，在EPAT软件 **Manual** 目录中也有一份使用介绍的pdf。
> - [Wireshark](https://www.wireshark.org/) 网络包分析工具

## 日志怎么抓，用什么工具抓？

### 1.选择正确且合适的日志输出端口

- USB的虚拟端口其中有一个为底层日志的输出端口。可从设备管理器端口属性中“设备实例路径”的值为"USB\VID_19D1&PID_0001&MI_04\xxxxxx&0&0004"锁定到底层日志输出端口是哪一个。

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=N2VlY2JiYWU4MzBkNzM2OTAzNDIwMWVhYmFkNDg3NDNfOVBGdmZFRTAzYm5nREs3TkIzcG8xelJZSkNjMkZKeVNfVG9rZW46V2ZhYWI4TVlTb09ZV2Z4WGdoVGNKREJYbnliXzE3MjcxNTg2ODk6MTcyNzE2MjI4OV9WNA)

​        **建议使用USB来抓取日志**

​        **优点：USB虚拟端口输出速率很高，所以基本不会出现丢日志的现象**

​        **缺点：连接USB时不会进入休眠**

- **DBG_UART**串口需要以**6M**波特率输出底层日志，此串口输出的数据要通过EPAT工具才可以解析。
- **优点：进入休眠的日志也同样可以抓取**
- **缺点：但因为波特率要求在6M，所以对串口线的要求很高，如果引出的杜邦线太长或者质量不高，也会影响日志输出的数据，导致工具不能正常解析**

### 2.认识EPAT工具中图标功能

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=MjM0MjcyZWE1YWJiMjY2NzcxZGUwMGY5Y2UxYWQ3MzdfdndYVjB4VWNnOThkYmZnWkNKWThNaG9MOUFJcmlTSFJfVG9rZW46TFNqVWI0Y0Yyb01Wbzd4S250ZWN3NUNJbmRnXzE3MjcxNTg2ODk6MTcyNzE2MjI4OV9WNA)

图从左往右的顺序介绍

1. 打开日志文件，需要在打开EPAT工具时跳出的"**Select Data Source**"选择框中选择"**Select From Local Files**"，才能点击打开日志文件的功能，可以打开ZIP压缩包和Bin格式的日志文件。
2. 保存日志，会将已抓取到的日志导出，以ZIP压缩包的方式保存，方便提供给技术同事或研发同事分析。
3. 更新解析日志的数据库文件，在抓日志的时候，可以不匹配，等在使用EPAT打开日志文件的时候再做匹配解析。
4. 筛选查看日志，如果不了解，用不到这个功能
5. 启动开始抓日志，如果没有日志出来，请检查日志端口有没有选择正确，有没有勾选打开；确认端口正确，也以勾选，还是没有日志出来，请尝试：
   1. 重启模块
   2. 勾选选择的端口从其他串口调试工具尝试打开是否可以正常输出数据（正常打开输出的就是乱码）
   3. 如果使用AT固件，默认**DBG_UART**端口输出是**6M**波特率，可以通过**AT+ECPCFG=logBaudrate,6000000** 指令修改，波特率设置请不要低于**6M**，不然很容易出现丢日志、抓的不全。
6. 暂停日志
7. 停止抓日志，点击完停止后，就可以选择保存日志 发给技术/研发同事分析了。
8. 清除日志，建议每次正式准备抓日志前清理一下日志，这样保存出来的日志给技术同事分析会方便很多。
9. 搜索当前view视图的日志内容
10. 设备端口配置界面

### 3.底层日志抓取步骤

I. 打开EPAT工具，抓日志选择第一项“Serial Device”

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=MDk1OGEwODZkYjkwYTRkMWE4ZDEyMWFiNzExNWRmYWVfYXUzUk1QRGwwMnR6dGxwbmwzRFpxVHRheVNNUk9zcm1fVG9rZW46SnlVRmJRdXNpb2ZkeE54R2lIcGNKOWxmbkhoXzE3MjcxNTg2ODk6MTcyNzE2MjI4OV9WNA)

II. 选择日志端口，准备抓取log

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=NDVhNjE3MWE5OWFjZmYxNGI3ZDYzOGRiODM3ZDNiZDNfNTM1azVqSVBEb1pHd3JlOVZBNDZ2WTRoMFF1U1h2TEpfVG9rZW46R0JtNWJ5Y0VNb0dPMXl4YW5GamNGdmRobndiXzE3MjcxNTg2ODk6MTcyNzE2MjI4OV9WNA)

#### 选择使用USB的虚拟日志端口

1. 打开设备端口配置界面
2. 关闭或打开端口，如果端口被占用，工具也不会提示"端口已被占用"，所以如果发现端口选择正确，并且日志还是没有出来的话，可以确认下日志端口是否有被占用，而导致EPAT没有打开日志端口。
3. Device0、Device1 两个复选框，二选其一
4. 打开日志输出端口和修改波特率的界面。
5. 选择从设备管理器端口属性中**“设备实例路径”的值为"USB\VID_19D1&PID_0001&MI_04\xxxxxx&0&0004"的日志输出端口。**
6. **USB**的虚拟日志端口不用修改波特率。

> 这时前面流程都走完了，但是发现没有日志出来。首先可以确认下模块是否开机，最直接的方式就是量vbat的电压是否在4.3v~3.3v之间，并且看VDD_EXT是否有1.8v或3.3v，电压正常就说明模块是处于开机状态了，其他类似于看网络灯没亮、USB端口没显示这种条件不够准确，因为这些也会存在其他因素而导致状态不正常。
>
> 接下来继续排查，USB虚拟日志端口选择的是否正确，如果虚拟端口没显示出来，确认下LuatOS开发程序内是否调用了"pm.power(pm.USB, false)"关闭usb功能的接口，AT开发使用AT+ECPCFG?指令查看"**usbCtrl**"属性的值是否为2，如果是2代表关闭了usb功能，需要手动设置下AT+ECPCFG="usbCtrl",0  将usb功能打开，然后重启模块，如果还是没有端口显示，就需要从硬件、USB数据线、电脑端口方面排查，先做交叉测试。
>
> 有时还遇到过从模块dm、dp飞出的连接线过长，也会导致usb虚拟端口无法识别不能正常显示，**把dm、dp和usb的连接线 整体缩短到30cm左右，端口才能正常显示。但理论上还是要看使用的usb线和杜邦线的传输质量是否优秀**。
>
> 有时使用win7/win8的系统遇到怎么着都出不来usb的虚拟端口，原因是780E模块的USB驱动使用的是[微软系统自带的usb驱动](https://learn.microsoft.com/zh-cn/windows-hardware/drivers/usbcon/usb-driver-installation-based-on-compatible-ids#versions-supported)，所以仅支持在win10和win11上驱动。如果是win10/win11上面的方法都尝试过，端口也依然没有出来，也不妨用另一台电脑试一下看看是否是驱动问题，可能电脑上装的win10系统是简装版，缺少了一些驱动。

#### 选择使用DBG_UART串口

1. 抓日志用的usb转ttl的串口工具需要支持6M波特率，电脑上并且装了对应串口工具用到的驱动（一般从网络上或者购买商家那里可以了解到需要用什么驱动）。
2. 打开设备端口配置界面
3. 关闭或打开端口，如果端口被占用，工具也不会提示"端口已被占用"，所以如果发现端口选择正确，并且日志还是没有出来的话，可以确认下日志端口是否有被占用，而导致EPAT没有打开日志端口。
4. Device0、Device1 两个复选框，二选其一
5. 打开日志输出端口和修改波特率的界面。
6. 选择日志输出端口。
7. **DBG_UART**端口波特率输出可手动写入修改为**6000000（6M）**波特率。

> 使用DBG_UART串口没输出出来日志，排除步骤和USB也有点相同之处。
>
> 首先确认下模块是否开机，最直接的方式就是量vbat的电压是否在4.3v~3.3v之间，并且看VDD_EXT是否有1.8v或3.3v，电压正常就说明模块是处于开机状态了，其他类似于看网络灯没亮、USB端口没显示 这种条件不够准确，因为这些也会存在其他因素而导致状态不正常。
>
> 接下来继续排查，DBG_UART日志串口选择的是否正确，确认下LuatOS开发程序内是否有通过云编译关闭了uart0的日志输出，AT开发使用AT+ECPCFG?指令查看，要DBG_UART0输出日志，需要几条指令配置一下
>
> AT+ECPCFG="logPortSel",1                 // 只从UART0输出日志
>
> AT+ECPCFG=logBaudrate,6000000        // 修改日志输出波特率为6M
>
> AT+ECPCFG="logCtrl",2                        // 输出log等级为ALL，全部任何日志都输出
>
> 指令配置完之后重启模块，正常来说日志应该就可以吐出来了。如果还是没有日志，尝试用sscom这种串口调试工具打开相同的端口，看下是否有日志输出（正常会输出一堆的乱码），没有输出的话就需要排查下打开的端口、串口接线，比如rx/tx反接一下，有没有短路。并且如果是从预留的测试点用杜邦线飞出的DBG_UART_TX和DBG_UART_RX，**那需要注意杜邦线的长度一定要短，不然也会影响输出的日志出现丢失**。

#### 进阶玩法--两个端口都使用

没错，还可以同时使用USB的虚拟日志端口和DBG_UART日志串口来抓取日志，这样做的好处**是在进入休眠场景的时候，待USB断开，就会用DBG串口输出日志，等模块唤醒时就会重新虚拟出来USB端口，就会从USB的日志口抓取日志**。

如果通过DBG_UART串口来抓取非休眠场景的日志，由于底层业务逻辑过多，各种日志都会长时间大批量输出，只用6M的波特率还是避免不了可能出现丢日志的情况。而用串口抓取休眠中的日志时，由于一些底层业务会关闭，输出的日志相对并没有特别频繁，所以在休眠中丢日志概率会小一些。

但两个端口同时使用，这样就把两个端口的优势都使用上了，无论是休眠场景还是其他业务逻辑场景，基本上不会出现任何日志丢失的情况，但要求就是两个端口都要有预留出来。

1. 打开设备端口配置界面
2. 关闭或打开端口，如果端口被占用，工具也不会提示"端口已被占用"，所以如果发现端口选择正确，并且日志还是没有出来的话，可以确认下日志端口是否有被占用，而导致EPAT没有打开日志端口。
3. 日志端口可以同时打开两个，一个用模块的**DBG_UART**端口打开，另一个使用USB的日志输出端口。

> AT固件需要设置以下指令（重启生效）才能设置日志端口可以从USB和DBG_UART两个端口输出。 AT+ECPCFG=logPortSel,2                // USB和DBG_UART都允许输出底层日志
>
> 下面两个指令如果不配置，那么插入usb不会进入休眠，配置下面指令之后，相当于就算接入usb也允许进入休眠。 AT+ECPCFG="usbSlpMask",1           // USB不参与休眠投票 AT+ECUSBSYS="VBUSModeEn",1,"VBUSWkupPad",1           // usb的vbus引脚不参与休眠投票

1. 打开日志输出端口和修改波特率的界面。
2. 选择日志输出端口。
3. **USB**的虚拟日志端口不用修改波特率。

​        **DBG_UART**端口波特率输出可手动写入修改为**6000000（6M）**波特率。

因为这个项目没有用休眠场景，就直接用USB来抓日志了，按照上面的流程接上USB，打开日志的虚拟端口，成功看到了有日志出来。下面只需要挂着等问题出现就好了。

（有抓过底层日志的朋友肯定想起来，不是还有一步匹配解析日志的数据库MDB.txt文件吗。其实如果只是导出pcap看网络包，不需要去匹配数据库文件）

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=NjYxZmIzMmE4MmM3NDZhODQzZjE0NzdkYzM2MjdjMmFfMzFocXBSMG9tUFlHdXNUbms2MExwZDlYcUFuaU5kd2tfVG9rZW46RDVnZWJhd0dnb29lZEJ4N3FIb2NGT2J4bnJiXzE3MjcxNTg2ODk6MTcyNzE2MjI4OV9WNA)

## 要怎么导出pcap文件，查看网络抓包？

首先在抓取到复现的日志之后，不要着急，先停止日志打印。然后在当前是**SigLogger**视图的日志窗口时，才能看到并点击右上角的**SigLog**菜单栏，打开**SigLog**菜单栏后，点击"**Export As pcap file**"，选择一个导出路径和起一个文件名称，**文件名称可不能和当前文件夹内的.pcap名称重复，因为导出的数据内容是不会覆盖的**，随后点击保存，即可导出pcap格式的抓包文件。

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=ZTJmNzk3MWYzZmQ5YzNjNGU3MjhjYjk5M2YyMzI5YTdfMFJoUG04SDg2cGFicnlSdHlNWmlmMTVDWFBBM0wxRWZfVG9rZW46RmhvWWJQUkdPb25NemZ4OEJnT2NheEZCbldmXzE3MjcxNTg2ODk6MTcyNzE2MjI4OV9WNA)

## 通过Wireshark开始分析

好的，网络包也抓到了，调转回来继续分析“TCP长链接，定时上报GPS/基站/wifi的定位数据，没有休眠需求，但时不时在发送数据的时候，会出现AT+CIPSEND 发数据发着发着出现返回+CME: ERROR 3”的问题。

先前文章开头已经分析出是TCP链接出现断开，而导致**AT+CIPSEND**命令返回 **+CME: ERROR 3**，但还不清楚具体是模块主动断开的，还是服务器端断开的链接。下面我们就通过导出的pcap文件，打开看一下。根据日志的时间戳看到复现时间在18:56.24左右，那我们先定位到这个时间附近看一下。

![img](https://e3zt58hesn.feishu.cn/space/api/box/stream/download/asynccode/?code=ZmExYTQ5ZTI4ODU0YzNjYjBhMDEzNGMzMjRjZjM2NzJfeTREMlFRemhhdGE5cHhyUWVrQjRkeGc5bWdaTENiamhfVG9rZW46WEZ2TWJFdnRWb0YybVZ4TE1GNmNFZ1g2bmRnXzE3MjcxNTg2ODk6MTcyNzE2MjI4OV9WNA)

结果确实找到了[FIN,ACK]请求断开连接的网络包，在确认下发出的ip地址是**112.74.41.204**，目标地址是**10.49.81.92**。怎么判断哪个是模块，哪个是服务器端呢，也很简单，还是从上面那张图片举例，流程中现在有检测如果发现**AT+CIPSEND**发送失败，就发送**AT+CEREG?**、**AT+CIPSTATUS**，等返回结果为 **+CEREG:0,1**和**STATE: TCP CLOSED**时，就重新建立连接。 从AT流程中看出在**19:00:12**时有发送**AT+CIPSTART=xxxxxx,xxx**，来建立新链接。

从图片中网络包的同一时间**19:00:12**，也确实出现了[SYN]建立连接的请求，发出的地址是**10.49.81.92**，那这个就是模块端的ip地址了。以此推断出另一个**112.74.41.204** 就是服务器端的ip地址（一般如果服务器是自己公司建立维护的，可以向自己公司的相关负责的同事询问一下，服务器ip是哪一个）

既然找出了发出[FIN,ACK]请求断开连接的网络包是**112.74.41.204**这个服务器端的ip地址，这样就明白了是服务器端主动把链接关闭的。

不过正常来说被动断开连接模块应该会出现"**CLOSED**"的URC上报，但为什么没。。。 哦~ 原来有上报啊，是我忘记加在收到**CLOSED**的URC上报后，尝试重连的逻辑了，那这个就很简单了，出现断链之后，先通过**AT+CEREG?**获取到模块已成功注网的状态，然后再发送**AT+CIPSTART=xxxxxx,xxx**做重连。

最终导致断开连接的这个“罪犯”也是找到了是服务器的问题，不过我们用的服务器，是老板找的第三方，在拿出这个网络抓包（证据）之后，以为能知道是什么原因呢，结果一直在"踢皮球"，说他们也是负责代理，他们也要去确认，诶~ 沟通起来那是可真累啊， 一整天都过去了，直到最后也不知道是啥原因，由于项目赶时间，解决完这个问题后，又要看下一个问题了！
