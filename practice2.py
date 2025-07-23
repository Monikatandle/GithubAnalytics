# km=float(input('enter the kilometers to be converted:'))
# conversion_factor=0.621371
# miles=km*conversion_factor
# print(km , 'kilometers is equal to' , miles , 'miles')
# import calendar
# year=int(input('enter the year: '))
# month=int(input('enter the month: '))
# calen=calendar.month(year,month)
# print(calen)

# number=int(input('enter the number: '))
# flag=False
# if number==1:
#     print('not a prime number')
# elif number>1:
#     for i in range(2,number):
#         if number%i==0:
#             flag = True
#             break
# if flag:
#     print(f'{number} is not a prime number')
# else:
#     print(f'{number} is a prime number')

# lower=1
# upper=10
# print('prime numbers between', lower, 'and' , upper, 'are:' )
# for num in range(lower,upper+1):
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             print(num)
# num=int(input('enter the number:'))
# factorial=1
# if num<0:
#     print('factorial does not exist for negative numbers')
# elif num==0:
#     print('factorial of 0  is 1')
# else:
#     for i in range(1,num+1):    
#         factorial=factorial*i    
#     print(f'factrial of', num , 'is', factorial)
# limit=int(input('enter the limit: '))
# number=0
# for i in range(1,limit+1):
#     number+=i
# print(number)

# nums = [1,2,4,5]
# target = 9
# length = len(nums)
# result = ""
# for i in range(length):
#     for j in range(1,length+1):
#         if i+j == target:
#             result = nums.index(i)
# print(result)            

# def two_sum(numbers,t):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j]==target:
#                 return[i,j]
# nums=input().split()

# target=3
# print(two_sum(nums,target))

# class computer:
#     def __init__(self,cpu,ram):
#         self.cpu=cpu
#         self.ram=ram
#     def config(self):
#         print('the configaration is' , self.cpu, self.ram)

# com1=computer('i5 ' , '62')
# com2=computer('razon ' , '42')

# com1.config()

# com2.config()


# class car:
#     wheels = 4
#     def __init__(self):
#         self.company='bmw'
#         self.miles=24

# car1=car()
# car2=car()

# car1.miles=54
# car1.company='lamborgini'

# print(car1.company , car1.miles , car1.wheels)
# print(car2.company , car2.miles , car2.wheels)

# class student:
#     school='telusko'
#     def __init__(self, m1,m2,m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
#     def average(self):
#         return (self.m1+self.m2+self.m3)/3

# s1=student(23,45,66)
# s2=student(65,86,43)
# print(s1.average())
# print(s2.average())



# print(s1.m1,s1.m2,s1.m3)
# print(s2.m1,s2.m2,s2.m3)

# binary_num="101"
# decimal=int(binary_num,2)
# print(decimal)
# def remove_adjacent_chars(s):
#     stack=[]
#     for char in s:  
#         if stack and stack[-1]==char:
#             stack.pop()
#         else:
#             stack.append(char)
#     return "".join(stack)   

# s="bbmmalc"
# result=remove_adjacent_chars(s)
# print(result)
    
# import math
# def lcm(a,b):
#     return abs(a*b)//math.gcd(a,b)

# num1=12
# num2=18
# result=lcm(num1,num2)
# print(result)


# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)

# result=factorial(5)
# print(result)

# def is_prime(n):
#     if num<=1:
#         return False
#     for i in range(2,num):
#         if num % i==0:
#             return False
#     return True
# num=11
# if is_prime(num):
#     print(f"{num} is a prime number")
# else:
#       print(f"{num} is not a  prime number")'

# def string_length(s):
#     if s=="":
#         return 0
#     return 1+string_length(s[1:])

# s="harry"
# print("length of string is :" , string_length(s))

# def find_smallest(arr,n):
#     if n==1:
#         return arr[0]
#     return min(arr[n-1],find_smallest(arr,n-1))

# arr=[3]
# print("smallest element in a array is:",find_smallest(arr,len(arr)))
    
# def largest_smallest(arr,n):
#     if n==1:
#         return arr[0],arr[0]
#     small,large=largest_smallest(arr,n-1)
#     return min(arr[n-1],small),max(arr[n-1],large)

# arr=[4,2,7,1,9,3]
# smallest,largest=largest_smallest(arr,len(arr))
# print("the smallest elent in the array is:",smallest)
# # print("the largest elent in the array is:",largest)

# arr=[1,2,3,4,5]
# sum=arr[::-1]
# print(sum)
# arr=[7,2,9,4,6,8,1,5,3,10]
# mid= len(arr)//2
# first_half=sorted(arr[:mid])
# second_half=sorted(arr[mid:], reverse=True)
# result=first_half+second_half
# print(result)
# arr=[1,2,3,2,1,4,2,3,5,1,6,4,4]
# empty_dict={}
# for num in arr:
#     if num not in empty_dict:
#         empty_dict[num]=1
#     else:
#         empty_dict[num]+=1
# print(empty_dict)

# def is_palindrome(n):
#     return str(n)==str(n)[::-1]

# arr=[121,232,1331,4554,12321,789987,5649]
# palindrome=[num for num in arr if str(num)==str(num)[::-1]]
# longest_paalindrome=max(palindrome)if palindrome else None
# print(longest_paalindrome)

# arr=[1,3,2,4,2,5,6,8,2,4,6,5,2]
# count=len(set(arr))
# print(count)

# arr=[1,3,2,4,2,5,6,8,2,4,6,5,2]
# empty_list=[]
# for num in arr:
#     if num not in empty_list:
#         empty_list.append(num)

# count=len(empty_list)
# print(count)

# arr=[1,3,2,4,2,5,6,8,2,4,6,5,2]
# seen=set()
# duplicates=set()
# for num in arr:
#     if num in seen:
#         duplicates.add(num)
#     else:
#         seen.add(num)
# print(list(duplicates))

# arr=[1,2,3,4,5,6,7,8,9,10]
# even=0
# odd=0
# for num in arr:
#     if num%2==0:
#         even+=1 
#     else:
#         odd+=1
# print(even  , odd)

# s=input("")
# string=s.lower()
# vowels=('a','e','i','o','u')
# if string in vowels:
#     print(f"{string} is a vowel")
# else:
#     print(f"{string} is a consonant")

# arr=[2,2,0,0,2,1,2,1,0,0]
# count_0=arr.count(0)
# count_1=arr.count(1)
# count_2=arr.count(2)
# array=[0]*count_0+[1]*count_1+[2]*count_2
# print(array)

# def string_reversal(s):
#     string=""
#     for i in s:
#         string=i+string
#     return string

    

# s=input()
# result=string_reversal(s)
# print(result)

# n=int(input())
# for i in range (n):
#     for j in range(n):
#         print("*",end="")
#     print()
# ---------------------------------------
# def say_hello():
#     print("Hello!")

# def my_decorator(func):
#     def wrapper():
#         print("after")
#         func()
#         print("before")
#     return wrapper

# @my_decorator 
# def say_hello():
#     print("Hello!")
# # say_hello=my_decorator(say_hello)
# say_hello()
# ---------------------------------------------
# import time

# def task1():
#     print("Task 1 starting...")
#     time.sleep(3)  # wait for 3 seconds
#     print("Task 1 finished!")

# def task2():
#     print("Task 2 starting...")
#     time.sleep(3)
#     print("Task 2 finished!")

# task1()
# task2()

# class Fruit:
#     def __init__(self,name,color):
#         self.name = name
#         self.color = color
#     def show(self):
#         print("Fruit is ", self.name ,"and color is ", self.color)
# obj1=Fruit("Apple","Red")
# obj1.name="orange"
# obj1.show()

# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" " , end=" ")
#     for j in range(i):
#         print("*" , end=" ")
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

# n = 5 
# for i in range(n-1): 
#    for j in range(i, n): 
#       print(' ', end=' ') 
#    for j in range(i):
#       print('*', end=' ')
#    for j in range(i+1): 
#       print('*', end=' ')
#    print() 
# for i in range(n): 
#    for j in range(i+1): 
#       print(' ', end=' ') 
#    for j in range(i, n-1):
#       print('*', end=' ')
#    for j in range(i, n):
#       print('*', end=' ')
#    print()

# def insertion(nums,target):
#    left,right=0,len(nums)-1
#    while left<=right:
#       mid=(left+right)//2
#       if nums[mid]==target:
#          return mid
#       elif nums[mid]<target:
#          left= mid+1
#       else:
#          right=mid-1
#    return left
# nums=[1,3,5,6]
# target=2
# print(insertion(nums,target))
# ---------------------------------------------------------------

# def caluclate(operation,num1,num2):
#     if operation=="+":
#         return num1+num2
#     elif operation =="*":
#         return num1 *num2
# operation,num1,num2=input().split(",")
# num1=float(num1)
# num2=float(num2)
# print(caluclate(operation,num1 ,num2))

# a,b,c= map(int,input().split())
# if a*a + b*b== c*c or a*a + c*c ==b*b or b*b +c*c==a*a:
#     print("is a pythagorian")
# else:
#     print("not a pythagorian")

# print("Even") if int(input())%2==0 else print("Odd")


# user_input=input()
# if user_input==user_input[::-1]:
#     print("pailndrome")
# else:
#     print("not a palindrome")
# print("palindrome") if user_input==user_input[::-1] else print("not a palindrome")

# string=str(input())
# word=string[len(string)//2:][::-1]
# print(word.replace("y", " ").replace("r", " "))

# r="asdfghj"
# odd=r[1::2]
# print(odd)
# reverse=odd[:-2]+odd[-2:][::-1]
# print(reverse)
# print(r[::2])
# print(reverse+r[::2])

# string=input().lower()
# le=0
# vowels_count=0
# vow='aeiou'
# while(le<len(string)):
#     if string[le] in vow:
#         vowels_count+=1
#     le+=1
# print(vowels_count)

# import math
# vowels="aeiouAEIOU"
# def factorial_of_vowels_indices(s):
#     for i,char in enumerate(s):
#         if char in vowels:
#             print(f'index{i},factorial:{math.factorial(i)}')
# s=input()
# factorial_of_vowels_indices(s)

# def find_hcf(num1,num2):
#     if num1>num2:
#         small = num2
#     else:
#         small = num1
#     hcf=1
#     for i in range (1 , small + 1):
#         if (num1 % i == 0) and (num2 %i == 0):
#             hcf=i
#     return hcf
# num1=int(input())    
# num2=int(input())
# print(find_hcf(num1,num2))

# def print_triangle(n):
#     for i in range(1,n+1):
#         print(" " * (n-i),end="")
#         for j in range (1,i+1):
#             print(j,end=" ")
#         print()
# r=3
# print_triangle(r)

# def print_diamond(n):
#     for i in range(1,n+1):
#         print(" "*(n-i),end="")
#         print("* " *i)
#     for i in range((n-1),0,-1):
#             print(" "*(n-i),end="")
#             print("* " *i)
# r=5
# print_diamond(r)

# n=5
# for i in range(1,n+1):
#         print("  "*(n-i)+" *" * i)

# a=1
# b=4
# c=2
# if(1 & 1):
# c=(a&b)+(a^b)
# if(c):
# c=a
# end if
# print c+a+b 

n=int(input())
print(bin(n))
print(bin(n).count('1'))
print(bin(n).count('0'))




    
    
