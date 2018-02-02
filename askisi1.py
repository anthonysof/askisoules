from random import randint
from random import shuffle
def create_player_choices():
    player = []
    for i in range(5):
        player.append(randint(1,80))
    return player

def check_win(players,all_players):
    res = ""
    for i in range(players):
        if "".join(str(x) for x in all_players[i]) == "BINGO":
            res = "player "+str(i+1)+" won"
    return res

def check_player(all_players,num):
    for player in all_players:
        for i in range(5):
            if player[i] == num and i == 0:
                player[i] = "B"
            elif player[i] == num and i==1:
                player[i] = "I"
            elif player[i] == num and i==2:
                player[i] = "N"
            elif player[i] == num and i==3:
                player[i] = "G"
            elif player[i] == num and i == 4:
                player[i] = "O"

def announce_number(pool):
    if pool:
        return pool.pop()
    else:
        return "loss"

def create_pool():
    pool = []
    for i in range(1,81):
        pool.append(i)
    shuffle(pool)
    return pool
sum = 0
for i in range(1000):
    players = 100
    #players = int(raw_input("dwse ari8mo paixtwn"))
    all_players = []
    pool = create_pool()
    for i in range(players):
        all_players.append(create_player_choices())
    #print all_players
    res = ""
    count = 1
    while True:
        num = announce_number(pool)
        check_player(all_players,num)
        res = check_win(players,all_players)
        if res != "":
            #print res
            #print all_players
            #print "we announced "+str(count)+" numbers"
            break
        count+=1
    sum+=count
average = float(sum)/1000.0
print "xriazontai kata meso oro: "+str(average)+" ari8moi"





