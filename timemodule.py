# # class employee:
# #     def __init__(self,name,id):
# #         self.name=name
# #         self.id =id
    
# # class programmer(employee):
# #     def __init__(self,name,id,lang):
# #         super().__init__(name,id)
# #         self.lang=lang

# # rohan=employee('rohan das','45')
# # print(rohan.name)
# # print(rohan.id)
# # harry=programmer('harry','56','english')

# # # print(harry.name)
# # # print(harry.id)
# # print(harry.lang)

# class vector:
#     def __init__(self,i,j,k):
#         self.i=i
#         self.j=j
#         self.k=k

#     def __str__(self):
#         return f'{self.i}i + {self.j}j + {self.k}k'
    
# a=vector(3 , 5 ,6 )
# print(a)

# class animal:
#     def __init__(self,name,species):
#         self.name=name
#         self.species=species
#     def make_sound(self):
#         print('sound made by the animal')

# class dog(animal):
#     def __init__(self,name,breed):
#         animal.__init__(self,name,species='dog')
#         self.breed=breed

#     def make_sound(self):
#         print('bark!!')

# s=animal('golden retriever','dobberman')
# s.make_sound()

# import time
# def usingwhile():
#     i=0
#     while i<50:
#         i=i+1
#         print(i)
# def usingfor():
#     for i in range(50):
#         print(i)

# init=time.time()
# usingfor()
# print(time.time()-init)
# init=time.time()
# usingwhile()
# print(time.time()-init)

# import time
# print(4)
# time.sleep(6)
# print(8)

# import time
# t=time.localtime()
# form_time=time.strftime('%y-%m-%d %H: %M:%S',t)
# print(form_time)

# import time
# t=time.localtime()
# form_time=time.strftime('%y-%m-%d  %H:%M:%S' )
# print(form_time)
 
 
# foods=list()
# while (food:=input('what food do u like?: '))!= 'quit':
#     foods.append(food)

import random
user_wins=0
computer_wins=0
options= ['rock' , 'paper' , 'scissors']

while True:
    user_input=input('type rock/paper/scissors or q to quit : ').lower()
    if user_input=='q':
        break
    if user_input not in options:
        continue

    random_number=random.randint(0,2)
    computer_pick=options[random_number]
    print('computer picked', computer_pick ,'.')
 
    if user_input=='rock' and computer_pick=='scissors':
        print('you won!!')
        user_wins+=1

    elif user_input=='paper' and computer_pick=='rock':
        print('you won!!')
        user_wins+=1
       
    elif user_input=='scissors' and computer_pick=='paper':
        print('you won!!')
        user_wins+=1

    else:
        print('you lost!!')
        computer_wins+=1

print('you won', user_wins , 'times')
print('computer won', computer_wins , 'times')
print('goodbye!!')