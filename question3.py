n=int(input("enter the number: "))
for i in range(1,11):
    j=i*n
    if j%2==0:
        result="even"
    else:
        result="odd"
    print(f"{n} x {i} = {j} is {result}")
