import random

def show(player_entry,comp_entry):
    print("player choose= "+player_entry+"\ncomputer choose= "+comp_entry)

choices = ["rock","paper","scissors"]
player_score=0
comp_score=0
while True:

    player_entry=None
    
    while player_entry not in choices:
        player_entry=input("please enter your select (rock,paper,scissors):\n")
        
    
    comp_entry=random.choice(choices)

    show(player_entry,comp_entry)

    if player_entry==comp_entry:
        print("equal")
    
    elif player_entry=="rock" and comp_entry == "scissors":
        print("player won")
        player_score+=1
    
    elif player_entry=="rock" and comp_entry == "paper":
        print("computer won")
        comp_score+=1
    
    elif player_entry=="paper" and comp_entry == "scissors":
        print("computer won")
        comp_score+=1
    
    elif player_entry=="paper" and comp_entry == "rock":
        print("player won")
        player_score+=1

    elif player_entry=="scissors" and comp_entry == "paper":
        print("player won")
        player_score+=1
        
    elif player_entry=="scissors" and comp_entry == "rock":
        print("computer won")
        comp_score+=1
    
    print("player score= "+str(player_score)+"\ncomputer score= "+str(comp_score))
    
    select=["yes","no"]

    while select not in select:
        select=input("do you want contiune yes/no:\n")

    if select=="yes":
        pass

    elif select=="no":
        break

if player_score > comp_score:
    print("PLAYER WON THIS GAME!!!")
elif player_score < comp_score:
    print("COMPUTER WON THIS GAME!!!")
else:
    print("EQUAL")