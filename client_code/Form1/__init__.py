from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.build_revenue_graph()
    self.build_marketing_graph()
    
  def build_revenue_graph(self):
    # Get the data from our server function, and store it as 'db_data'
    db_data = anvil.server.call('get_revenue')

    # Create a Bar plot with this data, and change the colour of the markers
    self.plot_1.data = go.Bar(
      x = [x['date'] for x in db_data],
      y = [x['amount'] for x in db_data],
      marker=dict(color='#2196f3')
    )
  
  def build_marketing_graph(self):
    # We’re calling a function on your local machine from the web!
    # Get the data and store it as 'marketing_data'
    marketing_data = anvil.server.call('get_marketing_data')
    # Create a Line plot with this data, and change the colour of the line
    self.plot_3.data = go.Scatter(x = [x['strategy'] for x in marketing_data],
                                  y = [x['count'] for x in marketing_data],
                                  mode='lines+markers',
                                  line=dict(color='#2196f3'))