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

print("Welcome to Rock Paper Scissors!")
x = int(input("choose 0 for rock,1 for paper and 2 for scissors\n"))
n = random.randint(0,2)
a = [rock,paper,scissors]
print(f"computer chose {n}")
if x == n:
    print("DRAW!")
    print(f"you choose {a[x]}"
          f"computer chose {a[n]}")
elif  x == 0 and n == 1:
    print(f"you chose rock {rock}\n"
          f"computer chose paper{paper}")
    print(" You lose")
elif x == 0 and n == 2:
    print(f"you chose rock {rock}\n"
          f"computer chose scissors {scissors}")
    print("You win")
elif x == 1 and n == 0:
    print(f"you chose paper {paper}\n"
          f"computer chose rock {rock}")
    print("You win")
elif x == 1 and n == 2:
    print(f"you chose paper {paper}\n"
          f"computer chose scissors {scissors}")
    print("You lose")
elif x == 2 and n == 0:
    print(f"you chose scissors {scissors}\n"
          f"computer chose rock {rock}")
    print("You lose")
elif x == 2 and n == 1:
    print(f"you chose scissors{scissors}\n"
          f"computer chose paper {paper}")
    print("You win")
else:
    print("invalid choice")

