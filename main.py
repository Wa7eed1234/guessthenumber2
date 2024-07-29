# # import random
#
# def guess_next_number(number):
#   """Guesses the next number after the given number.
#
#   Args:
#     number: The number to guess the next number after.
#
#   Returns:
#     The next number after the given number.
#   """
#
#   # Generate a random number between 1 and 10.
#   next_number = random.randint(1, 10)
#
#   # If the random number is equal to the given number, then generate a new random number.
#   while next_number == number:
#     next_number = random.randint(1, 10)
#
#   return next_number
#
# # Get the user's input.
# number = int(input("Enter a number: "))
#
# # Guess the next number.
# next_number = guess_next_number(number)
#
# # Print the next number.
# print("The next number is",next_number)



# Import the random module.
import random

# Create a list of numbers.
numbers = [2, 23, 34]

# Get the user's input.
number = int(input("Enter a number: "))

# Check if the number is in the list.
if number in numbers:
  # If the number is in the list, then print the next number in the list.
  print("The next number is", numbers[numbers.index(number) + 1])

else:
  # If the number is not in the list, then print a random number from the list.
  print("The next number is", random.choice(numbers))


