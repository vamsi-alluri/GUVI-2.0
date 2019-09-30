n = input()
if n[0]=='-' and (int(n[1])+int(n[len(n)-1]))%4==0:
    print("Yes",end="")
elif int(n)>0 and (int(n[len(n)-2])+int(n[len(n)-1]))%4==0:
    print("Yes",end="")
else:
    print("No",end="")
