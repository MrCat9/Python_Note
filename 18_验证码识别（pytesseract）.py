# -*- coding: utf-8 -*-

from PIL import Image
import pytesseract

# path = "validate_image1.jpg"
path = "5.jpg"  # 图片路径

# Image.open(path).show()

vcode = pytesseract.image_to_string(path)
# vcode = pytesseract.image_to_string(path, lang='osd')
# vcode = pytesseract.image_to_string(path, lang='eng')
# vcode = pytesseract.image_to_string(path, lang='chi_sim')

print("直接使用pytesseract识别:", vcode)


def identification_captcha(path):  # 识别验证码
    img = Image.open(path)  # 打开图片

    img = img.resize((1500, 360), Image.ANTIALIAS)
    img.show()
    print("放大后使用pytesseract识别:", pytesseract.image_to_string(img))

    img = img.convert('L')
    binaryImage = img.point(initTable(), '1')
    binaryImage.show()
    vcode = pytesseract.image_to_string(binaryImage)
    print('处理后使用pytesseract识别：', vcode)

    return vcode


def initTable(threshold=160):  # 图片二值化函数
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    return table


if __name__ == '__main__':
    identification_captcha(path)





# pytesseract安装 https://github.com/vipstone/faceai/blob/master/doc/tesseractOCR.md
# 语言包下载 （将下载的.traineddata文件拷贝到tessdata目录下） https://github.com/tesseract-ocr/tesseract/wiki/Data-Files

# 一款入门级的人脸、视频、文字检测以及识别的项目
# https://github.com/vipstone/faceai
