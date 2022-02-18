#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pickle

class Person:
    def __init__(self, nom, prenom, telephone='', adresse='', ville=''):
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.adresse = adresse
        self.ville = ville
       # self.id =

    def get_nom(self):
        return self.nom

    def get_prenom(self):
        return self.prenom

    def get_telephone(self):
        return self.telephone

    def get_adresse(self):
        return self.adresse

    def get_ville(self):
        return self.ville

    def __str__(self):
        return f"{self.get_nom()} {self.get_prenom()}"


class Ensemble:
    def __init__(self):

        self.list_person = {}

    def insert_person(self, person):

        prenom = person.get_prenom()
        nom = person.get_nom()
        self.list_person[f"{prenom} {nom}"] = person
        return f"{prenom} {nom} was added successfully"

    def delete_person(self, person):

        prenom = person.get_prenom()
        nom = person.get_nom()
        if not prenom and not nom: 
            return "Please insert a name to delete"
        values_to_del = []
        for element in self.list_person.keys():
            if prenom in element or nom in element:
                values_to_del.append(element)
        if values_to_del:
            for to_del in values_to_del:
                del self.list_person[to_del]
                print('Deleted: '+to_del)
            return f"Deleted : {values_to_del}"
        return "No such name was found"

    def search_person(self, name):

        names_fetched = []
        for element in self.list_person.keys():
            if name in element:
                names_fetched.append(self.list_person[element])
        return (names_fetched)

        # if not name:
        #     return "Please insert a name to delete"
        # names_fetched = []
        # for element in self.list_person.keys():
        #     if name in element:
        #         names_fetched.append(self.list_person[element])
        # if not names_fetched:
        #     return f"No names corresponding to {name} were found"
        # return f"The corresponding names were found : {names_fetched}"
    
    def save_persons(self):

        with open('filename.pickle', 'wb') as handle:
            pickle.dump(self.list_person, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def load_persons(self):

        with open('filename.pickle', 'rb') as handle:
            list_persons = pickle.load(handle)
            self.list_person = list_persons

    def __str__(self):

        test = ''
        for element in self.list_person:
            test += element
        return test
