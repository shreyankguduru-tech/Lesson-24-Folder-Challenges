TheBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' '}

boardKeys = []

for key in TheBoard:
    boardKeys.append(key)


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])



def game():

    turn = 'x'
    count = 0

    for i in range(10):
        printBoard(TheBoard)
        print("its your turn," + turn + ".move to which place?")

        move = input()

        if TheBoard[move] == ' ':
            TheBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        if count >= 5:
            if TheBoard['7'] == TheBoard['8'] == TheBoard ['9'] != ' ': 
                printBoard(TheBoard)
                print("\nGame over.\n")
                print("****" + turn + "won. ****")
                break
            elif TheBoard['4'] == TheBoard['5'] == TheBoard['6']!= ' ': 

                printBoard(TheBoard)
                print("\nGame Over.\n")
                print("****" + turn + "won, ****")
                break
            elif TheBoard['1'] == TheBoard['2'] == TheBoard['3'] != ' ':
                printBoard(TheBoard)
                print("\nGame over.\n")
                print("****" + turn + "won. ****")
                break

            elif TheBoard['1'] == TheBoard['4'] == TheBoard ['7'] != ' ': 
                            printBoard(TheBoard)
                            print("\nGame over.\n")
                            print("****" + turn + "won. ****")
                            break
            elif TheBoard['7'] == TheBoard['5'] == TheBoard ['3'] != ' ': 
                            printBoard(TheBoard)
                            print("\nGame over.\n")
                            print("****" + turn + "won. ****")
                            break
            elif TheBoard['1'] == TheBoard['5'] == TheBoard ['9'] != ' ': 
                            printBoard(TheBoard)
                            print("\nGame over.\n")
                            print("****" + turn + "won. ****")
                            break
            elif TheBoard['7'] == TheBoard['5'] == TheBoard ['3'] != ' ': 
                            printBoard(TheBoard)
                            print("\nGame over.\n")
                            print("****" + turn + "won. ****")
                            break
            elif TheBoard['1'] == TheBoard['5'] == TheBoard ['9'] != ' ': 
                            printBoard(TheBoard)
                            print("\nGame over.\n")
                            print("****" + turn + "won. ****")
                            break
        if count ==9:
                print("\nGame over.\n")
                print("its a Tie")

        if turn == 'x':
                turn = "O"
        else:
            turn = 'x'


    restart = input("do you want to play again? (y/n)")
    if restart == "y" or restart =="Y":
            for key in boardKeys:
                    TheBoard[key] = " "

            game()
if __name__ == "__main__":
        game()



        