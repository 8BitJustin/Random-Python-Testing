table = 0

def start():
    print('Welcome!')
    global gold
    gold = 0
    lobby()


def prompt():
    x = input('Type a command: ')
    return x


def current_gold():
    global gold
    print('Current gold is: ' + str(gold))


def lobby():
    global gold
    print('You are in the lobby.')
    command = prompt()
    if command.lower() == 'north':
        bedroom()
    elif command.lower() == 'gold':
        current_gold()
        lobby()
    else:
        lobby()


def bedroom():
    global gold
    global table
    print('You are in the bedroom.')
    command = prompt()
    if command.lower() == 'south':
        lobby()
    elif command.lower() == 'bed':
        print('You go to the bed and find nothing.')
        bedroom()
    elif command.lower() == 'table':
        if table == 0:
            print('You go to the table and find 50 gold.')
            gold = gold + 50
            table = 1
        else:
            print('There is nothing else here.')
        bedroom()
    elif command.lower() == 'gold':
        current_gold()
        bedroom()
    else:
        bedroom()

start()
