import turtle as t

t.Screen() #Preparations for this module. Remove or adjust in main code.
t.seth(270)
t.penup()
t.tracer(0,0) #Screen Stabilizer
stats_Start_Coords = -330,265
t.update()
t.goto(stats_Start_Coords)


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
while amount_players == None:
  amount_players = t.numinput('Free For All!','How many players are there?', default=4, minval=2, maxval=6)  

def playerStats():
    global amount_players
    for i in range(int(amount_players)):
        x = i + 1
        t.write('Player ' + str(x) + ' HP: ' + str(players['player' + str(x) + '_hp']), font=18)
        t.fd(20)
        t.write('Player ' + str(x) +' SP: ' + str(players['player' + str(x) + '_sp']), font=18)
        t.fd(40)
        print('')

def damageTake():
  damaged_Player = t.numinput('Free for All!','Which player took damage?', default = 3, minval = 1, maxval = amount_players)
  if damaged_Player == None:
    t.onkeypress(damageTake,'w')
    t.listen()
    return 'Empty'
  dmg = t.numinput('Free for All!','How much damage did they take?', default = 0, minval = 0, maxval = 100)
  if dmg == None:
    t.onkeypress(damageTake,'w')
    t.listen()
    return 'Empty'
#Handling Damage when a Shield is active.
  remaining_Dmg = 0
  if dmg < 0:
    dmg = int(dmg) * -1
  if players['player' + str(int(damaged_Player)) + '_sp'] > 0:
    players['player' + str(int(damaged_Player)) + '_sp'] = players['player' + str(int(damaged_Player)) + '_sp'] - int(dmg)
    if players['player' + str(int(damaged_Player)) + '_sp'] < 0:
      remaining_Dmg = players['player' + str(int(damaged_Player)) + '_sp'] 
      players['player' + str(int(damaged_Player)) + '_sp'] = 0
      if remaining_Dmg < 0:
        remaining_Dmg = int(remaining_Dmg) * -1
    players['player' + str(int(damaged_Player)) + '_hp'] = players['player' + str(int(damaged_Player)) + '_hp'] - int(remaining_Dmg)
    #End of Shield Damage check.
  else:
    players['player' + str(int(damaged_Player)) + '_hp'] = players['player' + str(int(damaged_Player)) + '_hp'] - int(dmg)
  if players['player' + str(int(damaged_Player)) + '_hp'] < 0:
    players['player' + str(int(damaged_Player)) + '_hp'] = 0
  t.penup()
  t.goto(stats_Start_Coords)
  t.clear()
  playerStats() 
  t.onkeypress(damageTake,'w')
  t.listen()

def shieldGive():
  shield = 25
  shielded_Player = t.numinput('Free for All!','Which player got shield', default = 3, minval = 1, maxval = amount_players)
  if shielded_Player == None:
    t.onkeypress(shieldGive,'q')
    t.onkeypress(damageTake,'w')
    t.listen()
    return 'No Shield Given'
  players['player' + str(int(shielded_Player)) + '_sp'] = players['player' + str(int(shielded_Player)) + '_sp'] + shield
  if players['player' + str(int(shielded_Player)) + '_sp'] >= 100:
    players['player' + str(int(shielded_Player)) + '_sp'] = 100
  t.penup()
  t.goto(stats_Start_Coords)
  t.clear()
  playerStats() 
  t.onkeypress(shieldGive,'q')
  t.onkeypress(damageTake,'w')
  t.listen()

playerStats()
t.onkeypress(damageTake,'w')
t.onkeypress(shieldGive,'q')
t.listen()

t.mainloop() #Keeping Test screen. Remove in main code.
