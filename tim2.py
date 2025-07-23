import random
top_of_range=input('type a number:')
guesses=0

if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print('please type a number larger than 0')
        quit()
else:
    print('please type a number next time')
    quit()

random_number=random.randint(0,top_of_range)

while True:
    guesses+=1
    user_guess=input('enter a guess a number')
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print('please enter a number')
        continue
    if user_guess==random_number:
        print('you got it!!')
        break
    else:
        if user_guess>random_number:
            print('you were above the number')
        else:
            print('you were below the number')

print(f'total number of guesses are {guesses}')

print('you got it in ' , guesses,'guesses')