n = int(input())
if n == 0:
    print("yes")
else:
    po = 1
    while (po<n):
        po = po * 2
    if po == n:
        print("yes")
    else:
        print("no")
