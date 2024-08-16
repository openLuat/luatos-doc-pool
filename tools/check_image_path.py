#!/usr/bin/python3

# -*- coding: utf-8 -*-

import os, shutil

def main():
    path = os.getcwd()
    for root, dirs, files in os.walk(path):
        for file in files:
            if not file.endswith('.md'):
                continue
            file_name = os.path.join(root, file)
            # print('{}'.format(file_name))
            lines = []
            with open(file_name, encoding="utf-8") as f :
                for line in f.readlines():
                    if "![" in line :
                        pos = line.find("![")
                        pos2 = line.find("../image/", pos)
                        if pos2 != -1:
                            pos2 = line.find("(../") + 1
                            if not os.path.exists(os.path.join(root, "image/")):
                                os.makedirs(os.path.join(root, "image/"))
                            
                            #print(line)
                            # 读取image的路径
                            pos3 = line.find(")", pos2)
                            image_src_path = line[pos2:pos3]
                            if "%" in image_src_path:
                                import urllib.parse
                                image_src_path = urllib.parse.unquote(image_src_path)
                            image_src_abs_path = os.path.join(root, image_src_path)
                            image_src_abs_path = os.path.abspath(image_src_abs_path).capitalize()
                            # print("图片旧路径", image_src_path, os.path.exists(image_src_abs_path))
                            if os.path.exists(image_src_abs_path) == False:
                                print('{}'.format(file_name))
                                print("旧图片不存在", image_src_abs_path)
                            else :
                                # 复制到image目录下
                                image_new_path = "image/" + image_src_path.split("/")[-1]
                                image_new_abs_path = os.path.join(root, image_new_path)
                                image_new_abs_path = os.path.abspath(image_new_abs_path).capitalize()
                                shutil.copyfile(image_src_abs_path, image_new_abs_path)
                                # print("图片新路径", image_new_path, os.path.exists(image_new_abs_path))
                                # 替换路径
                                line = line.replace(image_src_path, image_new_path)
                                # os.remove(image_src_abs_path)
                        lines.append(line)
                    elif "src=\"" in line :
                        print(line, file_name)
                        lines.append(line)
                    else:
                        lines.append(line)
            with open(file_name, mode="w+", encoding="utf-8") as f :
                f.writelines(lines)
if __name__ == '__main__':
    main()
