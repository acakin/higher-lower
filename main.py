from game_data import data
from replit import clear
from art import logo
from art import vs
import random

name, follower_count, description, country = "name", "follower_count", "description", "country"
def randomizer():
  number = random.choice(range(len(data)))
  choosen_data = data[number]
  return choosen_data
game_over = True
def comparer(x, y):
  return max(x, y)
counter = 0
a = randomizer()
while game_over:   
  b = randomizer()
  while a == b:
    a = randomizer()
    b = randomizer()
  
  print(logo)
  if counter != 0:
    print(f"You're right! Current score: {counter}")
  print(f"Compare A: {a[name]}, a {a[description]}, from {a[country]}.")
  print(vs)
  print(f"Against B: {b[name]}, a {b[description]}, from {b[country]}.")
  choice = input("Who has more followers? Type 'A' or 'B':").lower()
  if choice == "a":
    choice = a[follower_count]
  elif choice == "b":
    choice = b[follower_count]
  
  if choice != comparer(a[follower_count], b[follower_count]):
    clear()
    print(f"Sorry, that's wrong. Final score: {counter} ")
    game_over = False
  else:
    counter += 1    
    a = b
    clear()
    
    
    
  