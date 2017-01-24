def game_start():
    """Main game method. """
    pass


def generate_deck():
    """Generates 52 card deck, card values 1-10, and 12 face cards"""
    pass


def draw_card():
    pass


def ai_draw_card():
    pass


def game_end():
    pass


def user_prompt():
    print ("Hit or Stand?")
    x = raw_input("")
    print x.lower()
    if "hit" in x.lower():
        draw_card()
        print("You hit")
    elif x.lower() is "stand":
        draw_card()
        print("you stood")
    else:
        print("yo momma type better than u")
    return
