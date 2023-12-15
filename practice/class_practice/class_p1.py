class Student:
    name = None
    age = None
    tel = None

    #构造方法
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        # print(f"name:{self.name},age:{self.age},tel:{self.tel}")
    
    #__str__魔术方法
    def __str__(self) -> str:
        return f"name:{self.name},age:{self.age},tel:{self.tel}"

    #__lt__小于符号比较方法
    def __lt__(self,other):
        return self.age<other.age
    
    #__lr__支持了<=,>=
    def __le__(self,other):
        return self.age<=other.age
    
    def __eq__(self, other: object) -> bool:
        return self.age == other.age
    
    def say_hi(self):
        print(f"I am {self.name},hello")

    def say_hi2(self, msg):
        print(f"I am {self.name},{msg}")


stu1 = Student("Amy",20,"111111")
stu2=Student("Mike",15,"222222")
stu3=Student("Amy",20,"111111")
# stu1.name = "Mike"
# print(stu1)

# print(stu1>=stu2)
print(stu1==stu2)
# stu1.say_hi()
# stu1.say_hi2("hello everyone")
