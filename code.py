import sys
from itertools import groupby

raw_data = sys.stdin.readlines()
read_data = [ data.strip() for data in raw_data ]
number_of_test_case = read_data[0]
test_case = read_data[1:]

for case in test_case:
  words = list(case)
  uniq_words = "".join([ x[0] for x in groupby(words)])
  print len(case) -  len(uniq_words)
















    





  



