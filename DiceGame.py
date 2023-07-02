import random

def roll_dice(num):
  """Rolls num dice and returns the sum."""
  return sum(random.randint(1, 6) for _ in range(num))

def cee_lo():
  """Plays a game of Cee-Lo."""
  roll = roll_dice(3)
  if roll in (4, 5, 6):
    return "instant win"
  elif roll in (1, 2, 3):
    return "instant loss"
  else:
    return "point"

def craps():
  """Plays a game of Craps."""
  roll = roll_dice(2)
  if roll == 7 or roll == 11:
    return "natural"
  elif roll in (2, 3, 12):
    return "craps"
  else:
    return "point"

def main():
  """Plays a game of Cee-Lo or Craps."""
  while True:
    game = input("Choose a game: Cee-Lo (c) or Craps (cr): ")
    if game.lower() == "c":
      result = cee_lo()
      break
    elif game.lower() == "cr":
      result = craps()
      break
    else:
      print("Invalid game. Please choose either 'c' for Cee-Lo or 'cr' for Craps.")

  print(f"You rolled {result}.")

if __name__ == "__main__":
  main()
  
