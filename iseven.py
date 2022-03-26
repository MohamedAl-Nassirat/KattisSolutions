N,  K = [int(n) for n in input().split()]
product=1

for i in range(N):  
    a=int(input())
    if (a & 1) == 0:
        product *= a
    


if (product & ((1<<K)-1))== 0:
    print("1")
else: 
    print("0")
