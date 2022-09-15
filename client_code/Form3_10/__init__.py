from ._anvil_designer import Form3_10Template
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


class Form3_10(Form3_10Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #self.vmp_graph()
    #self.disponibilites_graph()
    #self.Concours_bancaires_courants_et_soldes_crediteurs_de_banques_et_C_C_P_graph()

    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form3', my_parameter="an_argument") #Retour

  def vmp_graph(self):
    db_data = anvil.server.call('display_financial_statement')
    self.plot_1.data = go.Scatter(
    x = [x['date_cloture_exercice'] for x in db_data],
    y = [x['Valeurs_mobilieres_de_placement_m1'] for x in db_data],
    fill=None,
    mode='lines',
    color='green',
    )

  def disponibilites_graph(self):
    db_data = anvil.server.call('display_financial_statement')
    self.plot_2.data = go.Scatter(
    x = [x['date_cloture_exercice'] for x in db_data],
    y = [x['Disponibilites_m1'] for x in db_data],
    fill=None,
    mode='lines',
    color='green',
    )
  def Concours_bancaires_courants_et_soldes_crediteurs_de_banques_et_C_C_P_graph(self):
    db_data = anvil.server.call('display_financial_statement')
    self.plot_3.data = go.Scatter(
    x = [x['date_cloture_exercice'] for x in db_data],
    y = [x['Concours_bancaires_courants_et_soldes_crediteurs_de_banques_et_C_C_P_m1'] for x in db_data],
    fill=None,
    mode='lines',
    color='red',
    )

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form3_10_2', my_parameter="an_argument") #Graph

