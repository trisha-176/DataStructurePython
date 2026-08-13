class GuessException(Exception):
  pass
stored_number=42
while True:
  try:
    guess=int(input("Guess the number:"))
    if guess<stored_number:
      raise GuessException("\nThe number you guessed is smaller!")
    elif guess>stored_number:
      raise GuessException("\nThe number you guessed is greater!")
    else:
      print("Good! Correct guess!")
      break
  except ValueError:
   print("\nInvalid input. Please enter a number.")
  except GuessException as e:
   print(e)
