import random
word=random.randint(0,9)
lenth=input("請輸入需要的密碼長度:")
try: 
    if int(lenth)<=20:
        for time in range(int(lenth)-1):
            word=word*10+random.randint(0,9)
        print(f"這是你的密碼:{str(word)}")
        print("請等待...")
        for i in range((int(lenth)*2900000)-(int(lenth)*int(lenth)*int(lenth))):
            a=0
        for p in range(50):
            print("")
        print("請再次輸入密碼:")
        ans=input()
        if str(word)==ans:   
            print("密碼正確!")
        else:
            print("密碼錯誤!")
except:
    print("請輸入數字。")