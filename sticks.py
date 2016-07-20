def take_sticks(player_turn):
    pick = input("{}: How many sticks do you take (1-3)? ".format(player_turn))
    try:
        pick = int(pick)
    except ValueError:
        print("Please enter a number between 1 and 3")
        return take_sticks(player_turn)
    if pick < 1 or pick > 3:
        print("Please enter a number between 1 and 3")
        return take_sticks(player_turn)
    else:
        return

def change_counter(counter, pick):
    counter -= pick
    print("There are now {} sticks on the board".format(counter))
    return counter

def win_or_lose(counter):
    if counter <= 0:
        print("{}, you win!".format(player_turn))
    else:
        return

def change_turn(opponent):
    return opponent[::-1]

def choose_sticks():
    number_of_sticks = int(input("How many stick would you like to start with on the table (10 -100): "))
    if number_of_sticks >= 10 and number_of_sticks <= 100:
        return number_of_sticks
    else:
        print("Please enter a number number between 10 and 100.")
        return choose_sticks()

def choose_opponent():
    opponent = input("Play against friend (1)\nPlay against the computer (2)\nWhich do you choose (1-2): ")
    if opponent == '1':
        return ['Player 1', 'Player 2']
    elif opponent == '2':
        return ['Human', 'Computer']

def main():
    print("Welcome to the game of sticks! Don't be the one to pick up the last stick")
    counter = choose_sticks()
    opponent = choose_opponent()
    print("There are {} sticks on the board".format(counter))
    while counter > 1:
        player_turn = opponent[0]
        opponent = change_turn(opponent)
        pick = take_sticks(player_turn)
        change_counter(counter, pick)
        win_or_lose(counter)


if __name__ == '__main__':
    main()
