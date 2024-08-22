import random

while True:
    a=random.randint(1,9)
    b=random.randint(1,9)
    ans=int(a)*int(b)
    print(str(a)+"*"+str(b)+"=?")
    word=input()
    try:
        if int(word)==int(ans):
            print("correct!")
        else:
            print("wrong!") 
    except:
        print("error")