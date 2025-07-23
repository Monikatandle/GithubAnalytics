# max product from an array
# def max_product(arr):
#     a_len=len(arr)
#     if a_len<2:
#         print("no such pair exists")
#         return

#     a = arr[0]
#     b = arr[1]
#     for i in range(0,len (arr)):
#         for j in range(i+1,len(arr)):
#             if(arr[i]*arr[j])>(a*b):
#                 a=arr[i]
#                 b=arr[j]
#     return a,b

# arr=eval(input("enter an array : "))
# print(max_product(arr))
# -------------------------------------
# import random
# def guess_number(n):
#     random_number=random.randint(1,n)
#     guess=0
#     while guess!=random_number:
#         guess=int(input(f"guss a number between 1 and {n}:"))
#         if guess<random_number:
#             print("too low")
#         elif guess> random_number:
#             print("too high")
#     print("congrats")
# guess_number(10)
# -----------------------------
# import random
# def computer_guess(x):
#     low = 1
#     high = x
#     feedback = ''
#     while feedback != 'c':
#         if low != high:
#             guess = random.randint(low, high)
#         else:
#             guess = low  # only one option left
#         feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
#         if feedback == 'h':
#             high = guess - 1
#         elif feedback == 'l':
#             low = guess + 1
#     print(f'Yay! The computer guessed your number,  correctly!')
# computer_guess(10)
# --------------------------------------------
# import random
# def play():
#     user=input("what's your choice?? r for Rock, p for Paper,s for Scissors")
#     computer = random.choice(["r","p","s"])
#     if user==computer:
#         return "it's a tie"
#     if win(user,computer):
#         return "you won"
#     return "you lost"
    
# def win(player,opponent):
#     if(player=="r"and opponent=="s") or (player=="s" and opponent=="p") or (player=="p" and opponent=="r"):
#         return True
# print(play())
# --------------------------------------------------------------


