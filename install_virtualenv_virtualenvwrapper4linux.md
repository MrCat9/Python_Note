# Linux下安装配置virtualenv和virtualenvwrapper

1. 安装virtualenv

   ```
   [user01@localhost ~]# pip3.7 install virtualenv
   ```

2. 安装virtualenvwrapper

   ```
   [user01@localhost ~]# pip3.7 install virtualenvwrapper
   ```

3. 创建一个文件夹，用于存放所有的虚拟环境

   ```
   [user01@localhost ~]# mkdir ~/.virtualenvs
   ```

4. 查询virtualenvwrapper.sh位置

   ```
   [user01@localhost ~]$ whereis virtualenvwrapper.sh
   virtualenvwrapper: /home/user01/.local/bin/virtualenvwrapper.sh
   ```

5. 设置环境变量

   ```
   [user01@localhost ~]$ vim ~/.bashrc
   ```

   把下面两行添加到~/.bashrc里

   ```
   # VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3.7
   export WORKON_HOME=/home/user01/.virtualenvs
   source /home/user01/.local/bin/virtualenvwrapper.sh
   ```

6. 更新~/.bashrc

   ```
   [user01@localhost ~]$ source ~/.bashrc
   ```

7. 测试是否安装完成

   列出虚拟环境列表

   ```
   [user01@localhost ~]$ workon
   ```

   创建新的虚拟环境，指定使用`python3.7`，虚拟环境名称为`tmp37`

   ```
   [user01@localhost ~]$ mkvirtualenv -p python3.7 tmp37
   ```

---

## 可能遇到的报错

### Linux下安装配置virtualenvwrapper报错/usr/bin/python: No module named virtualenvwrapper

#### 报错信息：

```
[user01@localhost ~]$ source ~/.bashrc
/usr/bin/python: No module named virtualenvwrapper
virtualenvwrapper.sh: There was a problem running the initialization hooks.

If Python could not import the module virtualenvwrapper.hook_loader,
check that virtualenvwrapper has been installed for
VIRTUALENVWRAPPER_PYTHON=/usr/bin/python and that PATH is
set properly.
```

#### 解决方法

安装步骤`5.`在设置环境变量时，指定virtualenvwrapper使用的python的位置

1. 设置环境变量

   ```
   [user01@localhost ~]$ vim ~/.bashrc
   ```

   把VIRTUALENVWRAPPER_PYTHON添加到~/.bashrc里

   ```
   VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3.7
   ```

2. 更新~/.bashrc

   ```
   [user01@localhost ~]$ source ~/.bashrc
   ```

3. 测试是否安装完成