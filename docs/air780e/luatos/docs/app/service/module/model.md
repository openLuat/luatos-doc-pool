# 硬件型号

模块远程升级需要上传模块硬件型号，硬件bsp型号，解决和分析某些问题的时候可能也会需要确认模块硬件型号，以下为模块硬件型号的获取方法。

## 获取硬件型号

**hmeta.model()**

获取模组硬件型号

```lua
sys.taskInit(function()
	log.info("hmeta-model", hmeta.model())
    -- 实例输出：hmeta-model	Air780E
end)
```

## 获取硬件bsp型号

**rtos.bsp()**

获取模组硬件型号

```lua
sys.taskInit(function()
	log.info("rtos.bsp", rtos.bsp())
    -- 实例输出：rtos-bsp	EC618
end)
```

