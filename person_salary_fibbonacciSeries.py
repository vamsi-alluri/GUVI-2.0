a = 1
b = 1
n = int(input())
while n!=0:
    a,b = b,a+b
    n -= 1
print(b*1000,end="")
