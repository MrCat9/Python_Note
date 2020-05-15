# CentOS7上部署jupyter

1. 新建虚拟环境，作为jupyter服务的运行环境

```
[user001@xxxx ~]$ mkvirtualenv venv_jupyter
```

2. 安装jupyter服务运行的依赖包

```
(venv_jupyter) [user001@xxxx ~]$ pip install ipython jupyter notebook
```

3. 生成配置文件

```
(venv_jupyter) [user001@xxxx ~]$ jupyter notebook --generate-config
```

> 生成的config file在/user0001/.jupyter/jupyter_notebook_config.py

4. 生成jupyter的访问密码

```
(venv_jupyter) [user001@xxxx ~]$ python

>>> from notebook.auth import passwd
>>> passwd('123456')
'sha1:0b0eb04384b2:01fcc86d6bfc37e8fb756be1e5d8965496fee8f1'
>>> exit()
```

5. 编辑jupyter的配置文件

```
(venv_jupyter) [user001@xxxx ~]$ vim /root/.jupyter/jupyter_notebook_config.py
```

```
c.NotebookApp.password = 'sha1:0b0eb04384b2:01fcc86d6bfc37e8fb756be1e5d8965496fee8f1'
c.NotebookApp.port = 8888
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.open_browser = False
```

6. 启动jupyter服务

```
(venv_jupyter) [user001@xxxx ~]$ jupyter notebook &
```

7. 退出虚拟环境

```
(venv_jupyter) [user001@xxxx ~]$ deactivate
```

8. 退出服务器连接

```
[user001@xxxx ~]$ exit
```
