#!/usr/bin/env python
#-- encoding: UTF-8

#made by pswsm

import random as rand
import os


def rps(user_choice: str) -> bool:
    """Main rock-paper-scissor function"""
    options: list[str] = ['rock', 'paper', 'scissors']
    cpu_option: str = rand.choice(options)

    if (user_choice == cpu_option):
        print(f"It's a tie!")
        return True
    elif ((user_choice.lower() == 'rock' and cpu_option == options[2])
          or (user_choice.lower() == 'paper' and cpu_option == options[0])
          or (user_choice.lower() == 'scissors' and cpu_option == options[1])):
        print(f'You win!')
        return False
    else:
        print(f'You loose!')
        return True


def valid_option(user_choice) -> bool:
    """Checks if user input is a valid option"""
    v_options: list[str] = ['rock', 'paper', 'scissors']

    if user_choice in v_options:
        return True
    else:
        print(f'Please input a valid option (Rock, Paper, Scissors).\n')
        return False

run: bool = True
while run == True:
    uc: str = input(f'Rock, Paper or Scissors?!?\t')
    while not valid_option(uc):
        os.system('clear')
        print(f'Not a valid option.\nValid options are:\n\t- Rock\n\t- Paper\n\t- Scissors')
        uc = input(f'Rock, Paper or Scissors?!?\t')
    
    os.system('clear')
    run = rps(uc)

