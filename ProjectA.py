import turtle as pen

#Screen
wn=pen.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)

#RoundCounter
segments = []
roundnumber = 0
pen = pen.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.ht()
pen.goto(0, 260)
textroundnumber = str(roundnumber) #Make the roundnumber into a string.
pen.write("Round:" + textroundnumber , align="center", font=("Courier, 24"))

def roundNumberFunction():
    global roundnumber
    roundnumber = roundnumber + 1
    pen.clear() #This clears the board. I only use this for the example now.
    textroundnumber = str(roundnumber)
    pen.write("Round:" + textroundnumber , align="center", font=("Courier, 24"))

wn.onkeypress(roundNumberFunction, "space")
wn.listen()


'''if input("space"):
    roundnumber = roundnumber + 1'''
