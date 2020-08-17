import itertools
from colorama import Fore, Back, Style, init
init()

def play_field(play_map, play=0, row1=0, col=0, just_display=False):
    try:
        if play_map[row1][col] != 0:
            print("Position already occupied, choose another")
            return play_map, False

        print("   "+"  ".join([str(i) for i in range(len(play_map))]))
        if not just_display:
            play_map[row1][col] = play


        for count, row in enumerate(play_map):
            clrrow = ""
            for item in row:
                if item == 0:
                    clrrow += "|  "
                elif item == 1:
                    clrrow += Fore.GREEN + '|X ' + Style.RESET_ALL
                elif item == 2:
                    clrrow += Fore.MAGENTA + '|O ' + Style.RESET_ALL
            print(count, clrrow)

        return play_map, True
    except IndexError as e:
        print("Put valid input for row and col: ", e)
        return play_map, False
    except Exception as e:
        print("something is wrong: ", e)
        return play_map, False

# for finding out winner


def win(tic):
    def all_comp(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
    # horizontal
    for row in tictac:
        # print(row)
        if all_comp(row):
            print(f"player {row[0]} is winner horizontally(-)!!")
            return True

    # diagonal:
    dia = []
    for col, row in enumerate(reversed(range(len(tictac)))):
        dia.append(tictac[row][col])
    if all_comp(dia):
        print(f"player {dia[0]} is winner diagonally(/)!!")
        return True

    dia = []
    for i in range(len(tictac)):
        dia.append(tictac[i][i])
    if all_comp(dia):
        print(f"player {dia[0]} is winner diagonally(\\)!!")
        return True

    # vertical:
    for col in range(len(tictac)):
        check = []

        for row in tictac:
            check.append(row[0])

        if all_comp(check):
            print(f"player {check[0]} is winner vertically(|)!!")
            return True

    return False


play1 = True
players = [1, 2]
while play1:
    size = int(input("what size of tic tac toe do you want?"))
    tictac = [[0 for i in range(size)] for j in range(size)]
    tic_won = False
    tictac, _ = play_field(tictac, just_display=True)
    choice = itertools.cycle([1, 2])
    while not tic_won:
        current = next(choice)
        print(f"current player: {current}")
        played = False
        while not played:
            col_c = int(input("choose column (0, 1, 2): "))
            row_c = int(input("choose row (0, 1, 2): "))
            tictac, played = play_field(tictac, current, row_c, col_c)

        if win(tictac):
            tic_won = True
            again = input("Wanna play another match?(y/n)")
            if again.lower() == "y":
                print("restarting")
            elif again.lower() == "n":
                print("Thanks for playing")
                play1 = False
            else:
                print("Invalid input. bye.")
                play1 = False
