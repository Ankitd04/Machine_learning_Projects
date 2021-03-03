# Import the libraries
from tkinter import *
import random

# Initialize the window
root = Tk()                                 # use to initialized Tkinter to create window
root.geometry('400x400')                    # sets the window width and height
root.resizable(0, 0)                        # by this command we can fix the size of the window
root.title('Game - Rock, Paper, Scissors')  # used to set the title of the window
root.config(bg='seashell3')               # use to set the color of the background

Label(root, text='Rock, Paper, Scissors', font='arial 20 bold', bg='seashell2').pack()
'''
Label() widget used when we want to display text that users can’t modify.
root is the name of our window
text which displays on the label as the title of that label
font in which form the text is written
pack used to the organized widget in form of block
'''

# for users choice
user_take = StringVar()
Label(root, text='choose any one: rock, paper, scissors', font='arial 15 bold', bg='seashell2').place(x=20, y=70)
Entry(root, font='arial 15', textvariable=user_take, bg='antiquewhite2').place(x=90, y=130)
'''
user_take is a string type variable that stores the choice that the user enters.
Entry() widget used when we want to create an input text field.
textvariable used to retrieve the text to entry widget
place() – place widgets at specific position
'''

# for Computer choice
comp_pick = random.randint(1, 3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick == 2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'

# function to start the game
Result = StringVar()


def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('tie, you both have selected same')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('you lose, Computer select paper. Computer won')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('You won, computer selected scissors')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('You won, computer selected rock')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('Computer won, computer selected scissors')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('Computer won, computer selected rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('You won, computer selected paper')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')

# function to reset


def Reset():
    Result.set("")
    user_take.set("")


# function to exit
def exit():
    root.destroy()
# root.destroy() will quit the rock paper scissors program by stopping the mainloop().

# Define buttons
Entry(root, font = 'arial 10 bold', textvariable = Result, bg = 'antiquewhite2', width = 50).place(x=25, y=250)

Button(root, font='arial 13 bold', text='PLAY', padx=5, bg='seashell4', command=play).place(x=150, y=190)

Button(root, font='arial 13 bold', text='RESET', padx=5, bg='seashell4', command=Reset).place(x=70, y=310)

Button(root, font='arial 13 bold', text='EXIT', padx=5, bg='seashell4', command=exit).place(x=230, y=310)

root.mainloop()
'''
Button() widget used when we want to display a button.
command called the specific function when the button will be clicked.
root.mainloop() method executes when we run our program
'''
