# jupyter使用不同内核（虚拟环境）

1. 创建工程的虚拟环境

    ```
    [user001@xxxx ~]$ mkvirtualenv venv_my_project
    ```

    ```
    # conda 新建python虚拟环境
    [user001@xxxx ~]$ conda create --name tmp_py310 python=3.10
    ```

2. 安装`ipykernel`

    ```
    (venv_my_project) [user001@xxxx ~]$ pip install ipykernel
    ```

3. 将工程的虚拟环境添加到jupyter内核

    ```
    (venv_my_project) [user001@xxxx ~]$ python -m ipykernel install --user --name=venv_my_project
    ```

---

- 查看 jupyter kernel

    ```
    [user001@xxxx ~]$ jupyter kernelspec list
    ```

- 删除 jupyter 内核

    ```
    [user001@xxxx ~]$ jupyter kernelspec remove venv_my_project
    ```
