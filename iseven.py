from time import process_time

t1_start = process_time() 
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

t1_stop = process_time()
   
print("Elapsed time:", t1_stop, t1_start) 
   
print("Elapsed time during the whole program in seconds:",
                                         t1_stop-t1_start) 












#import math

#N,  K = [int(n) for n in input().split()]
#logSum=0


















#for i in range(N):  
#    logSum += math.log(int(input()), 2)
#print(logSum)
#print((2**(logSum-K)))
#if (2**(logSum-K)).is_integer() == True:
#    print("1")
#else: 
#    print("0")