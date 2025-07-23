# def check_prime(n):
#     r=2
#     while(r<n):
#         if (n%r==0):
#             return False
#             break
#         r+=1
#     else:
#         if(n==0 or n==1):
#             return False
#         else:
#             return True
        
# def check_odd(n):
#     if (n%2==0):
#         return True
#     else:
#         return False
# e=int(input()[::-1])
# w=0
# while(e!=0):
#     if (check_prime(e%10)):
#         w*=e%10
#     else:
#         if(check_odd(e%10)):
#             w+=e%10
#         else:
#             w-=e%10
#     e=e//10
# print(w)
    
# st = input() #accenture is hiring freshers

# r = list(map(str,input().split(" ")))
# s = ""
# for i in range(len(r)):
#     if(i%2!=0):
#         s+=r[i].upper()+" "
#     else:
#         s+=r[i]+" "
# print(s.strip())

# rats

# r=list(map(str,input().split()))
# total_food= int(r[0])*int(r[1])
# c = list(map(int,r[2][1:-1].split(',')))
# s= 0
# house_count=0
# for i in c:
#     if (total_food <= sum(c)):
#         if (s < total):
#             s+=i
#             house_count+=1
#     else:
#         print("Not  enought food")
#         break
# print(f'Enough food\n{house_count}' if (total_food <= sum(c)) else f"{house_count}")

# w=list(map(int,input().split()))
# total_food_required=int(w[0])*int(w[1])
# total_units_present=w[2:]
# tummy=0
# if (total_food_required < sum(total_units_present)):    
#     indexing=0
#     while(tummy < total_food_required):
#         tummy += total_units_present[indexing]
#         indexing+=1
#     print(indexing)
# else:
#     print(0)    
# -----------------------------------------------
# a = input()
# a = a[1:-1].split(",")
# d = {}
# for i in a:
#     k , v = i.split(':')
#     d[k.strip("'\"")] = v.strip("'\"")

# # print(d)
# new_dict = {}
# seen_values= set()
# for key, value in d.items():
#     if value not in seen_values:
#         new_dict[key] = value
#         seen_values.add(value)
# print(new_dict)
# -----------------------------------------------------
# a = input()
# a = a[1:-1].split(",")
# d = {}
# for i in a:
#     k , v = i.split(':')
#     d[k.strip("'\"")] = v.strip("'\"")
# b=input()
# for key,value in d.items():
#     if key == b:
#         print(True)
#         print(key)
#     else:*9/
#         print(False)
# ------------------------------------------------------
# keys = eval(input())                           #['name', 'age', 'city']
# values = eval(input())                                #['Monika', 25]
# length = min(len(keys), len(values))  # Use shorter length
# d={}
# for i in range(length):
#     d[keys[i]] = values[i]
# print(d)
# # ------------------------------------------------------
# words=eval(input())
# result ={}
# for word in words:
#     first_letter=word[0]
#     if first_letter not in result:
#         result[first_letter] = []
#     result[first_letter].append(word)
# print(result)
# -----------------------------------------------------------
# a = input()
# a = a[1:-1].split(",")
# d = {}
# for i in a:
#     k , v = i.split(':')
#     d[k.strip("'\"")] = v.strip("'\"")
# new ={}
# for key,value in d.items():
#     new[value] = key
# print(new)
# # -----------------------------------------------------------
# a = input()
# a = a[1:-1].split(",")
# d1 = {}
# for i in a:
#     k , v = i.split(':')
#     d1[k.strip("'\"")] = v.strip("'\"")
# print(d1)

# b = input()
# b = b[1:-1].split(",")
# d2 = {}
# for i in b:
#     k , v = i.split(':')
#     d2[k.strip("'\"")] = v.strip("'\"")
# print(d2)

# merged = d1.copy()        
# merged.update(d2)       
# print(merged)
# -----------------------------------------------
# a = input()
# a = a[1:-1].split(",")
# d1 = {}
# for i in a:
#     k , v = i.split(':')
#     key = k.strip("'\"") 
#     value = v.strip("'\"")
#     d1[key] = int(value)

# sorted_items = sorted(d1.items(), key=lambda item: item[1])
# print(sorted_items)
# --------------------------------------------------
# def conBin(e):
#     st = ''
#     while(e):
#         st = str(e % 2) + st
#         e //= 2
#     return st[::-1]

# d = list(map(conBin,list(map(int,input().split(' ')))))
# print(d)
# r = []
# for e in d:
#     r.append(len(e))

# for i in range(len(d)):
#     if (len((d[i])) != max(r)):
#         d[i] = '0' * ((max(r)) - len(d[i])) + d[i]
# print(d)

# a,b = d
# count = 0
# for i in range(len(a)):
#     if a[i] != b[i]:
#         count += 1
# print(count)
# -----------------------------------------------------------
# l=[1,2,6,4,5,3]
# rating= [4,5,3,3,2,6]
# e=[]
# for i in range(len(rating)):
#     e.append(l[i]*rating[i])
# rmx = 0
# rind = 0
# for i in range(len(e)):
#     if (rating[i]*l[i] == ):
# print(e)
# k= rating.index(max(rating))
# print(k)

# if (rating[k]*l[k]==max(e)):
#     print(rating.index(max(rating)) + 1)
# else:
#     print(e.index(max(e)) + 1)
# --------------------------------------------------------

 
# w = "1119"
# for i in range(len(w)):
#     print(w[:len(w)-i]+' '+ w[len(w)-i:])
#     for j in range(i+1,len(w)):

# s = input("Enter number: ")
# n = len(s)
# for i in range(1, n):
#     print(s[:i], s[i:])

# for i in range(1, n):
#     for j in range(i + 1, n):
#         print(s[:i], s[i:j], s[j:])

# print(" ".join(s))
# ---------------------------------------------------------------

# string=input().split("]")
# arr1 = string[0]+"]"
# arr1 = eval(arr1)
# arr2 = eval(string[1])
# d={}
# length =min(len(arr1),len(arr2))
# for i in range(length):
#     d[arr1[i]]= arr2[i]
# print(d)
# -----------------------------------------------------------------
# string = input().split("} ")
# dictio = string[0] + "}"
# dictio = eval(dictio)
# isMatched = False
# matcher = string[1].replace("'","")
# for i in dictio:
#     if i== matcher:
#         print(f'(True,{dictio[i]})')
#         isMatched = True
# if(not isMatched):
#     print("(False,None)")
# __________________________________________________
# arr = eval(input())
# d={}
# for i in arr:
#     if i[0] not in d:
#         d[i[0]]= []
#     d[i[0]].append(i)
# print(d)

# ------------------------------------------------------
# arr = eval(input())
# d={}
# for i in arr:
#     if i[0] not in d:
#         d[i[0]]= {}
#     d[i][0][i[1]] = i[2]
# print(d) 

# a=[2,3,4,5,6]
# b=[9,1,2,3,4]
# for i in a:
#     for j in b:
#         if (i+j)==5:
#             print(i,j)
# ------------------------------------------------------
# s='183422'
# r=[]

# for i in range(2**(len(s)-1)):
#     p=[]
#     l=0
#     for j in range (len(s)):
#         if ((i>>j) & 1):
#             p.append(s[l:j+1])
#             l=j+1
#     p.append(s[l:])
#     r.append(p)

# def sumdigit(w):
#     s=0
#     while(w):
#         s+=w%10
#         w//=10
#     return s

# def ref(e):
#     w=[]
#     for i in e:
#         w.append(sumdigit(int(i)))
#     return w

# def filtersort(t):
#     if(t==sorted(t)):
#         return True
# f=list(map(ref,r))
# print(len(list(filter(filtersort,f))))
# -------------------------------------------------------
# num=int(input())
# if num == 1: 
#     print(1) 
# i = 2
# factorial = 1
# while factorial < num:
#     factorial *= i
#     if factorial == num:
#         print(i) 
#         break
#     i += 1
# else:
#     print("not a factorial")
# ---------------------------------------------------------  
# s='qwerty'
# vowels="aeiou"
# result=""
# for char in s:
#     if char in vowels:
#         result+=char
# ind=s.index(result)
# print(s[ind:]+s[:ind])
# ----------------------------------------------------------
# def is_prime(num):
#     if num < 2 :
#         return False
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             return False
#         return True
# num=[1,4,6,8,5,1,1,7]
# for i in range(len(num)):
#     if is_prime(num[i]):
#         num=num[i:]+num[:i]
# print(num)
# ----------------------------------------------------------
# def check_prime(w):
#     if w < 2 :
#         return False
#     for i in range(2,int(w**0.5)+1):
#         if w %i==0:
#             return False
#         return True

# w =[1,2,3,4,5]
# print(w)

# for i in range(len(w)):
    
#     if(str(w[i]).isalpha()):
#         if (w[i] in 'aeiou'):
#             r.append((w[1:]+w[:1]))
            
#         else:
#             if(check_prime(w[i])):
#                 r= w[i:]+w[:1]
# print(r)
# --------------------------------------------------------
# def lists(l1,l2,l3):
#     result=[]
#     for i in range(len(l1)):
#         l1[i]+=5
#         l2[i]+=10
#         l3[i]+=15
#     result+=l1,l2,l3
#     return result

# l1=list(map(int,input().split(' ')))
# l2=list(map(int,input().split(' ')))
# l3=list(map(int,input().split(' ')))
# print(lists(l1,l2,l3))
# -----------------------------------------------------------------
# profits=[60,100,120,50]
# weights=[10,20,30,40]
# w=40
# d={}
# d1={}
# for i in range(len(weights)):
#     for j in range(i+1,len(weights)):
#         if weights[i]+weights[j]==40:
#             d[weights[i]]=weights[j]
#             print(d)
#             if profits[i]+profits[j]==180:
#                 print(profits[i]+profits[j])
# dictio=dict(zip(weights,profits))
# print(dictio)
# for i in range(len(weights)):
#     for j in range(i+1,len(weights)):
#         if weights[i]+weights[j]==40:
#             d[weights[i]]=profits[i]
#             d1[weights[j]]=profits[j]
#             print(d.values(),d1.values()) 
# -----------------------------------------------------
# profits=[60,100,120,50]
# weights=[10,20,30,40]
# capacity=40

# def sorter(profits,weights,capacity):
#     n=len(profits)
#     dp=[[0]*(capacity+1) for x in range(n+1)]

#     for i in range(1,n+1):
#         wt , val = weights[i-1],profits[i-1]
#         for w in range(capacity+1):
#             if (wt<=w):
#                 dp[i][w] = max(dp[i-1][w] , dp[i-1][w-wt]+val)
#             else:
#                 dp[i][w] = dp[i-1][w]
#     return dp,dp[n][capacity]
# a,b = sorter(profits,weights,capacity)
# for i in a:
# #     print(i)
# # ---------------------------------------------------------------

# n=3
# l=[2,5,1]
# r=[5,2,4]
# max_value =0
# selected_index = 0
# for i in range(n):
#     value=l[i]*r[i]  
   
#     if value > max_value:
#         max_value = value
#         selected_index=i 
        
#     elif value == max_value:
#         if r[i]> r[selected_index]:
#             selected_index[i]
#         elif r[i] == r[selected_index]:
#             selected_index=i
# print(selected_index+1)
# ---------------------------------------------------
# main_str,pattern=input().split(' ')

# count=0
# for i in range(len(main_str)):
#     if main_str[i:i+len(pattern)] == pattern :
#         count += 1
# print(count)
# --------------------------------------------

# x,y = list(map(int,input().split()))
# xor = x^y
# print(bin(xor))
# print(bin(xor).count('1'))
# ------------------------------------------------------
# n=120
# count = 0
# for i in str(n):
#     if i!= '0':
#         if n % int(i) == 0:
#             count += 1
# print(count)
# ------------------------------------------------------

# <script>
#         setInterval(            
        
#             function randomcolor(){
#                 let hex='0123456789abcdef'
#                 let blank=''
#                 for(let i =0;i<6;i++){
#                     blank=blank+hex[Math.floor(Math.random()*16)]
                    
#                 }
#                 console.log(blank)

#                 document.body.style.background='#'+blank
#              } ,1
#             )
        
#     </script>