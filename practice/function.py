# 定义全局变量
num = 100


def my_len(data):
    """
    计算字符串长度
    :param data: String
    :return: 返回字符串的长度
    """
    count = 0
    global num  # 指定修改全局变量
    num = 200
    print(num)
    for i in data:
        count += 1
    return count

def fun_return():
    """
    函数多个返回值
    用逗号隔开即可
    """
    return 1,2

def user_info(name,age,gender):
    """
    键值对传参
    """
    print(f"name:{name},age:{age},gender:{gender}")

def user_info(name,age,gender="male"):
    """
    缺省参数
    """
    print(f"name:{name},age:{age},gender:{gender}")

def user_info2(*args):
    print(f"Type:{type(args)},content:{args}")


def user_info3(**kwargs):
    print(f"Type:{type(kwargs)},content:{kwargs}")

len = my_len("abcd")
print(len)
print(num)

if not len:
    print("false")

x,y = fun_return()
print(x,y)

user_info(age=20,name="Andy",gender="male")
user_info(age=20,name="Mike")
user_info(age=20,name="Amy",gender="female")

#不定长 - 位置不定长，*号
# 不定长定义的形式参数会作为元组存在，接受不定长参数的传入
user_info2("Tom",20,"male","beijing")

# 不定长，关键字不定长，**号
user_info3(name="Tom",age=20,gender="male",addr="Beijing")

# 函数作为参数传入
# 适合数据是确定的，但是对数据的计算逻辑不确定的情况
def test_func(compute):
    result = compute(1,2)
    print(result)
    return result

def compute(x,y):
    return x+y

result = test_func(compute)
# print(result)

# lambda表达式，一次性函数的使用
test_func(lambda x,y : x+y)
