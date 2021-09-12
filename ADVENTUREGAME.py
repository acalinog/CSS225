#ADVENTUREGAME
#Instructions
yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
actions = ["W", "A", "S", "D"]

import time

# Introduction
name = input("Hello! What is your name?\n")
print("Well hello, " + name + ". Let's get acquainted with the land!")
print("It is a sunny September morning. There is a dog laying on your porch and a cat meowing in the grass. Your house is green with moss and the air smells like apples.")
print("I hope you're an animal person because you will encounter many!\n")

#CHAPTER1
response = ""
while response not in yes_no:
    response = input("Should we introduce ourselves to our new friends?\nyes/no\n")
    if response == "yes":
        print("Great, an animal person? Let's head over to the porch now.\n")
    elif response == "no":
        print("That's okay! We can introduce ourselves to the locals first.")
        quit()
    else: 
        print("I'm sorry, can you try again.\n")
 
response = ""
while response not in directions:
    print("To your left, you see a broken down shed.")
    print("To your right, you see a large apple tree.")
    print("In front of you is your new house.")
    print("If you turn around, you'll head back into town square.\n")
    response = input("What direction would you like to go?\nleft/right/forward/backward\n")
    if response == "left":
        print("We will definitely have to fix this shed up. BUt you'll have to gather wood and learn how to use your tools " + name + ". We can do that tomorrow.")
        quit()
    elif response == "right":
        print("This is why we can smell apples in the air. What a lovely thing to have on the property.")
        quit()
    elif response == "forward":
        print("The dog will be so happy to meet someone new.\n")
        response = "" 
    elif response == "backward":
        print("We can say hello to the locals " + name + "!")
        quit()
    else:
        print("I'm sorry, can you try again.\n")

#CHAPTER2
print("The next day has apporached. Let's tackle it the best we can.")
print("As the rain pounded on the rooftop, the dog and cat slept by the fireplace. All that could be heard was the sounds of snores and rain.")
print("You learned quickly that the roof was weak and had many leaks.")
print("Let us venture out and find a way to fix the house.")

response = ""
while response not in yes_no:
    response = input("Should we head into town square to find a carpenter?\nyes/no\n")
    if response == "yes":
        print("Great,there should be a local carpentry building somewhere near.\n")
    elif response == "no":
        print("That's okay! We can always find something else to do.")
        quit()
    else: 
        print("I'm sorry, can you try again.\n")

#in town square
response = ""
while response not in directions:
    print("Left takes you to the doctor's office.")
    print("Going right will take you to the local grocery.")
    print("Forward takes us to the local carpenter.")
    print("Going backward takes us back to the house.")
    response = input("What direction would you like to go?\nleft/right/forward/backward\n")
    if response == "left":
        print("There is a doctor's office to your left. It looks very quaint. You should take note" + name + "That could come in handy if you aren't feeling well.")
    elif response == "right":
        print("To the right of you is a local grocery. We will most definitely need to head there at some point for plant seeds and snacks.\n")
    elif response == "forward":
        print("Moving forward takes us to the carpenter we are in search of!\n")
        print("We move forward and enter the building.")
        print("Let's introduce ourselves!")
        input("Should we approach the lady at the counter?\nyes/no\n")
        response == ""
    elif response == "backward":
        print("We cannot go back to the house to sleep " + name + "There is a lot to learn.")
        quit()
    else:
        print("I'm sorry, can you try again.\n")

#creating an interaction for a villager and the player
def villager():
    global npcName
    global response
    
#creating responses for the villagers to say
def responses():
    ["Hiya!", "Are you the new farmer?", "Where are you from?"]
def npcNameChoice():
    ["Aj", "Jake","Tristan", "Fredo"]
    
#shuffling the names 
def shuffle():
    shuffle (npcNameChoice)
    npcName = npcNameChoice[0]
    
    print(npcName, ":] Hello, I am", npcName, " , would you like to chat?")
    shuffle(responses)
    answer = input(print("Press y to talk to the villager"))
    if answer == "y":
        print(npcName, ":] ", responses[0])
    else: 
        print(npcName, ":] See ya")

#CHAPTER3
print("Its time to venture into the mines" + name + "!")
response = ""
while response not in yes_no:
    response = input("Should we go in? Do you have your weapon and tools?\nyes/no\n")
    if response == "yes":
        print("Awesome! Watch your surroundings and have fun!\n")
    elif response == "no":
        print("That's okay! We can do this another time.")
        quit()
    else: 
        print("I'm sorry, can you try again.\n")

response = ""
while response not in actions:
    print("Press W to hit the rock ahead of you.")
    print("Press A to hit the creature next to you.")
    print("Press S to move to the next floor.")
    print("Press D to leave the mines.\n")
    response = input("What direction would you like to go?\nW/A/S/S\n")
    if response == "W":
        print("Nice hit " + name + "! You found a gem.")
    elif response == "A":
        print("That creature was kind of scary. You didn't hit it very well and we will need to leave.\n")
        quit()
    elif response == "S":
        print("The difficulty of mining gets harder as we move floors.\n")
        response = "" 
    elif response == "D":
        print("Too scared " + name + "? We can try again later.")
        quit()
    else:
        print("I'm sorry, can you try again.\n")

#CHAPTER4
print("The sun shined down onto the land as you were coming back from the local grocery with vegetable seeds. There was a crispness to the air.")
response = ""
while response not in yes_no:
    response = input("Are you excited to be planting crops today," + name + "\nyes/no\n")
    if response == "yes":
        print("Yay! Lets start. \n")
    elif response == "no":
        print("That's okay! We can do this another time.")
        quit()
    else: 
        print("I'm sorry, can you try again.\n")

response = ""
while response not in directions:
    print("To your left, there is a water well. This is where you would refill your water pitcher.")
    print("To your right, you see a large patch of undisturbed soil.")
    print("In front of you is your new house.")
    print("If you turn around, you'll head back into town square.\n")
    response = input("What direction would you like to go?\nleft/right/forward/backward\n")
    if response == "left":
        print("You will need that water well after you have planted, " + name + "Fill up your water pitcher to water the plants after.")
    elif response == "right":
        print("This is the perfect spot to start planting!\n")
    elif response == "forward":
        print("The dog and cat seem to be watching you to see how you'll do. Lets not dissapoint.\n")
        response = "" 
    elif response == "backward":
        print("We can say hello to the locals later " + name + "!")
        quit()
    else:
        print("I'm sorry, can you try again.\n")

#CHAPTER5
print("The waves crashed against the wooden pier while the seagulls called out to each other. All that could be seen was the big blue ocean.")
print("TOday we learn how to fish!")
response = ""
while response not in yes_no:
    response = input("Have you fished before," + name + "?\nyes/no\n")
    if response == "yes":
        print("Great! So you're a pro. \n")
    elif response == "no":
        print("That's okay! Learning something new is always a good thing.")
    else: 
        print("I'm sorry, can you try again.\n")
        quit()
    