# python_notes 记录一些有关python的笔记

1_selenium在add_cookie之前要先get

2_快速退出递归可以考虑return和yield

3_从list中取出元素
pop,append,for

4_写文件(w,wb)读文件(r,rb)
with open("test.json", "w") as f:
        f.write(json_doc)
#### w下write()中的变量为str
#### wb下write()中的变量为byte
with open("test.json", "r") as f:
        doc = json.load(f)
#### 文件里都是英文的话r,rb都行
#### 文件里有中文的话用r会报错，用rb不会

5_全局变量要在某个方法内对其进行修改时，要用global

6_set可以对一个list去重，可以让两个list相减，得到差集

7_ HTTP状态码

8_geohash2

9_selenium设置无界面浏览，设置代理ip

10_list的指针问题

11_MySQL数据库储存位置

12_requests

13_用re去除所有html标签，保留标签里面的内容

13_2_用re匹配出img标签，再匹配出img标签中的图片url

14_re报错bad character range

15_插入到sql中的数据包含单引号（'）时，应将一个单引号（'）改成两个单引号（''）
str1 = str1.replace("'", "''")

16_进程和线程
父进程所有Python对象都必须通过pickle序列化再传到子进程去，所有，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。

17_从数据库中取出数据，转为list

18_验证码识别(pytesseract)

19_一款入门级的人脸、视频、文字检测以及识别的项目

20_ORM_sqlalchemy（用于操作数据库）

20_2_ORM_sqlalchemy（外键）

21_列表生成式
列出100以内3的倍数

22_获取list元素下标
