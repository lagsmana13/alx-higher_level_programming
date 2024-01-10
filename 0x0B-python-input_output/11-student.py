#!/usr/bin/python3
"""
Contains the class "Student" representing a student.
"""


class Student:
    """Representation of a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of a Student instance
        with specified attributes.

        Args:
            attrs (list): (Optional) The attributes to include in the dictionary representation.
        Returns:
            dict: The dictionary representation of the Student instance.
        """
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for a in attrs:
            try:
                new_dict[a] = self.__dict__[a]
            except KeyError:
                pass
        return new_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance with the provided JSON.

        Args:
            json (dict): The JSON dictionary containing the attributes to replace.
        """
        for key in json:
            try:
                setattr(self, key, json[key])
            except KeyError:
                pass
