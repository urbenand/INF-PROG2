import random


# main game
def main():
    # define variables
    min_size = 10  # min stack size
    max_size = 20  # max stack size
    winner = None  # define winners
    current_player = None  # define current player
    current_round = 1
    match_count = 0  # count how many matches already drawn

    # randomly define stack size
    stack_size = random.randint(min_size, max_size)

    # initialize remaining size
    stack_remaining_size = stack_size

    # Print intro and rules
    print("Welcome to draw-a-match.")
    print("Rules: The stack has a random size.")
    print("Each turn you have to choose between 1 or 3 matches to remove from the stack.")
    print("The player that draws the last match loses the game.")

    input("Press enter to start")
    print(f"The stack has {stack_size} matches.")

    # define start player
    current_player = define_starter()
    print(f"{translate_currentplayer(current_player)} starts.")

    # while winner is not defined, game goes on
    while winner is None:
        match_amount = 0

        # make player/computer turns
        if current_player == 1:
            match_amount = user_turn()
            current_player = 2
        elif current_player == 2:
            match_amount = computer_turn(current_round, stack_size, stack_remaining_size)
            current_player = 1

        # update stack size and current round (needed for computer strategy)
        stack_remaining_size -= match_amount
        current_round += 1

        # print remaining stack
        print_match(stack_remaining_size)
        print(f"The stack has {stack_remaining_size} matches left.")

        # if stack size is equal or less than 0, player loses
        if stack_remaining_size <= 0:
            winner = current_player

    # Print winner
    print(f"{translate_currentplayer(current_player)} wins.")


# user turn
def user_turn():
    user_turn_valid = None
    while user_turn_valid is None:
        user_draw = input("How many matches? (1-3): ")

        # catch non numeric values
        if user_draw.isnumeric():
            user_draw = int(user_draw)
            if user_draw in range(1,4):
                user_turn_valid = True
                return user_draw
            else:
                print("Please choose a value between 1 and 3!")
        else:
            print("Please choose a value between 1 and 3!")


# computer turn with strategic content
def computer_turn(current_round, stack_size, stack_remaining_size):
    computer_draw = 0

    if current_round in range(1,3):
        computer_draw = 3
    elif current_round <= 3 and stack_size >= 10:
        computer_draw = 3
    elif current_round > 2 and stack_remaining_size > 3:
        computer_draw = 3
    else:
        computer_draw = 1

    return computer_draw


# print match
def print_match(amount):
    for i in range(amount):
        print("=======O")


# define start player
def define_starter():
    starter = random.randint(1,2)
    return starter


# translate current player from numeric into readable
def translate_currentplayer(current_player):
    translated_name = ""

    if current_player == 1:
        translated_name = "Player 👤"
    elif current_player == 2:
        translated_name = "Computer 🤖"

    return translated_name


# call main function
main()
