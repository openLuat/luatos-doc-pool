# 典型硬件设计指南

- [简介](index.md)
- [USB Boot烧录](usb_boot.md)
- [BTB扩展接口](btb.md)
- [休眠](sleep.md)
- [4G天线调试:](4g_ant.md)
- [GNSS天线调试](gnss_ant.md)
- [设计音频注意事项](audio.md)
- [调试音频方法](audio_debug.md)

Air201板子设计精致小巧，整板大小只有33mm×16.5mm，厚度0.8mm，这块板子上承载了4G通讯模块、GPS芯片、同轴连接器、预留电池焊盘、4G天线、GPS天线、音频解码芯片、喇叭焊盘、按钮、加速度传感器、自弹式SIM卡座、TYPE-C接口，还有BTB 24PIN连接器，可用于再扩展连接LCD、Camera、Uart、I2C等通讯外设。

![img](https://l0x5bk8xnyd.feishu.cn/space/api/box/stream/download/asynccode/?code=MTFiMmYwMTljOTQwNWEwYTcwMjc1OWEwYTFhYjQ4OWVfS2swaFRjNDF2ajl5ZkpmSkNGb3FJd3FwcVRpbVdkbDVfVG9rZW46UG1zcmJUN3NSb0RjVGF4a3RpQWNzQlIybk9iXzE3MjcxODM1OTc6MTcyNzE4NzE5N19WNA)![img](https://l0x5bk8xnyd.feishu.cn/space/api/box/stream/download/asynccode/?code=YjQwZjMyZDk3ODlmMDg2MDBlMmQ2MGJjNTUyNjMxYTBfTWw2V0o1bGtxT25wS09FMWc5NWRmRUN0MXR0TWZpdXZfVG9rZW46S09xSmJUQ2Q5b2FjU3R4Yng4NWNwUXRzbmhiXzE3MjcxODM1OTc6MTcyNzE4NzE5N19WNA)

### GPIO 复用表格

[GPIO复用表格.pdf](https://cdn.openluat-luatcommunity.openluat.com/attachment/20240415144933952_Air780EP&Air780EPV_GPIO_table_20240415.pdf)

### 板子主要接口分布图

![img](https://l0x5bk8xnyd.feishu.cn/space/api/box/stream/download/asynccode/?code=Mzc1MmU1NDhmZjliZjU5MDVhNzBkNGFiZTJmYmQ1MjNfR2YzTTNQS3A1Z1BUQXpPOUpKa2dhT0Framh3YTI4dW1fVG9rZW46RDROQ2JjcHJrb05Sd1p4eHlEdGNIN0JKbllmXzE3MjcxODM1OTc6MTcyNzE4NzE5N19WNA)

![img](https://l0x5bk8xnyd.feishu.cn/space/api/box/stream/download/asynccode/?code=YTgwODVlMDVhNjkzOTdlOGM0MzYyYmM0MmM0NjllNzlfRVhUdUQ5WE41OXBKNHA4RGRCcnljTXVhV2Vhb3pwTktfVG9rZW46Wml3eWIydUo5b2xCQXF4TkdkcmNlRTF0bmdlXzE3MjcxODM1OTc6MTcyNzE4NzE5N19WNA)
