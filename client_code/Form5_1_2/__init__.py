from ._anvil_designer import Form5_1_2Template
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

class Form5_1_2(Form5_1_2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repartition_valeur_ajoutee()
    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    open_form('Form5_1', my_parameter="an_argument") #Retour

  def repartition_valeur_ajoutee(self):
    fig = anvil.server.call('partage_de_la_va')
    self.image_1.source = fig
    