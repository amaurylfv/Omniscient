from ._anvil_designer import Form3_3Template
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
import json

class Form3_3(Form3_3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.bank_balance_graph()
    #self.treasury_graph()

    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form3', my_parameter="an_argument") #Retour

  def bank_balance_graph(self):
    data = anvil.server.call('bank_balance_chart')
    fig = json.loads(data)
    self.plot_1.data = fig['data']
    self.plot_1.layout = fig['layout']

  def treasury_graph(self):
    data = anvil.server.call('treasury_chart')
    fig = json.loads(data)
    self.plot_2.data = fig['data']
    self.plot_2.layout = fig['layout']
