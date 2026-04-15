#Akmens šķēres papīrītis datorspēle

import random
from time import sleep
from os import system

datora_izveles = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""","""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""","""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""]
dators = random.choice(datora_izveles)


#ASCII formas
akmens = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

skeres = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

papirs = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

print("~~~~~~~~~~Akmens šķēres papīrītis!~~~~~~~~~~")
print("Akmens = R | Šķēres = S | Papīrs = P")

sleep(1)




izvele = input("Kādu priekšmetu jūs izvēlēsieties?").upper()

loading = "Loading"
for i in range(4):
    print(loading)
    sleep(1)
    system('cls')
    loading += "."


#spēle, ja spēlētājs izvēlas papīru
if izvele == "P":
    print(f"Jūs izvēlējāties: {papirs}")
    sleep(2)
    print("Dators izvēlējās: ", dators)
    if dators == """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""":
        sleep(2)
        print("Neizšķirts!")
    elif dators == """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""":
        sleep(2)
        print("Jūs uzvarējāt! Apsveicu!")
    else:
        sleep(2)
        print("Jūs zaudējāt :( Vēlu veiksmi nākamajā mēģinājumā!")


#spēle, ja spēlētājs izvēlās šķēres
if izvele == "S":
    print(f"Jūs izvēlējāties: {skeres}")
    sleep(2)
    print("Dators izvēlējās: ", dators)
    if dators == """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""":
        sleep(2)
        print("Jūs uzvarējāt! Apsveicu!")
    elif dators == """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""":
        sleep(2)
        print("Jūs zaudējāt :( Vēlu veiksmi nākamajā mēģinājumā!")
    else:
        sleep(2)
        print("Neizšķirts!")


#spēlē, ja spēlētājs izvēlās akmeni
if izvele == "R":
    print(f"Jūs izvēlējāties: {akmens}")
    sleep(2)
    print("Dators izvēlējās: ", dators)
    if dators == """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""":
        sleep(2)
        print("Jūs zaudējāt :( Vēlu veiksmi nākamajā mēģinājumā!")
    elif dators == """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""":
        sleep(2)
        print("Neizšķirts!")
    else:
        sleep(2)
        print("Jūs uzvarējāt! Apsveicu!")
