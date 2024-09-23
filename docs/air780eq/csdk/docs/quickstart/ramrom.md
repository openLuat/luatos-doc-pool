# Air780EQ的CSDK开发可用资源

## 内存分配

1. 整个芯片的RAM是1M字节
2. 实际可用RAM约420k字节, 静态分配,堆内存,栈内存,均从这420k字节中分配
3. 除静态分配的内存块之外,剩余的内存块为动态分配, 均划入堆内存
4. 栈内存, 由创建task时指定, 从堆内存中分配
5. 注意: 底层的回调的栈通常都很小, 不要在回调函数中做大的栈内存消耗, 也不要有长时间的阻塞操作

## Flash分区表

Air780EQ整个Flash是4M, 主要分成 BL/CP/AP/FS/FOTA等区域, 以下是默认大小

| 区域 | 偏移量|大小 | 备注 |
| --- | --- | --- | --- |
| ROM | 0x000000|8k | ROM代码 |
| FUSE| 0x002000|4k | FUSE, 存放配置信息 |
| BL  | 0x003000|72k | Bootloader, 压缩后存放在Flash中 |
| CP  | 0x01a000|400k | 协议栈程序和数据 |
| AP  | 0x07e000|2824k | APP, 存放APP的代码和数据 |
| FOTA| 0x340000|420k | Firmware Over The Air, 存放FOTA的代码和数据 |
| FS  | 0x3a9000|128k | 文件系统 |
| KV  | 0x3c9000|64k| Key-Value, 存放配置信息 |
| HIB | 0x389000|92k| 休眠数据备份区|
|NVRAM| 0x3f1000|52k| 非易失性RAM, 校准信息 |
|PLAT | 0x3fe000|4k| 平台配置信息 |

具体的分区文件, 请看源码目录下的分区文件, 默认的分区表为:

```
PLAT\device\target\board\ec7xx_0h00\common\inc\mem_map_csdk_716e.h
```

## 这里以BOOTLOADER分区的宏做详细讲解

```
#define BOOTLOADER_FLASH_LOAD_ADDR              (0x00803000)
#define BOOTLOADER_FLASH_LOAD_SIZE              (0x11000)//72kB, real region size
#define BOOTLOADER_FLASH_LOAD_UNZIP_SIZE        (0x18000)//96KB ,for ld
```

- `BOOTLOADER_FLASH_LOAD_ADDR` 是BOOTLOADER的Flash地址 + XIP的起始地址
- `BOOTLOADER_FLASH_LOAD_SIZE` 是BOOTLOADER存放在Flash中的大小, 因为BOOTLOADER是压缩过的
- `BOOTLOADER_FLASH_LOAD_UNZIP_SIZE` 是ld操作时,实际Bootloader的可用空间

这里涉及的一个概念, 就是716e中, BL/CP/AP在flash存放的时候, 是压缩过的

所以, 编译BL/CP/AP的时候, 需要满足2个条件:

1. 需要未压缩前的文件大小 `<` BOOTLOADER_FLASH_LOAD_UNZIP_SIZE, 在临时文件夹下, 表现的文件名带 "unZip"字样
2. 压缩后的文件大小 `<` BOOTLOADER_FLASH_LOAD_SIZE, 在临时文件夹下, 对应文件名不带 "unZip"字样

## 关于分区调整

1. 调整分区, 需要修改对应的宏定义, `LOAD_SIZE` 和 `LOAD_UNZIP_SIZE` 要同步修改
2. 只允许调整AP/FOTA/FS/KV这4个区域的大小,不可以调整其他分区的大小和位置!!
3. 不允许调整分区的先后顺序!!
