import card
import random



# When a card is drawn, it will be spliced from the deck array, and then
# appended into the appropriate hand


def game_debug():
    """Debug method for checking  functions"""
    # the start()function is NOT TO BE CALLED FROM THIS FUNCTION!!!!!!!!!!!
    # user_prompt()



def game_start():
    """Main game method. """
    # TODO make the stupid game
    running = True
    deck = generate_deck()
    ai_hand = []
    player_hand = []
    player_hand = draw_card(player_hand, deck, 2);
    ai_hand = draw_card(ai_hand, deck, 2);

    while(running):
        oldLen = len(player_hand)
        player_hand = user_prompt(player_hand, deck)
        ai_hand = ai_logic(ai_hand, deck)
        if(len(player_hand) == oldLen):
            running = False
    if(compare(player_hand, ai_hand) == True):
        print("You Win")
    else:
        print("You loose")


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

def ai_logic(ai_hand, deck):
    if(hand_sum(ai_hand) < 15):
        ai_hand = draw_card(ai_hand, deck, 1)
    return ai_hand

def draw_card(hand, deck, number_cards):
    for x in range(0, number_cards):
        size = len(deck)-1
        index = random.randint(0, size)
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


def display_hand(hand):
    """Takes a hand array, returns a string to be printed"""
    str_hand = ""
    for x in hand:
        str_hand += "%s " % x.real_value
    return str_hand

def compare(player_hand, ai_hand):
    """compares hands False means the player lost. True means the player won"""
    msg = "Your hand: %s, Ai_hand: %s" % (hand_sum(player_hand), hand_sum(ai_hand))
    print(msg)
    if hand_sum(player_hand) > 21:
        return False
    elif hand_sum(ai_hand) > 21:
        print("Ai Busted")
        return False
    elif hand_sum(player_hand) < hand_sum(ai_hand):

        return False
    elif hand_sum(player_hand) > hand_sum(ai_hand): return True
    else: main.panic()

def printHand(hand):
    s = "Hand: "
    for card in hand:
        s += "%s " % card.real_value
    print(s)
    return
def user_prompt(hand,deck):
    """prompts the user wether they want another card or not"""
    # TODO properly implement the game logic for this
    printHand(hand)
    print("Hit or Stand?")
    x = raw_input("")
    if "hit" in x.lower():
        hand = draw_card(hand, deck, 1)
        print("You hit")
        printHand(hand)
    elif x.lower() in "stand":
        return hand
    else:
        print("error retype command")
        user_prompt(hand, deck)
    return hand
