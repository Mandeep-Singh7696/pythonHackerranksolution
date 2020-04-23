##
f=open('f1.txt','r')
s=''
for i in f:
##    print(i[0])
    if len(i)>len(s):
        s=i
print(s)
f.close()
