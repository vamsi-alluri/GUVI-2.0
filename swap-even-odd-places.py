n = input()
for i in range(1,len(n),+2):
  	print(n[i]+n[i-1],end="")
if len(n)%2!=0:
  	print(n[len(n)-1])
