# -*- coding: utf-8 -*-


import camelot  # pip install camelot-py[cv]
# 要使用 flavor="lattice" 的话还需要安装 ghostscript
# pip install ghostscript
# 安装 ghostscript  # https://www.ghostscript.com/download/gsdnld.html


# tables = camelot.read_pdf('foo.pdf')  # 默认flavor='lattice'  # 使用ghostscript将PDF页面转换为图像
tables = camelot.read_pdf('foo.pdf', pages='all')
# tables = camelot.read_pdf('foo.pdf', flavor='stream')  # 将pdf视为图片
tables  # <TableList n=4>

tables.export('foo.csv', f='csv', compress=True)  # json, excel, html, sqlite  # 可以输出一个zip，包括pdf每一页的csv结果

tables[0]  # <Table shape=(7, 5)>
tables[0].parsing_report  # 获取解析报告  # {'accuracy': 95.08, 'whitespace': 51.43, 'order': 1, 'page': 1}

df = tables[0].df  # get a pandas DataFrame!  # 转df
tables[0].to_csv('foo.csv')  # to_json, to_excel, to_html, to_sqlite
