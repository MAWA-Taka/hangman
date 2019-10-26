
def hangman(word):
    wrong = 0
    stages =    ["",
                 "________        ",
                 "|       |       ",
                 "|       |       ",
                 "|       o       ",
                 "|      /|\      ",
                 "|      / \      ",
                 "|               "
                 ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンにようこそ！")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね"
        char = input(msg)
        while len(char) != 1 or char not in "abcdefghijklmnopqrstuvwxyz":
            msg = "入力は英小文字1文字だけだよ"
            char = input(msg)

        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1

        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は {}。".format(word))

import random
animals_list = ["cat", "dog", "lion"]
list_len = len(animals_list)
hangman(animals_list[random.randint(0, list_len - 1)])
