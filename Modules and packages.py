#Modules are different parts of a program that each handle seperate events. Usually each module is stored in a .py file

#the example below shows how to import a module located in the same folder
# game.py
# import the draw module
import draw

def play_game():
    ...

def main():
    result = play_game()
    draw.draw_game(result)

# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()

# draw.py

def draw_game():
    ...

def clear_screen(screen):
    ...

# game.py
# import the draw module
from draw import draw_game

def main():
    result = play_game()
    draw_game(result)


#Real world example
from Functions import sumOfTwoNumbers #normally you wouldn't have so many print functions

def math() :
    print(sumOfTwoNumbers(234,324))

math()
