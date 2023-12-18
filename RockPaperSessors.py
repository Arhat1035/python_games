import random

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


images = (rock, paper, scissors)

ask = int(input("What do you choose? Type 0 for rock, 1 for Paper or 2 for scissors"))
print(images[ask])

computer = random.randint(0, 2)
print("computer Choose")
print(images[computer])

if ask == computer:
    print("It is a tie")
elif ask == 0 and computer == 2:
    print("You Win")
elif ask == 0 and computer == 1:
    print("You Lose")
elif ask == 1 and computer == 0:
    print("You win")
elif ask == 1 and computer == 2:
    print("you Lose")
elif ask == 2 and computer == 1:
    print("You win")
elif ask == 2 and computer == 0:
    print("You Lose")
else:
    print("There is an error. Pls re try")
