#*********************************
# Name: Kazuhide Watanabe, Alex Carnes, Alex Patton
# email:  watanake@mail.uc.edu
#         carnesas@mail.uc.edu
#         pattona6@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:  10/31/2024
# Course #/Section: IS 4010/001 
# Semester/Year:   Fall/2024
# Brief Description of the assignment: Group project where each member creates a class to be called to the main module.
# Brief Description of what this module does: Creates a class called fridge and sets a default temperature for the fridge once it is plugged in. 
# After that you are able to change the temperature of the fidge between a cetain range. 
# Citations: In class notes, Bill Nicholson
# Anything else that's relevant:  This Class was assigned to Alex Patton
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
        @param temp int: The temperature of the vehicle
        """
        self.__temp = temp

    def get_fridgeTemp(self):
        """
        Gets the current temperature of the fridge.
        @return int: The current temperature of the fridge. 
        """
        return self.__temp
    
    def set_FridgeTemp(self, temp):
        """
        Set the temperature of the fridge to a value between 30 and 40
        @param temp int: The desired fridge temperature in fahrenheit.
        @print: A warning message if the temperatue is outside the valid range.
        """
        tempRange = range(30,41)
        if temp in (tempRange):
            self.__temp = temp
        else:
            print("Temperature cannot go out of 30-40 degrees Fahrenheit range")

    def __str__(self):
        """
        Returns a string representation of the current fridge temperature.
        @return String: A message displaying the current fridge temperature in Fahrenheit.
        """
        return f"The current fridge temperature is {self.__temp} degrees fahrenheit."

    def __repr__(self):
        """
        Returns a formal string representation of the Fridge object, including its current temperature. 
        @return String: A string containing the temperature code that can be executed to create a copy of the current object
        """
        return f"Fridge ('{self.__temp}')"

     
        
        





