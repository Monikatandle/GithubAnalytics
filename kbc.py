# print("Lets play Kaun Banega Crorepati")
# question = ("The International Literacy Day is observed on options ")
# options = (" A. Sep 8, B. Sep 22, C. Nov 10")
# print(question)
# print(options)

# answer = input("Enter the correct option: ")
# if(answer == "A" ):
#   print("Correct answer You win 1 Crore Ruppes")
# else:
#   print("Better luck next time")


questions = {
    "What is the capital of India": "Delhi",
    "What is the National Bird of India": "Peacock",
    "What is the National Animal of India": "Tiger",
    "How many states are there in India": "28",
}
Options = [
    ["Delhi", "Kolkata", "Mumbai", "Chennai"],
    ["Pigeon", "Crow", "humming bird", "Peacock"],
    ["Elephant", "Lion", "Tiger", "Liger"],
    ["9", "28", "31", "23"],
]
print(len(questions))
l = len(questions)
i = 0
for key, value in questions.items():
    print(key)
    print(value)
    ans = input(f"{key}?{Options[i]}: ")
    i = i + 1
    if value == ans:
        continue
    else:
        print("You are out")
        break

  