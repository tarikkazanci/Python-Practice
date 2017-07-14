input('Hello, welcome to my first Awesome Python App')

# Get user input. Whatever user inputs grab that and display to user with some message.
name = input('What is your name?')
print('Welcome', name)

python = input("Do you like Python? Y/N")

# Get user input. If user enters "Y" print that else print another one.
if python == 'Y':
    print("That's cool")
else:
    print("That sucks. You should learn it!")

askgame = input("Let's play a game. Are you ready? Y/N")

if askgame == 'Y':
    print("Alright")
else:
    print('Get the hell out of my program!')
    print('Just kidding')

# Get user input. If user enters right answer verify user answer. Otherwise reject user's answer

mathquest = input("What is the result of 5*4*3*2*1?")
if mathquest == "120":
    print("Got it!")
else:
    print("Are you kidding me?")

input('Here is another question')

lastquest = input("What is the capital city of Turkey?")
if lastquest == "Ankara":
    print("You're the best!")
else:
    print("Wrong answer")

input('Thank you for joining my app...')
