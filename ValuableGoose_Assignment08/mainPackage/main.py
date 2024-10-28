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
   
   
    #print("Vehicle class test logic...")
    #car = Vehicle("Corvette")   # Instantiation of a Vehicle object 
    #print("Type attribute of Vehicle object:", car.get_type())
    #print("Changing the type of the object...")
    #car.set_type("GTO")
    #print("Type attribute of Vehicle object:", car.get_type())

    #print("\n\nTesting the repr method...")

    #print("From __repr__():", car.__repr__())
    #carCopy = eval(car.__repr__())
    #print("Copied car:", carCopy.__str__())

    #print("Type attribute of original Vehicle object:", car.get_type())
    #print("Type attribute of copied Vehicle object:", carCopy.get_type())
    
    stove = Stove()
    stove.set_status("on")
    stove.set_stoveLevel("medium")
    print(stove.show_statusLevel())
    
    stove.set_status("off")
    print(stove.show_statusLevel())

    try:
        stove.set_stoveLevel("high")   
    except ValueError as e:
        print(e)