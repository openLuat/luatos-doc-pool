# 固件版本

模块远程升级需要上传模块固件版本，解决和分析某些问题的时候可能也会需要确认模块固件版本，以下为模块固件版本的获取方法。

## 获取固件版本

**rtos.version()**

获取固件版本号

```lua
sys.taskInit(function()
	log.info("luatos_version ", rtos.version())
    -- 实例输出：luatos_version 	V1112
end)
```
