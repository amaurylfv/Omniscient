from ._anvil_designer import Form4_5Template
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
import plotly.graph_objects as go
import json


class Form4_5(Form4_5Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_3.items = app_tables.invoice.search()
    self.activity_cost_chart()
    self.total_activity_cost_chart()
    self.variable_costs_versus_fixed_costs_daily_lines_chart()
    self.incomes_versus_fixed_costs_daily_lines_chart()
    self.correlation_coefficient_activity_cost_chart()
    self.marginal_cost_versus_marginal_income_chart()


    # Any code you write here will run when the form opens.


  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form4', my_parameter="an_argument")

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form1', my_parameter="an_argument")

  def activity_cost_chart(self):
    data = anvil.server.call('activity_cost_graph')
    fig = json.loads(data)
    self.plot_1.data = fig['data']
    self.plot_1.layout = fig['layout']

  def total_activity_cost_chart(self):
    data = anvil.server.call('total_activity_cost_graph')
    fig = json.loads(data)
    self.plot_2.data = fig['data']
    self.plot_2.layout = fig['layout']

  def variable_costs_versus_fixed_costs_daily_lines_chart(self):
    data = anvil.server.call('variable_costs_versus_fixed_costs_daily_lines_graph')
    fig = json.loads(data)
    self.plot_3.data = fig['data']
    self.plot_3.layout = fig['layout']

  def incomes_versus_fixed_costs_daily_lines_chart(self):
    data = anvil.server.call('incomes_versus_fixed_costs_daily_lines_graph')
    fig = json.loads(data)
    self.plot_4.data = fig['data']
    self.plot_4.layout = fig['layout']

  def correlation_coefficient_activity_cost_chart(self):
    data = anvil.server.call('correlation_coefficient_activity_cost')
    fig = json.loads(data)
    self.plot_5.data = fig['data']
    self.plot_5.layout = fig['layout']

  def marginal_cost_versus_marginal_income_chart(self):
    data = anvil.server.call('marginal_cost_versus_marginal_income_graph')
    fig = json.loads(data)
    self.plot_6.data = fig['data']
    self.plot_6.layout = fig['layout']
