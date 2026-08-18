def check_even_odd(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
n=int(input("enter the number: ")) 
result=check_even_odd(n)
print(result)
print(result*8)