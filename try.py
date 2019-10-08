#!/usr/bin/env python3

# Created by: Andrei Chirilov
# Created on: Oct 2019
# This program does the try statement

import random


def main():
    # comment

    random_number = random.randint(1, 10)

    # asking if they can guess my number that I choose between 0 and 10
    # Input
    print("Can you guess the number I chose from 0 to 10?")
    integer_as_string = input("Enter the number that you think I guessed: ")

    # process
    try:
        integer_as_int = int(integer_as_string)
        if random_number == integer_as_int:
            print("You guessed it :)")
        else:
            print("The correct number was {}".format(random_number))
    except Exception:
        print("That was not a number")
    finally:
        print("Thank you for playing.")


if __name__ == "__main__":
    main()
