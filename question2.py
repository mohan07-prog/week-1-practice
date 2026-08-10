name=(input("customer name: "))
age=int(input("age: "))
ticket=int(input("number of tickets: "))
if age<12:
    rate=120
elif age>12 and age<59:
    rate=200
else:
    rate=150
total=ticket*rate
if ticket>=5:
    discount=total*0.1
else:
    discount=total
print("customer name",name)
print("age",age)
print("number of tickets:",ticket)
print("rate:",rate)
print("total:",total)
print("discount:",discount)
print("final amount:")
    