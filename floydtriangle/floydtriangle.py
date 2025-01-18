b = int(input("Enter the number of rows : "))
n = 1
print("floydtriangle")
# Outer loops for rows
for i in range(1 , b+1):
    # inner loops for column
    for j in range(1 , i+1):
        print(n , end= " ")
        n = n+1
    print()