#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Application view superclass
"""

__author__ = 'Mohamed Ouertani'

class View():

    """View superclass"""

    def __init__(self, controller):
        self.controller = controller
        self.entries = ["Nom", "Prenom", "Telephone", "Adresse", "Ville"]
        self.functions = ["Chercher", "Inserer", "Effacer"]

    def get_value(self, key):
        """Get an input value"""


    def search_result(self,found_persons_list):
        """Display search result"""


    def delete_result(self,deleted_elements):
        """Display deletion result"""


    def insert_result(self,insertion_message):
        """Display insertion result"""


    def main(self):
        """Launch the view"""
