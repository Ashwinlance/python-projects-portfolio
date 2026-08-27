import time
import sys
import pygame

pygame.init()
sound = pygame.mixer.Sound("lose.mp3")

def stutter(text):
    for c in text:
        print(c, end="")
        sys.stdout.flush()
        pygame.time.wait(20)
    print()

def end():
    stutter("\n>>>>><<<<<\nYOU DIED\n>>>>><<<<<\n")
    sound.play()
    pygame.time.wait(6000)
    start()

def win():
    end_time = time.time()
    minutes = round(end_time / 60, 2)
    stutter("\n---------------------------------------------------\n")
    stutter(f"Well done! You escaped in {minutes} minutes!\n")
    stutter("---------------------------------------------------\n")
    pygame.time.wait(6000)
    start()

def start():
    stutter("\nYou wake up in a dark room with no memory of how you got there. You see a door in front of you and a door to your left.\n")
    choice = input("Which door do you choose? (left/front): ")
    if choice == "left": room1()
    elif choice == "front": room2()
    else: stutter("Invalid choice."); start()

def room1():
    stutter("\nYou enter a room with a table and a key on it. There is a door to your right and a door to your left.\n")
    choice = input("What do you do? (take key/left/right): ")
    if choice == "take key": stutter("\nYou take the key."); room3()
    elif choice == "left": room4()
    elif choice == "right": room5()
    else: stutter("Invalid choice."); room1()

def room2():
    stutter("\nYou enter a room with a window and a crowbar. There is a door to your left and a door to your right.\n")
    choice = input("What do you do? (take crowbar/left/right): ")
    if choice == "take crowbar": stutter("\nYou take the crowbar."); room6()
    elif choice == "left": room7()
    elif choice == "right": room8()
    else: stutter("Invalid choice."); room2()

def room3():
    stutter("\nYou enter a room with a locked door. There is a keyhole in the door.\n")
    choice = input("What do you do? (use key/leave): ")
    if choice == "use key": stutter("\nYou unlock the door and escape!"); win()
    elif choice == "leave": room1()
    else: stutter("Invalid choice."); room3()

def room4(): stutter("\nYou enter a room with a monster. The monster eats you."); end()
def room5(): stutter("\nYou enter a room with a trap. You fall into the trap and die."); end()
def room6():
    stutter("\nYou enter a room with a locked window. There is a keyhole in the window.\n")
    choice = input("What do you do? (use crowbar/leave): ")
    if choice == "use crowbar": stutter("\nYou break the window and escape!"); win()
    elif choice == "leave": room2()
    else: stutter("Invalid choice."); room6()
def room7(): stutter("\nYou enter a room with a bomb. The bomb explodes and you die."); end()
def room8(): stutter("\nYou enter a room with a painting. The painting comes to life and kills you."); end()

start()
