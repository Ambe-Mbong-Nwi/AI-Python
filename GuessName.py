
Myname = "Ambe"
trial = 0
name = input("Hello you have three trials to guess my name \n")
if name == Myname:
    break
    print("Well done you guessed correctly")
    
elif name != Myname:
    name = input("Sorry that was incorrect but have two more trials\n")

if name == Myname:
    print("Well done you guessed correctly")

elif name != Myname:
   name = input("Sorry that was incorrect but have one last trial\n")

if name == Myname:
    print("Well done you guessed correctly")
else:
    print("Sorry you failed there are no more trials for you")