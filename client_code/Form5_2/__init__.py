from ._anvil_designer import Form5_2Template
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

class Form5_2(Form5_2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #self.financial_structure_chart()
    self.actual_coverages_ratios_financial_equilibrium_lines_chart()
    self.previous_coverages_ratios_financial_equilibrium_lines_chart()
    self.radar_chart()
    self.trade_receivables()
    self.trade_payables()
    self.bullet_account_payables()
    self.bullet_account_receivables()
    self.financial_equilibrium_treemap_1()
    self.financial_equilibrium_treemap_2()
    self.actual_flow_times_lines_chart()
    self.previous_flow_times_lines_chart()

    # Any code you write here will run when the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form1', my_parameter="an_argument") #Accueil

  def button_1_click(self, **event_args):
    open_form('Form5_1', my_parameter="an_argument") #Retour

  def actual_coverages_ratios_financial_equilibrium_lines_chart(self):
    data = anvil.server.call('previous_coverages_ratios_financial_equilibrium_lines_graph')
    fig = json.loads(data)
    self.plot_1.data = fig['data']
    self.plot_1.layout = fig['layout'] 

  def previous_coverages_ratios_financial_equilibrium_lines_chart(self):
    data = anvil.server.call('previous_coverages_ratios_financial_equilibrium_lines_graph')
    fig = json.loads(data)
    self.plot_2.data = fig['data']
    self.plot_2.layout = fig['layout'] 
    
  #def financial_structure_chart(self):
    #data = anvil.server.call('histogramm_financial_structure')
    #fig = json.loads(data)
    #self.plot_2.data = fig['data']
    #self.plot_2.layout = fig['layout']
   
  def radar_chart(self):
    data = anvil.server.call('radar_financial_structure')
    fig = json.loads(data)
    self.plot_3.data = fig['data']
    self.plot_3.layout = fig['layout']

  def trade_receivables(self):
    data = anvil.server.call('gauge_trade_receivables')
    fig = json.loads(data)
    self.plot_4.data = fig['data']
    self.plot_4.layout = fig['layout']
  
  def trade_payables(self):
    data = anvil.server.call('gauge_trade_payables')
    fig = json.loads(data)
    self.plot_5.data = fig['data']
    self.plot_5.layout = fig['layout']

  def bullet_account_payables(self):
    data = anvil.server.call('bullet_trade_payables')
    fig = json.loads(data)
    self.plot_6.data = fig['data']
    self.plot_6.layout = fig['layout']

  def bullet_account_receivables(self):
    data = anvil.server.call('bullet_trade_receivables')
    fig = json.loads(data)
    self.plot_16.data = fig['data']
    self.plot_16.layout = fig['layout']

  def financial_equilibrium_treemap_1(self):
    data = anvil.server.call('treemap_financial_equilibrium_1')
    fig = json.loads(data)
    self.plot_7.data = fig['data']
    self.plot_7.layout = fig['layout']

  def financial_equilibrium_treemap_2(self):
    data = anvil.server.call('treemap_financial_equilibrium_2')
    fig = json.loads(data)
    self.plot_8.data = fig['data']
    self.plot_8.layout = fig['layout']

  def actual_flow_times_lines_chart(self):
    data = anvil.server.call('previous_flow_times_lines_graph')
    fig = json.loads(data)
    self.plot_9.data = fig['data']
    self.plot_9.layout = fig['layout']
  
  def previous_flow_times_lines_chart(self):
    data = anvil.server.call('previous_flow_times_lines_graph')
    fig = json.loads(data)
    self.plot_10.data = fig['data']
    self.plot_10.layout = fig['layout']