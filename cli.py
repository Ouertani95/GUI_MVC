#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Application cli view
"""

__author__ = 'Mohamed Ouertani'

# Standard library imports
from builtins import input
# Third party imports
import cmd2
# Local application imports
from view_obj import View


class CLI(cmd2.Cmd,View):

    """CLI view class"""

    def __init__(self,controller):
        cmd2.Cmd.__init__(self)
        View.__init__(self,controller)
        self.entries_values = {entry:"" for entry in self.entries}

    def get_value(self, key):
        """Get an input value"""
        return self.entries_values[key]

    def do_insert(self,args):
        """Get person informations to be inserted"""
        print(args)
        self.entries_values = {entry:"" for entry in self.entries}
        for entry in self.entries:
            self.entries_values[entry] = str(input(f"Saisir {entry} : "))
        # print(self.entries_values)
        self.controller.command_handle("Inserer")

    def insert_result(self,insertion_message):
        """Print insertion result"""
        self.poutput(cmd2.style(insertion_message, fg=cmd2.Fg.GREEN))

    def do_delete(self,args):
        """Get person informations to be deleted"""
        print(args)
        self.entries_values = {entry:"" for entry in self.entries}
        self.entries_values["Nom"] = str(input("Saisir Nom : "))
        self.controller.command_handle("Effacer")

    def delete_result(self,deleted_elements,deletion=False):
        """Print deletion results"""
        if deletion:
            self.poutput(cmd2.style(f"The following persons were deleted :\n - {deleted_elements}",
                        fg=cmd2.Fg.RED))
        else:
            self.poutput(cmd2.style(deleted_elements,fg=cmd2.Fg.RED))

    def delete_confirmation(self,persons_list):
        """Gets deletion confirmation before deleting persons"""
        persons_to_delete = ""
        for person in persons_list:
            persons_to_delete += f"""\n - {person["nom"]} {person["prenom"]}"""
        response = str(input("Are you sure you want to delete these persons?"
                            +persons_to_delete+"\n (type y or n ?) : "))
        while response not in ["y","n"]:
            response = str(input("Are you sure you want to delete these persons?"
                                +persons_to_delete+"\n (type y or n ?) : "))
        if response == "n":
            self.poutput(cmd2.style("Deletion aborted", fg=cmd2.Fg.RED))
            response = False
        else:
            response = True
        return response

    def do_search(self,args):
        """Get person informations to be searched"""
        print(args)
        self.entries_values["Nom"] = str(input("Saisir Nom : "))
        self.controller.command_handle("Chercher")

    def search_result(self, found_persons_list):
        """Print search results"""
        if not found_persons_list:
            result = "No persons were found"
            self.poutput(cmd2.style(result, fg=cmd2.Fg.RED))
        else:
            result = "the following persons were found : "
            self.poutput(cmd2.style(result, fg=cmd2.Fg.GREEN))
            for person in found_persons_list:
                person_id = f"""{person["nom"]} {person["prenom"]}"""
                self.poutput(cmd2.style(person_id, fg=cmd2.Fg.BLUE))

    def main(self):
        """Launch the CLI interface"""
        self.cmdloop()
