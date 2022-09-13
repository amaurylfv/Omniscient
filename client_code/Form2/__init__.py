from ._anvil_designer import Form2Template
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..Form2_1 import Form2_1

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.map_chart()
    #self.funnel_chart()

    # Any code you write here will run when the form opens.
  
  def button_1_click(self, **event_args):
    open_form('Form1', my_parameter="an_argument") #Accueil

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form2_1', my_parameter="an_argument") #Prévision des ventes
  def map_chart(self):
    self.plot_1.figure = anvil.server.call('map_chart')
