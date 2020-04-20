#Rental Car Final Project
#Final Draft
#Josh Ryther
#02/03/20

import sys
##Collect Customer Data (Rental Code and Rental Period)
rentalCode = input('(B)udget, (D)aily, or (W)eekly rental?\n')
rentalCode = str(rentalCode.upper())

if rentalCode not in ['B', 'D', 'W']:
	exit('Input error.  Please try again')
if rentalCode == 'B' or rentalCode == 'D':
	rentalPeriod = input('Number of Days Rented:\n')
else:
	rentalPeriod = input('Number of Weeks Rented:\n')

##Variable Example 1: Assigning a string and number to a variable
B = budget_charge = 40.00
D = daily_charge = 60.00
W = weekly_charge = 190.00

##Collect Customer Data (Miles traveled)
odoStart = input('Starting Odometer Reading:\n')
odoEnd = input('Ending Odometer Reading:\n')
totalMiles = int(odoEnd) - int(odoStart)

##Calculating Charges (Base Charge)
if rentalCode.title() == 'B':
##Variable Example 2: Modifying variables with data-type-appropriate operators
	baseCharge = float(rentalPeriod) * float(budget_charge)
elif rentalCode.title() == 'D':
	baseCharge = float(rentalPeriod) * float(daily_charge)
elif rentalCode.title() == 'W':
	baseCharge = float(rentalPeriod) * float(weekly_charge)
else:
	print('Input error.  Please try again.')

##Above and below are uses of branches.  There are examples of if, elif, and else statements
##Above: The if statement executes the correct base charge depending on the rental code inputed
##Below: The if statement calculates the correct charges based on miles driven depending on the rental code

##Calculating Charges (Charges based on miles traveled)
if rentalCode == 'B':
	mileCharge = totalMiles * 0.25
elif rentalCode == 'D':	
	averageDayMiles = int(totalMiles)/int(rentalPeriod)
	if averageDayMiles <= 100:
		extraMiles = 0
	elif averageDayMiles > 100:
		extraMiles = averageDayMiles - 100
	mileCharge = extraMiles * 0.25
elif rentalCode == 'W':
	averageWeekMiles = int(totalMiles)/ int(rentalPeriod)
	mileCharge = 0.0
	if averageWeekMiles > 900:
##Variable Example 3: Changing variable values
		mileCharge = 100.00 * int(rentalPeriod)

amtDue = int(baseCharge) + int(mileCharge)

##Rental Summary
print('\n\n\n\nRental Summary\n')
print('Rental Code: ' + rentalCode)
print('Rental Period: ' + rentalPeriod)
print('Starting Odometer: ' + odoStart)
print('Ending Odometer: ' + odoEnd)
print('Miles Driven: ' + str(totalMiles))
print('Amount Due: ' + '$%.2f' % amtDue)
