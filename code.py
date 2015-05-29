import sys

raw_data = sys.stdin.readlines()
read_data = [ data.strip() for data in raw_data ]
number_of_test_case = read_data[0]
test_case = read_data[1:]




def remove_identical_character(words):
    iwords = iter(words)
    clean_word = []
    first_item = iwords.next()
    second_item = iwords.next()
    if first_item == second_item:
      clean_word.append(first_item)
    else:
      clean_word.append(first_item)
      clean_word.append(second_item)

    return clean_word
    
    


for case in test_case:
  print remove_identical_character(case)
    





  



