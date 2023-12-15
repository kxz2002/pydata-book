#基础变量注解
import random
from typing import Union


var1:int = 1
var2:str = "String"
var3:bool = True

list1:list = [1,2,3,4]
# my_list: list[int] = [1,2,3,4]
tup1:tuple = (1,2,3)
var=random.randint(1,10) # type:int

# my_tup : tuple[Union[int,str]] = (1,2,"str")

#函数的注解：
#形参和返回值都是可以注解
#只是提示性的，并不影响实际参数的传入和返回值
def func(x:int,y:int) -> list:
    return x+y

def func_1(data:Union[int,str]) -> Union[int,str]:
    pass