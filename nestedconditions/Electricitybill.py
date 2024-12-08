units = int(input("Enter the units you have consumed"))
# Let's check the electricity bill of the user



if units <= 50:
    amount = units * 2.60
    supercharge = 25

elif units <= 100:
    amount = 130 + ( (units - 50) * 3.25)
    supercharge = 35
elif units <= 200:
    amount = 130 + 162.5 + ( (units - 100) * 5.26)
    supercharge = 45
else:
    amount = 130 + 162.5 + 526 + ((units - 200) * 8.45)
    supercharge = 75
    
total = amount + supercharge
print("\n the electricity bill = %.2f" %total)