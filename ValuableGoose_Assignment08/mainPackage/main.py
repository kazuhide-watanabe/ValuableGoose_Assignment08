#*********************************
# Name: Kazuhide Watanabe, Alex Carnes, Alex Patton
# email:  watanake@mail.uc.edu
#         carnesas@mail.uc.edu
#         pattona6@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:  10/31/2024
# Course #/Section: IS 4010/001 
# Semester/Year:   Fall/2024
# Brief Description of the assignment:  
# Citations: In class notes
# Anything else that's relevant:   
#**********************************

# main.py

from appliancePackage.stove import Stove


if __name__ == "__main__":
   # Create an instance of the Stove class
    stove = Stove("off")

    # Invoke non-dunder methods
    # Set the stove status to "on" and change the heat setting
    print("Turning the stove on and to medium heat...")
    stove.set_status("on")
    print("Current Status:", stove.get_status())  
    stove.set_stoveLevel("medium")
    print("Heat Level:", stove.get_stoveLevel()) 

    # Display the current status and setting
    print(stove.show_statusLevel())
    print("\n")
    
    # Turn the stove off and display the status again
    print("Changing the status of the stove...")
    stove.set_status("off")
    print("Current Status:", stove.get_status())
    print("Current Heat Level:", stove.get_stoveLevel())
    print(stove.show_statusLevel())
    
    print("\n")
    
    # Setting the Heat Level while the stove is off to trigger the ValueError
    print("Attempting to set Heat Level while stove is off...")
    try:
        stove.set_stoveLevel("high")   
    except ValueError as err:
        print(err)  
    
    # Invoke dunder methods
    print("\n\nTesting the str and repr method...")
    print("String representation (__str__):", str(stove))  
    
    print("From __repr__():", stove.__repr__())
    newStove = eval(stove.__repr__())
    print("New Stove:", newStove.__str__())
    