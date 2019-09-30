a,b,n = input().split()
n = int(n)
l = min(len(a),len(b))
diff = 0
for i in range(l):
    if a[i]!=b[i]:
        diff += 1
if diff == n:
    print("yes",end="")
else:
    print("no",end="")
