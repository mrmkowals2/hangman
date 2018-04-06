import random

words = ["pink"
         ,"band"
         ,"plough"
         ,"smoke"
         ,"cheese"
         ,"miniature"
         ,"tomohawk"
         ,"friendship"
         ,"zest"
         ,"time"
         ,"weird"
         ,"stop"
         ,"whipped"
         ,"president"
         ,"nails"
         ,"tinkle"
         ,"worship"
         ,"twist"
         ,"topple"
         ,"country"
         ,"teenager"
         ,"asphalt"
         ,"music"]

def hangman(word):
    wrong = 0
    stages =  [""
              ,"________        "
              ,"|       |       "
              ,"|       O       "
              ,"|      /|\      "
              ,"|      / \      "
              ,"|_______________"
              ,"|              |"]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "__" not in board:
            print("\n")
            print("You win!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong + 1]))
        print("\n")
        print("You lose! The word was {}.".format(word))

word_list_len = len(words)
randnum = random.randint(0,word_list_len-1)
hangman(words[randnum])
