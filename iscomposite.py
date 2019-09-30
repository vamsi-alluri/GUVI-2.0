n = int(input())
f = 1
for i in range(2,n//2):
    if n%i==0:
        f = -1
        break
if f == -1:
    print("yes",end="")
else:
    print("no",end="")
