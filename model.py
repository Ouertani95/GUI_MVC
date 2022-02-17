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
        return f"""{self.get_nom()} {self.get_prenom()}"""


class Ensemble:
    def __init__(self):
        self.list_person = {}

    def insert_person(self, person):
        if isinstance(person, Person):
            prenom = person.get_prenom()
            nom = person.get_nom()
            self.list_person[f"{prenom} {nom}"] = person
            print(f'Added: {prenom} {nom}')
    def delete_person(self, person):

        #TODO : modify deletion with empty string
        
        if isinstance(person, Person):
            prenom = person.get_prenom()
            nom = person.get_nom()
           # del self.list_person[]
            if not prenom and not nom: 
                print("STAHP")
            else:
                values_to_del = []
                for element in self.list_person.keys():
                    if prenom in element or nom in element:
                        values_to_del.append(element)
                if values_to_del:
                    for to_del in values_to_del:
                        del self.list_person[to_del]
                        print('Deleted: '+to_del)
                else:
                    print("no such name was found")

    def search_person(self, name):
        names_fetched = []
        for element in self.list_person.keys():
            if name in element:
                names_fetched.append(self.list_person[element])
        return (names_fetched)
    
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
