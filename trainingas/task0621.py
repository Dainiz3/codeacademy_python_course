# Create a public function, generate a dictionary with 10 random key value pairs.
# Keys: randon letter 
# Values: random number from 0 until 30
# Return: grazinti su Key didziausia value

# def randDict(n):
#     from random import randint

#     keys  = ["key"+str(i) for i in range(n)]
#     values = ["value"+str(i) for i in range(n)]
#     final_dict={}
#     for key in keys:
#         final_dict[key]=values.pop(randint(0,n))

#  print(final_dict) 

import random, string

def bigest_value(my_dictionary: dict) -> int:
    return max(my_dictionary.values())

def dict_generator():
    my_dictionary = {}

    while True:
        random_letter = random.choice(string.ascii_lowercase)
        random_number = random.randint(1, 30)

        if random_number not in my_dictionary.values():
            my_dictionary[random_letter] = random_number
        if len(my_dictionary) >= 10:
            break
    print(my_dictionary)
    return max(my_dictionary, key=my_dictionary.get)

print(dict_generator())

