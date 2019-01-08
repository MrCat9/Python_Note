# -*- coding: utf-8 -*-

import os
import shutil

BASE_DIR = os.getcwd()  # 当前文件所在的文件夹路径

for root, dirs, files in os.walk(BASE_DIR):
    for file in files:
        print(file)

files_list = os.listdir(BASE_DIR)  # 获取文件夹下的所有文件和文件夹
print(files_list)

try:
    os.mkdir("test_dir")  # 创建单个目录
    files_path = os.path.join(BASE_DIR, "test_dir_1\\test1")
    os.makedirs(files_path)  # 创建多级目录
    os.makedirs("test_dir_2\\test2")  # 创建多级目录
    print(files_path)
except Exception as e:
    print(str(e))

# 拷贝文件 file_path 到指定目录 tag_dir
# shutil.copy(file_path, tag_dir)
shutil.copy('test01.py', 'test_dir')

# 删除文件
os.remove(os.path.join(BASE_DIR, 'test_dir\\test01.py'))

# 删除文件夹
shutil.rmtree('test_dir')
shutil.rmtree('test_dir_1')

