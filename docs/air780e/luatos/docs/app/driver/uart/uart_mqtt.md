# MQTT-UART透传

## 介绍

MQTT-UART串口透传功能是一种将MQTT协议与UART串口通信相结合的技术，它允许用户通过MQTT协议将数据发送到远程服务器，并通过UART串口将数据传输到本地设备。这种功能在物联网（IoT）领域具有广泛的应用，例如智能家居、工业自动化、智能农业等。通过MQTT-UART串口透传功能，用户可以轻松实现设备之间的数据传输和通信，从而提高系统的可靠性和灵活性。

### MQTT协议有什么优缺点？

MQTT（Message Queuing Telemetry Transport）是一种轻量级的消息传递协议，具有以下优点：

1. 轻量级：MQTT协议的设计目标是轻量级，因此它的消息格式非常简单，消息头只有两个字节，这使得它非常适合在资源受限的设备上使用。

2. 可靠性：MQTT协议支持消息的确认和重传机制，确保消息能够可靠地传递到目标设备。

3. 网络适应性：MQTT协议支持多种网络协议，包括TCP、UDP等，这使得它可以在各种网络环境下使用。

4. 灵活性：MQTT协议支持发布/订阅模式，这使得消息的发布者和订阅者可以灵活地选择消息的发送和接收方式。

然而，MQTT协议也有一些缺点：

1. 传输效率较低：由于MQTT协议的消息格式较复杂，因此在传输大量数据时，其效率可能会低于TCP协议。

2. 不支持流式传输：MQTT协议不支持流式传输，这意味着如果需要连续传输大量数据，可能需要将数据分割成多个消息进行传输。

3. 安全性较低：MQTT协议本身不提供加密和认证机制，因此需要依赖其他安全机制来保护数据传输的安全性。

4. 服务器负载较高：由于MQTT协议支持大量的客户端连接，因此服务器需要处理大量的消息和连接，这可能会增加服务器的负载。

## 串口需要做的准备

### 1.初始化串口

本文示例：串口使用MAIN_UART(uart1)

~~~lua
local uartid = 1 -- 使用uart1，可根据实际设备选取不同的uartid

--初始化 参数都可以根据实施情况修改
uart.setup(
    uartid,--串口id
    115200,--波特率
    8,--数据位
    1--停止位
)
~~~

### 2.注册接收数据的回调函数

在模块收到从串口端过来的数据后，发布一条 "mqtt_pub" 消息，并携带要发布到哪个mqtt主题和具体数据两个参数。

~~~lua
uart.on(uartid, "receive", function(id, len)
    local data = ""
    while 1 do
        local tmp = uart.read(uartid)
        if not tmp or #tmp == 0 then
            break
        end
        data = data .. tmp
    end
    log.info("uart", "uart收到数据长度", #data)

    -- 告诉另一个正在等待接收"mqtt_pub"消息的task，要往MQTT服务器发布消息了
    sys.publish("mqtt_pub", pub_topic, data)
end)
~~~

## MQTT连接

### 1.建立MQTT链接

如果没有验证TCP服务的测试环境，或者连接其他TCP服务器出现了问题，想要另外找一个服务器做对比。
那可以使用合宙自建的MQTT测试服务器。

> host: lbsmqtt.airm2m.com
> port: 1884
> client: 任意（但注意不要用太简单，容易冲突的字符串）
> username: 任意
> password: 任意

~~~lua
local mqtt_host = "lbsmqtt.airm2m.com"
local mqtt_port = 1884
local mqtt_isssl = false
local client_id = nil
local user_name = "user"
local password = "password"
sys.taskInit(function()

    log.info("等待联网")
    -- 默认等到联网成功在往下执行
    sys.waitUntil("IP_READY")

    mqttc = mqtt.create(nil, mqtt_host, mqtt_port, mqtt_isssl)

    mqttc:auth(client_id,user_name,password) -- client_id必填,其余选填
    mqttc:keepalive(120) -- 设置心跳包时间，120s
    mqttc:autoreconn(true, 3000) -- 自动重连机制
    mqttc:connect() -- 连接mqtt
end)
~~~

### 2.注册MQTT事件回调函数

~~~lua
mqttc:on(function(mqtt_client, event, data, payload)
    log.info("mqtt", "event", event, mqtt_client, data, payload)
    
    -- 连接服务器成功
    if event == "conack" then
        sys.publish("mqtt_conack")
        mqtt_client:subscribe(sub_topic)--单主题订阅
        -- mqtt_client:subscribe({[topic1]=1,[topic2]=1,[topic3]=1})--多主题订阅，通过table的格式
    -- 接收到服务端的数据
    elseif event == "recv" then
        log.info("mqtt", "downlink", "topic", data, "payload", payload)
        sys.publish("mqtt_payload", data, payload)
    -- 向服务端发送数据的事件
    elseif event == "sent" then
        -- log.info("mqtt", "sent", "pkgid", data)
    -- 断开了连接
    elseif event == "disconnect" then
        -- 这里的逻辑处理也可以按业务需求改
        log.info("连接断开!")
    end
end)
~~~

### 3.将服务器接收到的数据发送至串口输出

~~~lua
sys.subscribe("mqtt_payload", function(topic, payload)
    log.info("uart", "uart发送数据长度", #payload)
    uart.write(uartid, payload)
end)
~~~

## 完整实例

~~~lua
-- Luatools需要PROJECT和VERSION这两个信息
PROJECT = "uart_mqtt"
VERSION = "1.0.0"

log.info("main", PROJECT, VERSION)

-- 引入必要的库文件(lua编写), 内部库不需要require
sys = require("sys")

if wdt then
    --添加硬狗防止程序卡死，在支持的设备上启用这个功能
    wdt.init(9000)--初始化watchdog设置为9s
    sys.timerLoopStart(wdt.feed, 3000)--3s喂一次狗
end

--根据自己的服务器修改以下参数
local mqtt_host = "lbsmqtt.airm2m.com"
local mqtt_port = 1884
local mqtt_isssl = false
local client_id = nil
local user_name = "user"
local password = "password"

local pub_topic = "/luatos/pub/"
local sub_topic = "/luatos/sub/"

local mqttc = nil

sys.taskInit(function() 
    log.info("等待联网")
    -- 默认等到联网成功在往下执行
    sys.waitUntil("IP_READY")
    -- 获取模块的IMEI
    local imei = mobile.imei()
    client_id = imei    -- 用IMEI作为client_id

    -- 在pub和sub的主题后添加imei，确保每个设备可以单独处理与自己对应的消息收发
    pub_topic = pub_topic .. imei
    sub_topic = sub_topic .. imei

    -- 打印一下上报(pub)和下发(sub)的topic名称
    -- 上报: 设备 ---> 服务器
    -- 下发: 设备 <--- 服务器
    -- 可使用mqtt.x等客户端进行调试
    log.info("mqtt", "pub", pub_topic)
    log.info("mqtt", "sub", sub_topic)

    mqttc = mqtt.create(nil, mqtt_host, mqtt_port, mqtt_isssl)

    mqttc:auth(client_id,user_name,password) -- client_id必填,其余选填
    mqttc:keepalive(120) -- 设置心跳包时间，120s
    mqttc:autoreconn(true, 3000) -- 自动重连机制

    mqttc:on(function(mqtt_client, event, data, payload)
        log.info("mqtt", "event", event, mqtt_client, data, payload)
        
        -- 连接服务器成功
        if event == "conack" then
            sys.publish("mqtt_conack")
            mqtt_client:subscribe(sub_topic)--单主题订阅
            -- mqtt_client:subscribe({[topic1]=1,[topic2]=1,[topic3]=1})--多主题订阅，通过table的格式
        -- 接收到服务端的数据
        elseif event == "recv" then
            log.info("mqtt", "downlink", "topic", data, "payload", payload)
            sys.publish("mqtt_payload", data, payload)
        -- 向服务端发送数据的事件
        elseif event == "sent" then
            -- log.info("mqtt", "sent", "pkgid", data)
        -- 断开了连接
        elseif event == "disconnect" then
            -- 这里的逻辑处理也可以按业务需求改
            log.info("连接断开!")
        end
    end)

    mqttc:connect()     -- 连接mqtt
    sys.waitUntil("mqtt_conack")    -- 等待连接成功的消息
    while true do
        -- 演示等待其他task发送过来的上报信息
        local ret, topic, data, qos = sys.waitUntil("mqtt_pub", 300000)
        if ret then
            -- 提供关闭本while循环的途径, 不需要可以注释掉
            if topic == "close" then break end
            mqttc:publish(topic, data, qos)
        end
        -- 如果没有其他task上报, 可以写个空等待
        --sys.wait(60000000)
    end
    mqttc:close()
    mqttc = nil
end)

local uartid = 1 -- 根据实际设备选取不同的uartid

--初始化
uart.setup(
    uartid,--串口id
    115200,--波特率
    8,--数据位
    1--停止位
)

uart.on(uartid, "receive", function(id, len)
    local data = ""
    while 1 do
        local tmp = uart.read(uartid)
        if not tmp or #tmp == 0 then
            break
        end
        data = data .. tmp
    end
    log.info("uart", "uart收到数据长度", #data)
    sys.publish("mqtt_pub", pub_topic, data)
end)

sys.subscribe("mqtt_payload", function(topic, payload)
    log.info("uart", "uart发送数据长度", #payload)
    uart.write(uartid, payload)
end)

-- 用户代码已结束---------------------------------------------
-- 结尾总是这一句
sys.run()
-- sys.run()之后后面不要加任何语句!!!!!
~~~
