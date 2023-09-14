my_dict = {"Tom": 99, "Amy": 100, "Bob": 88}
my_dict2 = dict()

# 字典不允许key重复，否则在后面的会把前面的覆盖掉
# key和value可以为任意的数据类型，但是key不可以是字典

# 取特定的值
score = my_dict["Tom"]
# print(score) 99

# 定义嵌套字典
stu_score = {
    "Tom": {"English": 100, "Math": 90, "Physics": 50},
    "Amy": {"English": 70, "Math": 80, "Physics": 70},
    "Bob": {"English": 60, "Math": 100, "Physics": 60},
}

#获取特定的值
# print(stu_score["Tom"]["English"])

#新增元素
my_dict["Alice"]=99
# print(my_dict) {'Tom': 99, 'Amy': 100, 'Bob': 88, 'Alice': 99}

#更新元素
my_dict["Tom"] = 89
# print(my_dict) {'Tom': 89, 'Amy': 100, 'Bob': 88, 'Alice': 99}

#删除元素pop
value = my_dict.pop("Tom")
# print(value)  89
# print(my_dict)  {'Amy': 100, 'Bob': 88, 'Alice': 99}

#获取全部的key
keys = my_dict.keys()
# print(keys) dict_keys(['Amy', 'Bob', 'Alice'])

#遍历字典 方式1：获取全部key之后再遍历
for key in keys:
    print(my_dict[key])

#方式2：直接对字典进行for循环
for key in my_dict:
    print(my_dict[key])

#清空clear
my_dict.clear()
# print(my_dict)