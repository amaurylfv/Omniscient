from ._anvil_designer import Form13Template
from anvil import *
import anvil.facebook.auth
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime 

class Form13(Form13Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
  def clear_inputs(self):
    # Clear our three text boxes
    self.date_picker_1.date = ""
    self.text_box_1.text = ""
    
  def file_loader_1_change(self, file, **event_args):
    # Upload the selected file into a Server Module
    c = FileLoader()
    alert(content="Êtes-vous-sûr ?",
               title="Importation",
               large=True,
               buttons=[
                 ("Oui", "YES"),
                 ("Non", "NO"),
               ])
    anvil.server.call('get_financial_statement', file)
    self.file_loader_1.clear()
    Notification("Les Etats financiers ont bien été importés !").show()
       
  def accounting_exercise_picker(self, file, **event_args):
    c.pick_time = True
    c.date = datetime.datetime.now()
  
  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    date = self.date_picker_1.date
    siren_query = self.text_box_1.text
    accounting_exercise_query = int(date.strftime('%Y%m%d'))

    dict = {	
			'siren_query' : siren_query ,
			'accounting_exercise_query' : accounting_exercise_query,
				}
    
    anvil.server.call('add_siren_and_accounting_exercise', dict)
    Notification("Requête en cours...").show()
    self.clear_inputs()
    anvil.server.call('get_siren')
    anvil.server.call('get_accounting_exercise')
    anvil.server.call('find_financial_statement')

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1', my_parameter="an_argument") #Accueil

  def button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert(content="Êtes-vous-sûr ?",
               title="Réinitialisation",
               large=True,
               buttons=[
                 ("Oui", "YES"),
                 ("Non", "NO"),
               ])
    anvil.server.call('delete_all_financials_statements')
    Notification("Tous les états financiers présents dans la base de données ont été supprimés.").show()



