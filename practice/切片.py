my_list = [0,1,2,3,4,5,6]
#从1开始到4结束，步长为1，进行切片
result1 = my_list[1:4]
# print(result1)  [1, 2, 3]

#从头开始，到尾结束，步长为1
result2 = my_list[:]
# print(result2)  [0, 1, 2, 3, 4, 5, 6]

#从头开始，到尾结束，步长为2
result3 = my_list[::2]
# print(result3)  [0, 2, 4, 6]

#从头开始，到尾结束，步长为-1(从后往前取) 
#这个方法很重要，可以实现倒序
result4 = my_list[::-1]
# print(result4)  [6, 5, 4, 3, 2, 1, 0]

#从4开始到1结束，步长为-1，进行切片
result5 = my_list[4:1:-1]
# print(result5)  [4, 3, 2]