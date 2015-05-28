# cat input.txt | python sum.py

import sys

raw_data = sys.stdin.readlines()
read_data = [data.strip() for data in raw_data]

number_of_test_case = read_data[0]
test_cases = read_data[1:]

zipped_test_cases = zip(test_cases, test_cases[1:])[::2]

for case in zipped_test_cases:
  print sum(map(int,case[1].split()))
