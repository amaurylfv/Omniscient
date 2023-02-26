from ._anvil_designer import Form3_9Template
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
import json

class Form3_9(Form3_9Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.repeating_panel_1.items = anvil.server.call('from_data_tables_get_accounting_balance')
    #self.vmp_graph()
    #self.disponibilites_graph()
    #self.Concours_bancaires_courants_et_soldes_crediteurs_de_banques_et_C_C_P_graph()

    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form3', my_parameter="an_argument") #Retour

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form3_10_2', my_parameter="an_argument") #Graph


  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    csv_file = anvil.server.call('financial_statement_data_to_csv')
    media = BlobMedia('text/plain', csv_file.get_bytes(), name='export.csv')
    download(media)

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    xlsx_file = anvil.server.call('financial_statement_data_to_xlsx')
    media = BlobMedia('text/plain', csv_file.get_bytes(), name='export.csv')
    download(media)

  def income_statement_board(self):
    data = anvil.server.call('income_statement_table')
    fig = json.loads(data)
    self.plot_1.data = fig['data']
    self.plot_1.layout = fig['layout']

  #def vmp_graph(self):
    #db_data = anvil.server.call('display_financial_statement')
    #self.plot_1.data = go.Scatter(
    #x = [x['date_cloture_exercice'] for x in db_data],
    #y = [x['Valeurs_mobilieres_de_placement_m1'] for x in db_data],
    #fill=None,
    #mode='lines',
    #color='green',
    #)

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
