import random
import cv2
import time



# clear screen object
def clear():
    print("\n" * 6)


# rock,paper, scissors object
def rock():

    rock_img = cv2.imread("Rock.jpg", 0)
    cv2.imshow("Rock", rock_img)
    cv2.waitKey(500)
    cv2.destroyAllWindows()


def paper():

    paper_img = cv2.imread("Paper.jpg", 0)
    cv2.imshow("Paper", paper_img)
    cv2.waitKey(500)
    cv2.destroyAllWindows()


def scissors():

    scissors_img = cv2.imread("Scissors.jpg", 0)
    cv2.imshow("Scissors", scissors_img)
    cv2.waitKey(500)
    cv2.destroyAllWindows()


userInput = input("Would you like to play? [y,n] \n")

while userInput == "y":
    clear()

# input option for player
    selected_option = input("Select rock, paper, scissors \n")
# list of options
    userList = ["rock", "paper", "scissors"]

    userListStr = (str(userList))

    clear()
# compare input with list
    if selected_option in userListStr:
        print("You selected: ", selected_option)
    else:
        print(" Please select an option from the list", userList)

    # convert input string to int
    if selected_option == 'rock':
        selected_option2 = int(1)
    elif selected_option == 'paper':
        selected_option2 = int(2)
    elif selected_option == 'scissors':
        selected_option2 = int(3)

# variable change
    computerList = [1, 2, 3]

# random selection of choices for cpu
    y = random.choice(computerList)

# change int to str
    if y == 1:
        computerList = "rock"
    elif y == 2:
        computerList = "paper"
    elif y == 3:
        computerList = "scissors"

# cpu selection display
    if y == 1:
        print("computer selected Rock")
        rock()

    elif y == 2:
        print("Computer selected Paper")
        paper()
    else:
        print("Computer selected Scissors")
        scissors()


# compare player input with cpu
    if selected_option == computerList:
        print("draw")
    elif selected_option != computerList:
        if selected_option == "rock" and computerList == "scissors":
            print("you win")
        elif selected_option == 'scissors' and computerList == "paper":
            print("you win")
        elif selected_option == 'paper' and computerList == 'rock':
            print("you win")
        else:
            print("you lose")

    clear()

    userInput = input(str("would you like to play again?"))

    time.sleep(10000)

    clear()

else:

    print("thanks for playing")

    time.sleep(10000)

    exit()
