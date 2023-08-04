import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

from art import logo
print(logo)

database = []
#HINT: You can call clear() to clear the output in the console.
print('Welcome to the secret auction program.')
user_name = input('What is your name?: ')
user_bid = int(input('What\'s your bid?: $'))


def blind_auction(name,bid):
  auction_database = {}
  auction_database['name'] = name
  auction_database['bid'] = bid
  
  database.append(auction_database)

blind_auction(name=user_name, bid=user_bid)

run = True
while run:
  ask_other_bid = input("Are there any other bidders? Type 'yes' or 'no'  ").lower()
  if ask_other_bid == 'yes':
    clear()
    new_bidder_name = input('What is your name?: ')
    new_bidder_bid = int(input('What\'s your bid?: $'))
    blind_auction(name=new_bidder_name, bid=new_bidder_bid)
  elif ask_other_bid == 'no':
    run = False

winner = max(database, key=lambda x: x['bid'])
clear()
print(f'The winner is {winner["name"]} with a bid of ${winner["bid"]}.')


