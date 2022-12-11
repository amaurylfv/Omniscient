from ._anvil_designer import Form3Template
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import json

from ..Form3_1 import Form3_1
from ..Form3_10 import Form3_10

class Form3(Form3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def button_1_click(self, **event_args):
    open_form('Form1', my_parameter="an_argument") #Accueil

  def button_11_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form3_10', my_parameter="an_argument") #Compte de résultat

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form3_1', my_parameter="an_argument") #Trésorerie




