# 780E开发板MQTT示例

- 本文档适用于780E开发板

- 关联文档和使用工具

  - [LuatOS-Soc固件获取](https://gitee.com/openLuat/LuatOS/releases)

  - [mqtt-demo](https://gitee.com/openLuat/LuatOS/tree/master/demo/mqtt)

  - [程序中使用函数讲解](https://wiki.luatos.com/api/mqtt.html)
  
  - [Luatools下载调试工具](https://gitee.com/openLuat/luatos-doc-pool/blob/master/doc/%E5%BC%80%E5%8F%91%E5%B7%A5%E5%85%B7%E5%8F%8A%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E/Luatools%E4%B8%8B%E8%BD%BD%E8%B0%83%E8%AF%95%E5%B7%A5%E5%85%B7.md)



### 1、环境准备

1、780E开发板一套，记得装一个能用的sim卡

![](..\image\LuatOS开发资料\示例\MQTT.fx\开发板.jpg)

### 2、配置连接MQTT.fx

打开mqtt.fx软件准备配置连接文件

![](..\image\LuatOS开发资料\示例\MQTT.fx\mqtt.fx配置1-1.png)

![](..\image\LuatOS开发资料\示例\MQTT.fx\mqtt.fx配置1-2.png)

打开程序，匹配mqtt连接的参数



![](..\image\LuatOS开发资料\示例\MQTT.fx\mqtt.fx配置1.png)

![](..\image\LuatOS开发资料\示例\MQTT.fx\mqtt.fx配置2.png)

连接服务器：

![](..\image\LuatOS开发资料\示例\MQTT.fx\mqtt.fx配置3.png)

### 3、固件及脚本下载

![](..\image\LuatOS开发资料\示例\MQTT.fx\Luatools下载.png)

### 4、效果展示

订阅模块发布的消息

![](..\image\LuatOS开发资料\示例\MQTT.fx\模块发布消息.png)

给模块发布消息

![](..\image\LuatOS开发资料\示例\MQTT.fx\模块订阅消息.png)



