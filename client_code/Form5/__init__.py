from ._anvil_designer import Form5Template
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..Form12 import Form12

class Form5(Form5Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
  def button_2_click(self, **event_args):
    open_form('Form1', my_parameter="an_argument") #Accueil

  def button_1_click(self, **event_args):
    open_form('Form12', my_parameter="an_argument") #Marketing

