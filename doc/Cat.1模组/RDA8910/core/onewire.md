@[TOC]

# onewire
lua.onewire 单总线传感器库，支持ds18b20和dht11（LuatOSVer>=3106）
## onewire_status常量

onewire状态

| **常量**                              | **说明**                    |
| ------------------------------------  | --------------------------- |
| onewire.OK                            | 读取完成，数据有效           |
| onewire.NOT_SENSOR                    | 未检测到传感器,请检查硬件连接 |
| onewire.READ_ERROR                    | 读取数据过程错误             |
| onewire.CHECK_ERROR                   | 数据校验错误                 |

---



## onewire.read_ds18b20(pio)

读取ds18b20温度值数字，精确到0.0625。结果被扩大10000倍

**参数**

| **参数**    | **释义**                                |
| -----------  | --------------------------------------- |
| pio        | gpio编号                              	|

**返回值**

| **返回值**    | **释义**                                | **取值**                                |
| -----------  | --------------------------------------- | --------------------------------------- |
| status        | 读取的状态                              | 见onewire_status常量                 |
| temperature   | 温度值                                  | 整数              |

**例子**

```lua
	local function testds18b20()
		sys.wait(5000)
		-- 个别gpio需要打开电压域才可以正常使用
		pmd.ldoset(15,pmd.LDO_VLCD)
		
		while true do
			local status,temperature = onewire.read_ds18b20(pio.P0_0)
			if status == onewire.OK then
				log.info("18b20","temperature:",temperature/10000)
			elseif status == onewire.NOT_SENSOR then
				log.info("18b20","未检测到传感器,请检查硬件连接")
			elseif status == onewire.READ_ERROR then
				log.info("18b20","读取数据过程错误")
			elseif status == onewire.CHECK_ERROR then
				log.info("18b20","数据校验错误")
			end
			sys.wait(1000)
			
                        		status,serial_info = onewire.read_ds18b20_serial(pio.P0_19)
			if status == onewire.OK then
				log.info("18b20",string.toHex(serial_info))
			elseif status == onewire.NOT_SENSOR then
				log.info("18b20","未检测到传感器,请检查硬件连接")
			elseif status == onewire.READ_ERROR then
				log.info("18b20","读取数据过程错误")
			elseif status == onewire.CHECK_ERROR then
				log.info("18b20","数据校验错误")
			elseif status == onewire.ONCRC8_CHECK_ERROR then
				log.info("18b20","序列号CRC8校验失败")
			end
			sys.wait(1000)
			
		end
	end
	sys.taskInit(testds18b20)

```
示例参考：[示例](https://doc.openluat.com/wiki/21?wiki_page_id=2671 "示例")

---



## onewire.read_dht11(pio)

读取dht11温度值和湿度值

**参数**

| **参数**    | **释义**                                |
| -----------  | --------------------------------------- |
| pio        | gpio编号                              	|

**返回值**

| **返回值**    | **释义**                                | **取值**                                |
| -----------  | --------------------------------------- | --------------------------------------- |
| status        | 读取的状态                              | 见onewire_status常量          			|
| temperature   | 温度值                                  | 整数          					    	|
| humidity     | 湿度值                                  | 整数             					 	|

**例子**

```lua
	local function testdht11()
		sys.wait(5000)
		-- 个别gpio需要打开电压域才可以正常使用
		pmd.ldoset(15,pmd.LDO_VLCD)
		while true do
			local status,temperature,humidity = onewire.read_dht11(pio.P0_0)
			if status == onewire.OK then
				log.info("dht11","temperature:",temperature)
				log.info("dht11","humidity:",humidity)
			elseif status == onewire.NOT_SENSOR then
				log.info("dht11","未检测到传感器,请检查硬件连接")
			elseif status == onewire.READ_ERROR then
				log.info("dht11","读取数据过程错误")
			elseif status == onewire.CHECK_ERROR then
				log.info("dht11","数据校验错误")
			end
			sys.wait(1000)
		end
	end
	sys.taskInit(testdht11)

```
示例参考：[示例](https://doc.openluat.com/wiki/21?wiki_page_id=2671 "示例")

---



