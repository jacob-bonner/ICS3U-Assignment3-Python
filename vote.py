#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: October 2019
# This program tells the user if they are old enough to vote in an election


def main():
    # This program tells the user if they are old enough to vote in an election

    # Input
    userAge = int(input("Enter your age here: "))
    print("")

    # Process
    if userAge >= 18:
        print("You are old enough to vote!")
    else:
        print("Sorry, you are not old enough to vote.")


if __name__ == "__main__":
    main()
