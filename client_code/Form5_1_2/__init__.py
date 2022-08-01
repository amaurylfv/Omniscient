from ._anvil_designer import Form5_1_2Template
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

class Form5_1_2(Form5_1_2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.build_pie_chart_1()
    self.build_pie_chart_2()
    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    open_form('Form5_1', my_parameter="an_argument") #Retour

    
  def build_pie_chart_1(self):
    # Get the data from our server function, and store it as 'db_data'
    fig = anvil.server.call('create_fig') 
    self.plot_1.figure = fig
    
  def build_pie_chart_2(self):  
    fig = anvil.server.call('create_pie') 
    self.plot_2.figure = fig