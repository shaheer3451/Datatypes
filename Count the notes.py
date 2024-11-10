# Take total amount as input from user
amount_input = int(input("Please Enter Amount for Withdraw :"))
# Calculating the number of notes of different denominations
note_1 = amount_input//100
note_2 = (amount_input%100)//50
note_3 = ((amount_input%100)%50)//10
print("notes of 100 rupee" , note_1)
print("notes of 50 rupee" , note_2)
print("notes of 10 rupee" , note_3)