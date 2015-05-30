import sys
import re
import operator
from dateutil import parser

raw_data = sys.stdin.readlines()
read_data = [ data.strip() for data in raw_data ]
number_of_test_case = read_data[0]
test_case = read_data[1:]
birthdate_list = {}

for case in test_case:
	personName= re.match(r'^\S*', case).group(0)
	personName
	birthdate = case.replace(personName,"")
	formated_birthdate = parser.parse(birthdate, dayfirst=True)
	birthdate_list[personName] = formated_birthdate



sorted_birthdate_list = sorted(birthdate_list.items(), key=operator.itemgetter(1))


print sorted_birthdate_list[-1][0]
print sorted_birthdate_list[0][0]
