# import random
# def check(comp,user):
#     if comp==user:
#         return 0
#     if comp==0 and user==1:
#         return -1
#     if comp==1 and user==2:
#         return-1
#     if comp==2 and user==0:
#         return -1
#     return 1
# comp=random.randint(0,2)
# user=int(input('0 for snake , 1 for water and 2 for gun :\n'))

# print('you:', user)
# print('computer:', comp)

# score=check(comp,user)
# if score==0:
#     print('its a draw')
# elif score==-1:
#     print('you lose')
# else:
#     print('you won')


# class math:
#     def __init__(self,num):
#         self.num=num
    
#     def addtonum(self,n):
#         self.num=self.num+n

#     @staticmethod
#     def add(a,b):
#         return a+b
# a=math(5)
# # print(a.num)
# a.addtonum(2)
# print(a.num)

# class employee:
#     company='samsung company'   #class variable
#     def __init__(self,name):
#         self.name=name
#         self.raise_amount=0.02
#     def showdetails(self):
#         print(f'the name of the employee is {self.name} and the raise amount is {self.raise_amount} in the {self.company}' )
# a=employee('harry')
# a.raise_amount=0.4
# a.showdetails()
# a1=employee('roshan')
# a1.showdetails()

# class library :
#     def __init__(self , books , no_of_books ):
#         self.books = books
#         self.no_of_books = no_of_books
#     def real_library(self):
#         print(f"the length of books : {self.no_of_books}")
#         for book in books:
#             print(book)

# books = ["harry potter1","harry potter2", "harry potter3"]

# novel = library(books , len(books))
# novel.real_library()


class library:
    def __init__(self,books,no_of_books):
        self.books=books
        self.no_of_books = no_of_books

    def original_library(self):
        print(f'the total no of books are: {self.no_of_books}')

        for book in books:
            print(book)

books=['end with us1', 'end with us 2']
a=library(books,len(books))
# print(a)
a.original_library()