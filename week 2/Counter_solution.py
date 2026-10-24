even = 0
odd = 0
print("Please enter the first whole number")
a=int(input())
print("Please enter the second whole number")
b=int(input())
print("Please enter the third number")
c=int(input())
if a%2==0:
    even +=1
else:
    odd +=1
if b%2==0:
    even +=1
else:
    odd +=1
if c%2==0:
    even +=1
else:
    odd +=1
print(f"There were {even} even and {odd} odd numbers.")
