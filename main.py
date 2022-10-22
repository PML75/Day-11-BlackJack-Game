from art import logo
import random 
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
comp_cards = []
user_cards = []

def deal_card():
  return random.choice(cards)

def hit_hand(hand):
  hand.append(random.choice(cards))

def play_again():
  player = input("\nDo you want to play again ? 'y' or 'n': ")
  if player == "y":
    clear()
    comp_cards.clear()
    user_cards.clear()
    start_game()
  else:
    print("Goodbye.")

def comp_compare():
  comp_total = add_hand(comp_cards)
  if comp_total < 17:
    hit_hand(comp_cards)
    print("Computer's new hand: [ ", end = "")
    print(*comp_cards, end = "")
    print(" ]")

def user_compare():
  user_total = add_hand(user_cards)
  if user_total == 21:
    print("You win!")
    play_again()
  elif user_total > 21:
    print("\nBusted. You lost!")
    play_again()
    return True
  
def compare(comp_hand, user_hand):
  comp_total = add_hand(comp_hand)
  user_total = add_hand(user_hand)

  if comp_total == 21 and user_total == 21:
    print("\nTwo Blackjack!? Tie game.")
  elif comp_total == 21 and user_total < 21:
    print("\nComputer has Blackjack! You lose.")
  elif comp_total > 21 and user_total < 21:
    print("\nComputer is over 21! You win.")
  elif user_total < 21 and user_total > comp_total:
    print("\nYou win!")
  play_again()

def stand_hand():
  print("")
  #check_hand(comp_cards, user_cards)

def add_hand(hand):
  hand_total = 0
  for card in hand:
    hand_total += card
  return hand_total

def start_game():
  bust = False
  while not bust:
    print(logo)
    black_jack = input("Do you want to play a game of blackjack? 'y' or 'n': ")
    
    #deal cards to computer and user
    if black_jack == "y":
      for card in range(2):
        comp_cards.append(deal_card())
        user_cards.append(deal_card())
      print("Your Hand: [", user_cards[0], user_cards[1], "]")
      print("Computer's Hand: [", comp_cards[0], "⬛ ]")
      continue_hit = False
  
      while not continue_hit:
        hit_stand = input("\nDo you want to hit or stand: 'hit' or 'stand': ")
        if hit_stand == "hit":
          hit_hand(user_cards)
          print("Your hand: [ ", end = "")
          print(*user_cards, end = "")
          print(" ]")
          if user_compare() == True:
            bust = True
            continue_hit = True
        else: 
          stand_hand()
          continue_hit = True
          bust = True
          print("Your hand: [ ", end = "")
          print(*user_cards, end = "")
          print(" ]")
          print("Computer's hand: [ ", end = "")
          print(*comp_cards, end = "")
          print(" ]")
          comp_compare()
          compare(comp_cards, user_cards)
    else:
      bust = True
      print("Goodbye!")
  
  
  
start_game()

  
