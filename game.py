import card
import random

ai_hand = []
player_hand = []
# When a card is drawn, it will be spliced from the deck array, and then
# appended into the appropriate hand


def game_debug():
    """Debug method for checking  functions"""
    # the start()function is NOT TO BE CALLED FROM THIS FUNCTION!!!!!!!!!!!
    # user_prompt()
    deck = generate_deck()
    draw_card(player_hand, deck)



def game_start():
    """Main game method. """
    # TODO make the stupid game
    pass


def generate_deck():
    """Generates 52 card deck, card values 1-10, and 12 face cards"""
    deck = []
    for x in range(0, 52):
        deck.append(card.Card(x, (x % 13)+1))
        deck[x].get_real_value()
        # print(deck[x].real_value)
    return deck

def hand_sum(hand):
    sum = 0
    for card in hand:
        sum = sum + card.real_value
    return sum

def draw_card(hand, deck):
    # TODO implement logic to append a random card from deck to a hand
    # TODO encapsulate this function under one draw_card() function
    size = len(deck)-1
    index = random.randint(0,size)
    card = deck[index]
    del deck[index]
    hand.append(card)
    return hand


def ai_draw_card():
    # TODO encapsulate this function under one draw_card() function
    pass


def game_end():
    # TODO determine if we need a game_end() function, wouldnt a return work?

    pass


def user_prompt():
    """prompts the user wether they want another card or not"""
    # TODO properly implement the game logic for this
    print("Hit or Stand?")
    x = raw_input("")
    print(x.lower())
    if "hit" in x.lower():
        draw_card()
        print("You hit")
    elif x.lower() is "stand":
        draw_card()
        print("you stood")
    else:
        print("yo momma type better than u")
    return
