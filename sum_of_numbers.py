#!/usr/bin/env python3
# Created by: Reid MacLean
# Created on: March 2025
# This program calculates the sum of numbers from 1 to n


def main():
    # Ask the user to enter a positive integer
    user_num = input("Enter a positive integer: ")

    # Try to convert input to float first to check for decimals
    try:
        user_number = float(user_num)
    except ValueError:
        print(user_num, "is not an integer.")
        return

    # Check if the number is not an integer
    if not user_number.is_integer():
        print(user_num, "is not an integer.")
        return

    # Convert to integer safely now
    user_number = int(user_number)

    # Check if the number is negative
    if user_number < 0:
        print(user_number, "is not a positive number.")
        return  # Exit the program early if input is invalid

    # Special case: if the number is 0, the sum is 0
    if user_number == 0:
        print("The sum of numbers from 0 to", user_number, "is: 0")
        return

    # Initialize a variable to store the sum
    sum_of_numbers = 0

    # Use a for loop to calculate the sum from 0 to the input number
    for i in range(0, user_number + 1):
        sum_of_numbers += i  # Add each number to the total sum

    # Display the result
    print("The sum of numbers from 0 to", user_number, "is:", sum_of_numbers)


# This ensures that the main() function only runs when this script is executed directly
if __name__ == "__main__":
    main()
