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

# Stove.py

class Vehicle(object):
    """
    Model a vehicle for sale by a retail operation. This is a very incomplete model.
    """
    def __init__(self, type):
        """
        Constructor (duh)
        @param type String: The type of vehicle
        
        """
        self.__type = type

    def get_type(self):
        """
        @return String: The vehicle type of the current object
        """
        return self.__type
    
    def set_type(self, type):
        """
        Assign a value to the vehicle type of the current object
        @param type String: The vehicle type to be assigned.
        """
        self.__type = type
        
    def print_type(self):
        """
        Print the vehicle type of the current object
        """
        print(self.__type)
        
    def __str__(self):
        """
        @return String: A human-readable basic representation of the current object. 
        Useful for debugging, documentation, etc.
        """
        return "type: " + self.__type

    def __repr__(self):
        """
        @return String: A string containing code that can be executed to create a copy of the current object
        """
        return f"Vehicle('{self.__type}')"


