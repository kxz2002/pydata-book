my_set = {"hello", "world", "python", "hello"}  # 集合可以去重并且乱序
my_set_2 = set()
# print(my_set) {'hello', 'world', 'python'}

my_set.add("LRL")
# print(my_set) {'hello', 'world', 'python', 'LRL'}

my_set.remove("hello")
# print(my_set) {'world', 'LRL', 'python'}

element = my_set.pop()
# print(element) 随机去除一个元素
# print(my_set)

# 清空集合
my_set.clear()

# 取两个集合的差集,两个原有集合不发生改变
set1 = {1, 2, 3}
set2 = {2, 3, 4}
new_set = set1.difference(set2)
# print(new_set) {1}

#消除两个集合的差集，在集合1里删除和集合2相同的元素
#会改变原有集合内容
set1.difference_update(set2)
# print(set1) {1}

#合并集合,不改变原有集合内容
set3 = set1.union(set2)
# print(set3) {1, 2, 3, 4}

for item in set3:
    print(item,end = " ")
