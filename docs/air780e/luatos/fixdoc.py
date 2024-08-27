#!/usr/bin/python3
import os, sys, re


def main():
    # 读取mkdocs文件
    with open('mkdocs.yml', 'r', encoding="utf-8") as f:
        for line in f.readlines():
            line = str(line).strip()
            if line.endswith(".md") :
                path = line.split(":")[-1].strip()
                path = os.path.join("docs", path)
                if os.path.exists(path) :
                    continue
                dirpath = os.path.dirname(path)
                print(dirpath)
                os.makedirs(dirpath, exist_ok=True)
                title =line.split(":")[0]
                title = title[1:].strip()
                # print(title)
                with open(path, 'w', encoding="utf-8") as f:
                    f.write("# " + title + "\r\n")

if __name__ == '__main__':
    main()