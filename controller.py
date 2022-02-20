#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Application controller
"""

__author__ = 'Mohamed Ouertani'

# Standard library imports
from builtins import input
# Local application imports
from gui import Interface
from cli import CLI
from model import Ensemble
from model import Person

class Controller():

    """Controller class in MVC model for application """

    def __init__(self):
        which_view = self.view_choice()
        if which_view == "1" :
            print("You chose a GUI")
            self.view = Interface(self)
        elif which_view == "2":
            print("You chose a CLI")
            self.view = CLI(self)
        self.model = Ensemble()

    @staticmethod
    def view_choice():
        """Choose between different views"""
        which_view = input("Type 1 for a GUI or 2 for a CLI : ")
        while which_view not in ["1","2"]:
            which_view = input("Type 1 for a GUI or 2 for a CLI : ")
        return which_view

    def start_view(self):
        """Launch the chosen view"""
        self.view.main()

    def search(self):
        """Control the search process between model and view"""
        nom = self.view.get_value("Nom")
        search_return = self.model.search_person(nom)
        self.view.search_result(search_return)

    def delete(self):
        """Control the deletion process between model and view"""
        family_name = self.view.get_value("Nom")
        if not family_name:
            message = "Please insert a family name to delete"
            self.view.delete_result(message)
        else:
            search_return = self.model.search_person(family_name)
            if not search_return:
                message = "No persons to delete with this name"
                self.view.delete_result(message)
            else:
                person_to_delete = self._create_person()
                delete_return = self.model.delete_person(person_to_delete)
                self.view.delete_result(delete_return)


    def insert(self):
        """Control the insertion process between model and view"""
        first_name = self.view.get_value("Prenom")
        family_name = self.view.get_value("Nom")
        if not first_name or not family_name:
            message = "Please insert at least first name and family name"
            self.view.insert_result(message)
        else:
            person_to_add = self._create_person()
            insert_return = self.model.insert_person(person_to_add)
            self.view.insert_result(insert_return)


    def _create_person(self):
        """Create a person object from input"""
        person = Person(self.view.get_value("Nom"),
            self.view.get_value("Prenom"),
            self.view.get_value("Telephone"),
            self.view.get_value("Adresse"),
            self.view.get_value("Ville"))
        return person

    def command_handle(self, command_id):
        """Identify chosen function and apply appropriate method"""
        if command_id == "Chercher":
            self.search()
        elif command_id == "Effacer":
            self.delete()
        elif command_id == "Inserer":
            self.insert()

    def save(self):
        """Save data in model before exiting the application"""
        self.model.save_persons()

    def load(self):
        """Load data in model while launching the application"""
        self.model.load_persons()


if __name__ == "__main__":
    controller = Controller()
    controller.load()
    controller.start_view()
    controller.save()
