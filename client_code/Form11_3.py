from ._anvil_designer import Form11_3Template
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

class Form11_3(Form11_3Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.fec_chart()
    self.repeating_panel_1.items = anvil.server.call('from_data_tables_get_conformity_results')
    #self.pie_chart_issuer()
    #self.get_locations()
    #self.issuer_map()
    self.from_fec_collected_vat_chart()
    self.from_fec_deductible_vat_chart()

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




  def fec_chart(self):
    # Get the data from our server function, and store it as 'db_data'
    data = anvil.server.call('from_fec_daily_movements_graph')
    fig = json.loads(data)
    self.plot_1.data = fig['data']
    self.plot_1.layout = fig['layout']

    #Nombre de journaux
    number_of_accounting_books = anvil.server.call('from_fec_number_of_accounting_books')
    self.label_3.text = number_of_accounting_books

    #Nombre de comptes
    number_of_accounts = anvil.server.call('from_fec_number_of_accounts')
    self.label_1.text = number_of_accounts

    #Nombre d'écritures
    number_of_journal_entries = anvil.server.call('from_fec_number_of_journal_entries')
    self.label_2.text = number_of_journal_entries

    #Racine des comptes fournisseurs
    account_root = anvil.server.call('from_fec_account_payable_root')
    self.label_4.text = account_root
    
    #Largeurs des comptes
    account_width = anvil.server.call('from_fec_detect_account_width')
    self.label_8.text = account_width
    
    #Charges la plus significatives
    #anomalie_facture = anvil.server.call('anomalies_factures')
    #self.label_7.text = anomalie_facture


  def pie_chart_issuer(self):
    data = anvil.server.call('supplier_diagramm')
    fig = json.loads(data)
    self.plot_2.data = fig['data']
    self.plot_2.layout = fig['layout']


  def get_locations(self):
    anvil.server.call('get_issuer_locations')

  def issuer_map(self):
    data = anvil.server.call('issuer_map')
    fig = json.loads(data)
    self.plot_3.data = fig['data']
    self.plot_3.layout = fig['layout']

  def from_fec_collected_vat_chart(self):
    data = anvil.server.call('from_fec_collected_vat_graph')
    fig = json.loads(data)
    self.plot_5.data = fig['data']
    self.plot_5.layout = fig['layout']

  def from_fec_deductible_vat_chart(self):
    data = anvil.server.call('from_fec_deductible_vat_graph')
    fig = json.loads(data)
    self.plot_6.data = fig['data']
    self.plot_6.layout = fig['layout']




