
def calculate (r, unit, arr, n):
    if n == 0:
        return -1 
        
    totalFoodRequired = r * unit 
    foodTillNow = 0 
    house = 0 
        
    for house in range (n):
        foodTillNow += arr[house] 
        if foodTillNow>=totalFoodRequired:
            break 
    if totalFoodRequired > foodTillNow:
        return 0
    return house + 1
	  
r = int (input ())
unit = int (input ())
n = int (input ())
  
arr = list (map (int, input ().split ()))
print (calculate (r, unit, arr, n))
# -------------------------------------------
# def OperationsBinaryString(s):
#     a=int(s[0])
#     i=1
#     while i<len(s):
#         if s[i]=="A":
#             a=a&int(s[i+1])
#         elif s[i]=="B":
#             a=a|int(s[i+1])
#         else:
#             a=a^int(s[i+1])
#         i+=2
#     return a
# s=input()
# print(OperationsBinaryString(s))
# --------------------------------------------
# def checkpassword(s,n):
#     if n<4:
#         return 0
#     if s[0].isdigit():
#         return 0
#     num=0
#     cap=0
#     for i in range(n):
#         if s[i]==" " or s[i]=="/":
#             return 0
#         if s[i]>="A" and s[i]<="Z":
#             cap+=1
#         if s[i].isdigit():
#             num+=1
#     if cap>0 and num>0:
#         return 1
#     else:
#         return 0
# s=input()
# n=len(s)
# print(checkpassword(s,n))
# -----------------------------------------
# n=int(input())
# m=int(input())
# sum1=0
# sum2=0
# for i in range(1,m+1):
#     if i%n==0:
#         sum1+=i
#     else:
#         sum2+=i
# print(abs(sum2-sum1))
# ------------------------------------------
# n=int(input())
# m=int(input())
# sum1=0
# sum2=0
# for i in range(1,m+1):
#     if i%n!=0:
#         sum1+=i
#     else:
#         sum2+=i
# print(abs(sum2-sum1))
# -------------------------------------
# length = int(input())
# arr = list(map(int, input().split()))
# even_arr = []
# odd_arr = []
# for i in range(length):
#     if i % 2 == 0:
#         even_arr.append(arr[i])
#     else:
#         odd_arr.append(arr[i])
# even_arr = sorted(even_arr)
# odd_arr = sorted(odd_arr)
# print(even_arr[len(even_arr)-2] + odd_arr[len(odd_arr)-2])
# -----------------------------------------
# n=int(input())
# sum1=int(input())
# arr=list(map(int,input().split()))
# if n<2:
#     print("-1")
# arr.sort()
# # arr= sorted(arr)
# for i in range (n-1):
#     if arr[i]+arr[i+1]<sum1:
#         print(arr[i]*arr[i+1])
#         break
# else :
#     print("0")
# ---------------------------------------
# first_number = int(input())
# second_number = int(input())
# for i in range(first_number, second_number+1):
#     reverse = 0
# temp = i
# while temp != 0:
#     remainder = temp % 10
# reverse = (reverse * 10)+remainder
# temp = temp // 10
# if i == reverse:
#     print(reverse, end=" ")
# -------------------------------------------
# import math
# x1 ,y1=1,1
# x2 ,y2=2,4
# x3 ,y3=3,6
# first_diff=math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))
# second_diff=math.sqrt(math.pow(x3-x2,2)+math.pow(y3-y2 ,2))
# third_diff=math.sqrt(math.pow(x3-x1,2)+math.pow(y3-y1,2))
# print(round(first_diff,2),round(second_diff,2),round(third_diff,2))
# ---------------------------------------
# table_num=int(input())
# sum=0
# for i in range (1,11):
#     value=table_num*i
#     print(value,end =" ")
#     sum=sum+value
# print()
# print(sum)
# --------------------------------------------
# array = []
# evenArr = []
# oddArr = []
# n = int(input("Enter the size of the array:"))
# for i in range(0,n):
#     number = int(input("Enter Element at {} index:".format(i)))
#     array.append(number)
#     if i % 2 == 0:
#         evenArr.append(array[i])
#     else:
#         oddArr.append(array[i])
# evenArr = sorted(evenArr)
# print("Sorted Even Array:", evenArr[0:len(evenArr)])
# oddArr = sorted(oddArr)
# print("Sorted Odd Array:", oddArr[0:len(oddArr)])
# print(evenArr[1] + oddArr[1])
# evenArr = sorted(evenArr)
# print("Sorted Even Array:", evenArr[0:len(evenArr)])
# oddArr = sorted(oddArr)
# print("Sorted Odd Array:", oddArr[0:len(oddArr)])
# print(evenArr[1] + oddArr[1])
# -------------------------------------------
# def caluclate(m,n):
#     sum=0
#     for i in range(m,n+1):
#         if (i % 3==0) and (i%5==0):
#             sum=sum+i
#     return sum
# m=int(input())
# n=int(input())
# result=caluclate(m,n)
# print(result)
# ----------------------------------------------
# def countExponents(i):
#     count = 0
#     while i%2 == 0 and i != 0:
#         count+=1
#         i = i//2
#     return count
# def maxExponents(a, b):
#     maximum, number = 0, a
#     for i in range(a,b):
#         temp = countExponents(i)
#         if temp>maximum:
#             maximum, number = temp, i
#     return number
# a, b = map(int,input().split())
# print(maxExponents(a, b))
# -------------------------------------------
# def operationChoices(c,a,b):
#     if c == 1 :
#         return(a+b)
#     elif c == 2:
#         return(a-b)
#     elif c == 3:
#         return(a*b)
#     else:
#         return(a//b)
# c,a,b = map(int,input().split())
# print(operationChoices(c, a, b))
# -------------------------------------------
# user=input()
# count=0
# final=""
# for i in user:
#     if i=="-":
#         count+=1
#     else:
#         final+=i
# print("-"*count,final)