n1=input()
k=1
for j in range(len(n1)-1):
    s=n1[j]+n1[j+1]
    p=int(s)
    if p<=26 and n1[j]!="0":
        k+=1
if k==3:
    print(k)
else:
    print(k+(k-1)//2)
