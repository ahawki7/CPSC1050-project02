import sys 
import os
from status_update import game_status

class combat:
    def __init__(self,bag):
        self.room=[]
        self.bag=bag

    def ushistory(self):
        print("in the corner of the room there is a lovely set of george washingtons fake teeth, do you want to go check it out?")
        answer=input("yes or no\n").strip().lower()
        if answer=="yes":
            if self.bag.check("tooth")==True :
                print("Wow these things are gross I can't believe you actually picked one of these up")
            else:
                print("one of the teeth is loose do you want to take it with you in your bag?")
                next_answer=input("yes or no\n").strip().lower()
                if next_answer=="yes":
                    print("great, its in your bag")
                    self.bag.add_to_bag("tooth")
                else:
                    print("guess not, they are kinda gross anyway")
        else:
            print("okay nevermind")

    def animals(self):
        print("There are three animals that strike your eye")
        print("They are the giant whale, zebra, and snake")
        going=True
        print("which one do you want to look at further?")
        answer=input("Choose 1 2 or 3:\n1: whale\n2: zebra\n3: Snake\nOR 0 to move on to the next room\n").strip()
        while going:
            if answer=="1":
                print("doesn't seem to be anything interesting going on here, you may want to look at a different artifact or keep going\n")
                print("which one do you want to look at further?")
                answer=input("Choose 1 2 or 3:\n1: whale\n2:zebra\n3: Snake\n OR 0 to move on to the next room\n").strip()
            elif answer=="2":
                if self.bag.check("hat"):
                    print("What is your favorite animal?")
                    animal=input("favorite animal: ")
                    print("You should probably move on now there is nothing else much to see here")
                else:
                    print("woah the zebra has such a cool hat on, do you want to keep it?")
                    next_answer=input("yes or no\n")
                    if next_answer=="yes":
                        self.bag.add_to_bag("hat")
                        print("Okay, its in your bag!")
                    else:
                        print("guess not, whats next?")
                print("which one do you want to look at further?")
                answer=input("Choose 1 2 or 3:\n1: whale\n2:zebra\n3: Snake \nOR 0 to move on to the next room \n").strip()
            elif answer=="3":
                print("Ouch")
                print("The snake bit you")
                print("you died")
                quit() 
            elif answer=="0":
                going=False
            else:
                print("that just wasnt an option")
                print("which one do you want to look at further?")
                answer=input("Choose 1 2 or 3:\n1: whale\n2:zebra\n3: Snake\n OR 0 to move on to the next room\n").strip()

    def dinosaurexhibit(self):
        print("Fun fact about dinosoars: They love jokes!")
        if self.bag.check("bone"):
            print("You have already prooved that you are a jokester so you can move on.")
        else:
            print("what do you call a sleeping dinosoar?")
            answer=input("A... ").strip().lower()
            if answer=="dino snore":
                print("good job! Heres a bone for your great sense of humor")
                self.bag.add_to_bag("bone")
                going=False
            else:
                print("WRONG it is a DINO SNORE!!!")
                print("lets try again")
                print("What do you call it when a dinosaur makes a goal with a soccer ball?")
                answer=input("A... ").strip().lower()
                if answer=="dino score":
                    print("good job! Heres a bone for your great sense of humor")
                    self.bag.add_to_bag("bone")
                    going=False
                else:
                    print("WRONG it is a DINO SCORE")
                    print("lets try again")
                    print("What did the Tyrannosaurus rex get after a tough workout?")
                    answer=input("A... ").strip().lower()
                    if answer=="dino sore":
                        print("good job! Heres a bone for your great sense of humor")
                        self.bag.add_to_bag("bone")
                        going=False
                    else:
                        print("wow you are terrible at this")
                        print("no bones for you move on")
                        going=False


    def art(self):
        print("there are 136 paintings in this room would you like to see one up close?")
        answer=input("choose a number between 1 and 136 or just say no to move on\n")
        while answer!="no":
            print("\nwhat a pretty painting\n")
            print("choose another to look at")
            answer=input("choose a number between 1 and 136 or just say no to move on\n")

    def geology(self):
        print("There is a piece of paper in the corner do you want to go over to it?")
        answer=input("yes or no\n").strip().lower()
        if answer=="yes":
            print("The paper is an ancient geology paper that says that mummies love really shiny rocks")
            if self.bag.check("gem"):
                print("good thing you have already collected a shiny rock!")
            else:
                print("next to the paper is the shiniest gem you have ever seen. Pick it up and take it with you?")
                next_answer=input("yes or no\n").strip().lower()
                if next_answer=="yes":
                    self.bag.add_to_bag("gem")
                    print("it is added to your bag")
                else:
                    print("alright then you probably dont need it anyway")
        else:
            print("Papers are boring anyway, do you want to pick up a random rock and call it a day?")
            if self.bag.check("rock"):
                print("looks like you already have, do you want to put it back?")
                next_answer=input("yes or no\n")
                if next_answer=="yes":
                    self.bag.remove("rock")
                else:
                    print("probably a good idea to hold onto it in case")
            else:
                next_answer=input("yes or no\n").strip().lower()
                if answer=="yes":
                    self.bag.add_to_bag("rock")
                    print("added to your bag")
                else:
                    print("The mummy probably would not like it anyway")

    def war(self):
        going=True 
        suit=False
        while going:
            print("on your right is an army suit with a hard hat, on your left is a gun, and straight ahead is a war medal. Which one do you want to look at?")
            answer=input("Choose a number:\n1: right\n2: left\n3: straight ahead\n").strip()
            if answer=="1":
                print("do you want to put the suit on?")
                if suit==True:
                    print("You already have it on silly!")
                else:
                    next_answer=input("yes or no\n").strip().lower()
                    if next_answer=="yes":
                        suit=True
                    else:
                        print("The suit probably was not important anyway")
                        suit=False
            elif answer=="2":
                print("you have the gun now, but it is too big to fit in your bag so you have to put it back")
            elif answer=="3":
                if suit==True:
                    print("Its a good thing you are wearing the bulletproof army suit because this room was boobytrapped")
                    print("Now lets get this uncomfy suit off")
                    if self.bag.check("medal"):
                        print("Nice work on making it to the medal, too bad you already put it in your bag")
                        going=False
                    else:
                        print("you safely made it to the medal, keep it?")
                        fifth_answer=input("yes or no\n").strip().lower()
                        check=True
                        while check:
                            if fifth_answer=="yes":
                                self.bag.add_to_bag("medal")
                                print("added to your bag")
                                going=False
                                check=False
                            elif fifth_answer=="no":
                                print("it probably wasn't important anyway")
                                check=False
                            else:
                                print("That was not a valid answer")
                                print("you safely made it to the medal, keep it?")
                                fifth_answer=input("yes or no\n").strip().lower()
                else:
                    print("ITS A BOOBY TRAP RUN!!!\n")
                    print("turns out that suit was bullet proof, would have been handy because you got shot and died.\n")
                    going=False
                    quit()
            else:
                print("That was not a valid answer")



                
    
    def ancienthistory(self):
        game_over=game_status()
        print("There is a big mummy laying sleeping in the middle of the room. Guess its time to wake her up")
        print("Before you have a change to think about your next move her eyes shoot awake and she starts coming towards you")
        print("Quick do something!!")
        answer=input("What are you going to do?\nchoose a number\n1: run away\n2: give the mummy your gifts\n3: ask the mummy for help out\n")
        valid=True
        while valid:
            if answer=="1":
                valid=False
                exit()
            elif answer=="2":
                valid=False 
                gifts=self.bag.list_contents()
                contents=self.bag.get_contents()
                print(gifts)
                if "rock" in contents:
                    print("The mummy looks in the bag and sees that you collected a random rock rather than just bringing her the shiniest one")
                    print("She throws it at your head and you die")
                    quit()
                elif len(contents)==5 :
                    print("The mummy is very happy to see that you got her the shiniest rock. You feel relieve wave over you, but then the mummy motions 4 tiny mummies to come over to her\n")
                    print("A small mummy walks forward and smiles at you, she is missing a tooth. You give her the tooth \n")
                    print("Next a mummy comes over that is missing some of his wrapping on his head, you give him the hat\n")
                    print("Then another mummy emerges and he is limping becuase his leg is broken, he takes the bone from you\n")
                    print("The fourth tiny mummy comes foreward and you give him the medal becuase what else do you have to offer\n")
                    print("the mother mummy gives you a key and points in the direction of a large door\n")
                    print("The key fits!!")
                    game_over.status(True)
                    valid=False 
                else: 
                    print("How dare you approach the mummy without enough gifts to offer her!! ")
                    print("RUN and find something more to offer her ")
                    valid=False
            elif answer=="3":
                valid=False
                print("Turns out the mummy was not in a helpful mood. She killed you")
                quit()
            else:
                print("This is important, choose one!!!")
                answer=input("What are you going to do?\nchoose a number\n1: run away\n2:give the mummy your gifts\n3: ask the mummy for help out\n")

