#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Application gui view
"""

__author__ = 'Mohamed Ouertani'

from view_obj import View
from tkinter import CENTER, RIGHT, Y
from tkinter import StringVar
from tkinter import messagebox
from tkinter import ttk
import ttkthemes as themes

class Interface(themes.ThemedTk,View):
    def __init__(self, controller):
        themes.ThemedTk.__init__(self)
        View.__init__(self,controller)
        self.widgets_labs = {}
        self.widgets_entry = {}
        self.widgets_button = {}
        self.set_theme("black")
    
    def get_value(self, key):
        return self.widgets_entry[key].get()

    def create_fields(self):
        big_frame = ttk.Frame(self)
        big_frame.grid(row=0,column=0)
        i, j  = 0, 0

        for idi in self.entries:
            lab = ttk.Label(big_frame, text=idi.capitalize())
            self.widgets_labs[idi] = lab
            lab.grid(row=i,column=0)

            var = StringVar()
            entry = ttk.Entry(big_frame, text=var)
            self.widgets_entry[idi] = entry
            entry.grid(row=i,column=1,columnspan=2,padx=5,pady=5)

            i += 1

        for idi in self.functions:
            buttonW = ttk.Button(big_frame, text = idi, command=(lambda button=idi: self.controller.command_handle(button)))
            self.widgets_button[idi] = buttonW
            buttonW.grid(row=i+1,column=j,padx=5,pady=5)
            #self.widgets_button[idi].config(command = idi)

            j += 1
    
    def search_result(self,found_persons_list):
        if not found_persons_list:
            messagebox.showwarning("Résultat recherche","Aucune personne avec ce nom n'a été trouvée")
        else:
            #Create new search result window
            search_window = themes.ThemedTk()
            search_window.set_theme("black")
            search_window.title("Liste de personnes")
            search_window.geometry(f"700x150+{self.winfo_screenwidth()//4}+0")
            #Create frame inside search result window 
            search_frame = ttk.Frame(search_window)
            search_frame.pack()
            #Add scrolbar
            y_scroll_bar = ttk.Scrollbar(search_frame)
            y_scroll_bar.pack(side=RIGHT,fill=Y)
            #Create and fill search result table
            search_table = ttk.Treeview(search_frame,yscrollcommand=y_scroll_bar.set)
            search_table["columns"] = ("Nom", "Prenom", "Telephone", "Adresse", "Ville")
            search_table.column("#0",anchor=CENTER,width=120,minwidth=120)
            search_table.heading("#0",text="",anchor=CENTER)
            for column_name in search_table["columns"]:
                search_table.column(column_name,anchor=CENTER,width=120,minwidth=120)
                search_table.heading(column_name,text=column_name,anchor=CENTER)
            id = 0
            for person in found_persons_list:
                search_table.insert(parent="",index='end',iid=id,text=f"Personne N°: {id+1}",
                value=(person.get_nom(),person.get_prenom(),person.get_telephone(),
                person.get_adresse(),person.get_ville()))
                id += 1
            #Configure scrollbar
            search_table.pack()
            y_scroll_bar.config(command=search_table.yview)
        self.refresh_entries()

    def delete_result(self,deleted_elements):
        messagebox.showinfo("Delete results",deleted_elements)
        self.refresh_entries()
        
    def insert_result(self,insertion_message):
        messagebox.showinfo("Insertion results",insertion_message)
        self.refresh_entries()
    
    def main(self):
        print("[View] main")
        self.create_fields()
        self.title("Annuaire")
        self._center_window()
        self.mainloop()
    
    def _center_window(self):
        self.update() #update object states (used to return new value of h / w)
        width = self.winfo_width()
        height = self.winfo_height()
        x_offset = ((self.winfo_screenwidth() - width) // 2 ) 
        # // is to return int of devision not float
        y_offset = ((self.winfo_screenheight() - height) // 2 )
        self.geometry(f"{width}x{height}+{x_offset}+{y_offset}")

    def refresh_entries(self):
        for entry in self.widgets_entry.values():
            entry.delete(0,"end")
     