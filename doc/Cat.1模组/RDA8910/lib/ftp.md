
@[TOC]

# ftp

模块功能：FTP客户端

## ftp.command(command, timeout)

FTP客户端命令

* 参数

|名称|传入值类型|释义|
|-|-|-|
|command|string|命令，例如"PWD","HELP","SYST"|
|timeout|number|**可选参数，默认为`0`** 接收超时时间，单位毫秒|

* 返回值

string,string,返回 response_code, response_message

* 例子

无

---

## ftp.pasv_connect(timeout) (local函数 无法被外部调用)

连接到PASV接口

* 参数

|名称|传入值类型|释义|
|-|-|-|
|timeout|number|**可选参数，默认为`0`** 接收超时时间，单位毫秒|

* 返回值

string,string,返回 response_code, response_message

* 例子

无

---

## ftp.login(ftp_mode, host, port, username, password, timeout, ssl, cert)

FTP客户端登录

* 参数

|名称|传入值类型|释义|
|-|-|-|
|ftp_mode|string|FTP模式"PASV"or"PORT",默认PASV:被动模式,PORT:主动模式(暂时仅支持被动模式)|
|host|string|ip地址|
|port|string|端口,默认21|
|username|string|用户名|
|password|string|密码|
|timeout|number|**可选参数，默认为`0`** 接收超时时间，单位毫秒|
|ssl|bool|可选参数，默认为nil，ssl，是否为ssl连接，true表示是，其余表示否|
|cert|table|可选参数，默认为nil，cert，ssl连接需要的证书配置，只有ssl参数为true时，才参数才有意义，cert格式如下：<br>{<br>caCert = "ca.crt", --CA证书文件(Base64编码 X.509格式)，如果存在此参数，则表示客户端会对服务器的证书进行校验；不存在则不校验<br>clientCert = "client.crt", --客户端证书文件(Base64编码 X.509格式)，服务器对客户端的证书进行校验时会用到此参数<br>clientKey = "client.key", --客户端私钥文件(Base64编码 X.509格式)<br>clientPassword = "123456", --客户端证书文件密码[可选]<br>}|

* 返回值

string,string,返回 response_code, response_message

* 例子

无

---

## ftp.upload(remote_file, local_file, timeout)

FTP客户端文件上传

* 参数

|名称|传入值类型|释义|
|-|-|-|
|remote_file|string|远程文件名|
|local_file|string|本地文件名|
|timeout|number|**可选参数，默认为`0`** 接收超时时间，单位毫秒|

* 返回值

string,string,返回 response_code, response_message

* 例子

无

---

## ftp.download(remote_file, local_file, timeout)

FTP客户端文件下载

* 参数

|名称|传入值类型|释义|
|-|-|-|
|remote_file|string|远程文件名|
|local_file|string|本地文件名|
|timeout|number|**可选参数，默认为`0`** 接收超时时间，单位毫秒|

* 返回值

string,string,返回 response_code, response_message

* 例子

无

---

## ftp.checktype(mode, timeout)

设置FTP传输类型 A:ascii I:Binary

* 参数

|名称|传入值类型|释义|
|-|-|-|
|mode A:ascii|string|I:Binary|
|timeout|number|**可选参数，默认为`0`** 接收超时时间，单位毫秒|

* 返回值

string,string,返回 response_code, response_message

* 例子

无

---

## ftp.pwd(timeout)

显示当前工作目录

* 参数

|名称|传入值类型|释义|
|-|-|-|
|timeout|number|**可选参数，默认为`0`** 接收超时时间，单位毫秒|

* 返回值

string,string,返回 response_code, response_message

* 例子

无

---

## ftp.cwd(path, timeout)

更改工作目录

* 参数

|名称|传入值类型|释义|
|-|-|-|
|path|string|工作目录|
|timeout|number|**可选参数，默认为`0`** 接收超时时间，单位毫秒|

* 返回值

string,string,返回 response_code, response_message

* 例子

无

---

## ftp.cdup(timeout)

回到上级目录

* 参数

|名称|传入值类型|释义|
|-|-|-|
|timeout|number|**可选参数，默认为`0`** 接收超时时间，单位毫秒|

* 返回值

string,string,返回 response_code, response_message

* 例子

无

---

## ftp.mkd(path, timeout)

创建目录

* 参数

|名称|传入值类型|释义|
|-|-|-|
|path|string|目录|
|timeout|number|**可选参数，默认为`0`** 接收超时时间，单位毫秒|

* 返回值

string,string,返回 response_code, response_message

* 例子

无

---

## ftp.list(file_irectory, timeout)

列出目录列表或文件信息

* 参数

|名称|传入值类型|释义|
|-|-|-|
|file_irectory|string|目录或文件|
|timeout|number|**可选参数，默认为`0`** 接收超时时间，单位毫秒|

* 返回值

string,string,返回 response_code, response_message

* 例子

无

---

## ftp.deletefolder(file_irectory, timeout)

删除目录

* 参数

|名称|传入值类型|释义|
|-|-|-|
|file_irectory|string|路径目录|
|timeout|number|**可选参数，默认为`0`** 接收超时时间，单位毫秒|

* 返回值

string,string,返回 response_code, response_message

* 例子

无

---

## ftp.deletefile(file_irectory, timeout)

删除文件

* 参数

|名称|传入值类型|释义|
|-|-|-|
|file_irectory|string|路径文件(相对/绝对)|
|timeout|number|**可选参数，默认为`0`** 接收超时时间，单位毫秒|

* 返回值

string,string,返回 response_code, response_message

* 例子

无

---
