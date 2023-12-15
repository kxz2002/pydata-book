"""
装饰器
不破坏目标函数原有的代码和功能的前提下，为目标函数新增功能
"""
#装饰器的一般写法：闭包
# def sleep():
#     import random
#     import time
#     print("sleeping...")
#     time.sleep(random.randint(1,5))

# def outer(func):
#     def inner():
#         print("I am going to sleep")
#         func()
#         print("I am going to get up")
#     return inner

# fn = outer(sleep)
# fn()

#装饰器的快捷写法：语法糖
def outer(func):
    def inner():
        print("I am going to sleep")
        func()
        print("I am going to get up")
    return inner

@outer
def sleep():
    import random
    import time
    print("sleeping...")
    time.sleep(random.randint(1,5))

sleep()