#列表List
names = ["Bob", "Tom", "Alice", "LRL"]

index = names.index("Tom") # 1

names[0]="Mike" #修改指定下标处的内容

names.insert(1,"Amy")
# print(names) ['Mike', 'Amy', 'Tom', 'Alice', 'LRL']

names.append("Bob")
# print(names) ['Mike', 'Amy', 'Tom', 'Alice', 'LRL', 'Bob']

names.extend(["Hellen","Kevin"]) #同append类似
# print(names) ['Mike', 'Amy', 'Tom', 'Alice', 'LRL', 'Bob', 'Hellen', 'Kevin']

#删除 方式一
del names[0]
# print(names) ['Amy', 'Tom', 'Alice', 'LRL', 'Bob', 'Hellen', 'Kevin']
#删除 方式二
element = names.pop(-1) 
# print(names) ['Amy', 'Tom', 'Alice', 'LRL', 'Bob', 'Hellen']
# print(element) Kevin

#删除某元素在列表里的第一个匹配项
names.append("Amy")
names.remove("Amy")
# print(names) ['Tom', 'Alice', 'LRL', 'Bob', 'Hellen', 'Amy']

#统计列表中某一个元素的数量
names.insert(2,"LRL")
# print(names.count("LRL")) 2

#统计列表元素数量
# print(len(names)) 7

#遍历列表
for element in names:
    print(element ,end=" ")


#排序
print(sorted(names))
#清空列表
names.clear()
# print(names) []


