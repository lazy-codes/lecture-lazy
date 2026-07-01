#Ticket price checker

age = input("Enter your age :")

age_int = int(age)

if age_int <= 0:
	print("Invalid age\nEnter valid age")
	
elif age_int <= 15:
	price = 29
	print(f"Here's your child ticket price :{price}")
	
elif age_int >=55:
	price = 59
	print(f"Here's your senior ticket price :{price}\n Discount applied")
	
else:
	price = 99
	print(f"Here's your adult ticket price :{price}")