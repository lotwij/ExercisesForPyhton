from QuestionClass import Question

Question_prompts = [
    "What is the coolest city?\n(A) Utrecht\n(B) New York\n(C) Rome\n\n",
    "What is the best drink?\n(A) Wine\n(B) Diet Coke\n(C) Vodka\n\n",
    "What is the best time of the year\n(A) My Birthday\n(B) Christmas\n(C) Eastern\n\n"
]

questions[
    Question(Question_prompts[0],"A"),
    Question(Question_prompts[1], "A"),
    Question(Question_prompts[2], "B")
]

def run_test(questions):
    score = 0
    for Question in questions