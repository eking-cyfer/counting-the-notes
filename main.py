# Taking total amount as input from user
Amount = int(input("Please Enter Amount for Withdraw : "))

# Calculating the number of notes of different denominations
note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10

print("notes of 100 cedis", note_1)
print("notes of 50 cedis", note_2)
print("notes of 10 cedis", note_3)
