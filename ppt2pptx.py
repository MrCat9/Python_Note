# -*- coding: utf-8 -*-


import os
import uuid
from win32com import client as wc  # ppt


PPT_DIR = '.'
fp = 'xxxx.ppt'


# ppt2pptx
ppt = wc.gencache.EnsureDispatch('PowerPoint.Application')  # 打开ppt应用程
# ppt.Visible = 1  # 可视化
ppt_file = ppt.Presentations.Open(fp)  # 打开.ppt文件
tmp_fp = os.path.join(PPT_DIR, 'tmp_' + ''.join(str(uuid.uuid4()).split('-')) + '.pptx')
ppt_file.SaveAs(tmp_fp)  # 要用绝对路径，用相对路径会报错
ppt_file.Close()  # 关闭原来ppt文件
ppt.Quit()

print('pptx file path:', tmp_fp)
