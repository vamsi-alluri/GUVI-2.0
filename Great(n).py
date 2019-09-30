n = input()
m = 0
j = 1
for i in n:
    m = m + int(i)
    j = j * int(i)
if m+j == int(n):
    print("Great",end="")
else:
    print("no",end="")
