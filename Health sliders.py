import turtle as t

t.hideturtle()
t.bgcolor('black')
t.color('white')
t.Screen()


players = {'player1_hp':100,
           'player1_sp':0,
           'player2_hp':100,
           'player2_sp':0,
           'player3_hp':100,
           'player3_sp':0,
           'player4_hp':100,
           'player4_sp':0,
           'player5_hp':100,
           'player5_sp':0,
           'player6_hp':100,
           'player6_sp':0
           }

amount_players = t.numinput('Free For All!','How many players are there?', default=4, minval=2, maxval=6)

t.penup()

t.setpos(-453.55,290.55)



def playerStats():
    global amount_players
    for i in range(int(amount_players)):
        x = i + 1
        t.penup()
        t.write('Player ' + str(x) + ' HP: ' + str(players['player' + str(x) + '_hp']) + '\nPlayer ' + str(x) +
              ' SP: ' + str(players['player' + str(x) + '_sp']),font=("Arial", 14, "normal"))
        t.seth(270)
        t.fd(150)





playerStats()

t.mainloop()
