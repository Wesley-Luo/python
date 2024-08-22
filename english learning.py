import random

def new_quest():
    ind = random.choice([1,2,3,4])
    if ind == 1:
        plus()
    elif ind == 2:
        minus()
    elif ind == 3:
        times()
    else:
        divide()

def plus():
    a = random.randint(1,10)
    b = random.randint(1,10)
    print(str(a)+"+"+str(b))

def minus():
    b = random.randint(1,10)
    a = random.randint(1,10)
    while a <= b:
        a = random.randint(1,10)
    print(str(a)+"-"+str(b))

def times():
    a = random.randint(1,10)
    b = random.randint(1,10)
    print(str(a)+"*"+str(b))
