# print(type([1,1,2]))
print(type(float("12")), float("12"))

message = "world"
print("hello %s" % message)
num = 11.2345
print("%.2f" % num)

name = "Mike"
age = 32
print(f"my name is {name}, my age is {age}")  # f => format

# print("what is your name?")
# name=input("what is your name?")
# print("my name is %s"%name)
# print会自动换行，print("hello",end='') 这样就不会自动换行了

age = 30
if age >= 50:
    print("I am old now.")
elif age >= 18:
    print("young")
else:
    print("Still a kid.")
