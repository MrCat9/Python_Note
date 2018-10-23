# -*- coding:utf-8 -*-

if __name__ == '__main__':
    data1 = {
        'name': "name",
        'number': "number",
    }

    data2 = {
        "price": "price",
        "amount": "amount"
    }

    data12 = dict(data1, **data2)

    print(data1)
    print(data2)
    print(data12)

"""
{'name': 'name', 'number': 'number'}
{'price': 'price', 'amount': 'amount'}
{'name': 'name', 'number': 'number', 'price': 'price', 'amount': 'amount'}
"""
