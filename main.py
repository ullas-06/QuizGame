import random
from question import quiz_questions  # The quiz_questions are present in another file question

random.shuffle(quiz_questions)  # Used to shuffle the questions

questions = quiz_questions[:20] # selecting first 20 questions from the shuffled list


score = 0
for i,que in enumerate(questions):  # Looping over randomly selected questions
    print(f"{i+1}. {que['question']}")

    for j,option in enumerate(que['options']):  # printing the options
        print(f"{j+1} {option}")

    res = int(input("Enter the Option\n"))  # user input

    if que['options'][res - 1] == que['answer']:  # comparing the answer with option
        score += 1
        print("Correct!\n")
    else:
        print(f"Wrong! The correct answer is: {que['answer']}\n")

print(f"The Final Score is: {score}/{len(questions)}")   # displaying the score