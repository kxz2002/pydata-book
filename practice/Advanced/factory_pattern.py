"""
工厂模式
将对象的生产由使用原生的类本身创建转换到由特定工厂方法来创建

好处：
大批量创建对象时有统一入口，方便维护代码
当发生修改时，仅修改工厂方法即可
符合世界现实的模式
"""

class Person:
    pass


class Student(Person):
    pass


class Worker(Person):
    pass


class Teacher(Person):
    pass


class PersonFactory:
    def getperson(self, p_type):
        if p_type == "w":
            return Worker()
        elif p_type == "s":
            return Student()
        else:
            return Teacher()


pf = PersonFactory()
worker = pf.getperson("w")
student = pf.getperson("s")
teacher = pf.getperson("t")
