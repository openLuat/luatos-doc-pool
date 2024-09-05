#!/usr/bin/python3
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

def do_build(path):
    # 读取mkdocs文件
    if not os.path.exists(path) :
        return
    root = os.path.abspath(path)
    # 拷贝产品手册的图片到当前目录
    shutil.copytree("../image", root + "/docs/image", dirs_exist_ok=True)
    # 拷贝产品手册的index到当前目录
    shutil.copytree("common/", root + "/docs/", dirs_exist_ok=True)

    # 拷贝自定义主题文件
    shutil.copytree("custom_theme", root + "/custom_theme", dirs_exist_ok=True)
    # 如果是AT文档,且不是Air724UG系列,那就拷贝一下AT手册
    if str(path).endswith("at") or str(path).endswith("at/") :
        if "air724ug" not in path:
            shutil.copytree("../doc/AT开发资料/AT_Command_Manual/docs/Command_List", root + "/docs/Command_List", dirs_exist_ok=True)


    # 构建简易博客
    build_blog()

    gitroot = os.path.abspath("../../")
    cmd = "docker run --rm -v {}:/opt/gitee/ -w /opt/gitee/luatos-doc-pool/docs/{} registry.cn-beijing.aliyuncs.com/wendal/mkdocs-material build"
    cmd = cmd.format(gitroot, path.replace("\\", "/"))
    try :
        print("path", path)
        subprocess.check_call(cmd, shell=True)
        if "/" in path and "\\" in path :
            os.makedirs("/opt/docs/site/" + path + "/", exist_ok=True)
            shutil.copytree(path + "/site", "/opt/docs/site/" + path + "/", dirs_exist_ok=True)
        else :
            if path == "root":
                print("copy from", path + "/site", "-->", "/opt/docs/site/")
                os.makedirs("/opt/docs/site/", exist_ok=True)
                shutil.copytree(path + "/site", "/opt/docs/site/", dirs_exist_ok=True)
            elif path == "blog":
                os.makedirs("/opt/docs/site/", exist_ok=True)
                shutil.copytree(path + "/site", "/opt/docs/site/blog/", dirs_exist_ok=True)
    except:
        import traceback
        traceback.print_exc()

def git_hook():
    subprocess.check_call(["git", "pull"])
    do_build("blog")
    for name in os.listdir(".") :
        if os.path.isdir(name) :
            do_build(os.path.join(name, "at"))
            do_build(os.path.join(name, "luatos"))
    # 然后还需要编译跟目录
    do_build("root")

if __name__ == '__main__':
    git_hook()
