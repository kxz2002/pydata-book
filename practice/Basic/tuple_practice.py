#元组
t1 = (1,"hello",True)
t2=tuple()
# print(f"t1的类型{type(t1)},t1的内容是{t1}")

#嵌套元组
t2 =((1,2,3),(4,5,6))
# print(t2[1][0])  4

#查找元素下标
index = t1.index(1)
# print(index)

t3 = (2,2,2,"hello",True)
num = t3.count(2)
# print(num) 3

#len
len = len(t3)

#元组里面嵌套list，list里面的内容是可以修改的
t4=(1,2,3,["hello","world"])
t4[3][0] = "HELLO"
# print(t4) (1, 2, 3, ['HELLO', 'world'])