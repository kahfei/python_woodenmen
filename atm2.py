import sys

raw_data = sys.stdin.readlines()
read_data = [ data.strip() for data in raw_data ]
transaction = map(int, ("".join(read_data)).split(" "))


balance = transaction[0]
amount = transaction[1]

def single_withdraw(amount):
	notes = [100,50,20]
	if amount % notes[0] == 0 :
		return True
	elif amount % notes[1] == 0 :
		return True
	elif amount % notes[2] == 0 :
		return True

def combine_withdraw(amount):
	notes = [100,50,20]
	remainder = amount % notes[0]
	if remainder > 0:
		remainder = remainder % notes[1]
		if remainder > 0:
			remainder = remainder % notes[2]
			if remainder > 0:
				return False
			else:
				return True
		else:
			return True
	else:
		return True

		
def withdraw(balance,amount):
	if balance < (amount + 1):
		print balance
	else:
		if single_withdraw(amount) == True:
			print balance - (amount + 1)
		elif combine_withdraw(amount) == True:
			print balance - (amount + 1)
		else:
			print balance

withdraw(balance,amount)



	


