"""
闭包相关知识
有时使用全局变量并不安全，全局变量可能会被其他程序修改
"""


def outer(logo):
    def inner(msg):
        print(f"<{logo}>{msg}<{logo}>")

    return inner


# fn1 = outer("Python")
# fn1("hello") <Python>hello<Python>

# 使用nonlocal关键字修改外部函数的值
def outer1(num1):
    def inner1(num2):
        nonlocal num1
        num1 += num2
        print(num1)
    return inner1

# fn = outer1(10)
# fn(10) 20
# fn(10) 30