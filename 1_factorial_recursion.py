# 1. FACTORIAL NUMBER
# import sys
# sys.setrecursionlimit(10000)        # to increase system stack memory
# def factorial(n):
#     assert n >= 0 and int(n) == n, 'the number must be a positive integer'  # if not then assert will throw the given exception
#     if n in [0,1]:
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(1.9))

# 2. FIBONACCI SEQUENCE
# def fibonacci(n):
#     assert int(n) == n and n >= 0 , 'only positive integers are allowed'
#     if n in [0,1]:
#         return n
#     else:
#         fibo = fibonacci(n-1) + fibonacci(n-2)
#         return fibo 
# print(fibonacci(1.9))

# with open("C:\\Users\\nitro\Documents\\krunal.txt",'r') as file:
#     a=file.read()
#     for i in a :
#         if i.isnumeric():
#             print(i)
        
# 3. FIND MAX NUMBER
# samplearray = [11,4,12,7]
# def findmax(samplearray, n):
#     if n == 1:
#         return samplearray[0]
#     return max(samplearray[n-1], findmax(samplearray, n-1))
# print(findmax(samplearray, 4))

# 4. FIND SUM OF DIGITS OF A POSITIVE NUMBER USING RECURSION
# def findsum(digit):
#     assert int(digit) == digit and digit >= 0 , 'only positive integers are allowed'
#     if digit == 0 or digit == 0:      # in most of the case digit(remainder) is going to be 0
#         return 0
#     return int(digit%10) + findsum(int(digit/10))

# print(findsum(123))

# 5. CALCULATE POWER USING RECURSIVE FUNCTION
# def power(num, n):
#     assert int(n) == n,  'exponent must be integer only'
#     if n == 0:
#         return 1
#     elif n < 0:
#         return 1/num *power(num, n+1)
#     return num*power(num, n-1)      # recursive case : x^n = x * X^(n-1)
 
# print(power(2,-4))

# 6. GREATEST COMMON DIVISOR (USING EUCLIDEAN RULE)
# def gcd(num1, num2):
#     assert int(num1) == num1 and int(num2) == num2, 'the numbers must be integer only'
#     # gcd of negative numbers is same as positive number
#     if num1 < 0:
#         num1 = -1*num1
#     if num2 < 0 :
#         num2 = -1*num2
#     if num2 ==0 :
#         return num1
#     return gcd(num2, num1%num2)

# print(gcd(48,1.8))

# 7. DECIMAL TO BINARY
# def decimalToBinary(num):
#     remainder = 0
#     quotient = 0
#     string = ' '
#     while num: 
#         quotient = num // 2
#         remainder = num % 2
        
#         num = quotient
#         string += str(remainder)
#     return string[::-1]      # reversing using slicing
# print(decimalToBinary(13))
# def decimalToBinary(num):
#     assert int(num) == num, 'only integers'
#     if num == 0:
#         return 0
#     else:
#         return num%2 + 10*decimalToBinary(int(num/2))

# print(decimalToBinary(-1.3))

# 8. PRODUCT OF ARRAY
# def productOfArray(arr):
#     length = len(arr)
#     if length == 1:
#         return arr[0]
#     return arr[length-1]*productOfArray(arr[:length-1])
# print(productOfArray([1,2,3,4]))  

# 9. RECURSIVE RANGE
# def recursiveRange(num):
#     if num == 0:
#         return 0
#     return num + recursiveRange(num-1)

# print(recursiveRange(3))

# 10. REVERSE
# def reverse(strng):
#     length = len(strng)
#     if length == 1:
#         return strng[0]
#     return strng[length-1] + reverse(strng[:length-1])
# print(reverse('python'))

# 11. PALINDROME
# def isPalindrome(strng):
#     length = len(strng)
#     reversedString = ''
#     if length == 1:
#         reversedString += strng[0]
#     else:
#         reversedString += (strng[length-1] + isPalindrome(strng[:length-1]))

#     if strng == reversedString:
#         return True
#     else:
#         return False
    
# print(isPalindrome('abc'))  
# def isPalindrome(strng):
#     reversedstring = strng[::-1]
#     if strng == reversedstring:
#         return True
#     else:
#         return False
     
# print(isPalindrome('abc'))

# 12. CALLBACK

# arr = [2,4,8]   
# def isOdd(num):
#     if num%2==0:
#         return False
#     else:
#         return True   
# def someRecursive(arr, isodd):
#     length = len(arr)
#     if length == 0:
#          return False
#     if isodd(arr[length-1]):
#             return True
#     return someRecursive(arr[:length-1], isodd)

# print(someRecursive(arr, isOdd))

# 13. FLATTEN

# arr = [1, 2, 3, [4, 5]]
# def flatten(arr):
#     list1 = []
#     for item in arr:
#         if item.__class__ == list:
#             list1.extend(flatten(item))
#         else:
#             list1.append(item)
#     return list1
# print(flatten(arr))
# def flatten(arr):
#     list1 = []
#     for i in arr:
#         if i.__class__ == list:
#             for j in i :
#                 list1.append(j)
#         else:
#             list1.append(i)
#     return list1
# print(flatten(arr))

# 14. CAPITALISE FIRST WORD

# arr = ['car', 'taco', 'banana']
# def capitaliseFirst(arr):
#     list1 = []
#     # for item in arr:
#     #     list1.append(item.capitalize())
#     # return list1
#     if len(arr) == 0:
#         return list1   
#     list1.append(arr[0][0].upper() + arr[0][1:])
#     return list1 + capitaliseFirst(arr[1:])


# print(capitaliseFirst(arr))

# 15. NESTED SUM

# obj2 = {
#   "a": 2,
#   "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
#   "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
#   "d": 1,
#   "e": {"e": {"e": 2}, "ee": 'car'}
# }
# def nestedEvenSum(obj,sum=0):
#     for value in obj.values():
#         if value.__class__ == dict:
#             sum+=nestedEvenSum(value)
#         else:
#             if value.__class__ == int and value%2 == 0:
#                 sum += value
#     return sum


# def nestedEvenSum(obj, sum=0):
#     for key in obj:
#         if type(obj[key]) is dict:
#             sum += nestedEvenSum(obj[key])
#         else:
#             if type(obj[key]) is int and obj[key]%2==0:
#                 sum+=obj[key]
#     return sum
# print(nestedEvenSum(obj2))

# 16. CAPITALISE ALL WORDS
# words = ['i', 'am', 'learning', 'recursion']
# def capitalizeWords(arr):
#     list1 = []
#     length = len(arr)
#     if length == 0 :
#         return list1
#     list1.append(arr[0].upper()) 
#     return list1 + capitalizeWords(arr[1:])
# print(capitalizeWords(words))

# 17. STRINGIFY NUMBERS
# obj = {
#   "num": 1,
#   "test": [],
#   "data": {
#     "val": 4,
#     "info": {
#       "isRight": True,
#       "random": 66
#     }
#   }
# }
# def stringifyNumbers(obj):
#     for key in obj:
#         if type(obj[key]) is int:
#             obj[key] = str(obj[key])
#         elif type(obj[key]) is dict:
#             stringifyNumbers(obj[key])
#     return obj
# print(stringifyNumbers(obj))

# 18. COLLECTING STRINGS
obj = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}
def collectString(obj):
    list1 = []
    for key in obj:
        if type(obj[key]) is str:
            list1.append(obj[key])
        elif type(obj[key]) is dict:
            return list1 + collectString(obj[key])
    return list1
print(collectString(obj))