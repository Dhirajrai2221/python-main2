# exercise 1 : Print first 10 natural using for and while loop
# sum = 0
# for i in range(1,11,1):
#     sum += i
# print(sum)

# i = 1
# sum = 0
# while i <= 10:
#     sum += i
#     i += 1
# print(f'{sum}')
    
# exercise 2 : calculate sum of all numbers from 1 to given number
# n = int(input("enter a number : "))
# sum = 0
# for i in range(1,n + 1,1):
#     sum += i
# print(sum)

# exercise 3 : WAP to print multiplication table of a given number

# n = int(input("Enter a number : "))
# for i in range(1,11,1):
#     print(f'{n} * {i} = {n * i}')
#     print( str(n) + " * " + str(i) + " = " +  str(n * i))
#     print(n, "*", i, "=", n * i)


# exercise 4 : use else block to display a message "Done" after successful execution of first 5 natural number using for loop

# for i in range(1,6):
#     print(i)
# else:
#     print("Done")

# exercise 5 : Display Fibonacci serise up to 10 terms
# 0 , 1, 1, 2, 3, 5 , 8 ........

# a , b = 0, 1
# print(a)
# print(b)
# for i in range(8):
#     c = a + b
#     print(c)
#     a = b
#     b = c
# range (0,1,2,3,4,5,6,7) = range(8)

# n = int(input("enter nth terms : "))
# a , b = 0, 1
# print(a)
# print(b)
# for i in range(0, n - 2):
#     c = a + b
#     print(c)
#     a = b
#     b = c




#!  Find the factorial of a given number

# n = int(input("enter a number : "))
# fact = 1
# if n < 0:
#     print("factorial does not exist for negative number")
# elif n == 0:
#     print("the factorial of 0 is 1")
# else:
#     for i in range(1,n + 1, 1):
#         fact *= i 
#     print(f'factorial of {n} = {fact}')


# ! exercise 8 : python for loop to sort the numbers in a list in ascending order
# nums = [11,4,1,50,80,32]

# for i in range(0,len(nums)):
#     for j in range(i + 1, len(nums)):
#         if(nums[i] > nums[j]):
#             temp = nums[i]
#             nums[i] = nums[j]
#             nums[j] = temp
# print(nums)


    
# ! exercise 9 : python for loop to find the minimum element in a list
# nums= [21,44,50,10,12]
# min = 100
# for n in nums:
#     if (n < min):
#         min = n
# print(f'Minimum element is {min}')


