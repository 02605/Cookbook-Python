from collections import OrderedDict


self_dict = OrderedDict()
self_dict['a'] = 1
self_dict['c'] = 2
self_dict['b'] = 3

for each_key, value in self_dict.items():
    print(each_key, '---', value)