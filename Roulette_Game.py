import time
import random

# Set the numbers and their corresponding colors
numbers = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11,
           30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22,
           18, 29, 7, 28, 12, 35, 3, 26]

colors = {0: "green", 32: "red", 15: "black", 19: "red", 4: "black",
          21: "red", 2: "black", 25: "red", 17: "black", 34: "red",
          6: "black", 27: "red", 13: "black", 36: "red", 11: "black",
          30: "red", 8: "black", 23: "red", 10: "black", 5: "red",
          24: "black", 16: "red", 33: "black", 1: "red", 20: "black",
          14: "red", 31: "black", 9: "red", 22: "black", 18: "red",
          29: "black", 7: "red", 28: "black", 12: "red", 35: "black", 3: "red", 26: "black"}

# Function to simulate a spinning wheel
def spin_wheel():
    for _ in range(5):
        for number in random.sample(numbers, len(numbers)):
            print('\033c', end='')  # Clear the console before printing
            print("Spinning wheel... ", number)
            time.sleep(0.1)

# Function to play the roulette game
def play_roulette():
    print("Welcome to the Roulette Game!")
    while True:
        print("\nSelect an option:")
        print("1. Spin the wheel")
        print("2. Quit")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            spin_wheel()
            selected_number = random.choice(numbers)
            color = colors[selected_number]

            print('\033c', end='')
            print("The wheel stopped at:", selected_number)
            print("Color:", color)
        elif choice == "2":
            print("Thank you for playing. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Start the roulette game
play_roulette()
`
