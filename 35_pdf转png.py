# -*- coding: utf-8 -*-

# 摘自  https://blog.csdn.net/XnCSD/article/details/80849996

# pip install PyMuPDF

import fitz
import glob
import os


def pdf_to_jpg(pdf_file_path):
    doc = fitz.open(pdf_file_path)

    try:
        pdf_file_name = pdf_file_path.replace('.pdf', '')
        os.mkdir(pdf_file_name + '_pdf2png')  # 创建单个目录
        print('创建目录 pdf2png')
    except Exception as e:
        print(str(e))

    for pg in range(0, doc.pageCount):
        page = doc[pg]
        zoom = int(200)  # 图片质量？
        rotate = int(0)  # 图片旋转
        trans = fitz.Matrix(zoom / 100.0, zoom / 100.0).preRotate(rotate)
        pm = page.getPixmap(matrix=trans, alpha=False)
        pm.writePNG('{}_pdf2png/{}.png'.format(pdf_file_name, str(pg + 1)))


if __name__ == '__main__':
    test_pdf_file_path = 'test_pdf_file.pdf'
    pdf_to_jpg(test_pdf_file_path)
    print('完成')
