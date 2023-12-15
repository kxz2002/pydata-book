#列表List
names = ["Bob", "Tom", "Alice", "LRL"]
# print(names[-1]) #-1代表最后一个元素
#列表里的元素可以不一样数据类型
my_list1 = ["Hello",True,100]
#嵌套列表
my_list2 = [[1,2,3],[4,5,6]]
# print(my_list2[0][1]) #嵌套列表可以嵌套下标
newName = {name for name in names if len(name) > 3}

some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
tups = [[x for x in tup] for tup in some_tuples]
flattened = [x for tup in some_tuples for x in tup]
# print(tups) [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(flattened) [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(newName)
newDict = {key: len(key) for key in names}
# print(newDict)

# dictionary = dict()
# dictionary["LRL"] = 1
# print(dictionary)

dictionary=dict.fromkeys(names)
# print(dictionary) {'Bob': None, 'Tom': None, 'Alice': None, 'LRL': None}

newSet = set([1,2,3,4])
print(6 in newSet)
print(newSet)
newSet.add(100)
print(newSet)
newSet.remove(100)
newSet.discard(1)
newSet.update([12,20])
print(newSet)