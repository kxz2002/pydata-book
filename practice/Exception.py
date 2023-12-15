try:
    f=open("F:/Repos/pydata-book/practice/test4.txt","r",encoding="UTF-8")
except:
    print("Except")

#捕获指定的异常
try:
    print(name)
    #1/0 更换为其他的异常模式，那么try except不会生效
except NameError as e:
    print(e)

#捕获多个异常
try:
    print(name)
    1 / 0
except(NameError,ZeroDivisionError):
    print("Except")


#捕获所有异常
try:
    print("hello")
    # print(name)
    # 1 /0 
    # f=open("F:/Repos/pydata-book/practice/test4.txt","r",encoding="UTF-8")
except Exception as e:
    print(e)
else:
    print("No Exception")
finally:
    #无论如何，finally语句必须执行
    # f.close()
    print("Finally")