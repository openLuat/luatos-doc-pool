
@[TOC]

# log

模块功能：系统日志记录,分级别日志工具

## _log(level, tag, ...) (local函数 无法被外部调用)

内部函数，支持不同级别的log打印及判断

* 参数

|名称|传入值类型|释义|
|-|-|-|
|level|param|日志级别，可选LOGLEVEL_TRACE，LOGLEVEL_DEBUG等|
|tag|param|模块或功能名称(标签)，作为日志前缀|
|...|param|日志内容，可变参数|

* 返回值

nil

* 例子

```lua
_log(LOGLEVEL_TRACE,tag, 'log content')
_log(LOGLEVEL_DEBUG,tag, 'log content')
```

---

## log.trace(tag, ...)

输出trace级别的日志

* 参数

|名称|传入值类型|释义|
|-|-|-|
|tag|param|模块或功能名称，作为日志前缀|
|...|param|日志内容，可变参数|

* 返回值

nil

* 例子

```lua
log.trace('moduleA', 'log content')
```

---

## log.debug(tag, ...)

输出debug级别的日志

* 参数

|名称|传入值类型|释义|
|-|-|-|
|tag|param|模块或功能名称，作为日志前缀|
|...|param|日志内容，可变参数|

* 返回值

nil

* 例子

```lua
log.debug('moduleA', 'log content')
```

---

## log.info(tag, ...)

输出info级别的日志

* 参数

|名称|传入值类型|释义|
|-|-|-|
|tag|param|模块或功能名称，作为日志前缀|
|...|param|日志内容，可变参数|

* 返回值

nil

* 例子

```lua
log.info('moduleA', 'log content')
```

---

## log.warn(tag, ...)

输出warn级别的日志

* 参数

|名称|传入值类型|释义|
|-|-|-|
|tag|param|模块或功能名称，作为日志前缀|
|...|param|日志内容，可变参数|

* 返回值

nil

* 例子

```lua
log.warn('moduleA', 'log content')
```

---

## log.error(tag, ...)

输出error级别的日志

* 参数

|名称|传入值类型|释义|
|-|-|-|
|tag|param|模块或功能名称，作为日志前缀|
|...|param|日志内容，可变参数|

* 返回值

nil

* 例子

```lua
log.error('moduleA', 'log content')
```

---

## log.fatal(tag, ...)

输出fatal级别的日志

* 参数

|名称|传入值类型|释义|
|-|-|-|
|tag|param|模块或功能名称，作为日志前缀|
|...|param|日志内容，可变参数|

* 返回值

nil

* 例子

```lua
log.fatal('moduleA', 'log content')
```

---

## log.openTrace(v, uartid, baudrate)

开启或者关闭print的打印输出功能

* 参数

|名称|传入值类型|释义|
|-|-|-|
|v|bool|false或nil为关闭，其余为开启|
|uartid|param|输出Luatrace的端口：1表示uart1,2表示uart2,3表示uart3|
|-|baudrate|可修改串口波特率，可选参数，默认115200|

* 返回值

nil

* 例子

```lua
log.openTrace(1,nil)
```

---
