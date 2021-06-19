x=int(input("enter :"))
y=input("Enter :").split()
n=input("enter :")
z=[]
for i in range(int(n)):
    a,b=set(input("Enter :")),input("Enter :")
    if(a=="interaction_update"):
        d=[input("enter :").split() for j in range(int(b))]
        y.intersection_update(set(d))
        z.append(y)
    elif(a=="update"):
        d=[input("enter :").split() for j in range(int(b))]
        y.update(set(d))
        z.append(y)
    elif(a=="symmetric_difference_update"):
        d=[input("enter :").split() for j in range(int(b))]
        y.symmetric_difference_update(set(d))
        z.append(y)
    elif(a=="difference_update"):
        d=[input("enter :").split() for j in range(int(b))]
        y.difference_update(set(d))
        z.append(y)
    else:
        pass
print(len(z))
