#Implementation of Tic-Tac-Toe game in python
#Author - Hitesh Thakur

import random;

#Initializing an empty array
a=[];

#Filling array with empty values
for i in range(0,10):
    a.append(" ");

#Basic print statements for the users
print("We welcome you to the board\n");
print("Enjoy playing TIC-TAC-TOE\n\n")
player1_name = input("Player 1 enter your name ::");
print("\n");
player2_name = input("Player 2 enter your name ::");
print("\n");

#Player1 function (Called when player one gets his first turn to choose the marker)
def player1():
    selected_values = [];
    check = True;
    while check == True:
        val_player1 = input(player1_name+" choose  X or 0 ::");
        print("\n");
        if val_player1 in ['X', '0']:
            check = False;
            if val_player1 == "X":
                val_player2 = '0';
            else:
                val_player2 = "X";
    selected_values.append(val_player1);
    selected_values.append(val_player2);
    return(selected_values);                #Returning the selected markers for each player

#Player2 function (Called when player one gets his first turn to choose the marker)
def player2():
    selected_values = [];
    check=True;
    while check==True:
        val_player2= input(player2_name+" choose  X or 0 ::");
        print("\n");
        if val_player2 in ['X','0']:
            check=False;
            if val_player2=="X":
                val_player1='0';
            else:
                val_player1="X";
    selected_values.append(val_player1);
    selected_values.append(val_player2);
    return (selected_values);               #Returning the selected markers for each player

#Random function
def randomcall():
    temp=random.randint(1,2);       #Generates random number either 1 or 2
    if temp==1:
        result=player1();           #Calling Player1 function
    else:
        result=player2();           #Calling Player2 function
    return result;                  ##Returning the selected markers for both player

#Display Function: Displayed on each player turn
def display():
    print(f"     {a[0]}     |       {a[0]}       |        {a[0]}");
    print(f"     {a[7]}     |       {a[8]}       |        {a[9]}");
    print(f"     {a[0]}     |       {a[0]}       |        {a[0]}");
    print(f"-- -- -- -- -- -- -- -- -- --");
    print(f"     {a[0]}     |       {a[0]}       |        {a[0]}");
    print(f"     {a[4]}     |       {a[5]}       |        {a[6]}");
    print(f"     {a[0]}     |       {a[0]}       |        {a[0]}");
    print(f"-- -- -- -- -- -- -- -- -- --");
    print(f"     {a[0]}     |       {a[0]}       |        {a[0]}");
    print(f"     {a[1]}     |       {a[2]}       |        {a[3]}");
    print(f"     {a[0]}     |       {a[0]}       |        {a[0]}");

#Game Function
def game( player1_name,player2_name,a):
    initiator=randomcall();             #Calling randomcall function
    gamer_one = initiator[0];
    gamer_two = initiator[1];
    turn_random=random.randint(1,2);    #To randomly give player turn in the beginning
    if turn_random==1:
        print("***"+player1_name+" get ready, you will be the playing first***\n");
        temp=player1_name;
        current=gamer_one;
        for i in range(0,9):
            print(temp+" use num pad to play your turn :\n");
            marked=int(input());
            a[marked]=current;
            display();
            checkwin(player1_name, player2_name, gamer_one, gamer_two, a);
            if temp==player1_name:
                temp=player2_name;
                current=gamer_two;
            else:
                temp=player1_name;
                current=gamer_one;
    else:
        print("***"+player2_name + " get ready, you will be the playing first***\n");
        temp = player2_name;
        current = gamer_two;
        for i in range(0, 9):
            print(temp + " use num pad to play your turn :\n");
            marked = int(input());
            a[marked] = current;
            display();
            checkwin(player1_name, player2_name, gamer_one, gamer_two, a);
            if temp == player2_name:
                temp = player1_name;
                current = gamer_one;
            else:
                temp = player2_name;
                current = gamer_two;

def checkwin(player1_name,player2_name,gamer_one,gamer_two,a):
    if (a[1]==a[2]==a[3]==gamer_one) or (a[4]==a[5]==a[6]==gamer_one) or (a[7]==a[8]==a[9]==gamer_one) or (a[1]==a[4]==a[7]==gamer_one) or (a[2]==a[5]==a[8]==gamer_one) or (a[3]==a[6]==a[9]==gamer_one)or (a[1]==a[5]==a[9]==gamer_one) or (a[3]==a[5]==a[7]==gamer_one):
        print("\n*****Kudos!!! "+ player1_name+" you won the game*****");
        exit();
    if (a[1]==a[2]==a[3]==gamer_two) or (a[4]==a[5]==a[6]==gamer_two) or (a[7]==a[8]==a[9]==gamer_two) or (a[1]==a[4]==a[7]==gamer_two) or (a[2]==a[5]==a[8]==gamer_two) or (a[3]==a[6]==a[9]==gamer_two)or (a[1]==a[5]==a[9]==gamer_two) or (a[3]==a[5]==a[7]==gamer_two):
        print("\n*****Kudos!!! " + player2_name + " you won the game*****");
        exit();

#Calling game function and passing player's name and empty array 
game(player1_name,player2_name,a);
