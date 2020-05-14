##Vending Machine-Break
candy=int(input("ENter the Number of Candies:"))
i=1
av=10
while i<=candy:
    if i>av:
        print("Out of Stock")
        break
    print("candy")
    i+=1
print("BYE")
