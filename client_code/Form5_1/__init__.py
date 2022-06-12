from ._anvil_designer import Form5_1Template
from anvil import *
import plotly.graph_objects as go
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..Form5_1_1 import Form5_1_1

class Form5_1(Form5_1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.build_structure_graph_1()

    # Any code you write here will run when the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form1', my_parameter="an_argument") #Accueil 

  def button_2_click(self, **event_args):
    open_form('Form5', my_parameter="an_argument") #Retour

  def button_1_click(self, **event_args):
    open_form('Form5_1_1', my_parameter="an_argument") #SIG

  def build_structure_graph_1(self):
    # Get the data from our server function, and store it as 'db_data'
    db = anvil.server.call('get_sig')
      
      # Create a Bar plot with this data, and change the colour of the markers
    self.plot_1.data = go.Bar(
      x = [x['Year'] for x in db],
      y = [x['EBE'] for x in db],
      marker=dict(color='#FCBF49')
    )
    # Style the plot and add a plot title
    self.plot_1.layout.title = "Structure financière"

  def build_structure_graph_2(self):
    # Get the data from our server function, and store it as 'db_data'
    db = anvil.server.call('get_sig')
      
      # Create a Bar plot with this data, and change the colour of the markers
    self.plot_2.data = go.Bar(
      x = [x['Year'] for x in db],
      y = [x['EBE'] for x in db],
      y = [x['Marge commerciale'] for x in db],
      marker=dict(color='#FCBF49')
    )
    # Style the plot and add a plot title
    self.plot_1.layout.title = "Structure financière"

