print("Enter your marks obtained in 5 subjects:   ")
mark1=int(input("Mark1: "))
mark2=int(input("Mark2: "))
mark3=int(input("Mark3: "))
mark4=int(input("Mark4: "))
mark5=int(input("Mark5: "))
mark6=int(input("Mark6: "))
mark7=int(input("Mark7: "))
avg = mark1+mark2+mark3+mark4+mark5+mark6+mark7
tot = avg/7
if avg >= 90:
    print("grade A*")
elif avg >= 80:
    print("grade A")
elif avg >= 70:
    print("B*")
elif avg >= 60:
    print("C")
elif avg >= 50:
    print("grade D")
elif avg >= 40:
    print("grade E-")
elif avg >= 20:
    print("F-") 
else:
    print("Invalid input please try again!")
