import os
clear = clear = lambda: os.system('clear')
from art import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
clear()
print(logo)
def cal_total(list):
  current = 0
  for i in list:
    current += i
  return current
def game():
  def repeat_game():
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == "y":
      clear()
      game()
    else:
      return
  players = [
    {
      "name": "dealer",
      "cards": [],
      "total": 0
    },
    {
      "name": "player one",
      "cards": [],
      "total": 0
    }
  ]
  for player in players:
    for i in range(2):
      players[i]["cards"].append(random.choice(cards))
    player["total"] = cal_total(player["cards"])
    if players[0]["total"] == 21:
      print("House wins")
      print(players[0]["total"])
      repeat_game()
    elif players[1]["total"] == 21:
      print("Player one wins")
      print(players[1]["total"])
      repeat_game()

  

  def status():
    print(f"Your cards: { players[1]['cards'] }, current score: {players[1]['total']}")
    print(f"Computer's first card: {players[0]['cards'][0]}")
  status()

  def house_play():
    print("--------------------------------")
    print(f"{players[0]['total']} ")
    playing = True
    while playing:
      if players[0]["total"] > 16:
        playing = False
      else:
        players[0]["cards"].append(random.choice(cards))
        players[0]["total"] = cal_total(players[0]["cards"])
        print("test")
        print(f"{players[0]['total']} ")
    winner = ""
    if players[0]["total"] > players[1]["total"]:
      winner = players[0]
    else:
      winner = players[1]
    print(f"The winner is {winner['name']} with the total of {winner['total']}")
    status()
    print(f"{players[0]['cards']} ")

  keep_playing = True
  while keep_playing:
    if input("Type 'y' to get another card, type 'n' to pass:") == "n":
      status()
      keep_playing = False
      house_play()
      repeat_game()
    else:  
      players[1]["cards"].append(random.choice(cards))
      players[1]["total"] = cal_total(players[1]["cards"])
      status()
      if players[1]["total"] >= 21:
        keep_playing = False
        print("You loose, sorry 🥵")
        repeat_game()
    
wanna_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
if wanna_play == "y":
  game()

