from view_obj import View
from model import Ensemble
from model import Person

class Controller():
    def __init__(self):
        self.view = View(self)
        self.model = Ensemble()
    
    def start_view(self):
        self.view.create_fields()
        self.view.main()
    
    def search(self):
        nom = self.view.get_value("Nom")
        found_persons = self.model.search_person(nom)
        self.view.search_results_window(found_persons)
      
    def delete(self):
        person_to_delete = self._create_person()
        self.model.delete_person(person_to_delete)
        #TODO : add view part
    
    
    def insert(self):
        person_to_add = self._create_person()
        self.model.insert_person(person_to_add)
        #TODO : add view part
    
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
