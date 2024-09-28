# 如何修改docs的文档

docs是指 [https://docs.openluat.com](https://docs.openluat.com) 的文档，也就是你正在访问的这个网站

## 网站介绍

1. 整个网站的内容, 使用git管理, 放在了 [https://gitee.com/openLuat/luatos-doc-pool](https://gitee.com/openLuat/luatos-doc-pool) 仓库中
2. 整个网站分成3部分,多个子网站:
    - 根网站, 位于 `docs/root` 目录
    - 模组子网站, 位于 `docs/airXXX` 目录, 其中XXXs是模块的名称
    - 功能子网站, 位于docs下, 例如 `docs/blog` `docs/dtu` 目录, 分别对应技术博客和DTU功能
3. 网站使用mkdocs构建, 具体配置在 `mkdocs.yml` 中, 每个子网站都有自己的配置文件, 并共享一份`docs/base.yml`基础配置
4. 网站的上方导航栏和左侧导航条, 使用 `mkdocs.yml` 中的nav配置
5. 文件编码使用UTF-8
6. 整个网站使用到 markdown 和 yaml 语法, 请参考 [https://markdown.com.cn/](https://markdown.com.cn/) 和 [https://www.runoob.com/w3cnote/yaml-intro.html](https://www.runoob.com/w3cnote/yaml-intro.html)
7. 整个网站使用git钩子自动部署, 正常情况下提交后10分钟即可访问到新的内容

## 修改文档

1. 找到需要修改的文档，例如：`docs/air780e/luatos/index.md`
2. 修改文档内容, 推荐使用vscode修改,文件编码使用UTF-8
3. 如需添加图片, 放在md文件所在目录的image子目录中,并使用相对路径引用图片
4. 提交PR/直接提交到仓库
5. 如果是PR, 等待作者合并
6. 如果是直接提交, 会触发自动部署, 稍等几分钟即可访问到新的内容

## 添加文档

1. 打开需要添加的文档目录, 不要使用中文文件名和中文目录名称, 避免使用特殊字符作为文件名
2. 例如：`docs/air780e/luatos/app/socket/tcp/tcp_kcp.md`
3. 在对应的子站的mkdocs.yml中添加文档的路径, 参考里面的nav配置
4. 提交PR/直接提交到仓库
5. 如果是PR, 等待作者合并
6. 如果是直接提交, 会触发自动部署, 稍等几分钟即可访问到新的内容
