print("===== PYTHON LEARNING GAME =====")
print("Welcome! Let's test your knowledge.\n")

score = 0

questions = {
    "What is 5 + 5? ": "10",
    "What is 6 x 3? ": "18",
    "What is 20 - 8? ": "12",
    "What is 36 / 6? ": "6",
    "What is 2 ** 3? ": "8"
}

for question, answer in questions.items():
    user_answer = input(question)

    if user_answer.strip() == answer:
        print("Correct! Well done.\n")
        score += 1
    else:
        print("Wrong! The correct answer is", answer, "\n")

print("===== QUIZ COMPLETED =====")
print("Your score:", score, "out of", len(questions))

if score == 5:
    print("Excellent! You have mastered this lesson!")
elif score >= 3:
    print("Good job! Keep practising.")
else:
    print("Keep learning. You will get better!")

