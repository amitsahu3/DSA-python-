# 1. updating /inserting the list 

# mylist = [1,2,3,4,5,6,7]
# print(mylist)

# mylist.insert(4,15) # O(n) as we have to shift every element right
# mylist.append(55)   # O(1) as adding to the end
# print(mylist)
# newlist = [8,9,10]
# mylist.extend(newlist) # O(n) as we might have n/m elements 
# print(mylist)

# mylist[1:2] = ['x', 'y']    # using slice operator upadting multiple indxs
# print(mylist)

# # 2. deleting  
# mylist.pop(1) # idx based  O(1)/O(n)
# print(mylist)

# del mylist[2:4] # using slice can dkt multiple elements, idx based also O(n)
# print(mylist)

# mylist.remove(5)  # value based O(n)
# print(mylist)

# 3. searching 
# if 4 in mylist:
#     print(mylist.index(4))     # O(n) as all elements will be searched
# else:
#     print("value doesnot exist.")

# def search(list,value):
#     for i in list : # O(n) as all elements will be searched 
#         if i == value:
#             print(list.index(value))
#     return " value doesnot exist"
# search(mylist, 5)
# LIST OPERATORS

# # * : repeat any thing 
# a=[0,1]
# a=a*4
# print(a)    # [0, 1, 0, 1, 0, 1, 0, 1]

# a= "spam"
# b=list(a)
# print(b)    # ['s', 'p', 'a', 'm']

# # DELIMITER AND JOIN
# delimiter= '+'
# c=['hi','i','am','amit']
# print(delimiter.join(c))    # hi+i+am+amit
