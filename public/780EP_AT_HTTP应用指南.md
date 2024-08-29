# 简介

> - 关联文档和使用工具：
>
>   - [AT固件获取](https://gitee.com/openLuat/airm2m-ec718-at/releases)
>   - [AT指令手册](https://doc.openluat.com/article/4985)
>

# 概述

4G模块支持HTTP和HTTPS协议， HTTP应用的基本流程如下：

     1、激活PDP（参考：http://oldask.openluat.com/article/937）
    
     2、初始化HTTP服务
    
     3、设置HTTP会话参数
    
     4、如果要支持SSL，配置SSL参数
    
     5、如果使用POST命令，输入POST数据
    
     6、发起HTTP请求
    
     7、收到HTTP应答，读取应答数据
    
     8、终止HTTP服务
    
     第1步出现异常后：首先需要排查http连接和请求参数是否正常，通过postman是否可以请求成功，模块上网是否正常（AT+CEREG?）
    
     第2步到第5步，只要输入格式正确，基本不会出问题；如果出错，可以跳过，直接处理第6步的异常
    
     第6步和第7步出现异常后：终止HTTP服务，有选择性的去激活PDP；然后再有选择性的激活PDP，从第2步开始重新执行

# 材料准备
- [EVB_Air780EP]开发板一套，包括天线SIM卡
- USB线
- PC电脑
- 串口调试工具（如果没有准备，推荐可以使用llcom，下载地址：https://llcom.papapoi.com）
- AT固件获取：https://gitee.com/openLuat/airm2m-ec718-at/releases ，进页面按下Ctrl+F 搜索 **AirM2M_780EP_LTE_AT** 即可找到780EP模块所使用的AT固件，推荐选用该固件名称后面数字版本号最高的最新relase版本进行调试。
- 当前文档示例使用[AirM2M_780EP_V1007_LTE_AT版本固件](https://cdn.openluat-erp.openluat.com/erp_site_file/product_file/sw_file_20240422190620_AirM2M_780EP_V1007_LTE_AT.zip)（除780EP模块不能烧录，但可以在上面AT固件获取连接获取到其他模块型号的AT固件。）

 <img src="image/微信图片_20240722101832.jpg" width="50%">

# HTTP GET请求示例

具体指令和参数使用说明，可参考[AT指令手册](https://doc.openluat.com/article/4985)

~~~
AT+CPIN?

+CPIN: READY    //查询sim卡是否正常

OK

AT+CGATT?

+CGATT: 1        //查询是否附着上数据网络，如果返回+CGATT: 0表示未附着上

OK

AT+SAPBR=3,1,"CONTYPE","GPRS"

OK

AT+SAPBR=3,1,"APN",""    //设置APN，此处""表示使用从网络端自动获取到的APN

OK

AT+SAPBR=1,1             //发起激活PDP的请求

OK

AT+SAPBR=2,1             //注意：此命令仅仅查询PDP地址，可以不执行

+SAPBR: 1,1,"10.159.1.145"    //请求到的PDP地址

OK

AT+HTTPINIT

OK

AT+HTTPPARA="CID",1

OK

AT+HTTPPARA="URL","airtest.openluat.com"

OK

AT+HTTPACTION=0		// GET请求

OK

+HTTPACTION: 0,200,285

AT+HTTPREAD

+HTTPREAD: 285

<!DOCTYPE html>
<html lang="en">


<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    Hello
</body>

</html>
OK
~~~



在这个过程中，注意事项如下：

>1、发送AT+HTTPACTION命令后，收到OK仅仅表示4G模块开始处理这条命令，并不表示请求发送成功，收到了应答；只有收到+HTTPACTION: n,statusCode,len才表示请求结束，statusCode表示应答成功，其余都表示应答失败
>2、HTTP应答数据的缓冲区大小为4KB，如果返回的http body数据超过了这个大小，则需要**断点下载，可以使用AT+HTTPPARA命令，通过设置BREAK和BREAKEND参数来实现**
>
>2、HTTP被动断开示例
>发送AT+HTTPACTION命令，和服务器建立了http连接后，如果连接异常被动断开，会输出+HTTPACTION: <Method>,<StatusCode>,<DataLen>提示
>
>3、PDP被动去激活示例
>先来看下PDP被动去激活时的AT命令处理序列，如果不理解AT命令含义，请自行参考AT手册。
>
>+PDP DEACT		// 出现PDP去激活的URC上报，后面如果没做任何处理，接着做http请求会失败，可以按照下方的建议处理。
>
>
>
>应对处理每次结束都需要重新走一遍HTTP请求流程
>
>第一种方法：
>
>AT+CIPSHUT		// 关闭移动场景
>
>第二种方法：
>
>AT+CIPSHUT		// 关闭移动场景
>
>AT+CGDCONT=5,"IP",""//请填写实际APN 
>
>AT+CGACT=1,5
>
>第三种方法：
>
>AT+CFUN=0		// 进入飞行模式
>
>AT+CFUN=1		// 退出飞行模式
>
>第四种方法：
>
>AT+RESET		// 重启模块

参考下发流程中收到"+SAPBR 1: DEACT"错误提示，表示PDP被动去激活，为异常处理的触发点。

~~~
AT+HTTPINIT

OK

AT+HTTPPARA="CID",1

OK

AT+HTTPPARA="URL","www.baidu.com"

OK

AT+HTTPACTION=0			// 传入0为GET请求

OK 

+SAPBR 1: DEACT       	// 此处PDP被动去激活

+HTTPACTION: 0,601,0

AT+HTTPTERM

OK                     	// 此处无论返回OK、ERROR还是CME ERROR，都直接跳过，不用做正确性判断

AT+SAPBR=0,1

+CME ERROR: 3         	// 此处无论返回OK、ERROR还是CME ERROR，都直接跳过，不用做正确性判断

--------------------

下方进行异常处理
AT+CIPSHUT				// 关闭移动场景

OK

AT+CGDCONT=5,"IP",""	// 请填写实际APN 

OK

AT+CGACT=1,5			// 激活PDP

OK

AT+HTTPINIT

OK

AT+HTTPPARA="CID",1

OK

AT+HTTPPARA="URL","airtest.openluat.com"

OK

AT+HTTPACTION=0

OK

+HTTPACTION: 0,200,285
~~~



# HTTP POST请求示例

POST请求流程与GET流程基本一致，只有**AT+HTTPACTION**指令参数要从**AT+HTTPACTION=0**变为**AT+HTTPACTION=1**

具体指令和参数使用说明，可参考[AT指令手册](https://doc.openluat.com/article/4985)

~~~
AT+CPIN?

+CPIN: READY    //查询sim卡是否正常

OK

AT+CGATT?

+CGATT: 1        //查询是否附着上数据网络，如果返回+CGATT: 0表示未附着上

OK

AT+SAPBR=3,1,"CONTYPE","GPRS"

OK

AT+SAPBR=3,1,"APN",""    //设置APN，此处""表示使用从网络端自动获取到的APN

OK

AT+SAPBR=1,1             //发起激活PDP的请求

OK

AT+SAPBR=2,1             //注意：此命令仅仅查询PDP地址，可以不执行

+SAPBR: 1,1,"10.159.1.145"    //请求到的PDP地址

OK

AT+HTTPINIT

OK

AT+HTTPPARA="CID",1

OK

AT+HTTPPARA="URL","airtest.openluat.com"

OK

AT+HTTPACTION=1		// POST请求

OK

+HTTPACTION: 0,200,285

AT+HTTPREAD

+HTTPREAD: 285

<!DOCTYPE html>
<html lang="en">


<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    Hello
</body>

</html>
OK
~~~






# HTTPS SSL请求示例

具体指令和参数使用说明，可参考[AT指令手册](https://doc.openluat.com/article/4985)

带SSL证书双向验证功能的HTTPS过程：

> AT+FSCREATE="ca.crt" 				// 创建服务器端CA 证书文件 
> OK
>
> AT+FSCREATE="client.crt" 			// 创建客户端证书文件
> OK 
>
> AT+FSCREATE="client.key" 			// 创建客户端密钥文件 
> OK 
>
> AT+FSWRITE="ca.crt",0,2080,15 	   // 文件长度2080字节只是举例，要根据实际填写。指令发送后会返回">"，随后写入数据
>
> 这里输入CA证书文件 
> OK 
>
> AT+FSWRITE="client.crt",0,128,10 	// 指令发送后会返回">"，随后写入数据
> 这里输入客户端证书文件 
> OK 
>
> AT+FSWRITE="client.key",0,188,10  	// 指令发送后会返回">"，随后写入数据
> 这里输入客户端密钥文件 
> OK 
>
> AT+SAPBR=3,1,"CONTYPE","GPRS" 
> OK 
>
> AT+SAPBR=3,1,"APN","" 				// 设置PDP承载之APN参数 模块注册网络后会从网络自动获取<apn>并激活一个 PDP上下文，用于RNDIS上网使用（此<apn>可以通 过AT+CGDCONT?来查询），所以输入 AT+SAPBR=3,<cid>,"APN","" 即可，模块内部会按 照自动获取的<apn>来设置APN 
> OK 
>
> AT+SAPBR=1,1 
> OK 
>
> AT+SAPBR=2,1 
> +SAPBR: 1,1,010.169.179.213 
>
> OK 
>
> 下发ssl配置请根据实际请求服务器所需要的进行设置
>
> AT+SSLCFG="cacert",153,"ca.crt" 	  // 设置服务器CA 证书 SSL 上下文id，在TCP单链接的情况下缺省为0； 在HTTPS链接下为153，下同 
> OK 
>
> AT+SSLCFG="clientcert",153,"client.crt" 	// 设置客户端证书 
> OK 
>
> AT+SSLCFG="clientkey",153,"client.key" 	// 设置客户端KEY 
> OK 
>
> AT+SSLCFG="seclevel",153,2 			// 设置安全等级
> OK 
>
> AT+SSLCFG="ciphersuite",153,0X0035 	// 设置加密套件 
> OK 
>
> AT+SSLCFG="clientrandom",153,01B12C31 41516171F19202122232425262728293031 323334353637D 	// 设置随机数 
> OK 
>
> AT+HTTPINIT 		// HTTP协议栈初始化
> OK 
>
> AT+HTTPPARA="CID",1 // 设置HTTP会话参数：CID 
> OK 
>
> AT+HTTPPARA="URL","https://**.***.***" // 设置HTTP会话参数：URL 请写具体的网址，而不要照抄 
> OK 
>
> AT+HTTPACTION=0 	// GET 开始 
> OK 
>
> +HTTPACTION:0,200,1348 
>
> +HTTPACTION:0,200,1348 
>
> +HTTPACTION:0,200,1348 … … 	// 出现这些URC上报表明GET数据成功，等待READ 
>
> AT+HTTPREAD 					// 读取从HTTP 服务器GET的数据 
>
> +HTTPREAD:1592 ……………… 	// ...表示HTTP数据 
>
> OK
>
> AT+HTTPTERM 		// 结束HTTP服务
> OK



# 断点续传

在实际的应用场景中，可能需要下载一个非常大的文件，例如几百K字节、几M字节，但是4G模块中HTTP可用的内存缓冲区780EP模块只有4KB左右，当文件大小超过这个缓冲区时，就要使用断点续传功能来分段下载处理了。下面以“下载一个119345字节的文件”为例，来说明如何使用断点续传功能（注意：本示例仅仅演示了正常流程的HTTP AT命令，完整流程以及异常处理流程请参考本文应用流程部分）

~~~=
AT+CGATT?

+CGATT: 1

OK

AT+SAPBR=3,1,"CONTYPE","GPRS"

OK

AT+SAPBR=3,1,"APN",""

OK

AT+SAPBR=1,1

OK

AT+SAPBR=2,1

+SAPBR: 1,1,"10.55.195.210"

OK

AT+HTTPINIT 

OK

AT+HTTPPARA="URL","http://rcems.hzccs.com/upfile/ROBAM-M2-V13704A7-20240308-APP.bin"

OK

AT+HTTPACTION=2		// 使用head方式请求

OK

+HTTPACTION: 2,200,0


AT+HTTPHEAD		

+HTTPHEAD: 247
Accept-Ranges: bytes
ETag: W/"119345-1710117624106"
Last-Modified: Mon, 11 Mar 2024 00:40:24 GMT
Content-Type: application/octet-stream
Content-Length: 119345
Date: Mon, 22 Jul 2024 03:34:24 GMT
Keep-Alive: timeout=20
Connection: keep-alive

OK


//如下指令，表示下载文件的第一个3KB数据

AT+HTTPPARA="BREAK",0

OK

AT+HTTPPARA="BREAKEND",3071

OK

AT+HTTPACTION=0

OK

+HTTPACTION: 0,206,3072


AT+HTTPREAD

+HTTPREAD: 3072

......                          //此处输出3072字节数据

OK			//表示下载文件的第一个3KB数据完成


//如下指令，表示下载文件的第二个3KB数据

AT+HTTPPARA="BREAK",3072

OK

AT+HTTPPARA="BREAKEND",6143

OK

AT+HTTPACTION=0

OK

+HTTPACTION: 0,206,3072


AT+HTTPREAD

+HTTPREAD: 3072

......                          //此处输出3072字节数据

OK		 //表示下载文件的第二个3KB数据完成

//此处参考上文指令，一直循环读取文件的下一个300KB数据，直到读取结束

......

AT+HTTPTERM			// 断开HTTP

OK

~~~





# 常见问题

## 1、HTTP支持多连接吗
目前HTTP仅支持单连接，不支持多连接

## 2、HTTPS如何使用
本文主要描述了基本流程和异常处理，对于HTTPS使用方法没有做过多描述，这一部分，请自行参考[AT指令手册](https://doc.openluat.com/article/4985)HTTP章节下《使用方法举例》中的"带SSL证书验证功能的HTTPS流程"使用方法；支持的SSL参数，请自行参考AT+SSLCFG命令说明
如果SSL的参数配置不变，则每次开机运行过程中，仅设置一次即可

## 3、重试多次PDP，HTTP应用一直连接失败
如果重试多次PDP激活，PDP一直激活失败，或者HTTP一直请求应答失败，则尝试使用如下手段恢复：

​	使用RESET引脚复位模块

​	极端情况下，直接给模块断电，再上电，POWER KEY引脚拉低开机

## 4、HTTP下载的大文件如何可靠的发送给MCU（AT流控）

需要在断点续传流程指令里开头加入AT+IFC的配置指令

AT+HTTPREAD

+HTTPREAD: 3072

......                          //此处输出3072字节数据

OK
…处的3072字节数据，是模块通过UART AT口发送给MCU，在实际传输过程中，由于串口芯片驱动、MCU端的处理能力、波特率的选择都存在不确定性，可能会导致MCU端接收到的数据，实际上没有3072字节，这就要求UART AT口打开流控功能。模块支持硬件流控和软件流控两种：

硬件流控，参考如下步骤操作：
（1） 模块和MCU的UART口，CTS、RTS要交叉相连

（2） MCU端固件要支持并且打开硬流控功能

（3） MCU端要发送AT+IFC=2,2命令到模块端，打开模块端的硬流控功能

软件流控，参考如下步骤操作：
（1） MCU端固件要支持并且打开软流控功能

（2） MCU端要发送AT+IFC=1,1命令到模块端，打开模块端的软流控功能

## 5、为什么我只发了10字节消息，100次却消耗了很多流量？
因为还有HTTP自带的请求头。

## 6、为什么频繁请求会失败?
HTPP连接总数数量有限，且不支持HTTP2多路复用连接，因此建议等一个HTTP连接返回请求结果之后，再去请求下一个连接；不要使用循环定时器方式不断的发起新的HTTP请求。

## 7、如何POST文件?
主要是使用AT+HTTPDATA命令录入文件数据后，发送AT+HTTPACTION=1利用post上传

## 8、数据发送接收缓存问题
AT版本：有缓存机制，内存中有一个的缓冲区（780EP模块AT固件HTTP缓存为4KB），发送和接受使用的是同一块缓冲区，发送和收到数据后，插入此缓冲区，然后通过AT口输出urc，提示收到的数据长度；缓冲区满之后，再收到新数据，会丢弃新收到的数据，并通过AT口输出urc提示出错；需要读取数据时，发送AT+HTTPREAD命令读取，可分段读取，也可全部读取

注意：缓冲区位于内存中，断电或者重启后，缓存表中的数据会被清空；虽然缓冲区可以缓存很多数据，但是建议收到数据时，通过AT+HTTPREAD及时读取出来，以防缓冲区满出错

----

> 合宙支持AT功能的模组型号，除本文介绍的Air780EP外，
> 还有Air780EPA、Air780E、Air780EX、Air724UG、Air201、Air780EQ、Air700ECQ、Air700EAQ、Air780EPT、Air780EPS等型号，
> 本文介绍的HTTP应用流程，同样也适用于这些型号。


![选型手册简洁版01](image/1.jpg)
![选型手册简洁版02](image/2.jpg)
