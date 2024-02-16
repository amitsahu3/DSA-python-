# importing array module
from array import * 

# 1. creating and traversing an array
my_array= array('i',[1,2,3,4,5])

# for i in my_array:
#     print(i)

# # 2. accessing elements
# print(my_array[3])

# # 3. append any value 
# my_array.append(6)  # at the end (O(1))
# print(my_array)

# 4. insert value using insert function
# my_array.insert(1,9)        # tme consuming as shifting of elements takes place
# print(my_array)

# # 5. extend the array
# my_array1=array('i',[10,11,12])
# my_array.extend(my_array1)
# print(my_array)

# 6. add items from list into array using fromlist() fuction
# temp_list=[20,21,22]
# my_array.fromlist(temp_list)
# print(my_array)

# # 7. remove element
# my_array.remove(21)
# print(my_array)

# # 8. remove last using pop()
# my_array.pop()
# print(my_array)

# # 9. fetch any element using index()
# print(my_array.index(5))

# # 10. reverse() to reverse array
# my_array.reverse()
# print(my_array)

# # 11. get array buffer info through buffer_info() method
# print(my_array.buffer_info())   # (location, no of elements)-->(2657194163408, 5)

# # 12. check for no. of occurrences of an element using count() method
# my_array.append(5)
# print(my_array.count(5))

# 13. convert array to string using tolist() method
# strtemp= my_array.tostring()
# print(strtemp)

# 14. convert array to python list with same elements using tolist() 
print(my_array.tolist())

# 15. append a string to char array using fromstring()

# 16. slice the elements
print(my_array[:3]) 
