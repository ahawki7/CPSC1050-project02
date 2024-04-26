"""
Author:         Alaina Hawkinson
Date:           04/25/2024
Assignment:     Project 02
Course:         CPSC1051
Lab Section:    001

CODE DESCRIPTION: This code holds each scenario for the different exhibits that the player will go to.   
"""

import sys #import ability to import modules
import os #import operating system
from status_update import game_status # import status_update class from game_status module

class combat: #all of the scenarios for going in the room
    def __init__(self,bag): #initialize the room 
        self.room=[]
        self.bag=bag

    def ushistory(self): #scenario of what happens in the US history exhibit
        print("in the corner of the room there is a lovely set of george washingtons fake teeth, do you want to go check it out?")
        answer=input("yes or no\n").strip().lower() #answer whether or not to explore 
        if answer=="yes": # if they do want to see the teeth
            if self.bag.check("tooth")==True : # sees if the teeth are already in the bag
                print("Wow these things are gross I can't believe you actually picked one of these up") # if they are print this out
            else: # if they are not
                print("one of the teeth is loose do you want to take it with you in your bag?")
                next_answer=input("yes or no\n").strip().lower() # ask if they want to add it to the bag
                if next_answer=="yes": # if they do 
                    print("great, its in your bag") 
                    self.bag.add_to_bag("tooth")# it is added to the bag
                else:
                    print("guess not, they are kinda gross anyway") # if they do not want to add it this is printed
        else:
            print("okay nevermind") # if they do not want to explore this is printed 

    def animals(self): #scenario for the animal exhibit
        print("There are three animals that strike your eye")
        print("They are the giant whale, zebra, and snake")
        going=True #initialize that the loop is still going
        print("which one do you want to look at further?")
        answer=input("Choose 1 2 or 3:\n1: whale\n2: zebra\n3: Snake\nOR 0 to move on to the next room\n").strip() #player is asked to choose a number for a close up look

        while going:
            if answer=="1": # if the player inputs number 1 
                print("doesn't seem to be anything interesting going on here, you may want to look at a different artifact or keep going\n")
                print("which one do you want to look at further?")
                answer=input("Choose 1 2 or 3:\n1: whale\n2:zebra\n3: Snake\n OR 0 to move on to the next room\n").strip() #asked to input another number
            elif answer=="2": # if the player chooses 2
                if self.bag.check("hat"): #Checks to see if the player has already picked up the hat
                    print("What is your favorite animal?") #asks the player a useless question
                    animal=input("favorite animal: ")
                    print("You should probably move on now there is nothing else much to see here") # tells the player to move on
                else: # if the player did not already pick up the hat
                    print("woah the zebra has such a cool hat on, do you want to keep it?") 
                    next_answer=input("yes or no\n") #player inputs whether they want to get the hat or not
                    if next_answer=="yes": # if the answer is yes it is added to their toolbox
                        self.bag.add_to_bag("hat")
                        print("Okay, its in your bag!") 
                    else:
                        print("guess not, whats next?") # if the answer is anything else they are asked where they want to go next 
                print("which one do you want to look at further?")
                answer=input("Choose 1 2 or 3:\n1: whale\n2:zebra\n3: Snake \nOR 0 to move on to the next room \n").strip()
            elif answer=="3": #if the player chooses three they die
                print("Ouch")
                print("The snake bit you")
                print("you died")
                quit() # quits program
            elif answer=="0": # if the player chooses 0
                going=False # the loop ends 
            else:
                print("that just wasnt an option") # if they put an invalid option they are asked to input a different option
                print("which one do you want to look at further?")
                answer=input("Choose 1 2 or 3:\n1: whale\n2:zebra\n3: Snake\n OR 0 to move on to the next room\n").strip()

    def dinosaurexhibit(self): # scenario for the dinosaur exhibit
        print("Fun fact about dinosoars: They love jokes!")
        if self.bag.check("bone"): #checks to see if they have already collected the item 
            print("You have already prooved that you are a jokester so you can move on.") #moves on if they have
        else: # if they have not
            print("what do you call a sleeping dinosoar?")
            answer=input("A... ").strip().lower() # asked to answer a joke
            if answer=="dinosnore": # if they get the joke correct
                print("good job! Heres a bone for your great sense of humor")
                self.bag.add_to_bag("bone") # bone is added to the bag
            else: # if they get the answer wrong
                print("WRONG it is a DINOSNORE!!!") # prints out right answer
                print("lets try again") 
                print("What do you call it when a dinosaur makes a goal with a soccer ball?")
                answer=input("A... ").strip().lower() # asked to answer another joke
                if answer=="dinoscore": # if they get it right
                    print("good job! Heres a bone for your great sense of humor")
                    self.bag.add_to_bag("bone") # bone is added to bag
                else:#if they get it wrong
                    print("WRONG it is a DINOSCORE") #prints out correct answer
                    print("lets try again")
                    print("What did the Tyrannosaurus rex get after a tough workout?")
                    answer=input("A... ").strip().lower() #asked to answer another joke
                    if answer=="dinosore": #if they get it right
                        print("good job! Heres a bone for your great sense of humor")
                        self.bag.add_to_bag("bone") #bone is added to their bag
                    else:
                        print("wow you are terrible at this, the answer was DINOSORE.") # if they get them all wrong they do not get a bone but they can try again later
                        print("no bones for you move on")


    def art(self): #scenario for art exhibit 
        print("there are 136 paintings in this room would you like to see one up close?")
        answer=input("choose a number between 1 and 136 or just say no to move on\n") #user chooses a number
        while answer!="no": #until they answer no they will just be looking at paintings 
            print("\nwhat a pretty painting\n")
            print("choose another to look at")
            answer=input("choose a number between 1 and 136 or just say no to move on\n")

    def geology(self): #scenario for geology exhibit 
        print("There is a piece of paper in the corner do you want to go over to it?")
        answer=input("yes or no\n").strip().lower() # inputs yes or no
        if answer=="yes": # if they answer yes
            print("The paper is an ancient geology paper that says that mummies love really shiny rocks")
            if self.bag.check("gem"): #checks to see if they have already collected the gem
                print("good thing you have already collected a shiny rock!")
            else: # if they have not collected the gem
                print("next to the paper is the shiniest gem you have ever seen. Pick it up and take it with you?") 
                next_answer=input("yes or no\n").strip().lower() #player inputs whether they want to keep the rock 
                if next_answer=="yes": # if they say yes it is added to the bag
                    self.bag.add_to_bag("gem")
                    print("it is added to your bag")
                else: # if they say no they move on
                    print("alright then you probably dont need it anyway")
        else: # if they do not want to see the paper
            print("Papers are boring anyway, do you want to pick up a random rock and call it a day?")
            if self.bag.check("rock"): #see if the rock is already in their bag
                print("looks like you already have, do you want to put it back?")
                next_answer=input("yes or no\n") # ask if they want to put it back
                if next_answer=="yes": # if they answer yes
                    self.bag.remove("rock") # the rock is removed from their bag
                else: # if they choose no it is still in their bag
                    print("probably a good idea to hold onto it in case")
            else: #if the rock is not in their bag
                next_answer=input("yes or no\n").strip().lower() #ask if they want to keep the rock
                if answer=="yes": #if yes the rock is added to their bag 
                    self.bag.add_to_bag("rock")
                    print("added to your bag")
                else: # if no then it is not on added 
                    print("The mummy probably would not like it anyway")

    def war(self): # scenario for the war exhibit 
        going=True #initializes that the loop is still going
        suit=False # initializes that the player is not wearing the suit 
        while going: #while the loop is still going 
            print("on your right is an army suit with a hard hat, on your left is a gun, and straight ahead is a war medal. Which one do you want to look at?")
            answer=input("Choose a number:\n1: right\n2: left\n3: straight ahead\n").strip() # inputs what they want to look at 
            if answer=="1": # if they choose 1
                print("do you want to put the suit on?")
                if suit==True: # check to see if they are already wearing the suit
                    print("You already have it on silly!")
                else:
                    next_answer=input("yes or no\n").strip().lower() # if not they answer whether they want to put it on
                    if next_answer=="yes": # if they answer yes , suit is changed to True
                        suit=True
                    else: # if not nothing happens
                        print("The suit probably was not important anyway")
                        suit=False
            elif answer=="2": #if they choose 2 nothing happens
                print("you have the gun now, but it is too big to fit in your bag so you have to put it back")
            elif answer=="3": # if they choose 3
                if suit==True: # if they are wearing the suit 
                    print("Its a good thing you are wearing the bulletproof army suit because this room was boobytrapped")
                    print("Now lets get this uncomfy suit off") # takes off the suit
                    if self.bag.check("medal"): #check to see if they already have the medal 
                        print("Nice work on making it to the medal, too bad you already put it in your bag")
                        going=False # ends loop
                    else: # if it is not in the bag already
                        print("you safely made it to the medal, keep it?") #ask if they want to keep the medal
                        fifth_answer=input("yes or no\n").strip().lower()
                        check=True # initialize loop
                        while check:
                            if fifth_answer=="yes": #if they say yes add it to bag
                                self.bag.add_to_bag("medal")
                                print("added to your bag")
                                going=False #end loop
                                check=False # end other loop
                            elif fifth_answer=="no": # if they say no dont add it to bag
                                print("it probably wasn't important anyway")
                                check=False #end loop
                            else: # if they say anything else ask again
                                print("That was not a valid answer")
                                print("you safely made it to the medal, keep it?")
                                fifth_answer=input("yes or no\n").strip().lower()
                else:# if the suit is not on and they chose 3 they die
                    print("ITS A BOOBY TRAP RUN!!!\n")
                    print("turns out that suit was bullet proof, would have been handy because you got shot and died.\n")
                    going=False #end loop
                    quit() #end program
            else:
                print("That was not a valid answer") #ask again



                
    
    def ancienthistory(self): #scenario in the ancient history exhibit 
        game_over=game_status() #initialize the game_status class
        print("There is a big mummy laying sleeping in the middle of the room. Guess its time to wake her up")
        print("Before you have a change to think about your next move her eyes shoot awake and she starts coming towards you")
        print("Quick do something!!")
        answer=input("What are you going to do?\nchoose a number\n1: run away\n2: give the mummy your gifts\n3: ask the mummy for help out\n") # ask how they want to interact with the mummy
        valid=True # initialize valid 

        while valid: # while loop is still going 
            if answer=="1": # if they answer 1 then they choose a different room to go in 
                valid=False # end loop
                exit() # probably not needed
            elif answer=="2": # if they choose 2 
                valid=False  # end loop
                gifts=self.bag.list_contents() # get list of items in bag
                contents=self.bag.get_contents() # get separate list of items in bag
                print(gifts) # print the string 
                if "rock" in contents: # if they picked up the rock they die
                    print("The mummy looks in the bag and sees that you collected a random rock rather than just bringing her the shiniest one")
                    print("She throws it at your head and you die")
                    quit() # end program
                elif len(contents)==5 : # if they did not pick up the rock and have 5 other things then they wong
                    print("The mummy is very happy to see that you got her the shiniest rock. You feel relief wave over you, but then the mummy motions 4 tiny mummies to come over to her\n")
                    print("A small mummy walks forward and smiles at you, she is missing a tooth. You give her the tooth \n")
                    print("Next a mummy comes over that is missing some of his wrapping on his head, you give him the hat\n")
                    print("Then another mummy emerges and he is limping becuase his leg is broken, he takes the bone from you\n")
                    print("The fourth tiny mummy comes foreward and you give him the medal becuase what else do you have to offer\n")
                    print("the mother mummy gives you a key and points in the direction of a large door\n")
                    print("The key fits!!")
                    game_over.status(True) # make the game over
                    valid=False  #end loop
                else: # if they do not meet the requirements they get another chance
                    print("How dare you approach the mummy without enough gifts to offer her!! ")
                    print("RUN and find something more to offer her ")
                    valid=False #end loop
            elif answer=="3": # if they choose 3 they die
                valid=False #end loop
                print("Turns out the mummy was not in a helpful mood. She killed you")
                quit() #end program
            else: # if they do not input a valid answer they are asked again
                print("This is important, choose one!!!")
                answer=input("What are you going to do?\nchoose a number\n1: run away\n2:give the mummy your gifts\n3: ask the mummy for help out\n")

