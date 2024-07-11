@[TOC]

# rtos
系统相关接口
## rtos.receive(timeout)

接收消息

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|timeout|number|超时返回以毫秒为单位，可以用#rtos.INF_TIMEOUT#表示阻塞等待消息|  |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|msg,msgpara|table/number|如果msg为table类型，msg根据不同的消息msg.id会有不同的数据，如果msg为number类型，msg根据不同的消息msg会有不同的数据。具体的数据如下|   |

**例子**

```lua
 msg,msgpara = rtos.receive(timeout)
--[[
返回值：table或者number类型,如果msg为table类型，msg根据不同的消息msg.id会有不同的数据，如果msg为number类型，msg根据不同的消息msg会有不同的数据。具体的数据如下 

    1.rtos.MSG_TIMER 定时器超时消息：
	msg.timer_id或者 msgpara 为超时的定时器 id
	
	2.rtos.MSG_UART_RXDATA 串口 ATC 数据提醒：
	msg.uart_id 或者msgpara为收到的数据的串口id或者atc,收到该消息后可以通过uart.read接口读取数据

	3.rtos.MSG_KEYPAD 键盘消息,必须初始化按键(#rtos.init_module#)后才会有键盘消息：
	msg.pressed 按键按下/弹起
	msg.key_matrix_row 按键所在行值
	msg.key_matrix_col 按键所在列值

	4.rtos.WAIT_MSG_TIMEOUT 等待消息超时

	5.rtos.MSG_INT 中断消息：
	msg.int_id 中断 id
	msg.int_resnum 中断 pin 脚编号

	6.rtos.MSG_PMD 电源管理消息：
	msg.present 电池在位状态
	msg.level 百分比 0-100
	msg.voltage 电池电压
	msg.charger 充电器在位状态
	msg.state 充电状态:0-不在充电 1-充电中 2-充电停止
]]

```
此API仅推荐给lib脚本使用，不推荐用户应用脚本使用；
用户应用脚本可以直接使用sys API，链接为：[sys.run](https://doc.openluat.com/wiki/21?wiki_page_id=2295#sysrun_403 "sys.run")

---



## rtos.sleep(millisecond)

延时函数

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|millisecond|number|延时时间(以毫秒为单位)|  |

**返回值**

无

---



## rtos.timer_start(timer_id,timerout)

启动定时器

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|timer_id|number|定时器id(可以是任意整数)或者定时器到时msg.timer_id值为启动时定时器|   |
|timeout|number|定时器延时时间(以毫秒为单位)|   |

**返回值**

无

此API仅推荐给lib脚本使用，不推荐用户应用脚本使用；
用户应用脚本可以直接使用sys API，链接为：[sys.timerStart](https://doc.openluat.com/wiki/21?wiki_page_id=2295#systimerStartfnc_ms__213 "sys.timerStart")

---



## rtos.timer_stop(timer_id)

停止定时器

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|timer_id|number|输入与启动定时器时定义的 id 即可停止定时器|   |

**返回值**

无

此API仅推荐给lib脚本使用，不推荐用户应用脚本使用；
用户应用脚本可以直接使用sys API，链接为：[sys.timerStop](https://doc.openluat.com/wiki/21?wiki_page_id=2295#systimerStopval__154 "sys.timerStop")

---



## rtos.init_module(modId, ...)

初始化外设模块，目前支持rtos.MOD_KEYPAD，rtos.MOD_ALARM对应的外部消息处理函数通过rtos.on注册。

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|modId|number|模块ID|  |
|...|number|初始化参数|   |

**返回值**

无

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2304 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2179 "示例")

---



## rtos.poweron_reason()

读取开机原因值

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|rtos.POWERON_KEY(=0)|number|按键开机|   |
|rtos.POWERON_CHARGER(=1)|number|充电开机| |
|rtos.POWERON_ALARM(=2)|number|闹钟开机| |
|rtos.POWERON_RESTART(=3)|number|软件（异常）重启开机| |
|rtos. POWERON_EXCEPTION(=4)|number|看门狗重启| |
|5|number|硬件重启|  |

**例子**

```lua
    reason=rtos.poweron_reason()

```
示例参考：[示例](https://doc.openluat.com/wiki/21?wiki_page_id=2161 "示例")

---



## rtos.poweron(flag)

是否启动 GSM 开机

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|flag|number|0表示不启动系统/1表示启动系统|0/1|

**返回值**

无
此API仅推荐给lib脚本使用，不推荐用户应用脚本使用。

---



## rtos.poweroff([type])

软件关机

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|可选参数，默认为0|number|0正常关机；1关机充电|1/0|

**返回值**

无
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/blob/master/script_LuaTask/lib/powerKey.lua "示例")

---



## rtos.restart()

软件重启

**参数**

无

**返回值**

无

此API仅推荐给lib脚本使用，不推荐用户应用脚本使用；
用户应用脚本可以直接使用sys API，链接为：[sys.restart](https://doc.openluat.com/wiki/21?wiki_page_id=2295#sysrestartr_7 "sys.restart")


---



## rtos.tick()

获取系统tick

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|系统启动后的计数个数|number$result|单位为5ms|0-5d638865→-5d638865-0|

**例子**

```lua
--[[
    返回值的变化：从0递增到5d638865，溢出变成-5d638865，慢慢增加到0;
]]

```
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/blob/master/script_LuaTask/demo/fs/testFs2sysperform.lua "示例")

---



## rtos.set_alarm(on,year,month,day,hour,min,sec)

打开/关闭闹钟

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|on|bool|1表示打开/0表示关闭|  |
|year|number|闹钟日期-年|   |
|month|number|闹钟日期-月|   |
|day|number|闹钟日期-日|   |
|hour|number|闹钟时间-小时|   |
|min|number|闹钟时间-分钟|   |
|sec|number|闹钟时间-秒|   |

**返回值**

无

[示例](https://doc.openluat.com/wiki/21?wiki_page_id=2161 "示例")

---



## rtos.keypad_state(param1, param2)

powerKey按键状态获取

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|param1|number|   |0xff|
|param2|number|   |0xff |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0表示低，按键处于按下状态|  |
|result|number|1表示高，按键处于抬起状态|  |
|result|number|表示暂不支持|  |

**例子**

```lua
    level = rtos.keypad_state(0xff, 0xff)

```

---



## rtos.get_env_usage()

获取 lua 任务消息队列的使用百分比

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|percentage|number|百分比(例如使用了80%,则percentage为80)|0-100%|

**例子**

```lua
    percentage=rtos.get_env_usage()

```

---



## rtos.get_version()

获取底层固件版本号

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|string|底层固件Core版本号|   |

示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/blob/master/script_LuaTask/demo/audio/testAudio.lua "示例")

---



## rtos.get_hardware()

获取硬件版本号

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|string|获取模块硬件版本号|   |

---



## rtos.set_trace(v, uartid)

设置trace开关和端口

**参数**

无

**返回值**

无

---



## rtos.get_fs_free_size(mode,formatKb,&fs_param)

获取文件系统剩余空间

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|param1|string|设备名称|0(本地空间),1(SD卡),2(U盘),3(外挂flash，LCD复用管脚，V_LCD供电),4(外挂flash，使用GPIO pin脚复用，V_PAD_1V8供电)|
|param2|string|返回值单位|1(返回值单位kb),0(返回值单位Bytes)|
|param3|string|外挂flash文件系统路径|根据具体路径进行写入|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|文件系统剩余空间，单位Bytes|   |

**例子**

```lua
--[[
    当mode=0时 本地空间
    rtos.get_fs_free_size()

    当mode=1时 SD卡 
    当mode=2时 U盘  
    当mode=3时 外挂flash，LCD复用管脚，V_LCD供电
    param3为外挂flash文件系统具体路径
    当mode=4时 外挂flash，GPIO pin脚复用，V_PAD_1V8供电
    param3为外挂flash文件系统具体路径
    rtos.get_fs_free_size(1，1)
    rtos.get_fs_free_size(3，1，"/ext1")
  ]]

```
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/msc "示例")

---



## rtos.get_fs_total_size(param1,param2,param3)

获取文件系统总空间

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|param1|string|设备名称|0(本地空间),1(SD卡),2(U盘),3(外挂flash，LCD复用管脚，V_LCD供电),4(外挂flash，使用GPIO pin脚复用，V_PAD_1V8供电)|
|param2|string|返回值单位|1(返回值单位kb),0(返回值单位Bytes)|
|param3|string|外挂flash文件系统路径|根据具体路径进行写入|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|文件系统剩余空间，单位Bytes|   |

**例子**

```lua
--[[
    当mode=0时 本地空间
    rtos.get_fs_free_size()

    当mode=1时 SD卡 
    当mode=2时 U盘  
    当mode=3时 外挂flash，LCD复用管脚，V_LCD供电
    param3为外挂flash文件系统具体路径
    当mode=4时 外挂flash，GPIO pin脚复用，V_PAD_1V8供电
    param3为外挂flash文件系统具体路径
    rtos.get_fs_total_size(1,1)
    rtos.get_fs_total_size(3,1,"/ext1")
  ]]

```
示例参考：[示例](https://gitee.com/openLuat/Luat_Lua_Air724U/tree/master/script_LuaTask/demo/msc "示例")

---



## rtos.make_dir(path)

创建目录

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|path|string|文件夹路径|  |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|bool|true表示创建成功，false表示失败|true/false|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1956 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2172 "示例")

---



## rtos.remove_dir(path)

删除文件夹

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|path|string|文件夹路径|  |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|bool|true表示删除成功，false表示失败|true/false|

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1956 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2172 "示例")

---



## rtos.rename_dir(oldpath,newpath)

重命名文件夹

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|oldpath|string|文件夹路径|  |
|newpath|string|文件夹路径||

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|0表示修改成功||

详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=1956 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2172 "示例")

---



## rtos.set_time(year,month,day,hour,min,sec)

设置系统时间

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|year|number|闹钟日期-年|  |
|month|number|闹钟日期-月|  |
|day|number|闹钟日期-日|  |
|hour|number|闹钟时间-小时|  |
|min|number|闹钟时间-分钟|  |
|sec|number|闹钟时间-秒|  |

**返回值**

无

---



## rtos.fota_start()

远程升级初始化

**参数**

无

**返回值**

无

此API仅推荐给lib脚本使用，不推荐用户应用脚本使用；
用户应用脚本可以直接使用update API，链接为：[update.request](https://doc.openluat.com/wiki/21?wiki_page_id=2297#updaterequestcbFnc_url_period_redir_7 "update.request")

---



## rtos.fota_process(data, len)

远程升级

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|data|string|从网络端下载的固件包，部分数据 ，string类型，二进制数据流|   |
|len|number|差分包的总长度(不是本次写入的数据长度)|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|固件数据包处理正常，可以继续下载|0|
|result|number|内存不足|-99|
|result|number|固件校验错误|-96|
|result|number|固件写入错误|-94|

**例子**

```lua
--[[
    注意:当返回值为-96时，可能是由于多种原因造成的。
    但是返回-96时就是固件出错了，更换新固件即可。
]]

```

此API仅推荐给lib脚本使用，不推荐用户应用脚本使用；
用户应用脚本可以直接使用update API，[update.setDownloadProcessCbFnc](https://doc.openluat.com/wiki/21?wiki_page_id=2297#updatesetDownloadProcessCbFnccbFnc_36 "update.setDownloadProcessCbFnc")

---



## rtos.fota_end()

远程升级结束，不管升级成功还是失败，都要调用一下该接口。

**参数**

无

**返回值**

无

**例子**

```lua
--[[
    注意:固件下载成功后，需要调用一下rtos.restart()接口，进行固件更新
]]

```
此API仅推荐给lib脚本使用，不推荐用户应用脚本使用；
用户应用脚本可以直接使用update API，链接为：[update.request](https://doc.openluat.com/wiki/21?wiki_page_id=2297#updaterequestcbFnc_url_period_redir_7 "update.request")

---



## rtos.get_fatal_info()

获取异常死机信息

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|获取线程的状态信息| |

此API仅推荐给lib脚本使用，不推荐用户应用脚本使用；
用户应用脚本可以直接使用errDump API，链接为：[errDump](https://doc.openluat.com/wiki/21?wiki_page_id=2271 "errDump")

---



## rtos.remove_fatal_info()

清除异常死机信息

**参数**

无

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|number|移除线程的状态信息| |

此API仅推荐给lib脚本使用，不推荐用户应用脚本使用；
用户应用脚本可以直接使用errDump API，链接为：[errDump](https://doc.openluat.com/wiki/21?wiki_page_id=2271 "errDump")

---



## rtos.toint64(str,typ)

将数字字符串转为int64类型数据

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|str|string|待转换的字符串|  |
|typ|string|"big"或"little"(表示大端还是小端)|big/little|

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|string|int64数据的二进制内容字符串|   |

---



## rtos.hextodec(str)

将16进制字符串转为10进制字符串

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|str|string|待转换的字符串|   |

**返回值**

|返回值|类型|释义|取值|
|-|-|-|-|
|result|string|int64数据的十进制内容字符串|   |

---



## rtos.openSoftDog(timeout))

打开看门狗接口

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|timeout|number|超时时间|  |

**返回值**

无

参考示例：[示例](https://doc.openluat.com/wiki/21?wiki_page_id=2196 "示例")

---



## rtos.eatSoftDog()

喂狗接口

**参数**

无

**返回值**

无

参考示例：[示例](https://doc.openluat.com/wiki/21?wiki_page_id=2196 "示例")

---



## rtos.closeSoftDog()

关闭看门狗接口

**参数**

无

**返回值**

无

参考示例：[示例](https://doc.openluat.com/wiki/21?wiki_page_id=2196 "示例")

---



## rtos.notify_sim_detect(nsim,connect)

sim卡热插拔

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|nsim|number|sim卡number，sim0为1，sim1为2|1/2|
|connect|number|0代表拔卡，1代表插卡|0/1|

**返回值**

无

**例子**

```lua
--[[
    硬件上将sim卡的插拔和某个IO关联起来，软件上将这个IO配置为中断，
    当sim卡插拔时，产生IO中断，根据中断状态，调用rtos.notify_sim_detect接口来实现热插拔的检测
]]

```
详细指南：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2026#SIM_126 "指南")

---



## rtos.on(msgId, cbFnc)

注册外部消息的处理函数

**参数**

|参数|类型|释义|取值|
|-|-|-|-|
|msgId|number|外部消息ID|   |
|cbFnc|number|外部消息的处理函数|    |

**返回值**

无

**例子**

```lua
--[[
    一般来说，用户在自己的应用脚本中不需要使用此接口，一些必须的外部消息处理逻辑在lib脚本中已经封装实现
    外部消息的定义参考：
        http://doc.openluat.com/wiki/6?wiki_page_id=1730
        http://doc.openluat.com/wiki/6?wiki_page_id=1769
        有定时器消息，串口消息，socket消息，音频播放消息等等
]]

```
详细指南和示例参考：[指南](https://doc.openluat.com/wiki/21?wiki_page_id=2304 "指南") [示例](https://doc.openluat.com/wiki/21?wiki_page_id=2179 "示例")

---



