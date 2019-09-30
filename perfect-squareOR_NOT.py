import math
n,m = map(int,input().split())
a = math.sqrt(n*m)
if a*a == n*m:
    print("yes",end="")
else:
    print("no",end="")
