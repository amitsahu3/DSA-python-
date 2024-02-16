# my_dict = dict()
# print(my_dict)
# my_dict2 = {}
# print(my_dict2)

# UPDATE / ADD AN ELEMENT           # TC: O(n) ; SC: MORTIZED O(1) SPACE DOUBLES AFTER THE MAX LIMIT IS REACHED
my_dict = {'name':'edy', 'age':'26'}
my_dict['age'] = 27
my_dict['address'] = 'london'
my_dict['education'] = 'master'
#print(my_dict)

# TRAVERSAL             # TC:O(n) ; SC:O(1)
# def traversal(dict):
#     for key in dict:
#         print(key, dict[key])
#traversal(my_dict)

# LINEAR SEARCH             # TC: O(n) ; SC:O(1)
# def search(dict, value):
#     for key in dict:
#         if dict[key] == value:
#             return key, value
#     return 'value doesnot exist'
#print(search(my_dict, 27))

# DELETION

# using del         # TC: O(1), as uses hash table operation ; SC:O(1)
# del my_dict['age']
# print(my_dict)

# using pop         # TC: O(1), as uses hash table operation ; SC:O(1)
# removed_element = my_dict.pop('name', None)     # if not found then istead of raising an error it should return 'None'
# print(my_dict)

# using popitem() : deletes the last key:value pair
# TC: O(1) ; SC:O(1) hash table operation
# removed_element = my_dict.popitem()
# print(removed_element)

# using clear()     TC:O(N) ; SC:O(1) no addition memory required
# my_dict.clear()
# print(my_dict)

# DICTIONARY METHODS
# 1.clear()
# 2.copy(): creates a shallow copy , doesnot changes the original dictionary
# new_dict = my_dict.copy()
# print(new_dict)
# print(my_dict)
# 3. items() : returns a list of (key ,value )tuple

# 4. keys(): returns a view object that displays a list of keys
#print(my_dict.keys())

# 5. values(): returns a view object that displays a list of values
# print(my_dict.values())

# DICTIONARY COMPREHENSION
# import random
# city_names= ['paris', 'ny', 'london', 'madrid']
# city_temps = {city : random.randint(20,30) for city in city_names}
# # print(city_temps)
# above_25 = {city: temp for (city, temp) in city_temps.items() if temp > 25}
# print(above_25)

# DICTIONARY CODING
# 1. Frequency of words
# words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
# def count_words(words):
#     word_count = {}
#     for word in words:
#         if word not in word_count.keys():
#             word_count[word] = 0
#         word_count[word] += 1
#     return word_count
# print(count_words(words))

# 2. Common Keys
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 3, 'c': 4, 'd': 5}
# def merge_dicts(dict1, dict2):
#     common_keys = dict1.copy()
#     for key in dict2.keys():
#         if key in common_keys.keys():
#             common_keys[key] += dict2[key]
#         else:
#             common_keys[key] = dict2[key]
#     return common_keys
# print(merge_dicts(dict1, dict2))

# 3. higest value key
# my_dict = {'a': -5, 'b': 0, 'c': 222}
# def max_value_key(my_dict):
#     max = 0
#     max_key = ' '
#     for key in my_dict.keys():
#         if my_dict[key] > max:
#             max = my_dict[key]
#             max_key = key
#     return max_key
# print(max_value_key(my_dict))

# 4. exchanging the key value pair

# my_dict = {'a': 1, 'b': 2, 'c': 3}

# def reverse_dict(my_dict):
#     reversed_dict = {}
#     for key,value in my_dict.items():
#         reversed_dict[value] = key
#     return reversed_dict  
# print(reverse_dict(my_dict))

# # another method
# def reverse_dict(my_dict):
#     return {v: k for k, v in my_dict.items()}

# 5. Same Frequency
list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 2]
def check_same_frequency(list1, list2):
    
    dict1 = {}
    for i in list1:
        if i in dict1.keys():
            dict1[i] += 1
        else:
            dict1[i] = 1
    dict2 = {}
    for i in list2:
        if i in dict2.keys():
            dict2[i] += 1
        else:
            dict2[i] = 1    
    if dict1 == dict2:
        return True
    else:
        return False
    
print(check_same_frequency(list1,list2))


