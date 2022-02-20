#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Application gui view
"""

__author__ = 'Mohamed Ouertani'

# Standard library imports
from tkinter import CENTER, RIGHT, Y
from tkinter import StringVar
from tkinter import messagebox
from tkinter import ttk
# Third party imports
import ttkthemes as themes
# Local application imports
from view_obj import View

class Interface(themes.ThemedTk,View):

    """GUI view class"""

    def __init__(self, controller):
        themes.ThemedTk.__init__(self)
        View.__init__(self,controller)
        self.widgets_labs = {}
        self.widgets_entry = {}
        self.widgets_button = {}
        self.title("Annuaire")
        self.set_theme("black")

    def get_value(self, key):
        """Get an input value"""
        return self.widgets_entry[key].get()

    def search_result(self,found_persons_list):
        """Display search result"""
        if not found_persons_list:
            messagebox.showwarning("Résultat recherche",
            "Aucune personne avec ce nom n'a été trouvée")
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
            person_id = 0
            for person in found_persons_list:
                search_table.insert(parent="",index='end',iid=person_id,
                                    text=f"Personne N°: {person_id+1}",
                                    value=(person["nom"],person["prenom"],person["telephone"],
                                    person["adresse"],person["ville"]))
                person_id += 1
            #Configure scrollbar
            search_table.pack()
            y_scroll_bar.config(command=search_table.yview)
        self._refresh_entries()

    def delete_result(self,deleted_elements,deletion=False):
        """Display deletion result"""
        if deletion:
            messagebox.showinfo("Delete results",
                                f"The following persons were deleted :\n - {deleted_elements}")
        else:
            messagebox.showinfo("Delete results",deleted_elements)
        self._refresh_entries()

    def delete_confirmation(self,persons_list):
        """Gets deletion confirmation before deleting persons"""
        persons_to_delete = ""
        for person in persons_list:
            persons_to_delete += f"""\n - {person["nom"]} {person["prenom"]}"""
        response = messagebox.askyesno("Deletion ?",
                                       "Are you sure you want to delete these persons?"
                                       +persons_to_delete)
        if not response:
            messagebox.showinfo("Deletion abortion","Deletion aborted")
            self._refresh_entries()
        return response


    def insert_result(self,insertion_message):
        """Display insertion result"""
        messagebox.showinfo("Insertion results",insertion_message)
        self._refresh_entries()

    def main(self):
        """Launch the GUI"""
        print("[View] main")
        self._create_fields()
        self._center_window()
        self.mainloop()

    def _create_fields(self):
        """Create all the widgets inside the main window"""
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
            button_w = ttk.Button(big_frame, text = idi, command=
            (lambda button=idi: self.controller.command_handle(button)))
            self.widgets_button[idi] = button_w
            button_w.grid(row=i+1,column=j,padx=5,pady=5)
            #self.widgets_button[idi].config(command = idi)

            j += 1

    def _center_window(self):
        """Center the GUI window inside the screen"""
        self.update() #update object states (used to return new value of h / w)
        width = self.winfo_width()
        height = self.winfo_height()
        x_offset = ((self.winfo_screenwidth() - width) // 2 )
        # // is to return int of devision not float
        y_offset = ((self.winfo_screenheight() - height) // 2 )
        self.geometry(f"{width}x{height}+{x_offset}+{y_offset}")

    def _refresh_entries(self):
        """Refresh all entry widgets"""
        for entry in self.widgets_entry.values():
            entry.delete(0,"end")
