S=int(input())
G=list(map(int,input().split()))[:S]
a=len(G)
l2=[]
for i in range(a):
  b=i+1
  for j in range(b,a):
    if G[i]==G[j] and G[i] not in l2:
      l2.append(G[i])
l2.sort()
if len(l2)==0:
    print("unique")
else:
    print(*l2,end=' ')
