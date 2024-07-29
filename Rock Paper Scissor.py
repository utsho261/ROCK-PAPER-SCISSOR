import random
import time


GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'

colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN]

def print_welcome_message():

    for _ in range(2):
        for color in colors:
            print(f"\r{color}        WELCOME TO ROCK PAPER SCISSOR{RESET}", end='', flush=True)
            time.sleep(0.1)
    print(f"\r        WELCOME TO ROCK PAPER SCISSOR")


print_welcome_message()

Wcount = 0
Lcount = 0
Dcount = 0

print("")
name = input("        Enter Your Name: ").upper()
n = int(input(f"        Hey {name}! How Many Times Do You Want To Play: "))
print("")
print(f"        OK, Let's Play The Game")
print("")
A = ["1. Rock","2. Paper","3. Scissor"]
for _ in range(n):
    print("")
    print("                ROCK PAPER SCISSOR")
    print("                 \033[96m_______________\033[0m")
    print("                 \033[96m|\033[0m  \033[95m1. Rock\033[0m    \033[96m|\033[0m")
    print("                 \033[96m|\033[0m  \033[95m2. Paper\033[0m   \033[96m|\033[0m")
    print("                 \033[96m|\033[0m  \033[95m3. Scissor\033[0m \033[96m|\033[0m")
    print("                 \033[96m|_____________|\033[0m")
    print("")

    while True:
        x = int(input(f"        {name}, Choose any number between 1 to 3: "))
        print("")
        if 1 <= x <= 3:
            break
        else:
            print(RED + "            Invalid Choice" + RESET)
            print(RED + f"            {name}! Please Enter a number between 1 to 3" + RESET)
            print("")


    if 1 <= x <= 3:
        print("            You Select      :",A[x-1])
        y = random.randint(1,3)
        print("            Computer Select :",A[y-1])

        print("")

        if x == 1 and y == 2:
            print("            Game Result: ", end="")
            print("\033[91mComputer Have Won The Game\033[0m")
            Lcount += 1


        elif x == 1 and y == 3:
            print("            Game Result: ", end="")
            print(f"\033[92mYou Have Won The Game\033[0m ")
            Wcount += 1

        elif x == 2 and y == 1:
            print("            Game Result: ", end="")
            print(f"\033[92mYou Have Won The Game\033[0m ")
            Wcount += 1

        elif x == 2 and y == 3:
            print("            Game Result: ", end="")
            print("\033[91mComputer Have Won The Game\033[0m")
            Lcount += 1

        elif x == 3 and y == 1:
            print("            Game Result: ", end="")
            print("\033[91mComputer Have Won The Game\033[0m")
            Lcount += 1

        elif x == 3 and y == 2:
            print("            Game Result: ", end="")
            print(f"\033[92mYou Have Won The Game\033[0m ")
            Wcount += 1

        else:
            print("            Game Result: ", end="")
            print("\033[93mGame Draw\033[0m")
            Dcount += 1

        print("    \033[90m<----------------------------------------->\033[0m")
        print("")


print(f"Number of wins: {Wcount}")
print(f"Number of losses: {Lcount}")
print(f"Number of Draws: {Dcount}")
print(f"So Final Winner is " f"{YELLOW + 'No One' + RESET if Wcount == Lcount else (f'{GREEN}{name}{RESET}' if Wcount > Lcount else f'{RED}Computer{RESET}')}.")
