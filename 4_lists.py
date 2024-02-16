# # accessing elements of list
# shopping_list = ['milk', 'cheese', 'butter']
# #print(shopping_list[-2])

# # traversing through a list
# # for i in shopping_list:
# #     print(i)

# # inserting and updating
# mylist = [1,2,3,4,5,6]
# newlist = [7,8,9]
# #mylist[2] = 33
# mylist.extend(newlist)
# #print(mylist)

# # search in list 
# target =  4
# # if target in mylist:
# #     print("in list")
# # else:
# #     print("not found")

# # def seach_list(plist, target):                  # tc:O ; sc:O(1)
# #     for i, value in enumerate(plist):            # eneumerate keeps track of index and value both
# #         if value == target:
# #             return i
# #     return -1
# # print(seach_list(mylist, target))

# # operations in list
# a = [1,2,3]
# b = [4,5,6]
# #print(a+b)      # concatenation

# a = a*4
# #print(a)

# # strings from list
# a = 'spam0,spam1,spam2'
# b = a.split(",")            # delimiter = separtor
# c = ['hey', 'there']
# d = (' '.join(c))
# # print(c)
# # print(a)
# #print(d)

# # list comprehension        ( strings(other sequences) can also be comprehended)
# prev_list = [1,2,3]
# new_list = [i*2 for i in prev_list]
# new_list1 = [i for i in prev_list if i < 2]
# #print(new_list1) 

# sentence = "My name is amit"
# def is_consonants(letter):
#     vowels = "aeiou"
#     return letter.isalpha() and letter.lower() not in vowels

# consonants = [i for i in sentence if is_consonants(i)]
# #print(consonants)

# prev_list = [-1,10,-20,70,-90]
# new_list = [number if number > 0 else 0 for number in prev_list]
# #print(new_list)

# # # NO OF DAYS PROGRAM
# # temps = []
# # n = int(input('no of days:'))
# # for i in range(n):
# #     temp = float(input(f'enter temperature for day {i}'))
# #     #temp = 0
# #     temps.append(temp)
# # avg = sum(temps)/n
# # days = 0
# # for i in range(n):
# #     if temps[i] > avg:
# #         days+=1
# # #print(f"average = {avg} \n {days} above average")

# find all pairs of integers whose sum is equal to a given number
# mylist = [2,6,3,9,11]
# num = int(input('enter target:'))
# def findpairs(mylist, num):
#     for i in range(len(mylist)):
#         for j in range(i+1, len(mylist)):
#             if mylist[i] == mylist[j]:
#                 continue
#             elif mylist[i] + mylist[j] == num:
#                 print(mylist[i], mylist[j]) 
# findpairs(mylist, num)

# IF ARRAY CONTAINS A NUMBER
# import numpy as np
# myarray = np.array([1,2,3,4,5,6,7,8,9])
# def search_array(myarray, value):
#     for i in range(len(myarray)):
#         if myarray[i] == value:
#             print(f'found at {i} position')
        
# search_array(myarray, 4)

# MAX PRODUCT OF TWO INTEGERS 
# def max_product(arr):
#     arr.sort(reverse=True)
#     return arr[0]*arr[1]

# REMOVING THE DUPLICATES
# mylist = [1,1,2,3,3,2,4]
# newlist = []
# def remove_duplicates(mylist):
#     for element in mylist:
#         if element in newlist:
#             continue
#         else:
#             newlist.append(element)
# remove_duplicates(mylist)
# print(newlist)
    
# FIND ALL PAIRS OF AN INTEGER ARRAY WHOSE SUM IS EQUAL TO A GIVEN NUMBER
# def pair_sum(arr, target_sum):
#     result = []
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] + arr[j] == target_sum:
#                 result.append(f"{arr[i]}+{arr[j]}")
#     return result
 
# arr = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
# target_sum = 7
# print(pair_sum(arr, target_sum))


# UISNG SET() TO FIND DUPLICATES
# def contains_duplicate(nums):
#     seen = set()
#     for num in nums:
#         if num in seen:
#             return True
#         seen.add(num)
#     return False

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
# print(contains_duplicate(nums))

# TWO LISTS PERMUTATIONS OF EACH OTHER
# def permutations(list1, list2):
#     if len(list1) != len(list2):
#         return False
#     list1.sort()
#     list2.sort()
#     if list1 == list2:
#         return True
#     else:
#         return False
    
# list1 = ['a', 'b', 'c']
# list2 = ['b', 'c', 'a']
# print(permutations(list1, list2))

# ROTATION OF MATRIX

# METHOD 1
# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]
# def rotate(matrix):

#     # TRANSPOSING THE MATRIX
#     a = []
#     for i in range(len(matrix)):
#         c = []
#         for j in range(len(matrix[0])):
#             c.append(matrix[j][i])
#         a.append(c)
    
#     # EXCHANING FIRST AND LAST COLUMNS
#     blank = []
#     for i in range(len(matrix)):
#         blank1 = []
#         for j in range(len(matrix[0])-1, -1, -1):
#             blank1.append(matrix[j][i])
#         blank.append(blank1)

#     return blank
# print(rotate(matrix))

# METHOD 2
# def rotate(matrix):
#     # TODO
#     n = len(matrix)
 
#     # Transpose the matrix
#     for i in range(n):  # Iterate over the rows
#         for j in range(i, n):  # Iterate over the columns starting from the current row 'i'
#             # Swap the elements at positions (i, j) and (j, i)
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
 
#     # Reverse each row
#     for row in matrix:  # Iterate over each row in the matrix
#         row.reverse()  # Reverse the elements in the current row
#     return matrix
