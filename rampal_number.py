n = int(input())
m = 0
if n>0:
    i = 0
    while i!=2:
        i+=1
        t = n%10
        m = m + t
        n //= 10
elif n<0:
    n = abs(n)
    m = n%10
    while n>10:
        n //= 10
    m += n
if m%4==0:
    print("yes",end="")
else:
    print("no",end="")
