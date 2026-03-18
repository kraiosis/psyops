import random
import time
import sys

def memgame():
    """
    A simple memory game
    """
    # Generate a random integer between 1 and 10 (inclusive)
    random_integer = random.randint(1234567, 7654321)

    # Print a character/string with no newline at the end
    print(f"Remember this number: {random_integer}", end="", flush=True) # flush=True ensures it prints immediately print( random_integer, end="", flush=True) # flush=True ensures it prints immediately
    time.sleep(2) # Wait a moment

    # Overwrite the previous output with spaces, then a new char/string, then a carriage return
    # The number of spaces should be at least the length of the previous output
    sys.stdout.write('\r' + ' ' * 50 + '\r')
    sys.stdout.flush() # Ensure it's displayed

    guess = int(input("What number do you remember? Enter a number: "))

    if guess == random_integer:
        print("Correct!")
    else:
        print("Incorrect. The number was", random_integer)

    # Wait a moment
    time.sleep(2)
