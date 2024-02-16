## 1.
# def middle(lst):
#     if len(lst)<=2:
#         print(lst)
#     else:
#         newList = lst[1:len(lst)-1]
#         print(newList)
# myList = [3]
# middle(myList)
# # 2.
# def sumDiagonal(a):
#     sum = 0
#     for i in range(len(a)):
#         for j in range(len(a[0])):
#             if i == j :
#                 sum += a[i][j]
#     return sum
# myList = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]]
# print(sumDiagonal(myList))
# # 3. 
# def firstSecond(given_list):
     
#     a = given_list   #make a copy
 
#     a.sort(reverse=True)
 
#     print(a)
 
#     first = a[0]
 
#     second = None
 
#     for element in given_list:
 
#         if element != first:
 
#             second = element
 
#             return first, second
# myList = [1,2,4,6,8,34,5,2,3,22,3,54,34]
# print(firstSecond(myList))
# # 4. 
# def removeDuplicates(myList):
#     new_list=[]
 
#     for i in myList:
 
#         if i not in new_list:
 
#             new_list.append(i)
 
#     return new_list
# 5. 
def pairSum(myList, sum):
    result = []
    for i in range(len(myList)):
        for j in range(i+1,len(myList)):
            if myList[i] + myList[j] == sum:
                result.append(str(myList[i]) +"+"+ str(myList[j]))
    return result