from ._anvil_designer import Form4Template
from anvil import *
import anvil.facebook.auth
import plotly.graph_objects as go
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..Form4_2 import Form4_2
from ..Form4_4 import Form4_4
from ..Form4_6 import Form4_6

class Form4(Form4Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.filled_area_chart()
    self.bar_chart()
    self.time_series_chart()

    # Any code you write here will run when the form opens.
    
  def button_1_click(self, **event_args):
    open_form('Form1', my_parameter="an_argument") #Accueil

  def button_3_click(self, **event_args):
    open_form('Form4_2', my_parameter="an_argument") #Gestion des tâches
    
  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form4_4', my_parameter="an_argument") #Analyse des coûts

  def button_7_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form4_6', my_parameter="an_argument") #Analyse des risques

  def filled_area_chart(self):
    fig = anvil.server.call('filled_area')
    self.plot_1.figure = fig

  def bar_chart(self):
    fig = anvil.server.call('bar_chart')
    self.plot_2.figure = fig
    
  def time_series_chart(self):
    fig = anvil.server.call('time_series_chart')
    self.plot_3.figure = fig


