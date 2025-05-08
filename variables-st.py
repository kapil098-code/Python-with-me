#Variable = A container for a value  (string , integer, float, boolean)
#   A variable behaves as if it was the value it contains

#string
first_name = "bro"
print(first_name)
print(f"This was a string {first_name}")

#integer
age = 89
print(age)
print(f"this was my {age}")

#float
price = 13.2 
print(price)
print(f"the price is $ {price}")

#boolean
is_student = "true"
print(f"the person you meet is one of the faviourate coder {is_student}")

# boolean
is_student = False
for_sale = True

if for_sale:
    print("That item is for sale")
else:
    print("That item is Not available")