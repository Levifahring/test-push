# @TODO: Your code here
#fish = "halibut"

#letters = []

#for letter in fish: 
	letters.append(letter)
#print(letters)


#list comprehension
#letters = [letter for letter in fish]

#print(letter)


capital_letters = []
for letter in fish:
	capital_letters.append(letter.upper())
print(capital_letters)

capital_letters = [letter.upper() for letter in fish]

july_temperatures = [87, 85, 92, 79, 106]
hot_days = []

for temp in july_temperatures:
	if temp > 90:
		hot_days.append(temp)
print(hot_days)

hot_days = [temp for temp in july_temperatures if temp > 90]