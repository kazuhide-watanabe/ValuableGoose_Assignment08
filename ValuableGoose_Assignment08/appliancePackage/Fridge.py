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

# Fridge.py

class Fridge(object):
    """
   Model a fridge that can change temperature between 30 and 40 degrees Farenheit 
    """
    def __init__(self, temp):
        """
       Creates a starting point for the fridge once it is plugged in and sets it to the default 
       temperature of 37 degrees Fahrenheit
        """
        self.__temp = "37 degrees Fahrenheit"

    # gets the current temperature of the stove
    def get_fridgeTemp(self):
     
        return self.__temp
    
    # sets the fridge temperature
    def set_FridgeTemp(self, temp):
        tempRange = range(30,41)
        if temp in (tempRange):
            self.__ = temp
        else:
            print("Temperature cannot go out of 30-40 degrees Fahrenheit range")

    def __str__(self):
         return f"Fridge is {self.__temp}."

    def __repr__(self):
         return f"Fridge ('{self.__temp}')"

     
        
        





