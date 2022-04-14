n=int(input())
reverse=[]
for i in range(n):
    x=input()
    reverse.append(x)

reverseOrder= reverse[::-1]

print(*reverseOrder, sep="\n" )