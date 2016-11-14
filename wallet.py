wallet = 15

def buy_game():
    """Silly script to indicate to buy a game if the funds in wallet were avail."""
    if wallet >= 13.37:
        print('Im\'ma get that game!')
    else:
        print('Gotta get money to get that game!')

buy_game()