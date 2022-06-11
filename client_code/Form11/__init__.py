from ._anvil_designer import Form11Template
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form11(Form11Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def button_2_click(self, **event_args):
    open_form('Form1', my_parameter="an_argument") #Accueil

    

  def file_loader_1_change(self, file, **event_args):
    # Upload the selected file into a Server Module
    c = FileLoader()
    invoice_data = anvil.server.call('get_invoice_data', file)
    c.clear()    

