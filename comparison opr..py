#comparison operator (1)

year = int(input("Enter any year here :"))

if year % 4 == 0:
	print("It's a leap year")

else:
	print("Not a leap year")
	
#comparison operator (2)

str_1 = input("Enter your string :")
str_2 = input("Enter your string :")

if str_1 < str_2:
	print(f" {str_1} comes first alphabetically")
	
elif str_1 > str_2:
	print(f" {str_2} comes first alphabetically")
	
else:
	print("Both strings are same.")