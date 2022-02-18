from view_obj import View
from model import Ensemble
from model import Person

class Controller():
    def __init__(self):
        # which_view = self.view_choice()
        # if which_view == 1 :
        #     print("You chose a GUI")
        # else:
        #     print("You chose a CLI")
        self.view = View(self)
        self.model = Ensemble()
    
    def view_choice(self):
        which_view = input("Type 1 for a GUI or 2 for a CLI : ")
        while which_view not in ["1","2"]:
            which_view = input("Type 1 for a GUI or 2 for a CLI : ")
        return which_view
    
    def start_view(self):
        self.view.create_fields()
        self.view.main()
    
    def search(self):
        nom = self.view.get_value("Nom")
        search_return = self.model.search_person(nom)
        self.view.search_results(search_return)
      
    def delete(self):
        first_name = self.view.get_value("Prenom")
        family_name = self.view.get_value("Nom")
        if not first_name or not family_name:
            message = "Please insert at least first name and family name to delete"
            self.view.delete_results(message)
        else:
            person_to_delete = self._create_person()
            delete_return = self.model.delete_person(person_to_delete)
            self.view.delete_results(delete_return)
    
    
    def insert(self):
        first_name = self.view.get_value("Prenom")
        family_name = self.view.get_value("Nom")
        if not first_name or not family_name:
            message = "Please insert at least first name and family name"
            self.view.insert_results(message)
        else:
            person_to_add = self._create_person()
            insert_return = self.model.insert_person(person_to_add)
            self.view.insert_results(insert_return)
    
    def refresh(self):
        self.view.refresh_entries()
    
    def _create_person(self):

        person = Person(self.view.get_value("Nom"),
            self.view.get_value("Prenom"),
            self.view.get_value("Telephone"),
            self.view.get_value("Adresse"),
            self.view.get_value("Ville"))
        return person

    def button_press_handle(self, buttonId):
        print("[Controller][button_press_handle] "+ buttonId)
        if buttonId == "Chercher":
            self.search()
        elif buttonId == "Effacer":
            self.delete()
        elif buttonId == "Inserer":
            self.insert()
        else:
            self.refresh()

    def save(self):
        self.model.save_persons()

    def load(self):
        self.model.load_persons()

    

if __name__ == "__main__":
    controller = Controller()
    controller.load()
    controller.start_view()
    controller.save()
