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

  def file_loader_1_change(self, file, **event_args):
    # Upload the selected file into a Server Module
    c = FileLoader()
    anvil.server.call('get_financial_statement', file)
    
    c.clear()   
  def accounting_exercise_picker(self, file, **event_args):
    c.pick_time = True
    c.date = datetime.datetime.now()

  def clear_inputs(self):
    # Clear our three text boxes
    self.date_picker_1.date = ""
    self.text_box_1.text = ""
  
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
    Notification("Vos états financiers ont été importés !").show()
    self.clear_inputs()
    anvil.server.call('get_siren')
    anvil.server.call('get_accounting_exercise')

