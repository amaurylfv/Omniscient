#Import des diverses librairies
from ._anvil_designer import Form1Template
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
import anvil.google.auth
from anvil.tables import app_tables
import json

#Import des pages de navigation de la nav-bar
from ..Form2 import Form2
from ..Form3 import Form3
from ..Form4 import Form4
from ..Form4_2 import Form4_2
from ..Form4_4 import Form4_4
from ..Form4_6 import Form4_6
from ..Form5 import Form5
from ..Form5_1 import Form5_1
from ..Form5_1_2 import Form5_1_2
from ..Form5_3 import Form5_3
from ..Form6 import Form6
from ..Form7 import Form7
from ..Form8 import Form8
from ..Form9 import Form9
from ..Form10 import Form10
from ..Form11 import Form11
from ..Form13 import Form13


class Form1(Form1Template):

  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run when the form opens.
    self.monthly_revenue_card()
    self.monthly_revenue_chart()
    self.monthly_expenses_chart()
    self.monthly_expenses_card()
    self.ca_graph()
    self.expenses_chart()
    #self.resultat_exercice_graph()
    #self.build_charges_graph()
    self.pie_product()
    #self.marge_commerciale()
    
#boutons qui permettent la navigation entre les rubriques (Marketing, Finance, etc.)
  def button_1_click(self, **event_args):
    open_form('Form2', my_parameter="an_argument") #Marketing
    
  def button_2_click(self, **event_args):
    open_form('Form3', my_parameter="an_argument") #Comptabilité
    
  def button_3_click(self, **event_args):
    open_form('Form4', my_parameter="an_argument") #Gestion
    
  def button_4_click(self, **event_args):
    open_form('Form5', my_parameter="an_argument") #Finance
    
  def button_5_click(self, **event_args):
    open_form('Form6', my_parameter="an_argument") #Audit
    
  def button_6_click(self, **event_args):
    open_form('Form7', my_parameter="an_argument") #Juridique
    
  def button_7_click(self, **event_args):
    open_form('Form8', my_parameter="an_argument") #Fiscalité
    
  def button_8_click(self, **event_args):
    open_form('Form10', my_parameter="an_argument") #Social
    
  def button_9_click(self, **event_args):
    open_form('Form13', my_parameter="an_argument") #Paramètres
    
  def button_10_click(self, **event_args):
    open_form('Form11', my_parameter="an_argument") #Données
    
  def ca_graph(self):
    data = anvil.server.call('graph_chiffre_affaires_anterieurs')
    fig = json.loads(data)
    self.plot_1.data = fig['data']
    self.plot_1.layout = fig['layout']

  def monthly_revenue_card(self):
    data = anvil.server.call('monthly_revenue_label')
    self.label_1.text = data

  def monthly_revenue_chart(self):
    data = anvil.server.call('monthly_revenue_graph')
    fig = json.loads(data)
    self.plot_2.data = fig['data']
    self.plot_2.layout = fig['layout']
    
  def monthly_expenses_card(self):
    data = anvil.server.call('total_charges')
    self.label_2.text = data
    
  def expenses_chart(self):
    data = anvil.server.call('graph_charges_anterieurs')
    fig = json.loads(data)
    self.plot_3.data = fig['data']
    self.plot_3.layout = fig['layout']
    
  def monthly_expenses_chart(self):
    data = anvil.server.call('monthly_expenses_graph')
    fig = json.loads(data)
    self.plot_4.data = fig['data']
    self.plot_4.layout = fig['layout']     

  def pie_product(self):
    data = anvil.server.call('pie_product')
    fig = json.loads(data)
    self.plot_6.data = fig['data']
    self.plot_6.layout = fig['layout']

  #def marge_commerciale(self):
    #db = anvil.server.call('marge_commerciale')


    



