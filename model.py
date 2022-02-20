#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Application model
"""

__author__ = 'Mohamed Ouertani'

# Standard library imports
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

    def delete_person(self, persons_list):
        """Delete existing persons"""
        names_list = []
        for person in persons_list:
            prenom = person["prenom"]
            nom = person["nom"]
            person_id = f"{prenom} {nom}"
            names_list.append(person_id)
            del self.list_person[person_id]
        deleted_persons = "\n - ".join(names_list)
        return f"{deleted_persons}"

    def search_person(self, name):
        """Search corresponding persons"""
        names_fetched = []
        for person in self.list_person.values():
            if name.upper() in person.get_nom().upper():
                names_fetched.append({"nom":person.get_nom(),
                                      "prenom":person.get_prenom(),
                                      "telephone":person.get_telephone(),
                                      "adresse":person.get_adresse(),
                                      "ville":person.get_ville()})
        return names_fetched


    def save_persons(self):
        """Save existing persons before exiting application"""
        with open('yearbook_save.pickle', 'wb') as handle:
            pickle.dump(self.list_person, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def load_persons(self):
        """Load existing persons while loading application"""
        with open('yearbook_save.pickle', 'rb') as handle:
            list_persons = pickle.load(handle)
            self.list_person = list_persons

    def __str__(self):
        return " ".join(self.list_person)
