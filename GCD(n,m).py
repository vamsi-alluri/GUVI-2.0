n = [int(x) for x in input().split()]
mi = min(n)
ma = max(n)
del n
if mi ==0:
    print(ma)
else:
    for i in range(mi,0,-1):
        if ma%i==0:
            print(i,end="")
            break
    else:
        print("-1",end="")
