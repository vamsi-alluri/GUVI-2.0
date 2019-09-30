dummy = int(input())
n = input().split()
n = "".join(n)
res = []
for i in range(1,dummy,+2):
    res.append(n[i])
    res.append(n[i-1])
if len(n)%2!=0:
    res.append(n[len(n)-1])
print(" ".join(res))
