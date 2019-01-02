# -*- coding: utf-8 -*-
# 根据dict中的某一key的value，对dict的list去重，value相同视为重复


def dict_list_duplicate(dict_list, duplicate_key):
    temp_list = []
    new_dict_list = []
    for dict_ in dict_list:
        value = dict_[duplicate_key]
        if value not in temp_list:
            temp_list.append(value)
            new_dict_list.append(dict_)
    return new_dict_list


if __name__ == '__main__':
    old_dict_list = [
        {"title": "title1", "name": "name1"},
        {"title": "title2", "name": "name2"},
        {"title": "title1", "name": "name3"},
    ]
    print(old_dict_list)
    # [{'title': 'title1', 'name': 'name1'}, {'title': 'title2', 'name': 'name2'}, {'title': 'title1', 'name': 'name3'}]

    new_dict_list = dict_list_duplicate(old_dict_list, "title")  # 根据dict中的title去重，title相同视为重复
    print(new_dict_list)
    # [{'title': 'title1', 'name': 'name1'}, {'title': 'title2', 'name': 'name2'}]

