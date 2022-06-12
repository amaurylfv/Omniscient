from ._anvil_designer import Form5Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..Form5_1 import Form5_1

class Form5(Form5Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
  def button_1_click(self, **event_args):
    open_form('Form1', my_parameter="an_argument") #Accueil

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form5_1', my_parameter="an_argument") #Profitabilité


