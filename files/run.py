# WAP to demonstrate modules. Follow the following directory structure:
# ONLY FOLLOW THE STRUCTURE NOT THE FOLDER/FILE NAMES. So basically
# there should be three folders you can name them anything you want. Inside of each
# folder write a program containing a function. The program run.py (see above) will
# import all the three functions from the three folders and use them to demonstrate that
# it indeed used those functions in some meaningful way.
# [Name of the file main file should be run.py other files/folders can be named
# appropriately] (3 points)

from mod1 import first as one
from mod2 import second as two
from mod3 import third as three

def demo() -> None:
    one.function1()
    print()
    two.function2()
    print()
    three.function3()
    

if __name__ == '__main__':
    demo()

