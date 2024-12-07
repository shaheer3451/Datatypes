medical_cause = input(" Did you have a medical cause Y or N")
attendance = int(input("Enter the Attendance of the students"))
 
 
if  medical_cause == "Y":
    print("allowed")
else:
    if attendance >= 75:
        print("allowed")
    else:
        print("Not allowed")
 
    