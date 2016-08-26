
# -*- coding: utf8 -*-
#calculate your debts
#http://marioalvarez.me
#http://twitter.com/nezsbit
#http://github.com/nezbit

print 'This script is for calculate yours debts\n'

option = ['Yes', 'Y', 'yes']

print 'Do you want to pay any debt now? \n Yes or No? '
ask = raw_input() 

debt = 0
pays = 0

for ask in option:

	
	print 'How many you debt?'
	amount = float(raw_input())


	print 'How many you will pay NOW?'
	pay = float(raw_input())
	
	pays+= 1 
	
	debt = (amount - pay)

	if debt <= 0:
		print 'One debt less :D !! '
		print 'You payed in %d times \n'%pays
		break
	
	print 'What is the  % of APR?'
	apr = float(raw_input())
	
	calc = (apr / 100.0) * debt #calculate the % APR
	debt += calc

	print 'You debt %f' %debt

	if debt <= 0:
		print 'One debt less :D !! '
		print 'You payed in %d times \n'%pays
		break

if ask == 'no' or ask == 'No':
	print 'OK... Bye!!! \n' 
	quit()
	



 	