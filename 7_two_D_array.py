# we use numpy module as it works best with multidimensional array
import numpy as np

array2d = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(array2d)

# 1. INSERTION

# #inserting column(axis=1)
# new_array2d = np.insert(array2d, 0, [[1,2,3,4]],axis=1) #new_array2d = np.append(array2d,[[1,2,3,4]],axis=1) ,append is used to add at the end of array 
# print("column adding")    
# print(new_array2d)

# #inserting row(axis=0)
# new_array2d = np.insert(array2d, 0, [[1,2,3,4]],axis=0) 
# print("row adding")       
# print(new_array2d)

# # 2. ACCESSING 
# def array_access(array2d, row_idx, column_idx):
#     if row_idx >= len(array2d) and column_idx >= len(array2d):
#         print("incorrect index")
#     else:
#         print(array2d[row_idx][column_idx])

# array_access(array2d, 2,3)

# # 3. TRAVERSAL 
# def traversal(array):
#     for i in range(len(array)): # length of array is row length,if we put index 0 then column length 
#         for j in range(len(array[0])):
#             print(array[i][j])
# traversal(array)

# # 4. LINEAR SEARCHING 
# def search(array,value):
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             if array[i][j] == value:
#                 return "the value is located at index:" +str(i)+" ,"+str(j)
#     return "not found"
# print(search(array2d,14))

# DELETION
new_array = np.delete(array2d, 0, axis = 1)
print(new_array)