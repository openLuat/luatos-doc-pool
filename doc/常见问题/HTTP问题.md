## 1. 是否支持HTTPS
>支持，TLSV1.2。
>支持证书配置，支持单向认证和双向认证。
>支持如下六种加密套件：
>0X0035 TLS_RSA_WITH_AES_256_CBC_SHA
>0X002F TLS_RSA_WITH_AES_128_CBC_SHA
>0X0005 TLS_RSA_WITH_RC4_128_SHA
>0X0004 TLS_RSA_WITH_RC4_128_MD5
>0X000A TLS_RSA_WITH_3DES_EDE_CBC_SHA
>0X003D TLS_RSA_WITH_AES_256_CBC_SHA256

## 2. 为什么频繁请求会失败
>支持的http连接总数有限，最多支持8个连接，包括其它TCP的连接。
>建议一个http连接返回请求结果之后，再去请求下一个连接；不要使用循环定时器方式不断的发起新的http请求。

## 3. 如何POST文件
>主要是使用AT+HTTPDATA命令录入文件数据【Air724模块最大长度为 319488，Air780E模块AT 版本最大长度为 3356，LSAT 版本 最大长度为 130048】后，发送AT+HTTPACTION=1利用post上传。

## 4. 数据接收发送缓存问题
>有缓存机制，内存中有一个的缓冲区（724模块319488字节，780e模块at版本为4KB，last版本为128k），收到数据后，插入此缓冲区，然后通过AT口输出urc，提示收到的数据长度；缓冲区满之后，再收到新数据，会丢弃新收到的数据，并通过AT口输出urc提示出错；需要读取数据时，发送AT+HTTPREAD命令读取，可分段读取，也可全部读取。<br>
>注意：缓冲区位于内存中，断电或者重启后，缓存表中的数据会被清空；虽然缓冲区可以缓存很多数据，但是建议收到数据时，通过AT+HTTPREAD及时读取出来，以防缓冲区满出错。

## 5. 为什么https访问失败
>参考问题1，检查服务器是否支持模块支持的加密套件。

## 6. 为什么我只发了10字节消息，100次却消耗了那么多流量？
>因为还有HTTP自带的请求头，详细说明参考socket问题章节的【如何统计流量】部分描述。

## 7. HTTP支持多连接吗
>目前HTTP仅支持单连接，不支持多连接。

## 8. HTTPS如何使用
>参考AT手册HTTP章节下《使用方法举例》中的"带SSL证书验证功能的HTTPS流程"使用方法；支持的SSL参数配置，请自行参考AT+SSLCFG命令说明。<br>
>如果SSL的参数配置不变，则每次开机运行过程中，仅设置一次即可。

## 9. 重试多次PDP，HTTP应用一直连接失败
>如果重试多次PDP激活，PDP一直激活失败，或者HTTP一直请求应答失败，则尝试使用如下手段恢复：
>1、使用RESET引脚复位模块。
>2、极端情况下，直接给模块断电，再上电，POWER KEY引脚拉低开机。

## 11. HTTP如何下载大文件（断点续传）
>在实际的应用场景中，可能需要下载一个非常大的文件，例如几百K字节、几M字节，但是4G模块中HTTP可用的内存缓冲区为（724模块319488字节，780e模块at版本为4KB，last版本为128k），当文件大小超过这个缓冲区时，就要使用断点续传功能来分段下载处理了。<br>
>下面以“下载一个11975260字节的文件”为例，来说明如何使用断点续传功能。（注意：本示例仅仅演示了正常流程的HTTP AT命令，完整流程以及异常处理流程请参考本文应用流程部分）。
```
AT+HTTPINIT

OK

AT+HTTPPARA="URL","http://openluat-erp.oss-cn-hangzhou.aliyuncs.com/erp_site_file/product_file/sw_file_20200108162920_Luat_V0028_ASR1802.zip"

OK

AT+HTTPACTION=2

OK

+HTTPACTION: 2,200,0

AT+HTTPHEAD 

+HTTPHEAD: 454

server: aliyunoss

date: thu, 16 jan 2020 06:50:58 gmt

content-type: application/zip

content-length: 11975260                            //此处的11975260表示文件总大小

connection: keep-alive

x-oss-request-id: 5e2007d108f4be32353a92ae

accept-ranges: bytes

etag: "a5b9cc75c0f26413bbaf00a0fa952bb2"

last-modified: wed, 08 jan 2020 08:29:29 gmt

x-oss-object-type: normal

x-oss-hash-crc64ecma: 16925484473913319613

x-oss-storage-class: standard

content-md5: pbnmdcdyzbo7rwcg+pursg==

x-oss-server-time: 111

OK

//如下指令，表示下载文件的第一个300KB数据

AT+HTTPPARA="BREAK",0

OK

AT+HTTPPARA="BREAKEND",307199

OK

AT+HTTPACTION=0

OK

+HTTPACTION: 0,206,307200

AT+HTTPREAD

+HTTPREAD: 307200

......                          //此处输出307200字节数据

OK

 //表示下载文件的第一个300KB数据完成

//如下指令，表示下载文件的第二个300KB数据

AT+HTTPPARA="BREAK",307200

OK

AT+HTTPPARA="BREAKEND",614399

OK

AT+HTTPACTION=0

OK

+HTTPACTION: 0,206,307200

AT+HTTPREAD

+HTTPREAD: 307200

......                          //此处输出307200字节数据

OK

 //表示下载文件的第二个300KB数据完成

//此处参考上文指令，一直循环读取文件的下一个300KB数据，直到读取结束

......

AT+HTTPTERM

OK
```

##  11. HTTP下载的大文件如何可靠的发送给MCU（AT流控）

>问题10中......处的307200字节数据，是模块通过UART AT口发送给MCU，在实际传输过程中，由于串口芯片驱动、MCU端的处理能力、波特率的选择都存在不确定性，可能会导致MCU端接收到的数据，实际上没有307200字节，这就要求UART AT口打开流控功能。模块支持硬流控和软流控两种：
>1、硬流控，参考如下步骤操作：
>（1）   模块和 的UART口，CTS、RTS要交叉相连。
>（2）   MCU端固件要支持并且打开硬流控功能。
>（3）  MCU端要发送AT+IFC=2,2命令到模块端，打开模块端的硬流控功能。<br>
>2、软流控，参考如下步骤操作：
>（1）  MCU端固件要支持并且打开软流控功能。
>（2）   MCU端要发送AT+IFC=1,1命令到模块端，打开模块端的硬流控功能。
