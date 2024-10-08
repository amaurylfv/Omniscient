from ._anvil_designer import Form5Template
from anvil import *
import anvil.facebook.auth
import plotly.graph_objects as go
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import json

from ..Form5_1 import Form5_1
from ..Form5_2 import Form5_2
from ..Form5_3 import Form5_3

class Form5(Form5Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #self.build_structure_graph_1()
    self.profitability_horizontal_bar_chart()
    self.profitability_line_chart()
    self.rentability_horizontal_bar_chart()
    self.rentability_line_chart()
    #self.build_structure_graph_2()
    self.profitabilité()
    self.total_charges_fixes()
    self.total_charges_variables()
    self.taux_de_marges_sur_cv()
    self.seuil_de_rentabilite()
    
    # Any code you write here will run when the form opens.
    
  def button_1_click(self, **event_args):
    open_form('Form1', my_parameter="an_argument") #Accueil

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form5_1', my_parameter="an_argument") #Profitabilité

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form5_2', my_parameter="an_argument") #Structure financière

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form5_3', my_parameter="an_argument") #Rentabilité
  
  #def build_structure_graph_1(self):
    # Get the data from our server function, and store it as 'db_data'
    #db = anvil.server.call('display_financial_statement')
      
      # Create a Bar plot with this data, and change the colour of the markers
    #self.plot_1.data = go.Scatter(x = [x['date_cloture_exercice'] for x in db],
                                  #y = [x['Chiffres_daffaires_nets_m1'] for x in db],
                                  #mode='lines+markers',
                                  #line=dict(color='#EAE2B7'))
    
  def profitability_horizontal_bar_chart(self):
    data = anvil.server.call('horizontal_bar_graph_profitability')
    fig = json.loads(data)
    self.plot_1.data = fig['data']
    self.plot_1.layout = fig['layout']
    
  #def build_structure_graph_2(self):
    # Get the data from our server function, and store it as 'db_data'
    #db = anvil.server.call('display_financial_statement')
      
      # Create a Bar plot with this data, and change the colour of the markers
    #self.plot_2.data = go.Scatter(x = [x['date_cloture_exercice'] for x in db],
                                  #y = [x['Resultat_exercice_m1'] for x in db],
                                  #mode='lines+markers',
                                  #line=dict(color='#EAE2B7'))

  def profitability_line_chart(self):
    data = anvil.server.call('lines_graph_profitability')
    fig = json.loads(data)
    self.plot_2.data = fig['data']
    self.plot_2.layout = fig['layout']

  def rentability_horizontal_bar_chart(self):
    data = anvil.server.call('horizontal_bar_graph_rentability')
    fig = json.loads(data)
    self.plot_3.data = fig['data']
    self.plot_3.layout = fig['layout']
  
  def rentability_line_chart(self):
    data = anvil.server.call('lines_graph_rentability')
    fig = json.loads(data)
    self.plot_4.data = fig['data']
    self.plot_4.layout = fig['layout']
    
  def profitabilité(self):
    self.label_2.text = anvil.server.call('profitabilité')
    
  def total_charges_fixes(self):
    self.label_5.text = anvil.server.call('total_charges_fixes')
    
  def total_charges_variables(self):
    self.label_6.text = anvil.server.call('total_charges_variables')
    
  def taux_de_marges_sur_cv(self):
    self.label_7.text = anvil.server.call('taux_de_marge_sur_coûts_variables_label')
  
  def seuil_de_rentabilite(self):
    self.label_3.text = anvil.server.call('seuil_de_rentabilité')
    
    
