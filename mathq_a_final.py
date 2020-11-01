#!/usr/bin/env python3
# mathq_a_final.py -- an interactive math program
# Written by Department of Computer Science of Hunter College
# September 5, 2020
# Usage: mathq_a_final.py
#-----------------------------------------------------------------------------
# Main program
#-----------------------------------------------------------------------------
import random # can you guess what random is for?
import re     # what about this module?
print("Welcome to the mathq program.")
print("Input \"q\" to quit the program")
keep_asking_questions = True
correct=0.0
incorrect=0.0
while keep_asking_questions:
    # <<Generate a random math question and its solution>> 
    first_num = random.randint(0,9)
    second_num = random.randint(0,9)
    operator = random.randint(0,4)
    if operator == 1:
        # <<create multiplication question and solution>>
        solution = first_num * second_num
        question = "%d x %d = " % (first_num, second_num)
    elif operator == 2:
        # <<create addition question and solution>>
        solution = first_num + second_num
        question = "%d + %d = " % (first_num, second_num)
    elif operator == 3:
        # <<create minus question and solution>>
        solution = first_num + second_num
        (solution, first_num)= (first_num, solution)
        question = "%d - %d = " % (first_num, second_num)
    else:
        # <<create division question and solution>>
        while (first_num*second_num==0) and (second_num==0):
            # << check for zero division, if true, reroll >>
            first_num = random.randint(0,9)
            second_num = random.randint(0,9)
        solution = first_num * second_num
        (solution, first_num) = (first_num, solution)
        question = "%d / %d = " % (first_num, second_num)
    # <<Display the question and get valid response>>
    response_is_not_valid = True
    while response_is_not_valid:
        print(question, '?')
        response = input("> ")
        # <<check if response is valid>>
        match = re.search("^[0-9]+$|^q$", response)
        if match:
            response_is_not_valid = False
        else:
            print("That was an invalid response. Enter a number or 'q' to quit.")
    # <<Check correctness of user's response>>
    if response == 'q':
        keep_asking_questions = False
    else:
        if int(response) == solution:
            print('Correct!') # adjust indentation
            #increase the correct count
            correct+=1
        else:
            print("Incorrect! %s %d" % (question, solution))
            #increase incorrect count
            incorrect+=1
total=correct+incorrect
if total ==0:
    #check for no question is answer
    print("No score available")
else:
    percentage=correct*100/total
    print("You answered %d out of %d questions correctly, or %0.1f" % (correct, total, percentage),"% correctly.")
    print("Thank you for playing mathq")
print("Exiting the mathq program.")

