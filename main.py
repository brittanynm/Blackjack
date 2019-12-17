
from random import choice
import random
import time

deck = {
    'Ace of Spades':11,
    '2 of Spades':2, 
    '3 of Spades':3,
    '4 of Spades':4, 
    '5 of Spades':5, 
    '6 of Spades':6,
    '7 of Spades':7, 
    '8 of Spades':8, 
    '9 of Spades':9,
    '10 of Spades':10, 
    'Jack of Spades':10,
    'Queen of Spades':10, 
    'King of Spades': 10,
    
    'Ace of Hearts':11, 
    '2 of Hearts':2, 
    '3 of Hearts':3,
    '4 of Hearts':4, 
    '5 of Hearts':5, 
    '6 of Hearts':6,
    '7 of Hearts':7, 
    '8 of Hearts':8, 
    '9 of Hearts':9,
    '10 of Hearts':10, 
    'Jack of Hearts':10,
    'Queen of Hearts':10, 
    'King of Hearts': 10,
    
    'Ace of Clubs':11, 
    '2 of Clubs':2, 
    '3 of Clubs':3,
    '4 of Clubs':4, 
    '5 of Clubs':5, 
    '6 of Clubs':6,
    '7 of Clubs':7, 
    '8 of Clubs':8, 
    '9 of Clubs':9,
    '10 of Clubs':10, 
    'Jack of Clubs':10,
    'Queen of Clubs':10, 
    'King of Clubs': 10,
    
    'Ace of Diamonds':11, 
    '2 of Diamonds':2, 
    '3 of Diamonds':3,
    '4 of Diamonds':4, 
    '5 of Diamonds':5, 
    '6 of Diamonds':6,
    '7 of Diamonds':7, 
    '8 of Diamonds':8, 
    '9 of Diamonds':9,
    '10 of Diamonds':10, 
    'Jack of Diamonds':10,
    'Queen of Diamonds':10, 
    'King of Diamonds': 10
}
def prints_greeting():
    """Prints introductory greeting"""
    print()
    print("Let's 👏  play 👏  Blackjack!")
    print()
    time.sleep(1)

def deal_card():
    card_keys = list(deck.keys()) #generates a list of keys in the dict
    new_card = random.choice(card_keys) #store face card to show user
    
    return new_card

def check_ace(player_total, sum_of_p_total):
    if sum_of_p_total > 21:
        for idx, num in enumerate(player_total):
            if num == 11:
                player_total[idx] = 1
                return player_total
    else:
        return False    

def check_21_or_bust(sum_of_p_total, player_total):
    if sum_of_p_total > 21:
        print("")
        print(" ❌  💀  Busted 💀  ❌ ")
        time.sleep(2)
        print()
        return True
    elif sum_of_p_total == 21 and len(player_total) == 2:
        print()
        print(" ♠️ ♥️ ♣️ ♦️ ♠️ ♥️ ♣️ ♦️ ♠️ ♥️ ♣️ ♦️ ")
        print("      Blackjack! Woo!")
        print(" ♠️ ♥️ ♣️ ♦️ ♠️ ♥️ ♣️ ♦️ ♠️ ♥️ ♣️ ♦️ ")
        time.sleep(2)
        print()
        return True        
    elif sum_of_p_total == 21:
        print()
        print("Nice -- 21! Woo!")
        time.sleep(2)
        print()
        return True

def check_winner(sum_of_p_total, sum_of_d_total):
    print(" - You ended the game with", sum_of_p_total, "vs. Dealer at", sum_of_d_total, "-")
    print()
    if sum_of_d_total > 21 and sum_of_p_total > 21:
        print("You both busted.")
        print()    
    elif sum_of_d_total == sum_of_p_total:
        print("😮  WOW - a tie! Play another game to see who wins  😈")
        print()
    elif sum_of_d_total <= 21 and sum_of_p_total <= 21 and sum_of_d_total > sum_of_p_total:
        print("💰  Dealer wins. 💰")
        print()
    elif sum_of_d_total <= 21 and sum_of_p_total > 21:
        print("💰  Dealer wins. 💰")
        print()       
    elif sum_of_p_total <= 21 and sum_of_d_total <= 21 and sum_of_p_total > sum_of_d_total:
        print("🎉 🎉 🎉 🎉 🎉 🎉  You win!  🎉 🎉 🎉 🎉 🎉 🎉")
        print()
    elif sum_of_p_total <= 21 and sum_of_d_total > 21:
        print("🎉 🎉 🎉 🎉 🎉 🎉  You win!  🎉 🎉 🎉 🎉 🎉 🎉")
        print()   

def main():
    prints_greeting()

    while True:
        player_hand = [] #face cards to show user their hand
        player_total = [] #values of cards in hand

        new_card = deal_card() 
        player_hand.append(new_card) #add to list to show player
        new_card_value = deck[new_card] #get the value for that key
        player_total.append(new_card_value) #adds value to list
        deck.pop(new_card) #remove card from deck

        card_2 = deal_card()
        player_hand.append(card_2) #add to list to show player
        card2_value = deck[card_2] #get the value for that key
        player_total.append(card2_value) #adds value to list
        deck.pop(card_2) #remove card from deck

        while True:
            sum_of_p_total = sum(player_total) #single int to show hand total

            print("Your hand:")
            print()
            for card in player_hand:
                print(">", card)
            print()
            if check_ace(player_total, sum_of_p_total) == True:
                return player_total
            sum_of_p_total = sum(player_total) #single int to show hand total
            print(sum_of_p_total, "is your total")

            if check_21_or_bust(sum_of_p_total, player_total) == True:
                break
            print()
            hit_stay = input("Would you like to [h]it or [s]tay? > ")
            hit_stay = hit_stay.lower()

            if hit_stay.startswith('h'):
                print()
                card = deal_card()
                print("🂡 🂣 🂥 >>>", card)
                player_hand.append(card) #add to list to show player
                card_value = deck[card] #get the value for that key
                player_total.append(card_value) #adds value to list
                deck.pop(card) #remove card from deck
                time.sleep(1)#wait a second to reveal full hand
            elif hit_stay.startswith('s'):
                print()
                print()
                break
            else:
                print("❌  Please choose hit or stay   ❌ ")

            
        print("Dealer's turn . . . ")
        print()
        time.sleep(1)
        dealer_hand = []
        dealer_total = []
        sum_of_d_total = sum(dealer_total)

        c1 = deal_card() 
        dealer_hand.append(c1) #add to list to show player
        c1_value = deck[c1] #get the value for that key
        dealer_total.append(c1_value) #adds value to list
        deck.pop(c1) #remove card from deck

        c2 = deal_card()
        dealer_hand.append(c2) #add to list to show player
        c2_value = deck[c2] #get the value for that key
        dealer_total.append(c2_value) #adds value to list
        deck.pop(c2) #remove card from deck

        while True:
            sum_of_d_total = sum(dealer_total)

            print("Dealer's hand:")
            print()
            for card in dealer_hand:
                print(">", card)
            print()
            if check_ace(dealer_total, sum_of_d_total) == True:
                return dealer_total
            sum_of_d_total = sum(dealer_total) #single int to show hand total
            print("Dealer is at", sum_of_d_total)

            if check_21_or_bust(sum_of_d_total, dealer_total) == True:
                break
            # print()
            time.sleep(1)
            if sum_of_d_total <= 16:
                print()
                time.sleep(4)
                card = deal_card()
                print("🂡 🂣 🂥 >>>", card)
                dealer_hand.append(card) #add to list to show player
                card_value = deck[card] #get the value for that key
                dealer_total.append(card_value) #adds value to list
                deck.pop(card) #remove card from deck
                time.sleep(1)#wait a second to reveal full hand
            elif sum_of_d_total > 16:
                time.sleep(1)
                print()
                print(" - Dealer ended the game with", sum_of_d_total, "-")
                print()
                time.sleep(2)
                break
        check_winner(sum_of_p_total, sum_of_d_total)
        time.sleep(2)
        exit = input("Press Enter for a new game or [q] to quit. ").lower()
        print("------------------------------------------")
        if 'q' in exit:
            print()
            print("Game has ended.")
            break
        print()

main()
