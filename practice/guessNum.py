import random
target = random.randint(0,100)
num = int(input("Please enter a number.\n"))
while True:
    if num==target :
        print("Success !\n")
        break
    else:
        if num > target:
            print("Larger\n")
            num = int(input("Please enter a number.\n"))
        else:
            print("smaller\n")
            num = int(input("Please enter a number.\n"))


