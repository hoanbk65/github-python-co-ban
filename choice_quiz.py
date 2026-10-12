from quiz import Quiz

question =[
    "Câu 1: Đội bóng nào về nhì WC 2022? \nA. Argentina \nB. Pháp \nC. Croatia \nD. Brazil \n",
    "Câu 2: Đội bóng nào vô địch WC 2022? \nA. Argentina \nB. Pháp \nC. Croatia \nD. Brazil \n",
    "Câu 3: Đội bóng nào về nhì WC 2018? \nA. Argentina \nB. Pháp \nC. Croatia \nD. Brazil \n",
]

quiz = [
    Quiz(question[0], "B"),
    Quiz(question[1], "A"),
    Quiz(question[2], "C"),
]

def run_quiz(quiz):
    score = 0
    for q in quiz:
        print(q.question)
        user_input = input("Your answer: ")
        if user_input == q.answer:
            
            score += 1
            print("Correct!")

run_quiz(quiz)