from collections import defaultdict


self_multi_dict1 = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

self_multi_dict2 = {
    'a': ['a', 'b', 'c'],
    'b': ['d', 'e']
}


d = defaultdict(list)
for each_list in [self_multi_dict1.items(), self_multi_dict2.items()]:
    for key, value in each_list:
        d[key].append(value)

print(d.get('a'))