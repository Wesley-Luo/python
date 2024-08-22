print("please enter a number:")
ans=int(input())
total=[]
for scan in range(ans):
    if ans%(scan+1)==0:
        total.append(scan+1)
print("answer:"+str(total))