age = int(input("Enter your age: "))  

if age >= 20:
    print("You are not allowed")
elif age < 10:
    print("You are too young to be allowed")
else:
    for i in range(10, 20):  
        if age == i:
            print(f"Age {age} is allowed")
            break
    else:
        print(f"Age {age} is not in the allowed range")
