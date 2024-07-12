
@[TOC]

# errDump

模块功能：系统错误日志管理(强烈建议用户开启此模块的“错误日志上报调试服务器”功能).

错误日志包括四种：

1、系统主任务运行时的错误日志

此类错误会导致软件重启，错误日志保存在/luaerrinfo.txt文件中

2、调用sys.taskInit创建的协程运行过程中的错误日志

此类错误会终止当前协程的运行，但是不会导致软件重启，错误日志保存在/lib_err.txt中

3、调用errDump.appendErr或者sys.restart接口保存的错误日志

此类错误日志保存在/lib_err.txt中

4、调用errDump.setNetworkLog接口打开网络异常日志功能后，会自动保存最近几种网络异常日志

错误日志保存在/lib_network_err.txt中

5、底层固件的死机信息

其中2和3保存的错误日志，最多支持5K字节

每次上报错误日志给调试服务器之后，会清空已保存的日志

## errDump.appendErr(s)

追加错误信息到LIB_ERR_FILE文件中（文件最多允许存储5K字节的数据）

* 参数

|名称|传入值类型|释义|
|-|-|-|
|s|string|用户自定义的错误信息，errDump功能模块会对此错误信息做如下处理：<br>1、重启后会通过Luat下载调试工具输出，在trace中搜索errDump.libErr，可以搜索到错误信息<br>2、如果用户调用errDump.request接口设置了错误信息要上报的调试服务器地址和端口，则每次重启会自动上报错误信息到调试服务器<br>3、如果用户调用errDump.request接口设置了定时上报，则定时上报时会上报错误信息到调试服务器<br>其中第2和第3种情况，上报成功后，会自动清除错误信息|

* 返回值

bool result，true表示成功，false或者nil表示失败

* 例子

```lua
errDump.appendErr("net working timeout!")
```

---

## errDump.setNetworkLog(flag)

配置网络错误日志开关

* 参数

|名称|传入值类型|释义|
|-|-|-|
|flag|bool|**可选参数，默认为`nil`** 是否打开网络错误日志开关，true为打开，false或者nil为关闭|

* 返回值

无

* 例子

```lua
errDump.setNetworkLog(true)
```

---

## errDump.request(addr, period, flag)

配置调试服务器地址，启动错误信息上报给调试服务器的功能，上报成功后，会清除错误信息

* 参数

|名称|传入值类型|释义|
|-|-|-|
|addr|string|调试服务器地址信息，支持http，udp，tcp<br>1、如果调试服务器使用http协议，终端将采用POST命令，把错误信息上报到addr指定的URL中，addr的格式如下<br>(除protocol和hostname外，其余字段可选；目前的实现不支持hash)<br>|------------------------------------------------------------------------------|<br>| protocol |||   auth    |      host       |           path            | hash  |<br>|----------|||-----------|-----------------|---------------------------|-------|<br>|          |||           | hostname | port | pathname |     search     |       |<br>|          |||           |----------|------|----------|----------------|       |<br>"   http(s)   :// user:pass @ host.com : 8080   /p/a/t/h ?  query=string  # hash  " <br>|          |||           |          |      |          |                |       |<br>|------------------------------------------------------------------------------|<br>2、如果调试服务器使用udp协议，终端将错误信息，直接上报给调试服务器，调试服务器收到信息后，要回复大写的OK；addr格式如下：<br>|----------|||----------|------|<br>| protocol ||| hostname | port |<br>|          |||----------|------|<br>"   udp    :// host.com : 8081 | <br>|          |||          |      |<br>|------------------------------|<br>3、如果调试服务器使用tcp协议，终端将错误信息，直接上报给调试服务器；addr格式如下：<br>|----------|||----------|------|<br>| protocol ||| hostname | port |<br>|          |||----------|------|<br>"   tcp    :// host.com : 8082 | <br>|          |||          |      |<br>|------------------------------||
|period|number|**可选参数，默认为`600000`** 单位毫秒，定时检查错误信息并上报的间隔|
|flag|bool|当使用合宙调试服务器时，此参数填为true；使用自定义服务器时，此参数可省略|

* 返回值

bool result，成功返回true，失败返回nil

* 例子

```lua
errDump.request("http://www.user_server.com/errdump")
errDump.request("udp://www.user_server.com:8081")
errDump.request("tcp://www.user_server.com:8082")
errDump.request("tcp://www.user_server.com:8082",6*3600*1000)
errDump.request("udp://www.hezhou_server.com:8083",6*3600*1000,true)
```

---
