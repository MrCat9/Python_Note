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

14_re报错bad character range

15_插入到sql中的数据包含单引号（'）的处理方法
