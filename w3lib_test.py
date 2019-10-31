# -*- coding: utf-8 -*-


import w3lib.html

html_str = '''      s<!--页眉（840*60） end-->
      <h1 style="display:block; position:relative; clear:both">新闻标题</h1>
      <div id="BaiduSpider" style="display:none">
'''
html_str = w3lib.html.remove_comments(html_str)  # 去除注释
# html_str = w3lib.html.remove_tags(html_str, which_ones=('style', ))  # 去除 style 标签
html_str = w3lib.html.remove_tags_with_content(html_str, which_ones=('style',))  # 去除 style 标签及其内容
print(html_str)
'''
      s
      <h1 style="display:block; position:relative; clear:both">新闻标题</h1>
      <div id="BaiduSpider" style="display:none">

'''
print('=' * 64)

#

html_str = '你好\x20啊\xa0啊\t啊\n啊'
html_str = w3lib.html.replace_escape_chars(html_str, which_ones=('\n', '\t', '\r', '\x20', '\xa0'), replace_by='/')  # 替换
print(html_str)
'''
你好/啊/啊/啊/啊
'''
print('=' * 64)

#

html_str = '''你好\x20啊\xa0啊\t啊\n啊
<p class="otitle">&nbsp;&nbsp;&nbsp;测试标题测试标题测试标题测试标题</p>
<p>&nbsp;</p>
<p>&nbsp;&nbsp;&nbsp;&ldquo;测试内容测试内容测试内容测试内容&rdquo;&mdash;&mdash;测试内容测试内容</p>
<p>&nbsp;&nbsp;&nbsp;测试内容测试内容&ldquo;测试内容测试内容&rdquo;测试内容</p>
'''
html_str = w3lib.html.remove_tags(html_str)  # 去除html标签
html_str = w3lib.html.replace_entities(html_str)  # 替换html实体
print(html_str)
'''你好 啊 啊	啊
啊
   测试标题测试标题测试标题测试标题
 
   “测试内容测试内容测试内容测试内容”——测试内容测试内容
   测试内容测试内容“测试内容测试内容”测试内容

'''
print('=' * 64)
