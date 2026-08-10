n=str(input("enter the word: "))
uppercase=0
lowercase=0
digitbox=0
spacebox=0
otherbox=0
for i in n:
    if i.isupper():
        uppercase+=1
    elif i.islower():
        lowercase+=1
    elif i.isdigit():
        digitbox+=1
    elif i.isspace():
        spacebox+=1
    else:
        otherbox+=1
print(f"uppercase: {uppercase}")
print(f"lowercase: {lowercase}")
print(f"digits: {digitbox}")
print(f"spaces: {spacebox}")
print(f"others: {otherbox}")


