# properties of arrays 
"""
arrays can..
1. store data of specific type
2. contiguously stored
3. each element of an array has a unique index
4. support only basic data types"""

# creating an array
import array                               # tc:O(1) ; sc:O(1) for empty creation ,and O(n) for arrays with elements
my_array = array.array('i')                 # integer type 
my_array1 = array.array('i', [1,2,3,4,5])
#print(my_array1)

# import numpy as np
# np_array = np.array([],dtype = int) 
# print(np_array)
# np_array1 = np.array([1,2,3,4]) 
# print(np_array1)

# inserting in array
"""insert at a particular index and all elements will shift to the right """
my_array1.insert(5, 6)  # tc:O(n) ; sc:O(1)
#print(my_array1)

# traversal in array
def traversal_array(array):         # tc:O(n) ; sc:O(1)
    for i in array:
        print(i)
#traversal_array(my_array1)

# access an element
def access_element(array, index):     # tc:O(1) ; sc:O(1)
    if index > len(array):
        print('index error!')
    else:
        print(array[index])
# access_element(my_array1, 1)

# searching in array
def search_array(array, element):      # tc:O(n) ; sc:O(1)
    for i in range(len(array)):
        if array[i] == element:
            return i
    return -1
#print(search_array(my_array1, 2))

# deleting an element
"""delete and shift left all the elements as empty cell inside the array is mot allowed"""
# my_array1.remove(1)     # tc:O(n) ; sc:O(1)

# appending at the end
my_array1.append(7)
my_array1.insert(0,0)

# extending the array
my_array2 = array.array('i',[9,10])
my_array1.extend(my_array2)

# using from list
temp_list = [11,12,13]
my_array1.fromlist(temp_list)

#my_array1.pop()
#print(my_array1.index(2))
#my_array1.reverse()
#print(my_array1)

# buiffer info ,location and number of elements 
#print(my_array1.buffer_info())

# counting no of occurences of elements in array
# my_array1.append(11)
# print(my_array1.count(11))

new_list = my_array1.tolist()

#print(my_array1[4:])


# 2D ARRAYS
import numpy as np
array2D = np.array([[11,15,10,6], [10,14,11,5], [12,17,12,8], [15,18,14,9]])
#print(array2D)

# insertion in 2D array
# 1. adding columns (all columns will be right shifted)         tc:O(mn)
new_array2d = np.insert(array2D, 0, [[1,2,3,4]], axis = 1)      # axis = 1 means column and 0 means row
#new_array2d = np.append(array2D, [[1,2,3,4]], axis = 1)
#print(new_array2d)

# accessing in two dimensional array   tc:O(1) ; sc:O(1)
def access_elements(array, row, column):
    if row >= len(array) and column>= len(array[0]):        # len(array) = no of rows, len(array[0]) = no of columns
        print("incorrect index")
    else:
        print(array[row][column])
#access_elements(new_array2d, 1, 2)

# traversal in 2D array     tc:O(mn) ; sc:O(1)
def traversal_array(array):
    for i in range(len(array)):
        print('\n')
        for j in range(len(array[0])):
            print(array[i][j], end = " ")
# print(new_array2d)
# traversal_array(new_array2d)

# search in 2D array         tc:O(mn) ; sc:O(1)
def search_array2d(array, value):  
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return "found at index " + str(i) + " " + str(j)
    return "not found"
#print(search_array2d(new_array2d, 9))

# deletion in 2D array    tc:O(mn) ; sc:O(mn) as all elements need to be copied
"""copy all elements except the row and column to be deleted"""

new_DT_array = np.delete(new_array2d, 0, axis = 1)
print(new_DT_array)