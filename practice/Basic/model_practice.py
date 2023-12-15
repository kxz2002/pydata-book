# 使用import导入模块
# import time
# print("hello")
# time.sleep(2)
# print("hello")

# 使用from导入time的功能
# from time import sleep
# print("hello")
# sleep(2)
# print("hello")

# 使用*导入time的全部功能
# from time import *
# print("hello")
# sleep(2)
# print("hello")

# 使用as给特定功能上别名
# import time as tt
# tt.sleep(2)
# from time import sleep as sl
# sl(2)

# 导入自定义模块
# import my_model
# result = my_model.test_A(1,2)
# print(result)

# 如果从不同模块导入了相同名字的函数，
# 那么后一个导入的会覆盖掉前一个
# from my_model import *
# test_B(1,2)#报错

#导入自定义包
# import my_package.my_model1
# import my_package.my_model2
# my_package.my_model1.print_info1()
# my_package.my_model2.print_info2()

# from my_package import my_model1
# my_model1.print_info1()

# from my_package.my_model1 import print_info1
# print_info1()

from my_package import *
my_model1.print_info1()
# my_model2.print_info2() 报错