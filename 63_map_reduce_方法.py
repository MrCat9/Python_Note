# -*- coding: utf-8 -*-


from functools import reduce


if __name__ == '__main__':
    list1 = [
        '363000.00元',
        '0',
        '2315835.00元',
        '198970.00元,120000.00元',
        '1028860.00元,508000.00元,1787000.00元',
        '30219757.25元',
    ]
    print(list1)

    def str_to_float(number_str):
        sum = 0.0  # 和
        str_list = number_str.split(',')
        for _number in str_list:
            _number = _number.replace('元', '')
            _number = float(_number)
            sum += _number
        return sum

    list1 = list(map(str_to_float, list1))
    print(list1)

    def add(x, y):
        return x + y

    total = reduce(add, list1)

    print(total)
