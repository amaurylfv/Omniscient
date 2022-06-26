from ._anvil_designer import Form5Template
from anvil import *
import plotly.graph_objects as go
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..Form5_1 import Form5_1
from ..Form5_3 import Form5_3

class Form5(Form5Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.taux_profitabilité()

    # Any code you write here will run when the form opens.
    
  def button_1_click(self, **event_args):
    open_form('Form1', my_parameter="an_argument") #Accueil

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form5_1', my_parameter="an_argument") #Profitabilité

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form5_3', my_parameter="an_argument") #Rentabilité
  
  def build_structure_graph_6(self):
    # Get the data from our server function, and store it as 'db_data'
    db = anvil.server.call('get_sig')
      
      # Create a Bar plot with this data, and change the colour of the markers
    self.plot_1.data = go.Scatter(x = [x['Year'] for x in db],
                                  y = [x["Résultat_exploitation"] for x in db],
                                  mode='lines+markers',
                                  line=dict(color='#EAE2B7'))
  
  
  def taux_profitabilité(self, **event_args):
    db = anvil.server.call('taux_profitabilité')
    self.label_2.text = db
    
    
