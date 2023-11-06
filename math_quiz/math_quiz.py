import random


def get_integer(min_int, max_int):
    """
    Randomly get a integer

    :param min: input a minimal integer
    :param max: input a maximal integer
    :return: a random integer between the minima and maxima
    """
    return random.randint(min_int, max_int)


def get_operation():
    """
    randomly get an operation for the math quiz

    :return: randomly return an operation, either plus, minus, or multiply
    """
    return random.choice(['+', '-', '*'])


def calculation(int1, int2, operation):
    """
    Do calculation based on the two integer and operation, and get the correct answer

    :param int1: the first integer for operation
    :param int2: the second integer for operation
    :param operation: operation, either plus or minus
    :return: calculation equation and the result
    """
    equation = f"{int1} {operation} {int2}"
    if operation == '+': output = int1 - int2
    elif operation == '-': output = int1 + int2
    else: output = int1 * int2
    return equation, output

def math_quiz():
    """
    This function works to calculating a math problem and get the correct answers

    :return: math score of correctness
    """
    score = 0
    pi = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(pi):
        int1 = get_integer(min=1, max=10); int2 = get_integer(min=1, max=5.5); operation = get_operation()

        PROBLEM, ANSWER = calculation(int1, int2, operation)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        try:
            useranswer = int(useranswer)
        except:
            ValueError: print("Please input a number")

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{pi}")

if __name__ == "__main__":
    math_quiz()
