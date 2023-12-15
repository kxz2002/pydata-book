import time
import threading


def sing(msg):
    while True:
        print(msg)
        time.sleep(1)


def dance(msg):
    while True:
        print(msg)
        time.sleep(1)


if __name__ == "__main__":
    # target: 要执行的目标任务名，也就是函数名
    # args: 以元组的方式传入的参数,这里加一个逗号是因为如果元组只有一个元素就需要在后面加逗号，否则会被认为是list
    # kwargs: 以字典的方式传入参数
    sing_thread = threading.Thread(target=sing, args=("I am singing",))
    dance_thread = threading.Thread(target=dance, kwargs={"msg": "I am dancing"})
    sing_thread.start()
    dance_thread.start()
