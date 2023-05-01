from ._anvil_designer import Form9_4Template
from anvil import *
import plotly.graph_objects as go
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form9_4(Form9_4Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.


  def button_1_click(self, **event_args):
    open_form('Form1', my_parameter="an_argument") #Accueil
