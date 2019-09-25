n = [int(x) for x in input().split()]
min = n[0]
for i in n:
    if min>i:
        min=i
print(min,end="")
