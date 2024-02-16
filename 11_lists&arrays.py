# # 1. FINDING PAIRS
# def findPairs(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] == nums[j]:          # as distincts pairs are allowed only
#                 continue
#             elif num[i] + num[j] == target:
#                 print(i,j)
# mylist= [1,2,3,2,3,4,5,6]
# findPairs(mylist,6)

# # 2. SEARCHING IN ARRAY
# import numpy as np

# myArray = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])


# def findNum(myArray, value):
#     for i in range(len(myArray)):
#         if myArray[i] == value:
#             print(i)
# findNum(myArray, 12)
# # 3. UNIQUE ELEMENTS IN A LIST
# list = [1,2,3,4,5,6,7,8,11,65]

# def isUnique(list):
#     a=[]
#     for i in list:
#         if i in a:
#             print(i)
#             return False
#         else:
#             a.append(i)
#     return True

# print(isUnique(list))
# # 4. PERMUTATION(if two lists are same or nit ,ie permutated forms of each other )
# def permutation(list1, list2):
#     if len(list1) != len(list2):
#         return False
#     list1.sort()
#     list2.sort()
#     if list1 == list2:
#         return True
#     else:
#         return False
# list1 = [1,2,3,4]
# list2 = [1,4,2,3]

# print(permutation(list1, list2))

# 5. ROTATE MATRIX
 