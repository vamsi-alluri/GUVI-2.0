dummy = int(input())
n = [int(x) for x in input().split()]
minn = n[0]
maxx = n[0]
min_index = 0
max_index = 0
for i in range(1,dummy):
    if minn>n[i]:
        minn = n[i]
        min_index = i
    if maxx<n[i]:
        maxx = n[i]
        max_index = i
print(min_index,max_index,end="")
