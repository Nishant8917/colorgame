# import the modules 
import tkinter
import random
  
# all of the possible colour.
colours = ['red','blue','green','pink','black',
           'yellow','orange','white','purple','brown']
score = 0
  
# time left in the game, initially 60 seconds.
timeleft = 60
  
#startGame function that will starts the game.
def startGame(event):
      
    if timeleft == 60:
          
        # countdown timer starts
        countdown()
          
    # run the function nextcolour to choose the following color appearing
    nextColour()
  
# Function to choose and display the next colour.

def nextColour():
  
    # globally scoped score and timeleft variables usage.
    global score
    global timeleft
  
    # the game is currently being played
    if timeleft > 0:
  
        # text input box activates
        e.focus_set()
  
        # if the colour typed is equal
        # to the colour of the text
        if e.get().lower() == colours[1].lower():
              
            score += 1
  
        # clear the text entry box.
        e.delete(0, tkinter.END)
          
        random.shuffle(colours)
          
        # change the colour to type, by changing the
        # text _and_ the colour to a random colour value
        label.config(fg = str(colours[1]), text = str(colours[0]))
          
        # update the score.
        scoreLabel.config(text = "Score: " + str(score))
  
  
# Countdown timer function 
def countdown():
  
    global timeleft
  
    # GAME being played
    if timeleft > 0:
  
        # timer decrrease 
        timeleft -= 1
          
        # updation of time in timeLabel
        timeLabel.config(text = "Time left: "
                               + str(timeleft))
                                 
        # run the function again after 1 second.
        timeLabel.after(1000, countdown)
  
  
# Driver Code
  
# create a GUI window
root = tkinter.Tk()
  
# set the title
root.title("COLLAGE OF COLORS")
  
# set the size
root.geometry("375x375")
  
# add an instructions label
instructions = tkinter.Label(root, text = "Type the colour"
                        " and not the word !!!",
                                      font = ('Helvetica', 12))
instructions.pack() 
  
# add a score label
scoreLabel = tkinter.Label(root, text = "Press enter to start",
                                      font = ('Helvetica', 12))
scoreLabel.pack()
  
# add a time left label
timeLabel = tkinter.Label(root, text = "Time left: " +
              str(timeleft), font = ('Helvetica', 12))
                
timeLabel.pack()
  
# add a label for displaying the colours
label = tkinter.Label(root, font = ('Helvetica', 60))
label.pack()
  
# add a text entry box for
# typing in colours
e = tkinter.Entry(root)
  
# run the 'startGame' function 
# when the enter key is pressed
root.bind('<Return>', startGame)
e.pack()
  
# set focus on the entry box
e.focus_set()
  
# start the GUI
root.mainloop()