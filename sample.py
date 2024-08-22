# for i in range(1, 5):
#     print(i)
# print("Hello")
# print("World")
# i=2+i
# print(i)
# print("你的名字是甚麼")
# name=input()
# print("你好"+name)
# print("What is your name?")
# name=input()
# print("Hello " + name+"!")
import random
# for i in range(1, 5):
a=random.randint(1,9)
b=random.randint(1,9)
# print(str(a) + "*" + str(b) + "=?")
print(f"{a} * {b} = ?")
word=a*b
number=input()
if int(number)==word:
    print("correct!")
else:
    print("wrong!")