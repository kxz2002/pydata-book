class Animal:#包含了抽象方法，因此这是一个抽象类
    def speak(self):
        pass #没有具体的方法体，因此这是一个抽象方法

#我们一般不会使用抽象类，而是使用抽象类具体的实现
class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Miao")


def make_noise(animal:Animal):
    animal.speak()


dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)