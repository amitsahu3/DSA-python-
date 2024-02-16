# creating a tuple      tc:O(1) , sc:O(n)
# newTuple = ('a', 'b', 'c', 'd')
# newtuple1 = tuple('abcde')  
# # print(newtuple1)
# print(newTuple)

# traversing a tuple        tc:O(n) , sc:O(1)
# for i in newtuple1:
#     print(i)

# search tuple
#print('f' in newtuple1)         #tc: O(n)

#print(newtuple1.index('e'))     #tc: O(n)

# def search(newtuple1, element):     # tc:O(n) ; sc:O(1)
#     for i in range(0, len(newtuple1)):
#         if newtuple1[i] == element:
#             return f'{element} found at {i} index'
#     return ' not found'
# print(search(newtuple1, 'f'))

# tuple operation
#print(newtuple1+newTuple)
# print(newTuple*2)

# mytuple = (1,2,3,4,2,1,3)
#print(mytuple.count(2))
#print(mytuple.index(2))
# print(tuple([1,2,1]))

# sum and product
# input_tuple = (1, 2, 3, 4)

# def sum_product(input_tuple):
#     sum = 0
#     prod = 1
#     for i in input_tuple:
#         sum+=i
#         prod*=i
#     return sum, prod
# print(sum_product(input_tuple))

# elementwise sum
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# tuple_list = []
# def tuple_elementwise_sum(tuple1, tuple2):
#     if len(tuple1) == len(tuple2):
#         for i in range(len(tuple1)):
#             tuple_list.append(tuple1[i]+tuple2[i])
#         return tuple(tuple_list)
#     else:
#         return 'length of tuples are not same'

# print(tuple_elementwise_sum(tuple1, tuple2))

# insert at the begining
# input_tuple = (2, 3, 4)
# value_to_insert = 1
# def insert_value_front(input_tuple, value_to_insert):
#     tuple_list = [value_to_insert]
#     for i in range(len(input_tuple)):
#         tuple_list.append(input_tuple[i])

#     return tuple(tuple_list)
# print(insert_value_front(input_tuple, value_to_insert))

# concatenate 
# input_tuple = ('Hello', 'World', 'from', 'Python')
# def concatenate_strings(input_tuple):
#     tuple_list = []
    
#     for i in range(len(input_tuple)):
#         tuple_list.append(input_tuple[i])
#     return ' '.join(tuple_list)
# print(concatenate_strings(input_tuple))

# diagonal elements
# input_tuple = (
#     (1, 2, 3),
#     (4, 5, 6),
#     (7, 8, 9)
# )
# def get_diagonal(tup):
#     tuple_list = []
#     for i in range(len(tup)):
#         for j in range(len(tup)):
#             if i == j:
#                 tuple_list.append(tup[i][j])
#     return tuple(tuple_list)                    #  return tuple(input_tuple[i][i] for i in range(len(input_tuple)))

# print(get_diagonal(input_tuple))


# common elements
# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = (4, 5, 6, 7, 8)
# def common_elements(tuple1, tuple2):
#     tuple_list = []
#     for i in tuple1:
#         if i in tuple2:
#             tuple_list.append(i)
#     return tuple(tuple_list)
# print(common_elements(tuple1, tuple2))      

# another way
"""return tuple(set(tuple1) & set(tuple2))
Convert both input tuples into sets using the set() constructor, 
then use the set intersection operator & to find the common elements 
between the two sets. Convert the resulting set of common elements back
 to a tuple and return it.
"""


    