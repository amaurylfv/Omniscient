from ._anvil_designer import Form4_6Template
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables





class Form4_6(Form4_6Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.build_cost_graph_1()
    self.build_cost_graph_2()
    

    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form4', my_parameter="an_argument")

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form1', my_parameter="an_argument")
    
  def build_cost_graph_1(self):
      # Get the data from our server function, and store it as 'db_data'
      db_data_2 = anvil.server.call('get_invoice')
      
      # Create a Bar plot with this data, and change the colour of the markers
      self.plot_1.data = go.Bar(
        x = [x['issuer'] for x in db_data_2],
        y = [x['amount_untaxed'] for x in db_data_2],
        marker=dict(color='#E35F30')
      )
      # Style the plot and add a plot title
      self.plot_1.layout.title = "Typologie des charges"
      