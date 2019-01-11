from QuestionClass import Question

question_prompts = [
    "What is the coolest city?\n(a) Utrecht\n(b) New York\n(c) Rome\n\n",
    "What is the best drink?\n(a) Wine\n(b) Diet Coke\n(c) Vodka\n\n",
    "What is the best time of the year\n(a) My Birthday\n(b) Christmas\n(c) Eastern\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)