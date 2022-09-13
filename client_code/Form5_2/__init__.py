from ._anvil_designer import Form5_2Template
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

class Form5_2(Form5_2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.line_chart_1()

    # Any code you write here will run when the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form1', my_parameter="an_argument") #Accueil

  def button_1_click(self, **event_args):
    open_form('Form5_1', my_parameter="an_argument") #Retour


  def line_chart_1(self):
    fig = anvil.server.call('ploty_test')
    self.image_1.source = fig
