from ._anvil_designer import Form2_3Template
from anvil import *
import anvil.facebook.auth
import plotly.graph_objects as go
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form2_3(Form2_3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.histogram()

    # Any code you write here will run when the form opens.

  def histogram(self):
    data = anvil.server.call('create_histogram')
    self.plot_1.figure = data

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form2', my_parameter="an_argument") #Retour
