# 切换SIM卡

合宙的大部分模组型号都有两路SIM卡引脚，支持双卡单待（即同一时间只能使用其中一个SIM通道）。

## 切换卡槽

**mobile.simid(id)**

```lua
-- 固定使用SIM0
mobile.simid(0) 
-- 固件使用SIM1    
mobile.simid(1)
-- 自动识别SIM0, SIM1 
mobile.simid(2) 
-- 自动识别SIM0, SIM1, 且SIM0优先
-- 提醒, 自动识别是会增加时间的
mobile.simid(2, true)
```

## 获取当前SIM卡槽

**mobile.simid()**

```lua
-- 自动识别SIM0, SIM1
mobile.simid(2) 

sys.taskInit(function() 
   	-- 如果在刚开机就要执行获取，最好先加些延时，防止sim卡刚上电还未准备好，读取失败。
    sys.wait(2000)     
    -- 获取当前SIM卡槽
	log.info("simid", mobile.simid()) 
    -- 实例输出：simid	0 （SIM卡插入SIM0卡槽）
end)
```

## 检测当前SIM卡是否准备好

**mobile.simPin()**

当前sim卡是否准备好，一般返回false就是没卡

```lua
-- 自动识别SIM0, SIM1
mobile.simid(2) 

sys.taskInit(function() 
   	-- 如果在刚开机就要执行获取，最好先加些延时，防止sim卡刚上电还未准备好，读取失败。
    sys.wait(2000)     
    -- 检测当前SIM卡是否准备好
	log.info("simPin",mobile.simPin() 
    -- 实例输出：simPin	true
end)
```



## sim卡不识别问题

mobile.simPin() 当前sim卡是否准备好，一般返回false就是没卡，如果返回false，可以按照以下情况排查：

### 硬件排查

1. 是否有查入SIM卡
2. SIM卡插入方向是否正确
3. 如果尝试过有其他卡插入可以读取到，就这张sim卡不行。
   - 可以检查下sim金属面是否比较脏、有刮痕，可以用橡皮擦或者少量酒精擦拭。
   - 卡的厚度相对比较薄，可以尝试垫一点卫生纸，缩短接触距离。
4. SIM卡电路设计有问题。可以进入 air780e.cn 打开硬件设计手册，其中包含SIM卡座的设计电路，作为排查参考。

### 软件排查

1. 是否将接口放在刚开机就立即会执行的位置，并且没有加延时。可能会出现模块开机sim卡还未读取到，软件就走到获取ICCID，这个时候就会获取失败。
2. SIM卡插入的sim硬件接口, 且切换到正确的SIM卡槽(开机立即设置,或者进飞行模式设置)

```
SIM0 -> mobile.simid(0)
SIM1 -> mobile.simid(1)

自动选择 -> mobile.simid(2)
```

