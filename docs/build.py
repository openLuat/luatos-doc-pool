#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os, sys, re
import json, shutil
import subprocess

def build_blog():
    try:
        subprocess.check_call(["git", "pull"])
    except :
        pass
    os.makedirs("blog/site/", exist_ok=True)
    shutil.copytree("../public/", "blog/docs/pages/", dirs_exist_ok=True)
    pages = os.listdir("blog/docs/pages")
    pages.sort(reverse=True)
    tmpl = """
# 合宙技术博客

"""
    mons = []
    for name in pages:
        if name.startswith("20") and name.endswith(".md"):
            month = name[:6]
            if month not in mons:
                mons.append(month)
                tmpl += "\n## %s\n\n" % month
            with open("blog/docs/pages/" + name, "r", encoding="utf-8") as f:
                title = f.read().split("\n")[0][1:].strip()

            tmp = "- %s [%s](pages/%s)\n" % (name.split("_")[0], title, name)
            tmpl += tmp
    with open("blog/docs/index.md", "w", encoding="utf-8") as f:
        f.write(tmpl)


def do_api_doc(path):
    jpath = os.path.join(path, "api.json")
    if not os.path.exists(jpath) :
        return
    with open(jpath, "r", encoding="utf-8") as f:
        jdata = json.load(f)
    wiki_root = os.path.join("..", "..", "luatos-wiki")
    if not os.path.exists(os.path.join(path, "docs", "api", "core")):
        os.makedirs(os.path.join(path, "docs", "api", "core"))
    if not os.path.exists(os.path.join(path, "docs", "api", "ext")):
        os.makedirs(os.path.join(path, "docs", "api", "ext"))
    ifile = open(os.path.join(path, "docs", "api", "index.md"), "w", encoding="utf-8")
    ifile.write("# LuatOS API索引\n\n")
    def copy_md(tp):
        tlist = []
        jdata[tp].sort()
        for k in jdata[tp]:
            if tp == "core" :
                tpath = os.path.join(wiki_root, "api", k + ".md")
                dpath = os.path.join(path, "docs", "api", "core", k + ".md")
            else:
                tpath = os.path.join(wiki_root, "api", "libs", k + ".md")
                dpath = os.path.join(path, "docs", "api", "ext", k + ".md")
            if not os.path.exists(tpath) :
                print("API文档不存在!!!", tpath)
                continue
            with open(tpath, encoding="utf-8") as f :
                line = f.readline().strip()[1:].strip()
                tlist.append([k, line])

            shutil.copy(tpath, dpath)
            # TODO 清理wiki中不支持的语法

        # 写入index.md
        with open(os.path.join(path, "docs", "api", tp, "index.md"), "w", encoding="utf-8") as f:
            if tp == "core" :
                f.write("# LuatOS 核心库API索引\n\n")
                ifile.write("## 核心库API索引\n\n")
            else:
                f.write("# LuatOS 扩展库API索引\n\n")
                ifile.write("\n## 扩展库API索引\n\n")
            for k in tlist:
                f.write("* [%s](%s)\n" % (k[1], k[0] + ".md"))
                ifile.write("* [%s](%s/%s)\n" % (k[1], tp, k[0] + ".md"))

    copy_md("core")
    copy_md("ext")
    ifile.close()

def do_build(path, copy_product=False):
    # 读取mkdocs文件
    if not os.path.exists(path) :
        return
    root = os.path.abspath(path)
    # 拷贝产品指南手册的index到当前目录
    if not path.startswith("air"):
        shutil.copytree("common/", root + "/docs/", dirs_exist_ok=True)
        shutil.copytree("../image", root + "/docs/image", dirs_exist_ok=True)
    else:
        shutil.copytree("common/", root + "/docs/", dirs_exist_ok=True, ignore=shutil.ignore_patterns('*.md'))

    # 拷贝自定义主题文件
    shutil.copytree("custom_theme", root + "/custom_theme", dirs_exist_ok=True)
    # 如果是AT文档,且不是Air724UG系列,那就拷贝一下AT手册
    if str(path).endswith("at") or str(path).endswith("at/") :
        if "air724ug" not in path:
            shutil.copytree("../doc/AT开发资料/AT_Command_Manual/docs/Command_List", root + "/docs/app/Command_List", dirs_exist_ok=True)
    
    # if copy_product and os.path.exists(copy_product) :
    #     if os.path.exists(root + "/docs/product/") :
    #         shutil.rmtree(root + "/docs/product/")
    #     shutil.copytree(copy_product, root + "/docs/product/", dirs_exist_ok=True)

    # 拷贝luatos的API文档
    if "luatos" in path:
        do_api_doc(path)

    gitroot = os.path.abspath("../../")
    cmd = "docker run --rm -v {}:/opt/docs/ -w /opt/docs/luatos-doc-pool/docs/{} registry.cn-beijing.aliyuncs.com/wendal/mkdocs-material build"
    # cmd = "docker run --rm -v {}:/opt/gitee/ -w /opt/gitee/luatos-doc-pool/docs/{} squidfunk/mkdocs-material:9.5.34 build"
    cmd = cmd.format(gitroot, path.replace("\\", "/"))
    try :
        # print("path", path)
        subprocess.check_call(cmd, shell=True)
        dst = "/opt/docs/site/" + path + "/"
        if "/" in path and "\\" in path :
            if os.path.exists(dst) :
                shutil.rmtree(dst)
        else :
            if path == "root":
                dst = "/opt/docs/site/"
            else:
                dst = "/opt/docs/site/%s/" % path
                if os.path.exists(dst) :
                    shutil.rmtree(dst)
        shutil.copytree(path + "/site", dst, dirs_exist_ok=True)
    except:
        import traceback
        traceback.print_exc()

def git_hook():
    subprocess.check_call(["git", "pull"])
    subprocess.check_call(["git", "pull"], cwd=os.path.join("..", "..", "luatos-wiki"))
    # 构建简易博客
    build_blog()
    do_build("blog")
    do_build("dtu")
    for name in os.listdir(".") :
        if os.path.isdir(name) :
            do_build(os.path.join(name, "luatos"))
            do_build(os.path.join(name, "at"))
            do_build(os.path.join(name, "csdk"))
    # 然后还需要编译跟目录
    do_build("root")

    # 调整site下所有文件的修改时间为固定值
    for root, dirs, files in os.walk("/opt/docs/site/"):
        for file in files:
            name = str(file)
            if name.endswith(".html") or name.endswith(".js") or name.endswith(".css") :
                continue
            filename = os.path.join(root, file)
            os.utime(filename, (0, 0))

if __name__ == '__main__':
    if len(sys.argv) > 1 :
        do_build(sys.argv[1])
    else :
        git_hook()
