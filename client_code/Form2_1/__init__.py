from ._anvil_designer import Form2_1Template
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form2_1(Form2_1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.histogram()

    # Any code you write here will run when the form opens.
    
  def histogram(self):
    data = anvil.server.call('create_histogram')
    self.plot_1.figure = data