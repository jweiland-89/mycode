#!/usr/bin/python3
"""Catching specific errors | Alta3 Research"""

# Start with an infinite loop
while True:
    try:
        print("Let's divide x by y!")
        x = int(input("What is the integer value of X? "))
        y = int(input("what is the integer value of Y? "))
        print("The value of x/y: ", x/y)
    except ZeroDivisionError as zerr:
        print ("Handling run-time error:", zerr)
    # General error handling
    # a practival use might be exceptions we haven't designed solution for yet
    except Exception as err:
        #sys.exc_info returns a 3 tuple with info about the exception handled
        print("We did not anticipate that:", err)
