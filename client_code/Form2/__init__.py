from ._anvil_designer import Form2Template
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import json

from ..Form2_1 import Form2_1

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.get_locations()
    self.customer_map()
    self.number_of_customers_label()
    self.main_customer_label()
    self.average_basket_label()
    self.average_profit_per_customers()
    self.customer_lifetime_value_label()
    self.purchase_frequency_label()
    self.churn_rate_label()
    
    #self.funnel_chart()

    # Any code you write here will run when the form opens.
  
  def button_1_click(self, **event_args):
    open_form('Form1', my_parameter="an_argument") #Accueil

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form2_1', my_parameter="an_argument") #Prévision des ventes
  
  def get_locations(self):
    anvil.server.call('get_customer_locations')
    
  def customer_map(self):
    data = anvil.server.call('customer_map')
    fig = json.loads(data)
    self.plot_1.data = fig['data']
    self.plot_1.layout = fig['layout']

  def number_of_customers_label(self):
    number_of_customers = anvil.server.call("number_of_customer")
    self.label_1.text = number_of_customers

  def main_customer_label(self):
    main_customer = anvil.server.call('main_customer_label')
    self.label_2.text = main_customer  

  def average_basket_label(self):
    average_basket = anvil.server.call("average_basket")
    self.label_3.text = average_basket

  def average_profit_per_customers(self):
    average_benefits = anvil.server.call("average_profits_per_customer")
    self.label_4.text = average_benefits

  def customer_lifetime_value_label(self):
    customer_lifetime = anvil.server.call("customer_lifetime_value")
    self.label_5.text = customer_lifetime

  def purchase_frequency_label(self):
    purchase_frequency_value = anvil.server.call("purchase_frequency")
    self.label_7.text = purchase_frequency_value

  def churn_rate_label(self):
    churn_rate_value = anvil.server.call("churn_rate")
    self.label_8.text = churn_rate_value