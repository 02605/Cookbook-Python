age_dict = {
    "rx": 20,
    "ws": 23,
    "wd": 18,
    "ds": 58
}

# 对字典的常规操作都只能应用到key
print(min(age_dict))
# 匿名函数
print(min(age_dict, key=lambda x: age_dict[x]))
# zip改变目标元组的顺序：value-key
print(min(zip(age_dict.values(), age_dict.keys())))