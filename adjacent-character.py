str=input()
l=len(str)
if l%2==0:
    a=0
    s=''
    for i in range(0,len(str),2):
        s+=str[i:i+2][::-1]
    print(s)
else:
    print('Odd length.')
