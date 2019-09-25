n,m = map(int,input().split())
a = [int(x) for x in input().split()]
if m in a:
    print(a.count(m)-1,end="")
else:
    print("-1",end="")
    
