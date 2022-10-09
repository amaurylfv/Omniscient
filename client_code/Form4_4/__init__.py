from ._anvil_designer import Form4_4Template
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
import plotly.graph_objects as go


class Form4_4(Form4_4Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_3.items = app_tables.invoice.search()
    self.build_invoice_graph()
    

    # Any code you write here will run when the form opens.
    
  def build_invoice_graph(self):
      # Get the data from our server function, and store it as 'db_data'
      db_data_2 = anvil.server.call('get_invoice')
      
      # Create a Bar plot with this data, and change the colour of the markers
      self.plot_1.data = go.Bar(
        x = [x['date'] for x in db_data_2],
        y = [x['amount'] for x in db_data_2],
        marker=dict(color='#F7DC6F')
      )
      # Style the plot and add a plot title
      self.plot_1.layout.title = "Détail des charges"

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form4', my_parameter="an_argument")

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form1', my_parameter="an_argument")


