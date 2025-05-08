import random
import math

def generate_addition(x, y):
    question = f"{x} + {y} = ?"
    answer = x + y
    return question, answer

def generate_square_root():
    numbers = random.choice(range(16, 145))
    question = f"√{numbers} = ?"
    answer = round(math.sqrt(numbers), 2)
    return question, answer

def main():
    print("Welcome to Smart Calculator!")
    score = 0
    for round_number in range(1, 6):
        print(f"\nChallenge {round_number}/5")
        challenge = random.choice(["addition", "sqrt"])
        if challenge == "addition":
           x = random.randint(1, 50)
           y = random.randint(1, 50)
           question, correct_answer = generate_addition(x, y)
        else:
           question, correct_answer = generate_square_root()
        print(question)
        user_answer = input("Your answer: ")
        try:
            user_answer = float(user_answer)
            if abs(user_answer - correct_answer) < 0.01:
               print("Correct!")
               score +=1
            else:
                 print(f"Wrong. The correct answer was {correct_answer}")
        except ValueError:
             print("Please enter a valid number: ")
    print(f"\nFinal score: {score}/5")
main()