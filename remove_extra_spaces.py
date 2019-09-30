n = [*input()]
space = 0
l = []
for i in range(len(n)):
    if n[i] == " " and space==0:
        l.append(n[i])
        space += 1
    elif n[i] == " " and space>=1:
        pass
    else:
        l.append(n[i])
        space = 0    
print(n)
        
