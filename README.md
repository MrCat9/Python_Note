# python_notes 记录一些有关python的笔记

1_selenium在add_cookie之前要先get

2_快速退出递归可以考虑return和yield

3_从list中取出元素
pop,append,for

4_写文件(w,wb)读文件(r,rb)
with open("test.json", "w") as f:
        f.write(json_doc)
# w下write()中的变量为str
# wb下write()中的变量为byte
with open("test.json", "r") as f:
        doc = json.load(f)
# 文件里都是英文的话r,rb都行
# 文件里有中文的话用r会报错，用rb不会
