import random
goal = 0

def count():
    global goal
    if int(word) == ans:
        goal = goal + 1
        print("correct!")
    else:
        goal = goal - 1
        print("wrong!")

    print("score:"+str(goal))

while True :
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    c = random.randint(1, 3)

    if c == 1:
        ans = int(a)*int(b)
        print(str(a)+"*"+str(b)+"=?")
        word = input()
        count()
    elif c == 2:
        ans = int(a)+int(b)
        print(str(a)+"+"+str(b)+"=?")
        word = input()
        count()
    else:
        if a > b:
            ans = int(a)-int(b)
            print(str(a)+"-"+str(b)+"=?")
            word = input()
            count()
        else:
            ans = int(b)-int(a)
            print(str(b)+"-"+str(a)+"=?")
            word = input()
            count()
    if goal==10:
        print("you win!")
        break
