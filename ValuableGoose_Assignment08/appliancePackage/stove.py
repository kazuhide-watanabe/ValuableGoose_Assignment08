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
# Brief Description of what this module does: Creates a class called stove that gets and sets the stove status and heat level
#then prints the current state of both. Includes error handling
# Citations: In class work, Bill Nicholson
# Anything else that's relevant: This Class was assigned to Alex Carnes
#**********************************

# Stove.py

class Stove(object):
    """
    Model a stove being turned on and set to a specific heat level. The stove starts off with a heat level of none. It can 
    be turned on and set to three heat levels: low, medium, and high.
    """
    def __init__(self):
        """
        Creates the starting point for the stove. The stove starts off with a heat level of none.
        """
        self.__status = 'off'
        self.__stoveLevel = 'none'

    def get_status(self):
        """
        Get the current status of the stove.
        @return String: The current status of the Stove. Is it on?
        """
        return self.__status
    
    def set_status(self, status):
        """
        Set the status of the stove to on or off.
        @param status String: The stove status to be assigned.
        @raise value error: If status isn't on or off
        """
        if status in ["on", "off"]:
            self.__status = status
            if self.__status == "off":
                self.__stoveLevel = "none"
        else:
            raise ValueError("The Stove's Status can only be 'on' or 'off'.")
     
    def get_stoveLevel(self):
        """
        Get the current heat level of the stove.
        @return String: The current heat level of the stove, is it none, low, medium, or high?
        """
        return self.__stoveLevel
    
    def set_stoveLevel(self, level):
        """
        Set a heat level to the stove.
        @param level String: The appliance heat level to be assigned 
        @raise value error: If heat level isn't low, medium, or high, or if the stove is off
        """
        if self.__status != "on":
            raise ValueError("The heat level cannot be set while the Stove is off")
        
        if level in ["low", "medium", "high"]:
            self.__stoveLevel = level
        else:
            raise ValueError("Stove level can only be equal to low, medium, or high")
                
        
    def show_statusLevel(self):
        """
        Print the current status and heat level of the stove
        @print str:the current status and the heat level of the stove
        """
        return f"Stove is {self.__status} and the heat level is set to {self.__stoveLevel}."
        
    #documentation needs to be edited
    def __str__(self):
        """
        @return String: A human-readable basic representation of the current object. 
        Useful for debugging, documentation, etc.
        """
        return f"Stove is {self.__status} and the heat level is set to {self.__stoveLevel}."
    # documentation needs to be edited
    def __repr__(self):
        """
        @return String: A string containing code that can be executed to create a copy of the current object
        """
        return f"Stove is {self.__status} and the heat level is set to {self.__stoveLevel}."
