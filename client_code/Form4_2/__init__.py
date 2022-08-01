from ._anvil_designer import Form4_2Template
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

class Form4_2(Form4_2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.gantt_chart()

    # Any code you write here will run when the form opens.
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form4', my_parameter="an_argument")# Retour  
    
  def gantt_chart(self):
    gantt_chart = anvil.server.call('create_gantt_chart')
    self.plot_1.figure = gantt_chart


