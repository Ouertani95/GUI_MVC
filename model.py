#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Application model
"""

__author__ = 'Mohamed Ouertani'

import pickle

class Person:

    """Person class"""

    def __init__(self, nom, prenom, telephone='', adresse='', ville=''):
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.adresse = adresse
        self.ville = ville

    def get_nom(self):
        """Get family name attribute of person"""
        return self.nom

    def get_prenom(self):
        """Get first name attribute of person"""
        return self.prenom

    def get_telephone(self):
        """Get phone number attribute of person"""
        return self.telephone

    def get_adresse(self):
        """Get address attribute of person"""
        return self.adresse

    def get_ville(self):
        """Get city attribute of person"""
        return self.ville

    def __str__(self):
        return f"{self.get_nom()} {self.get_prenom()}"


class Ensemble:
    """Ensemble class"""
    def __init__(self):

        self.list_person = {}

    def insert_person(self, person):
        """Insert new person"""
        prenom = person.get_prenom()
        nom = person.get_nom()
        self.list_person[f"{prenom} {nom}"] = person
        return f"{prenom} {nom} was added successfully"

    def delete_person(self, person):
        """Delete existing persons"""
        nom = person.get_nom()
        if not nom:
            return "Please insert a name to delete"
        values_to_del = []
        for element in self.list_person.keys():
            if nom.upper() in element.upper():
                values_to_del.append(element)
        if values_to_del:
            for to_del in values_to_del:
                del self.list_person[to_del]
                print('Deleted: '+to_del)
            return f"Deleted : {values_to_del}"
        return "No such name was found"

    def search_person(self, name):
        """Search corresponding persons"""
        names_fetched = []
        for element in self.list_person.keys():
            if name.upper() in element.upper():
                names_fetched.append(self.list_person[element])
        return names_fetched


    def save_persons(self):
        """Save existing persons before exiting application"""
        with open('filename.pickle', 'wb') as handle:
            pickle.dump(self.list_person, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def load_persons(self):
        """Load existing persons while loading application"""
        with open('filename.pickle', 'rb') as handle:
            list_persons = pickle.load(handle)
            self.list_person = list_persons

    def __str__(self):
        return " ".join(self.list_person)
