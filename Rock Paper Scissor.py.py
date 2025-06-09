from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# thriple quote allows multiple lines of code

AIchoice=randint(0,2)
playerchoice=input("What do you pick? 0, 1 or 2 for rock, paper and scissors respectively? ")
while True:
    try:
        playerchoice = int(playerchoice)

        if playerchoice not in [0, 1, 2]:
            playerchoice = input("Wrong input Ba-Baka ")
        else:
            break
    except ValueError:
        playerchoice=input("Enter the a number Senpai :C ")
choices=[rock,paper,scissors]
playerchoice=int(playerchoice)
print(choices[playerchoice])
print("computer choice: ")
if AIchoice==0:
    print(rock)
elif AIchoice==1:
    print(paper)
else:
    print(scissors)

if AIchoice==playerchoice:
    print("Its a draw")
elif AIchoice-playerchoice==1:
    print("Junior wins")
elif AIchoice-playerchoice==2:
    print("Oppa Wins")
elif AIchoice-playerchoice==-1:
    print("Oppa wins")
elif AIchoice-playerchoice==-2:
    print("Junior Wins")

else:
    print("bad input")
