# mydict = {
#     'name': 'eddy',
#     'age' : '27'
# }

# # 1. UPDATING ELEMENTS  # O(1) as adding value using a key
# mydict['address'] = 'London'

# 2. TRAVERSAL 
# def traverse(mydict):       # O(n) 
#     for key in mydict:      # O(1)
#         print(key, mydict[key])
# traverse(mydict)

# # 3. SEARCHING
# def search(mydict, value):
#     for key in mydict:      # tc: O(n), sc:O(1) as no ectra space is needed
#         if dict[key] == value:
#             print( key, value)
#         else:
#             print("the value does'nt exist")
# print(search(mydict, 27 ))

# # 4. DELETING 
# # tc: O(1) mostly, amortized O(n) in some cases
# # sc: O(1)
# mydict = {'name':'eddy', 'age':26, 'address':'london', 'education': 'masters'}
# print(mydict.pop('name'))   # returns value to be deleted(only deletes the value not key)
# print(mydict.popitem()) # delete any arbitrary key:value pair
# print(mydict.clear())   # clear all key:value pairs
# del mydict['age']   # any pair with key given

# 5. 
""" a) clear() doesnt take or return any parameter (none)
    b) copy() creates a shallow copy of dictionary without modifying it, no parameters taken
    c) fromkeys() returns a new dictionary with q sequence of keys
        newdict = {}. fromkeys([1,2,3], 0) # dictionary.fromkeys(sequence[],values)
        {1:0, 2:0, 3:0}
    d) get()
        mydict.get('age', 27)   # return 26 the value matching with key age
        mydict.get('city', 27)  # return 27 as city key doesnt exist
        mydict.get('city')      # returns none
    e) items() return all key value pairs
    f) keys() return keys
"""
