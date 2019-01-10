# -*- coding: utf-8 -*-
# python-docx-template 文档 https://docxtpl.readthedocs.io/en/latest/
# https://github.com/elapouya/python-docx-template/tree/master/tests
# https://github.com/elapouya/python-docx-template/blob/master/tests/inline_image.py

from docxtpl import DocxTemplate, InlineImage
# for height and width you have to use millimeters (Mm), inches or points(Pt) class :
from docx.shared import Mm, Inches, Pt
import jinja2


# #####################
# tpl = DocxTemplate("templates\\my_word_template.docx")  # 选择使用的.docx模板
# context = {'company_name': "World company"}  # company_name 是存在于my_word_template.docx文档里面的变量，就像这样{{company_name}}，直接放在my_word_template.docx文件的明确位置就行
# tpl.render(context)  # 这里是有jinjia2的模板语言进行变量的替换，然后便可以在输出的文档generated_doc.docx里面看到{{company_name}}变成了World company
# tpl.save("output\\generated_doc.docx")  # 保存
# #####################

# #####################
# from docx import Document
# tpl = DocxTemplate("templates\\my_word_template.docx")  # 选择使用的.docx模板
# sub = tpl.new_subdoc()
# sub.subdocx = Document('templates\\subdocx.docx')  # 要插入的文档
# context = {'sub': sub}  # 插入的文档内容放在tpl的{{sub}}位置
# tpl.render(context)
# tpl.save("output\\generated_doc.docx")  # 保存
# #####################


tpl=DocxTemplate('templates/inline_image_tpl.docx')  # 选择使用的.docx模板

context = {
    'myimage' : InlineImage(tpl,'templates/python_logo.png',width=Mm(20)),
    'myimageratio': InlineImage(tpl, 'templates/python_jpeg.jpg', width=Mm(30), height=Mm(60)),

    'frameworks' : [{'image' : InlineImage(tpl,'templates/django.png',height=Mm(10)),
                      'desc' : 'The web framework for perfectionists with deadlines'},

                    {'image' : InlineImage(tpl,'templates/zope.png',height=Mm(10)),
                     'desc' : 'Zope is a leading Open Source Application Server and Content Management Framework'},

                    {'image': InlineImage(tpl, 'templates/pyramid.png', height=Mm(10)),
                     'desc': 'Pyramid is a lightweight Python web framework aimed at taking small web apps into big web apps.'},

                    {'image' : InlineImage(tpl,'templates/bottle.png',height=Mm(10)),
                     'desc' : 'Bottle is a fast, simple and lightweight WSGI micro web-framework for Python'},

                    {'image': InlineImage(tpl, 'templates/tornado.png', height=Mm(10)),
                     'desc': 'Tornado is a Python web framework and asynchronous networking library.'},
                    ]
}
# testing that it works also when autoescape has been forced to True
jinja_env = jinja2.Environment(autoescape=True)  # 转义=True
tpl.render(context, jinja_env)
tpl.save('output/inline_image.docx')
