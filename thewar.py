##The War
r,a,c=input().split()
##print(r,a,c)
p=0
for i in range(1,int(r)+1):
    for j in range(1,int(c)+1):
        if (i+j)%2!=0:
            p+=1
print(p)
