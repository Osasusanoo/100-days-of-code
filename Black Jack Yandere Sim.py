import random
from art import logo,animeart

cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#Making a function to draw cards
def draw(player):
    player.append(random.choice(cards))

#Get the sum of cards
def total(player):
    acedetecter=False
    cardsum=0
    for x in player:
        cardsum+=x
        if x==11:
            acedetecter=True
    if cardsum>=22 and acedetecter==True:
        cardsum-=10

    return cardsum
#Checking the winner and giving the final result
def finalcheck(player1,player2):
    if (total(player1)>21):
        print("You went over. You lose Baka😭")
    elif total(player2)>21:
        print("CPU went over. You won (tsk)")
    elif total(player1)==total(player2):
        print("Its a draw senpai")
    elif total(player2)>total(player1):
        print("You lost womp womp")
    else:
        print("SUGOIIII, You won Senpai!")

def game():
    # Setting the starting deck
    print(logo)
    playerhand=[]
    CPUhand=[]
    
    draw(playerhand)
    draw(playerhand)
    playersize=total(playerhand)
    print(f"Your cards: {playerhand}, current score is {playersize}")
    if total(playerhand)==21:
        print("You Got A Black Jack onee-san! ")
        return
    draw(CPUhand)
    print(f"The Cpu first card is {CPUhand[0]} ")
    draw(CPUhand)
    drawagain= input("Type 'y' to get another card, type 'n' to pass: ")
    while drawagain=='y':
        draw(playerhand)
        if total(playerhand)>21:
            break
        else:
            print(f"Your cards: {playerhand}, current score is {total(playerhand)}")
            drawagain=input("do you want to draw another card? ")
    if total(CPUhand)==21:
        print("CPU hit that a black jack")

    if total(playerhand)<22:
        while total(CPUhand) < 14:
            draw(CPUhand)
    print(f"Your final hand: {playerhand}, final score: {total(playerhand)}")
    print(f"Computer's final hand: {CPUhand}, final score: {total(CPUhand)}")
    finalcheck(playerhand, CPUhand)
    return



#Initiating the program
startgame=input("Do you want to play a game of Blackjack Baka? Type 'y' or 'n': ")
while (startgame=='y'):
    game()
    startgame = input("Do you want to play a game of Blackjack Baka? Type 'y' or 'n': ")
    print("\n"*20)
else:
    print("Goodbye baka")
    print(animeart)
