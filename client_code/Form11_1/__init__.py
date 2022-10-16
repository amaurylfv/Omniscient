from ._anvil_designer import Form11_1Template
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

class Form11_1(Form11_1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = anvil.server.call('get_invoice')
    self.nombre_factures()

    # Any code you write here will run when the form opens.
    

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form11', my_parameter="an_argument") #Retour

  def plot_1_click(self, points, **event_args):
    """This method is called when a data point is clicked."""
    pass

  def plot_2_click(self, points, **event_args):
    """This method is called when a data point is clicked."""
    pass

  def plot_3_click(self, points, **event_args):
    """This method is called when a data point is clicked."""
    pass

  def nombre_factures(self):
    db = anvil.server.call('nombre_de_factures')
    self.label_1.text = db
  
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    csv_file = anvil.server.call('invoice_data_to_csv')
    media = BlobMedia('text/plain', csv_file.get_bytes(), name='export.csv')
    download(media)
    

