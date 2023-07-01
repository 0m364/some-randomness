import random

def spin_reel():
    symbols = ['🍎', '🍊', '🍇']
    return random.choice(symbols)

def play_slot_machine():
    reel1 = spin_reel()
    reel2 = spin_reel()
    reel3 = spin_reel()
    result = reel1 + " | " + reel2 + " | " + reel3

    print("Spinning the reels...\n")
    print(result)

    if reel1 == reel2 == reel3:
        print("\nCongratulations! You won!")
    else:
        print("\nBetter luck next time!")
    
while True:
    user_input = input("\nWould you like to play? (y/n): ")
    if user_input.lower() == 'y':
        play_slot_machine()
    else:
        print("Thank you for playing!")
        break
