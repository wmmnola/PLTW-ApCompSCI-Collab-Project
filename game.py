
deck = []
ai_hand = []
player_hand = []
# When a card is drawn, it will be spliced from the deck array, and then
# appended into the appropriate hand


def game_debug():
    """Debug method for checking  functions"""
    # the start()function is NOT TO BE CALLED FROM THIS FUNCTION!!!!!!!!!!!
    user_prompt()


def game_start():
    """Main game method. """
    # TODO make the stupid game
    pass


def generate_deck():
    """Generates 52 card deck, card values 1-10, and 12 face cards"""
    # TODO implement generation technique for cards
    pass


def draw_card():
    # TODO implement logic to append a random card from deck to a hand
    # TODO encapsulate this function under one draw_card() function
    pass


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
