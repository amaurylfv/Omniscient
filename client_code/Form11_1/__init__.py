from ._anvil_designer import Form11_1Template
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form11_1(Form11_1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = anvil.server.call('get_invoice')
    self.build_structure_graph_1()
    self.build_pie_chart_issuer()
    self.issuer_map()

    # Any code you write here will run when the form opens.
    

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form11', my_parameter="an_argument") #Accueil

  def plot_1_click(self, points, **event_args):
    """This method is called when a data point is clicked."""
    pass

  def plot_2_click(self, points, **event_args):
    """This method is called when a data point is clicked."""
    pass

  def plot_3_click(self, points, **event_args):
    """This method is called when a data point is clicked."""
    pass

  

  
  def build_structure_graph_1(self):
    # Get the data from our server function, and store it as 'db_data'
    db = anvil.server.call('get_invoice')
      
      # Create a Bar plot with this data, and change the colour of the markers
    self.plot_1.data = go.Bar(
      x = [x['date'] for x in db],
      y = [x['amount'] for x in db],
      marker=dict(color='#f4a261')
    )
    
    # Style the plot and add a plot title
    self.plot_1.layout.title = "Evolution des charges"
    
    #Charge la plus élevée
    max_invoice = sorted(db, key=lambda x: x['amount'], reverse=True)[0]
    self.label_1.text = f"{max_invoice['amount']:}"    
    
    #Fournisseur principal
    max_issuer = sorted(db, key=lambda x: x['amount'], reverse=True)[0]
    self.label_2.text = f"{max_issuer['issuer']:}"
    
  def build_pie_chart_issuer(self):  
    fig = anvil.server.call('create_pie') 
    self.plot_2.figure = fig
    
    self.plot_2.layout.title = "Dépendance économique"
    
  def issuer_map(self):
    anvil.server.call('issuer_map')
    