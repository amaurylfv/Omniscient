from ._anvil_designer import Form11_2Template
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

class Form11_2(Form11_2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.invoice_chart()
    self.build_pie_chart_issuer()
    self.get_locations()
    self.issuer_map()
    self.total_charges_fixes()
    self.total_charges_variables()

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

  

  
  def invoice_chart(self):
    # Get the data from our server function, and store it as 'db_data'
    data = anvil.server.call('invoice_graph')
    fig = json.loads(data)
    self.plot_1.data = fig['data']
    self.plot_1.layout = fig['layout']
    
    #Nombre de fournisseurs
    number_issuer = anvil.server.call('number_of_issuer')
    self.label_3.text = number_issuer
 
    #Charge la plus élevée
    max_invoice = anvil.server.call('main_supplier_label')
    self.label_1.text = max_invoice   
    
    #Fournisseur principal
    main_supplier = anvil.server.call('max_invoice_label')
    self.label_2.text = main_supplier
    
    #Facture en anomalie
    anomalie_facture = anvil.server.call('anomalies_factures')
    self.label_4.text = anomalie_facture
    
    
  def build_pie_chart_issuer(self):  
    fig = anvil.server.call('create_pie') 
    self.plot_2.figure = fig

    
  def get_locations(self):
    anvil.server.call('get_locations')
    
  def issuer_map(self):
    data = anvil.server.call('issuer_map')
    fig = json.loads(data)
    self.plot_3.data = fig['data']
    self.plot_3.layout = fig['layout']
    
  def total_charges_fixes(self):
    fixe = anvil.server.call('total_charges_fixes')
    self.plot_4.data = go.Bar(
      x = [fixe],
      y = [fixe],
      marker=dict(color='#e76f51')
    )
    
  def total_charges_variables(self):
    var = anvil.server.call('total_charges_variables')
    self.plot_5.data = go.Bar(
      x = [var],
      y = [var],
      marker=dict(color='#adc178')
    )
  
    