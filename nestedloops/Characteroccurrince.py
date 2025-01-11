a = input("Write your own word :")
b = input("Give your character :")
i = 0
c = 0
while( i < len(a)):
    if(a[i] == b):
        c = c+1
    i = i+1
    print("The total number of " , b ,"is" , c )