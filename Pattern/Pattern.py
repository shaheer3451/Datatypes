a = int(input("Enter the number of rows : "))
 # Outer loop is for row
 
for i in range(a):
    # inner loop is for column
    
    for j in range(i+1):
        print("*", end =" ")
    print()