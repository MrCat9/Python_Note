from PIL import Image
import pytesseract

path = "ValidateImage.jpg"

vcode = pytesseract.image_to_string(path)
print(vcode)




# pytesseract安装 https://github.com/vipstone/faceai/blob/master/doc/tesseractOCR.md

# 一款入门级的人脸、视频、文字检测以及识别的项目
# https://github.com/vipstone/faceai
