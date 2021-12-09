#!/usr/bin/env python
#-- encoding: UTF-8

#made by pswsm

import random as rand
import os


def rps(matches: int = 3) -> bool:
    """Main rock-paper-scissor function"""
    usr_points: int = 0
    cpu_points: int = 0
    options: tuple[str, str, str] = ('rock', 'paper', 'scissors')


    for i in range(int(matches)):
        print(f'Player: {usr_points} - Bot: {cpu_points}')
    
        u_input: str = input(f"What do you choose?\t")
        u_input = u_input.lower()
        cpu_option: str = rand.choice(options)

        is_valid = valid_option(u_input)
        if not is_valid:
            result = None
            return result
        result = chck_result(u_input, cpu_option, options)

        if result == 0:
            print(f"You Win, Perfect!")
            usr_points += 1
        elif result == 1:
            print(f"It's a tie!")
        elif result == 2:
            print(f'You loose!')
            cpu_points += 1
        else:
            print(f"Ooops, something went wrong!")

    return result

def chck_result(usr_choice, cpu_option, options) -> int:
    """Returns 0 if won,
               1 if tie,
               2 if loose."""
    if (usr_choice == cpu_option):
        return 1
    elif ((usr_choice == 'rock' and cpu_option == options[2])
          or (usr_choice == 'paper' and cpu_option == options[0])
          or (usr_choice == 'scissors' and cpu_option == options[1])):
        return 0
    else:
        return 2

def valid_option(u_input) -> bool:
    """Checks if user input is a valid option"""
    v_options: tuple[str, str, str] = ('rock', 'paper', 'scissors')

    for option in range(len(v_options)):
        if u_input.startswith(v_options[option][0]):
            u_input = v_options[option]

    if u_input in v_options:
        return True
    else:
        print(f'Please input a valid option (Rock, Paper, Scissors).\n')
        return False

if __name__ == "__main__":
    print("Running as a script")
else:
    print("Running as module")

rps()
