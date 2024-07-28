
'''
Author – Vihaan
Date – 1/23/2024
File name - Vihaan_Johnathan'sGame3.py
Purpose – Making a choose your own adventure game where the main character gets stuck in a forest and needs to
          escape. This is day 3 code. Today I will finish my game. I have 90% of my functions done, so today's
          code will be quick and easy. I will try, at the end, to re-arrange everything into a wild loop. If not,
          I will implement a while loop somewhere else. Most of today's lines will be commenting and explaining,
          and a bit of math. I will also remove "while True" and "break".
'''

#This imports random, so we can use random.randint() in the future of our code.
import random

#This imports time, so we can use time.sleep() in the future of our code.
import time

'''
A dictionary vs variable
    - A variable is a single piece of data, while dictionaries are key-value pairs. This will be more useful and
    more concise than variables for this case, as we are also changing the values throughout the code.
    - Dictionaries are also more versatile. You can easily update the value of any key, or delete the
    key altogether in the middle of the code.
'''

#This is the function that stores the entire game.
#The reason for this is that we can restart the game in the middle of the game or at the end.
#The use will become clearer at the end or as you scroll through the code.
def game():

    #Putting the game stats in a dictionary
    gameStats = {
        #This is the amount of gems the user has at the start.
        "gemCount": 0,
        #In this, gemCount is the key and 0 is the value.

        #This is the number of lives the user has.
        "lives": 3,
        #In this, lives is the key and 3 is the value.

        #This is the number of wands the user has.
        "numWand": 0,
        #In this, numWand is the key and 0 is the value.

        #This is the number of swords the user has.
        "numSword": 0}

    userName = input("Before we start, what is your name?:\n")
    print()

    #This is the function for an invalid entry (e.g., putting "5" when 1 and 2 were the options.)
    def invalidReminder():
        print("Invalid choice.")

    #This is the intro message of the game.
    def intro():
        print("*** JOHNATHAN'S FOREST ***\n")
        print(f"Hello {userName}. You were driving along the highway and got into a crash, and passed out. \
You find yourself in this forest and you need to escape. Quick.")
        input("Press Enter to continue...")

    #This is the rules of the game.
    def gameRules():
        print("RULES:\n     1. You must collect 5 gems in order to escape.\n     2. You only have 3 lives. \
Finish them, and you restart your journey.\n     3. Choose wisely, your actions have consequences.\n")
        input("Press Enter to continue...")

    #These are game shortcuts.
    def shortcuts():
        print("SHORTCUTS:\n1. Options will have numbers assigned to them. Enter the number.\n")

    gameRules()
    print()
    shortcuts()

    #This is the function to restart the game.
    def restartCall():
        restartAsk = input("Would you like to play again?\n     1. Yes\n     2. No\n")
        #Checks if the user wants to restart the game by inputting "1".
        if restartAsk == "1":
            #If so, it re-runs the entire game. This is why we stored the game in a function.
            #It also resets the amount of gems to 0, as you can see here:
            gameStats["gemCount"] = 0
            #This re-runs the game.
            game()
        #Checks if the user wants to quit the game by inputting "2".
        elif restartAsk == "2":
            #If so, it stops the entire game, and displays a final message.
            print("Alright! Hope you enjoyed!")
        else:
            #This calls the invalidReminder function.
            invalidReminder()

    intro()
    print()

    def narrator1():
        print("While exploring the forest, you found a lamp on the floor.")
        input("Press Enter to continue...\n")
        print("You rubbed it and a genie appeared!")
        input("Press Enter to continue...\n")

    #Calls our narrator1 function.
    narrator1()

    #This is genie dialogue.
    def genieDialogue1():
        print("\"Hello lost explorer. I see that you have gotten lost in this forest.\"")
        # This delays the next message by 1.75 seconds.
        time.sleep(1.75)

        print("\"I can help you find your way out. But I'll need you to do something for me in return.\"")
        # This delays the next message by 1.75 seconds.
        time.sleep(1.75)

        print("\"A long time ago, I lost my precious gems in a fight with the Inferno Lord.\"")
        # This delays the next message by 1.75 seconds.
        time.sleep(1.75)

        print("\"I need those gems in order to cast wishes. Without them, I'm just a useless hunk of air.\"\n")
        # This delays the next message by 1.75 seconds.
        time.sleep(1.75)

    #This is the question if the user wants to help the genie or not.
    def genieChoice1():
        genieInput1 = input("\"So, lost explorer, will you help me find them?\"\n    1. Yes\n    2. No\n")
        if genieInput1 == "1":
            print("You decided to help the genie.")
            #return True shows that it is a true condition, and that you wanted to help the genie.
            return True
        elif genieInput1 == "2":
            print("You decided not to help the genie. You explored by yourself for a while, and got eaten by a bear. You died.")
            restartCall()
            #return False shows taht it is a false condition, and that you don't want to help the genie.
            return False
        else:
            #This calls invalidReminder function.
            invalidReminder()
            #This re-calls this function as the input was invalid.
            genieChoice1()

    #This calls the genie dialogue function we created.
    genieDialogue1()

    #This calls the question function we created and checks if it is false. If it is false (eg, the player doesn't want to help
    #the geinie)
    if genieChoice1() == False:
        #This will exit the game if the player does not want to help the genie and not play again.
        return
        #We don't have to do if genieChoice1() == True:, as then it will just continue. We would also have to do while True to the
        #whole code aswell, and we don't want to do that.

    #This is genie dialogue #2.
    def genieDialogue2():
        print("\n\"Alright! Let me get you on your first mission!\"")
        time.sleep(1.75)
        print("\"For this, you have to choose the correct chest. Choose the wrong one, and a poisonous snake pops out, killing you!\
 If you choose the right chest, you will get a wand or a sword and 2 gems. Both will be useful.\"")
        time.sleep(1.75)
        print("\"But don't worry! I will give you 3 lives before you die!\"")

    genieDialogue2()

    #This is the 1st mission the user goes into.
    #As you will update the key values, gameStats will be a parameter in this function.
    def mission1(gameStats):
        time.sleep(2)
        print("\nYou have been teleported!")
        choice1 = input("There is a chest on the left and a chest on the right. Which one do you choose?\n    1. Left\n    2. Right\n")
        if choice1 == "1":
            chest1 = random.randint(1, 2)
            if chest1 == 1:
                print("You chose the left chest. You got a wand and 2 gems!")
                gameStats["numWand"] = 1
            if chest1 == 2:
                print("You chose the left chest. You got a sword and 2 gems!")
                gameStats["numSword"] = 1

            gameStats["gemCount"] = 2
            print(f"Now you have {gameStats['gemCount']} gems!")

        if choice1 == "2":
            print("You chose the wrong test! A venomous snake popped out and you died!")
            gameStats["lives"] = 2
            print(f"You have {gameStats['lives']} lives left!")
            time.sleep(1)
            print("Uh oh! You lost a life! It's alright though.")
            print("Although you don't get any weapon, you still get 2 gems!")
            gameStats["gemCount"] = 2
            print(f"Now you have {gameStats['gemCount']} gems!")

    mission1(gameStats)

    time.sleep(2)
    print("\n\"Thanks! Now I'll teleport you to the second mission!\"")
    print("\"This time there will also only be 2 chests. But this time, one chest has a gem and the other has the ability to reverse time\
 and teleport you back to the start!\"")
    time.sleep(1.75)

    #As you will update the key values, gameStats will be a parameter in this function.
    def mission2(gameStats):
        print("\nYou have been teleported!")
        choice2 = input("There is a chest on the left and a chest on the right. Which one do you choose?\n    1. Left\n    2. Right\n")
        if choice2 == "1":
            #This updates the key gemCount to 3
            gameStats["gemCount"] = 3
            print("You chose the correct chest, and you got a gem!")
            print(f"Now you have {gameStats['gemCount']} gems!")
        if choice2 == "2":
            print("You chose the wrong chest! You teleported back to the start!")
            print("WHOOOSH!\n")
            #Again, this restarts the game.
            game()

    mission2(gameStats)

    def genieDialogue3():
        #The reason we are using so many functions is so that our game loop looks cleaner and we're only calling these functions in them.
        print("\"Whoowey! Thank god you found the right chest!\"")
        time.sleep(1.75)
        print("\"Before I get you to the 3rd mission, let me just remind you of your inventory and stats.\"")
        time.sleep(1.75)

    #Although we're using the keys in f-strings, we're not updating the values, so gameStats is not a parameter in this function.
    def inventoryReminder():
        if gameStats["numWand"] == 1:
            print(f"\"You have 1 wand, {gameStats['gemCount']} gems, and {gameStats['lives']} lives\"")
        elif gameStats["numSword"] == 1:
            print(f"\"You have 1 sword, {gameStats['gemCount']} gems, and {gameStats['lives']} lives\"")
        else:
            print(f"\"You have no weapons, {gameStats['gemCount']} gems, and {gameStats['lives']} lives\"")

    #This calls the function.
    inventoryReminder()

    def genieDialogue4(gameStats):
        time.sleep(1.75)
        print("\"Time for the final room!\"")
        time.sleep(1.75)
        print("\"This time, there is going to be a ghost guarding the final chest!\"")
        time.sleep(1.75)
        print("\"If you have a weapon, you can instantly kill it. If not, it will land a hit on you that has a 25% chance of killing you.\"")

    genieDialogue4(gameStats)

    def mission3(gameStats):
        print("\nWhoosh! You got teleported to the final room!")
        print("Oh no! The ghost is coming right at you!\n")

        #This creates a function inside the function, just like game().
        def ghostAttack(gameStats):
            print("The ghost hit you!")
            input("Hit it back! Press Enter to hit!")
            #This basically checks if the user has a weapon (from mission 1).
            if gameStats["numWand"] == 1 or gameStats["numSword"] == 1:
                print("Great! You had a weapon, so you killed the ghost in one hit!\n")
                return True
            #This is if the user does not have a weapon (from mission 1).
            elif gameStats["numWand"] == 0 and gameStats["numSword"] == 0:
                print("Oh no! You don't have a weapon!")
                #Picks a random number from 1 to 4.
                ghostHit1 = random.randint(1, 4)
                #This is what happens if the random number is 1.
                if ghostHit1 == 1:
                    print("Oh no! The ghost killed you!")
                    #This takes away a life, because the user died.
                    gameStats["lives"] -= 1
                    #While the lives is greater than 0 (meaning the user has lives to spare) this happens.
                    while  gameStats["lives"] > 0:
                        #Re-calls this function.
                        ghostAttack(gameStats)
                    #When lives becomes 0, we call restartCall().
                    restartCall()
                    return False
                #This is if the random number is 2, 3, or 4.
                else:
                    print("Great! You dodged the ghost! You can finally get the chest!\n")
                    return True
        #Calls the function and checks if it was false previously.
        if ghostAttack(gameStats) == False:
            return

        #From now, its just dialogue.
        time.sleep(1.75)
        print("\nYou opened the chest and got 2 more gems! You finally have enough!\n")
        gameStats['gemCount'] = 5
        (f"Now you have {gameStats['gemCount']} gems!\n")

    def genieDialogue5():
        print(f"\"Thank you {userName}! Give me my gems, and I will grant your wish to leave!\"")
        time.sleep(1.75)
        input("Press Enter to give.\n")
        print("\"Thank you again, and farewell traveller! And for your service, I want to give you a complimentary genie friend!\"")
        time.sleep(1.75)
        print("\"Whenever you need me, just call my name in the air, and I will come!\"")
        time.sleep(1.75)
        print("You: \"But what is your name?\"")
        time.sleep(1.75)
        print("\n\"Johnathan!\"")
        time.sleep(1.75)

    def outro():
        print("\nThe genie teleported you out of the forest. You saw your car in the end and drove away.\n\n")
        time.sleep(3)
        print("*** THANK YOU FOR PLAYING! ***\n")
        #Checks if the user wants to restart the game by inputting "1".
        restartCall()



    mission3(gameStats)
    genieDialogue5()
    outro()

#This runs the entire game.
game()

