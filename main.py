import random
cnumber = random.randrange(1,101)
usernum = int (input("Enter your Number.......")) 
if usernum>cnumber:
    print("cumputer number",cnumber)
    print("your Gussing num is too high")
elif cnumber>usernum:
    print("cumputer number",cnumber)
    print("Your gussing num is too low")   
else:
    print("cumputer number",cnumber)
    print("Your Gussing num is equal")     
