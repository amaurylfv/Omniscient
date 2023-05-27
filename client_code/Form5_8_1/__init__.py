from ._anvil_designer import Form5_8_1Template
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import plotly.graph_objects as go
import anvil.server
from tables import app_tables
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form5_8_1(Form5_8_1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = anvil.server.call('get_sig')

    # Any code you write here will run when the form opens.


  def button_1_click(self, **event_args):
    open_form('Form5_1', my_parameter="an_argument") #Retour
