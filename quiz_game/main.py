def check_answer(user_answers, correct_answers):
    true_number = 0
    for index, (question, correct_answer) in enumerate(correct_answers.items()):
        user_answer = user_answers[index]
        if user_answer.lower() == correct_answer.lower():
            true_number += 1
            print("your answer =", user_answer, "\ncorrect answer =", correct_answer, "\n")
    print("your point =", str(true_number) + "/4")


questions = {
    'Who is the first president of Turkiye?': 'ataturk',
    'How many continents are there in the world?': '7',
    'What is the opening WC ?': 'water closet',
    'Who is created the coordinate system ?': 'descartes'
}

user_answers = []

print("*********WELCOME TO THE QUIZ GAME*********\n\n")
for question in questions.keys():
    entry = input(question + "-> ")
    user_answers.append(entry)

check_answer(user_answers, questions)