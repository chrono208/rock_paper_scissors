import random 

def RockPaperScissors():
    print("Hello friend.")
    name = input("What is your name?\n")
    print("Well, hello " + name)
    print("Let's play some Rock, Paper, Scissors!!")
    print("We will play three rounds.\n\n")
    count = 0
    while count != 3:
        compNumber = random.randint(1, 3)
        if compNumber == 1:
            compSelection = "Rock"
        elif compNumber == 2:
            compSelection = "Paper"
        else:
            compSelection = "Scissors"
        print("Pick one: Rock, Paper, or Scissors")
        playerSelection = input()
        if playerSelection == compSelection:
            print("That was a draw! Nice Try!\n\n")
        elif playerSelection == "Rock":
            if compSelection == "Paper":
                print("You lose!!\n\n")
            elif compSelection == "Scissors":
                print("You win!!\n\n")
        elif playerSelection == "Paper":
            if compSelection == "Scissors":
                print("You lose!!\n\n")
            elif compSelection == "Rock":
                print("You win!!\n\n")
        else:
            if compSelection == "Rock":
                print("You lose!!\n\n")
            elif compSelection == "Paper":
                print("You win!!\n\n")
        count = count + 1
    print("Thanks for playing!\n\n")