# a=int(input('enter the first digit'))
# b=int(input('enter the second digit'))
# print('the sum of two numbers is',a+b)
# --------------------------------------
# num1=10
# num2=3
# sum=num1+num2
# print('the sum of',num1,'and',num2, 'is',sum)
# ---------------------------------------
# def sum(a,b,c):
#     return a+b+c
# total_sum =sum(10,20,30)
# print(total_sum)
# ----------------------------------------
# def add(*args):
#     return sum(args)

# result=add(3,2,3,5,10) 
# print(result)
# -----------------------------------------
# n=int(input('enter a number:'))
# if n%2==0:
#     print('n is even ')
# else:
#     print('number is odd')
# ----------------------------------------
# n=int(input('enter a number:'))
# if n==0:
#     print('num is zero')
# elif n>0:
#     print('num is positive')
# else:
#     print('num is negative')
# --------------------------------------------
# def check_character():
#     if char.isalpha():
#         print(char ,'is an alphabet')
#     elif char.isdigit():
#         print(char, 'is an digit')
#     else:
#         print(char, 'is an special character')
# char=input('enter ur character')
# check_character()
# -----------------------------------------------
# def check_triangle(a,b,c):
#     if a==b==c:
#         print('the traiangle is equilateral')
#     elif a==b or b==c or c==a:
#         print('the triangle is isosceles')
#     else:
#         print('the traingle is scalene')
# s1=float(input('enter the length of first side'))
# s2=float(input('enter the length of second side'))
# s3=float(input('enter the length of third side'))
# check_triangle(s1,s2,s3)
# -----------------------------------------------
# n=int(input())
# if n%5==0 and n%11==0:
#     print('num is divisble by both 5 and 11')
# else:
#     print('num is not divisble by 5 and 11')
# # -----------------------------------------------
# def check_case(char):
#     if char.isupper():
#          print(char,'is an uppercase alphabet') 
#     elif char.islower():
#         print(char,'is an lowercase alphabet') 
#     else:
#         print(char,'is not an alphabet')
# char=input('enter any character')
# check_case(char)
# -----------------------------------------------
# def area_of_rectangle(length,breadth):
#     return length*breadth
# def area_of_triangle(base,height):
#     return 0.5*base*height

# length=float(input('enter length of the rectangle'))
# breadth=float(input('enter breadth of the rectangle'))
# rectangle_area=area_of_rectangle(length,breadth)
# print(rectangle_area)

# base=float(input('enter the base of the triangle'))
# height=float(input('enter the height of the triangle'))
# triangle_area=area_of_triangle(base,height)
# print(triangle_area)
# ---------------------------------------------------
# import cmath
# def find_roots(a,b,c):
#     discriminant=b**2-4*a*c
#     root1=(-b+cmath.sqrt(discriminant))/(2*a)
#     root2=(-b-cmath.sqrt(discriminant))/(2*a)
#     return root1,root2
# a=float(input('enter the coeffecient a:'))
# b=float(input('enter the coeffecient b:'))
# c=float(input('enter the coeffecient c:'))
# root1,root2=find_roots(a,b,c)
# print('the roots of quadratric equations are:')
# print('root1:',root1)
# print('root2:',root2)

# -------------------------------------------------

# def check_vowel_consonant(char):
#     vowels='aeiouAEIOU'
#     if char.isalpha(): 
#         if char in vowels:
#             return f'{char} is a vowel'
#         else:
#             return f'{char} is a consonant'
#     else:
#         return 'please enter an alphabet'
# alphabet=input('enter an alphabet":')
# result=check_vowel_consonant(alphabet)
# print(result)
# --------------------------------------------------
# def  check_tiangle(a,b,c):
#     if (a+b>c) and (a+c>b) and (b+c>a):
#         return True
#     else:
#         return False
# a=float(input('enter the length of the first side:'))
# b=float(input('enter the length of the second side:'))
# c=float(input('enter the length of the third side:'))

# if True:
#   print('triangle is valid')
# else:
#   print('triangle is not valid')
# result= check_tiangle(a,b,c)
# print(result)

# -------------------------------------------------
# def find_greatest(a,b,c):
#     if a>b and a>c:
#         return a 
#     elif b>a and b>c:
#         return b 
#     else:
#         return c 
# num1=float(input('enter a'))
# num2=float(input('enter b'))
# num3=float(input('enter c'))
# result=find_greatest(num1,num2,num3)
# print(f' the greatest number is: {result}')
# ---------------------------------------------------
# def factorial(n):
#     if n<0:
#         return 'factorial is not defined for negative '
#     elif n==0 or n==1:
#         return 1
#     else:
#         factorial=1
#         for i in range (2,n+1):
#             # factorial*=i
#             factorial=factorial*i
#         return factorial
# number=int(input('enter a number:'))
# print('factorial of', number , 'is', factorial(number)) 

# ---------------------------------------------------
# def check_leapyear(year):
#     if (year%4==0 and year%100!=0) or (year%400==0):
#         return True 
#     else:
#         return False
        
# year=int(input('enter the year'))
# if check_leapyear(year):
#     print(f'{year} is a leap year')
# else:
#      print(f'{year} is not a leap year')
# ---------------------------------------------------
# a=int(input('enter the first number'))
# b=int(input('enter the second number'))
# temp=a
# a=b
# b=temp
# print(a)
# print(b)

# a,b=b,a
# print(a)    
# print(b)

# a=a+b          
# b=a-b           
# a=a-b          
# print(a)
# print(b)
# --------------------------------------------------
# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range (2,n):
#         if n%i==0:
#             return False
#     return True
# num=int(input('enter anumber:'))
# if  is_prime(num):
#     print(f'{num} is a prime number')
# else:
#     print(f'{num} is not a prime number')
# ----------------------------------------------
# def gcd(a,b):
#     while b!=0:
#         a,b=b,a%b
#     return a
# num1=int(input('enter the first number'))
# num2=int(input('enter the second number'))
# result=gcd(num1,num2)
# print(f'the gcd of {num1} and {num2} is {result}')
# -------------------------------------------------
# def reverse_number(num):
#     number=str(num)
#     reversed_str=number[::-1]
#     reversed_str=int(reversed_str)
#     return reversed_str
# input=int(input('enter a number:'))
# result=reverse_number(input)
# print(f'the reversed number is {result}')

# ---------------------------------------------------
# def reverse(s):
#     str=''
#     for i in s:
#        str=i+str
#     return str
# s='geeks for geeks'
# print('the original string is ')
# print(s)
# print('the reversed string is ')
# print(reverse(s))

# def reverse_string(s):
#     string=''
#     for i in s:
#         string=i+string
#     return string
# s='monika'
# result=reverse_string(s)
# print('the reversed string is ', result)
# # ----------------------------------------------------
# def is_palindrome(number):
#     num_str = str(number)
#     return num_str == num_str[::-1]
# num = int(input("Enter a number: "))
# if is_palindrome(num):
#     print(f"{num} is a palindrome.")     
# else:
#     print(f"{num} is not a palindrome.")
# ----------------------------------------------------
# def Fibonacci(n):
#     if(n==0):
#         return 0
#     elif(n==1):
#         return 1
#     else :
#         return Fibonacci(n-1)+Fibonacci(n-2)
# number=int(input('enter the number'))
# print(Fibonacci(number))
# --------------------------------------------------
# def sum_of_digits(number):
#     num_str=str(abs(number))
#     total=0
#     for digit in num_str:
#         total+=int(digit)
#     return total
# num=int(input('enter a number:'))
# result=sum_of_digits(num)
# print('the sum of the digits of',num,'is:',result)

# def sum_of_digits(n):
#     number=str(abs(n))
#     total=0
#     for digit in number:
#         total+=int(digit)
#     return total
# input=int(input('enter the number:'))
# result=sum_of_digits(input)
# print(f'the sum of the given number is {result}')
# -----------------------------------------------
# def is_perfect(number):
#     if number<=0:
#         return False
#     sum_of_divisors=0
#     for i in range(1,number):
#         if number%i==0:
#             sum_of_divisors+=i
#     return sum_of_divisors==number
# num=int(input('enter a number:'))
# if is_perfect(num):
#     print(f'{num} is a perfect number')
# else:
#     print(f'{num} is not a perfect number')
#---------------------------------------------------

# lis ={2:54,6:54,9:56,4:56,5:67,6:78,7:89,8:90}
# e=list(sorted(r.keys()))
# e={}
# for i in e:
#     if i not in e:
#         e[i]=r[i]
# print(e)

# dict1= {2: 31, 3: 26, 4:1}
# result = {}
# for key, value in dict1.items():
#     if value % key == 0:
#         result[key] = value
# print(result)

# w ={
#     'A': {'Gokul' :32 , 'Harsh' : 89},
#     'B': {'Ravi' :25 , 'Varun' : 76},
#     'C': {'Rupa' :31 , 'Shreya' : 56}
# }

# count = 0
# for key in w.items():
#     count +=1
# print(count)


# count=0
# for key, value in w.items():
#     for name,score in value.items():
#         if score > 60:
#             count+=1
# print(count)
    
# count=0
# for key, value in w.items():
#     for name, score in value.items():
#             if score %2== 0:
#                 count += 1
# print(count)

# import math 
# def area_of_sector(angle,radius):
#     return (angle/360) * math.pi * radius**2

# minute_angle=21*6
# hour_angle=21*0.5

# radius_min=4
# radius_hour=4

# area_minute=area_of_sector(minute_angle,radius_min)
# area_hour=area_of_sector(hour_angle,radius_hour)

# total_area=area_minute + area_hour
# print(f'{total_area:.2f}')

# students = {
#     'Alice':{'Math':90, 'Science':85,'Geography':72,'history':88},
#     'Bob':{'Math':80, 'Science':95,'Geography':78,'history':82},
#     'Charlie':{'Math':85, 'Science':90,'Geography':88,'history':80},
# }

# sub=['Math']
# averages = {}
# for name, subjects in students.items():
#         if all()
#         print(['marks'],[marks[0]])
        
#     totalMarks = sum(subjects.values())
#     avg= totalMarks / len(subjects)
#     averages[name] = avg
# print(averages)

# def is_prime(j):
#     if j < 2:
#         return False
#     for i in range(2, int(j**0.5) + 1):
#         if j % i == 0:
#             return False
#     return True 
# creators = 15
# day = 10
# count = 0
# total_reels = creators * day
# for i in range(total_reels):
#     if is_prime(i):
#         count += 1
# print(count)

# time=10
# for i in count:
#     i * (10/100)
# -----------------------------------------
# s=str(input())
# freq_dict={}
# for i in s:
#     if i in freq_dict:
#         freq_dict[i]+=1
#     else:
#         freq_dict[i]=1
# print(freq_dict)

# -------------------------------------------n
# n,m=map(int,input().split())
# sum_divisible=0
# sum_not_divisible=0
# for i in range (1,m+1):
#     if i% n ==0:
#         sum_divisible += i
#     else:
#         sum_not_divisible += i
# print(sum_divisible-sum_not_divisible)
# ----------------------------------------------
# c,a,b=map(int,input().split())
# if c==1:
#     print(a+b)
# elif c==2:
#     print(a-b)
# elif c==3:
#     print(a*b)
# elif c==4:
#     print(a/b)
# --------------------------------------------
# vowels_count = 0
# consonant_count=0
# vowels='aeiou'
# s=str(input())
# for i in s:
#     if i in vowels:
#         vowels_count += 1
#     else:
#         consonant_count += 1
# print(f'({vowels_count}, {consonant_count})')
# ----------------------------------------------------
# s=str(input())
# result=''
# seen=set()
# for i in s:
#     if i not in  seen:
#         seen.add(i)
#         result += i 
# print(result)
# -----------------------------------------------------
# s=str(input())
# if s == s[::-1]:
#     print('True')
# else:
#     print('False')
#     ------------------------------------------------------
# s=str(input())
# words= s.split(' ')
# words.reverse()
# reversed_string=' '.join(words)
# print(reversed_string)
# ----------------------------------
# password = input()
# char_count = 0
# upper_count = 0
# digit_count = 0
# space_count = 0
# slash_count = 0
# for char in password:
#     if char.isalpha():
#         char_count += 1
#         if char.isupper():
#             upper_count += 1
#     elif char.isdigit():
#         digit_count += 1
#     elif char.isspace():
#         space_count += 1
#     elif char == '/':
#         slash_count += 1  
# is_digit = False
# if password[0].isdigit():
#     is_digit = True
# if (char_count >= 4 and upper_count >= 1 and digit_count >= 1 and space_count == 0 and slash_count == 0 and not is_digit):
#     print(1)
# else:
#     print(0)
# ----------------------------------------------------------------------
# seen=set()
# dic={}
# for key,value in d.items():
#     if value not in seen:
#         dic[key] = value
#         seen.add(value)
# # print(dic)

# list1 = eval(input())
# list2 = eval(input())
# merged_list = list1 + list2
# print(merged_list)
# -------------------------------------------------------
# numbers = eval(input())
# if not numbers :
#    print(0,0)
# else:
#    total_sum = sum(numbers)
#    average = total_sum / len(numbers)
#    print(f'({total_sum}, {average})')
# -------------------------------------------------------
# input=eval(input())
# even_numbers=[]
# odd_numbers=[]
# for i in input:
#     if i % 2==0:
#         even_numbers.append(i)
#     else:
#         odd_numbers.append(i)
# print(even_numbers, odd_numbers)
# ---------------------------------------------------------
# def most_frequent_character(s):
#     frequency = {}
#     for char in s:
#         if char in frequency:
#             frequency[char] += 1
#         else:
#             frequency[char] = 1
#     max_freq = max(frequency.values())
#     most_frequent_chars = [char for char, freq in frequency.items() if freq == max_freq]
#     return most_frequent_chars

# def evaluate_sequence(s):
#     operators = {'A':'&','B':'|','C':'^'}
#     result = int(s[0])
#     for i in range(1,len(s),2):
#         result = eval(f'{result} {operators[s[i]]} {s[i+1]}')
#     return result 
# s = input()
# print(evaluate_sequence(s))

# nums = list(map(int,input().split()))
# res = 0
# for num in nums:
#     res ^= num 
# print(res)

# def longest_word(sentence):
#     words = sentence.split()
#     if not words:
#         return ""
#     return max(words, key=len)

# sentence = input("Enter a sentence: ")
# print("Longest word:", longest_word(sentence))

# def replace_spaces(sentence, ch):
#     return sentence.replace(' ', ch)
# inputs = input('').rsplit(' ', 1)
# sentence, ch = inputs[0], inputs[1]
# print(replace_spaces(sentence, ch))

# def capitalize_words(sentence):
#     return ' '.join(word.capitalize() for word in sentence.split())
# s = input("Enter a sentence: ")
# print(capitalize_words(s))

# input=eval(input())
# input.sort(reverse=True)
# print(input[1])


#  intersection of two lists
# a,b = input().split('] [')
# a = a.strip('[]') 
# b = b.strip('[]')
# list_1 = list(map(int,a.split(',')))
# list_2 = list(map(int,b.split(',')))
# intersection = set(list_1) & set(list_2)
# print(list(intersection)) 

# input = input()
# nstring,tstring=input.split("]") 
# nums= eval(nstring + ']') 
# target = int(tstring.strip())

# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] + nums[j] == target:
#             print(f'[({i} , {j})]')         # [2, 7, 11, 15]
#                                             # target = 9)
                                              # Output: [(0, 1)

# s=input()
# freq_dict={}
# for char in s:
#     if char in freq_dict:
#         freq_dict[char]+=1
#     else:
#         freq_dict[char]=1
# print(freq_dict)




# for i in range(1,a+1):
#     print(" "*(a-1),end="") 
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# import math
# s = str(input())
# for index, char in enumerate (s):
#     if char in "aeiou":
#         if index %2==0:
#             print(math.factorial(index))
#         else:
#             print(index**3)


