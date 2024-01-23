'''
operations.py - This program will give the user 10 mathematical questions based on
the operator of their choosing. The user may also choose a "gauntlet" option which
will give them 20 questions with 5 questions using each operator. The user will
also have the option of specifying 1, 2, or 3-digit numbers for each question.
The results will be printed to the screen once the test has concluded.
'''


import random
import time
import pyinputplus as pyip


# Track the number of questions, correct answers and incorrect answers.
questions = 0
correct_answers = 0
incorrect_answers = 0


def single_add():
    """Gives the user a 1-digit addition problem.
    """
    global questions
    global correct_answers
    global incorrect_answers

    a = random.randint(0,9)
    b = random.randint(0,9)
    result = a + b

    print('-' * 20)
    answer = pyip.inputNum(prompt=f'\nWhat is {a} + {b}?\n')
    time.sleep(1)
    print(f'\nYour answer: {answer}')
    print(f'\nCorrect answer: {result}')
    time.sleep(2)

    questions += 1
    if result == answer:
        correct_answers += 1
    else:
        incorrect_answers += 1


def double_add():
    """Gives the use a 2-digit addition problem.
    """
    global questions
    global correct_answers
    global incorrect_answers

    a = random.randint(0,99)
    b = random.randint(0,99)
    result = a + b

    print('-' * 20)
    answer = pyip.inputNum(prompt=f'\nWhat is {a} + {b}?\n')
    time.sleep(1)
    print(f'\nYour answer: {answer}')
    print(f'\nCorrect answer: {result}')
    time.sleep(2)

    questions += 1
    if result == answer:
        correct_answers += 1
    else:
        incorrect_answers += 1


def triple_add():
    """Gives the user a 3-digit addition problem.
    """
    global questions
    global correct_answers
    global incorrect_answers

    a = random.randint(0,999)
    b = random.randint(0,999)
    result = a + b

    print('-' * 20)
    answer = pyip.inputNum(prompt=f'\nWhat is {a} + {b}?\n')
    time.sleep(1)
    print(f'\nYour answer: {answer}')
    print(f'\nCorrect answer: {result}')
    time.sleep(2)

    questions += 1
    if result == answer:
        correct_answers += 1
    else:
        incorrect_answers += 1


def single_sub():
    """Gives the user a 1-digit subtraction problem.
    """
    global questions
    global correct_answers
    global incorrect_answers

    a = random.randint(0,9)
    b = random.randint(0,9)
    result = a - b

    print('-' * 20)
    answer = pyip.inputNum(prompt=f'\nWhat is {a} - {b}?\n')
    time.sleep(1)
    print(f'\nYour answer: {answer}')
    print(f'\nCorrect answer: {result}')
    time.sleep(2)

    questions += 1
    if result == answer:
        correct_answers += 1
    else:
        incorrect_answers += 1


def double_sub():
    """Gives the user a 2-digit subtraction problem.
    """
    global questions
    global correct_answers
    global incorrect_answers

    a = random.randint(0,99)
    b = random.randint(0,99)
    result = a - b

    print('-' * 20)
    answer = pyip.inputNum(prompt=f'\nWhat is {a} - {b}?\n')
    time.sleep(1)
    print(f'\nYour answer: {answer}')
    print(f'\nCorrect answer: {result}')
    time.sleep(2)

    questions += 1
    if result == answer:
        correct_answers += 1
    else:
        incorrect_answers += 1


def triple_sub():
    """Gives the user a 3-digit subtraction problem.
    """
    global questions
    global correct_answers
    global incorrect_answers

    a = random.randint(0,999)
    b = random.randint(0,999)
    result = a - b

    print('-' * 20)
    answer = pyip.inputNum(prompt=f'\nWhat is {a} - {b}?\n')
    time.sleep(1)
    print(f'\nYour answer: {answer}')
    print(f'\nCorrect answer: {result}')
    time.sleep(2)

    questions += 1
    if result == answer:
        correct_answers += 1
    else:
        incorrect_answers += 1


def single_multi():
    """Gives the user a 1-digit multiplication problem.
    """
    global questions
    global correct_answers
    global incorrect_answers

    a = random.randint(0,9)
    b = random.randint(0,9)
    result = a * b

    print('-' * 20)
    answer = pyip.inputNum(prompt=f'\nWhat is {a} * {b}?\n')
    time.sleep(1)
    print(f'\nYour answer: {answer}')
    print(f'\nCorrect answer: {result}')
    time.sleep(2)

    questions += 1
    if result == answer:
        correct_answers += 1
    else:
        incorrect_answers += 1


def double_multi():
    """Gives the user a 2-digit multiplication problem.
    """
    global questions
    global correct_answers
    global incorrect_answers

    a = random.randint(0,99)
    b = random.randint(0,99)
    result = a * b

    print('-' * 20)
    answer = pyip.inputNum(prompt=f'\nWhat is {a} * {b}?\n')
    time.sleep(1)
    print(f'\nYour answer: {answer}')
    print(f'\nCorrect answer: {result}')
    time.sleep(2)

    questions += 1
    if result == answer:
        correct_answers += 1
    else:
        incorrect_answers += 1


def triple_multi():
    """Gives the user a 3-digit multiplication problem.
    """
    global questions
    global correct_answers
    global incorrect_answers

    a = random.randint(0,999)
    b = random.randint(0,999)
    result = a * b

    print('-' * 20)
    answer = pyip.inputNum(prompt=f'\nWhat is {a} * {b}?\n')
    time.sleep(1)
    print(f'\nYour answer: {answer}')
    print(f'\nCorrect answer: {result}')
    time.sleep(2)

    questions += 1
    if result == answer:
        correct_answers += 1
    else:
        incorrect_answers += 1


def single_div():
    """Gives the user a 1-digit division problem.
    """
    global questions
    global correct_answers
    global incorrect_answers

    a = random.randint(0,9)
    b = random.randint(1,9)
    result = int(a / b)

    print('-' * 20)
    answer = pyip.inputNum(prompt=f'\nWhat is {a} / {b}?\n')
    time.sleep(1)
    print(f'\nYour answer: {answer}')
    print(f'\nCorrect answer: {result}')
    time.sleep(2)

    questions += 1
    if result == answer:
        correct_answers += 1
    else:
        incorrect_answers += 1


def double_div():
    """Gives the user a 2-digit division problem.
    """
    global questions
    global correct_answers
    global incorrect_answers

    a = random.randint(0,99)
    b = random.randint(1,99)
    result = int(a / b)

    print('-' * 20)
    answer = pyip.inputNum(prompt=f'\nWhat is {a} / {b}?\n')
    time.sleep(1)
    print(f'\nYour answer: {answer}')
    print(f'\nCorrect answer: {result}')
    time.sleep(2)

    questions += 1
    if result == answer:
        correct_answers += 1
    else:
        incorrect_answers += 1


def triple_div():
    """Gives the user a 3-digit division problem.
    """
    global questions
    global correct_answers
    global incorrect_answers

    a = random.randint(0,999)
    b = random.randint(1,999)
    result = int(a / b)

    print('-' * 20)
    answer = pyip.inputNum(prompt=f'\nWhat is {a} / {b}?\n')
    time.sleep(1)
    print(f'\nCorrect answer: {result}')
    time.sleep(2)

    questions += 1
    if result == answer:
        correct_answers += 1
    else:
        incorrect_answers += 1


def main():
    """Main function to run the program. Gets the test mode and difficulty
    from the user.
    """
    # Get the user's desired test mode and the max number of digits for each number.
    print()
    test_mode = pyip.inputMenu(['Addition', 'Subtraction',
                                'Multiplication', 'Division', 'All'],
                               numbered=True)
    num_of_digits = pyip.inputMenu(['1-digit', '2-digit', '3-digit'],
                                 numbered=True,
                                 prompt="\nSelect the max number of digits for each number:\n")


    # Call program functions based on the user's settings.
    if test_mode == "Addition":
        if num_of_digits == "1-digit":
            while questions < 10:
                single_add()
        elif num_of_digits == "2-digit":
            while questions < 10:
                double_add()
        elif num_of_digits == "3-digit":
            while questions < 10:
                triple_add()

    if test_mode == "Subtraction":
        if num_of_digits == "1-digit":
            while questions < 10:
                single_sub()
        elif num_of_digits == "2-digit":
            while questions < 10:
                double_sub()
        elif num_of_digits == "3-digit":
            while questions < 10:
                triple_sub()

    if test_mode == "Multiplication":
        if num_of_digits == "1-digit":
            while questions < 10:
                single_multi()
        elif num_of_digits == "2-digit":
            while questions < 10:
                double_multi()
        elif num_of_digits == "3-digit":
            while questions < 10:
                triple_multi()

    if test_mode == "Division":
        if num_of_digits == "1-digit":
            while questions < 10:
                single_div()
        elif num_of_digits == "2-digit":
            while questions < 10:
                double_div()
        elif num_of_digits == "3-digit":
            while questions < 10:
                triple_div()

    if test_mode == "All":
        if num_of_digits == "1-digit":
            while questions < 20:
                single_add()
                single_sub()
                single_multi()
                single_div()
        elif num_of_digits == "2-digit":
            while questions < 20:
                double_add()
                double_sub()
                double_multi()
                double_div()
        elif num_of_digits == "3-digit":
            while questions < 20:
                triple_add()
                triple_sub()
                triple_multi()
                triple_div()


    # Print results of test.
    print()
    print('-' * 30)
    print('\nHere are your results:')
    print(f'Questions: {questions}')
    print(f'Correct answers: {correct_answers}')
    print(f'Incorrect answers: {incorrect_answers}')
    time.sleep(5)


if __name__ == "__main__":
    main()
