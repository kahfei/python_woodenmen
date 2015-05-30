import sys

raw_data = sys.stdin.readlines()
read_data = [ data.strip() for data in raw_data ]
transaction = map(int, ("".join(read_data)).split(" "))
bank_charges = 1

balance = transaction[0]
amount = transaction[1]



notes = iter([100, 50, 20]) 

def no_small_change(amount):
	if amount % 10 == 0: 
		return True

def withdraw(amount):
  if no_small_change(amount):
  	remainder = amount % notes.next()
  	if remainder > 0:
  		remainder = remainder % notes.next()
  		if remainder > 0:
  			remainder = remainder % notes.next()
  	print "Your balance is {balance}".format(balance=balance-amount)
  else:
  	print balance

withdraw(amount)





  
 
