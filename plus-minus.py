a=[1,1,0,-1,-1]
p=z=n=0
for i in a:
    if(i>0):
        p+=1
    elif(i==0):
        z+=1
    else:
        n+=1
b=len(a)
c=p/b
d=z/b
e=n/b
print("%.6f"%c)
print("%.6f"%e)
print("%.6f"%d)
