##function 1-leap year
def leap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return 'True'
            else:
                return 'False'
        else:
            return 'True'
    else:
        return 'False'               
y=int(input('Enter the Year to be checked:'))
res=leap(y)
print(res)
