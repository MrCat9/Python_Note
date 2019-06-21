# -*- coding: utf-8 -*-


class ThisIsClass:
    def __init__(self):
        print('hello')

    @staticmethod
    def s_fun():
        print('s_fun')

    def fun(
            self,
            num: int,  # 接收的参数类型为 int  # 不传 int 的话也不会报错/警告
            text: str,
    ):
        print('this is fun' + text, num, self)
        return 'fun_return_str'


def my_fun() -> str:  # 返回 str
    c = (
        ThisIsClass()
        .fun(
            123,
            'sss'
        )
    )
    return c


if __name__ == '__main__':
    t = my_fun()
    print(t)
    '''
    hello
    this is funsss 123 <__main__.ThisIsClass object at 0x00000241297FA550>
    fun_return_str
    '''

    # ThisIsClass.fun(321, 'aaa')  # 报错

    ThisIsClass.fun('obj', 321, 'aaa')  # 不报错  # 把 obj 当实例传过去
    '''
    his is funaaa 321 obj
    '''

    ThisIsClass().fun(321, 'aaa')  # 不报错  # 等价于实例调用实例方法
    '''
    hello
    this is funaaa 321 <__main__.ThisIsClass object at 0x000001C57E93DA90>
    '''
