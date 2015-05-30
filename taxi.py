import sys
import math 
raw_data = sys.stdin.readlines()
read_data = [ data.strip() for data in raw_data ]
number_of_groups = read_data[0]
groups = read_data[1:]

total_people = sum(map(int,("".join(groups)).split(" ")))

number_of_taxi = int(math.ceil(total_people / 4))

print number_of_taxi

