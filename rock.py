import random
random_option="notdefind"
winner="notdefind"
rnd_score=0
player_score=0
rnd=random.randint(0,2)
print("**********rock,paper,scissor**********")
player=input("enter your option: ")
if rnd==0:
    random_option="rock"
elif rnd==1:
    random_option="paper"
else:
    random_option="scissor"
if random_option=="rock" and player=="rock":
    print("robot said:",random_option)
    random_option="notdefind"
    print("nobody win!")
elif random_option=="rock" and player=="paper":
    print("robot said:",random_option)
    random_option="notdefind"
    print("player win!")
    player_score=player_score+1
elif random_option=="rock" and player=="scissor":
    print("robot said:",random_option)
    random_option="notdefind"
    print("robot win!")
    rnd_score=rnd_score+1
elif random_option=="paper" and player=="rock":
    print("robot said:",random_option)
    random_option="notdefind"
    print("robot win!")
    rnd_score=rnd_score+1
elif random_option=="paper" and player=="paper":
    print("robot said:",random_option)
    random_option="notdefind"
    print("nobody win!")
elif random_option=="paper" and player=="scissor":
    print("robot said:",random_option)
    random_option="notdefind"
    print("player win!")
    player_score=player_score+1
elif random_option=="scissor" and player=="rock":
    print("robot said:",random_option)
    random_option="notdefind"
    print("player win!")
    player_score=player_score+1
elif random_option=="scissor" and player=="paper":
    print("robot said:",random_option)
    random_option="notdefind"
    print("player win!")
    rnd_score=rnd_score+1
elif random_option=="scissor" and player=="scissor":
    print("robot said:",random_option)
    random_option="notdefind"
    print("nobody win!")
if rnd_score>player_score:
    winner="robot"
else:
    winner="player"
print(f"************so,{winner} is the winner!************")
again=input("do you want to play again?y/n: ")
while again=="y":
    if rnd_score==3:
        print("robot win faster than you!")
        break
    rnd=random.randint(0,2)
    random_option="notdefind"
    print("**********rock,paper,scissor**********")
    player=input("enter your option: ")
    if rnd==0:
        random_option="rock"
    elif rnd==1:
        random_option="paper"
    else:
        random_option="scissor"
    if random_option=="rock" and player=="rock":
        print("robot said:",random_option)
        print("nobody win!")
    elif random_option=="rock" and player=="paper":
        print("robot said:",random_option)
        print("player win!")
        player_score=player_score+1
    elif random_option=="rock" and player=="scissor":
        print("robot said:",random_option)
        print("robot win!")
        rnd_score=rnd_score+1
    elif random_option=="paper" and player=="rock":
        print("robot said:",random_option)
        print("robot win!")
        rnd_score=rnd_score+1
    elif random_option=="paper" and player=="paper":
        print("robot said:",random_option)
        print("nobody win!")
    elif random_option=="paper" and player=="scissor":
        print("robot said:",random_option)
        print("player win!")
        player_score=player_score+1
    elif random_option=="scissor" and player=="rock":
        print("robot said:",random_option)
        print("player win!")
        player_score=player_score+1
    elif random_option=="scissor" and player=="paper":
        print("robot said:",random_option)
        print("robot win!")
        rnd_score=rnd_score+1
    elif random_option=="scissor" and player=="scissor":
        print("robot said:",random_option)
        print("nobody win!")
    if rnd_score==3:
        print("robot win faster than you!")
        break
    if rnd_score>player_score:
        winner="robot"
    else:
        winner="player"
    print(f"************so,{winner} is the winner!************")
    if rnd_score==3:
        print("robot win faster than you!")
        break
    elif player_score==3:
        print("you win faster!")
        break
    again=input("do you want to play again?y/n: ")