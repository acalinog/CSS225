#Chapter 1 


def start():
    print("Hello! What is your name?")
    print("It was a sunny September morning. There was a dog laying on the porch and a cat meowing in the grass. The house was green with moss and the air smelled of apples.")

#player needs to pick which animal to interact with first. Dog or cat? or if they want to chat with locals first.

def animal():
    print("Which animal would you like to chat with first? Or would you like to chat with the locals?")
    answer = input(animal or locals"):
        d = porch_dog()
        c = grass_cat()
        l = locals_chat()
        if "d" in answer:
            porch_dog()
            #d to chat with the dog
        elif "c" in answer:
            grass_cat()
            #c to chat with the cat
        else "l" in answer:
            locals_chat()
            #l to chat with locals

def land():
    print("You should explore your new land!")


