from collections import Counter

def int_to_list_of_ints(number):
    list_of_ints = [int(x) for x in str(number)]
    return list_of_ints

def check_non_decresing(list_of_ints):
    correct = False
    for ix, x in enumerate(list_of_ints):
        if ix < len(list_of_ints)-1:
            if list_of_ints[ix] <= list_of_ints[ix+1]:
                correct = True
            else:
                correct = False
                break
    return correct

def check_groups(list_of_ints):
    counted = Counter(list_of_ints)
    groups = 0
    for x in counted.values():
        if x >=2:
            groups += 1
    if groups > 1:
        return True
    return False
    

def check_correct_range(number):
    if 372**2 <= number <= 809**2:
        return True
    return False


numbers = 0
for number in range(372**2,809**2+1):
    if check_correct_range(number) and check_non_decresing(int_to_list_of_ints(number)) and check_groups(int_to_list_of_ints(number)):
        numbers += 1

print(numbers)
