from ._anvil_designer import Form4_3_2Template
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

class Form4_3_2(Form4_3_2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.vente_de_marchandises_ant_graph()
    self.production_vendue_biens_ant_graph()
    self.production_vendue_services_ant_graph()
    self.chiffre_affaires_nets_ant_graph()
    self.vente_de_marchandises_act_graph()
    self.production_vendue_biens_act_graph()
    self.production_vendue_services_act_graph()
    self.chiffre_affaires_nets_act_graph()

    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form3', my_parameter="an_argument") #Retour

  def vente_de_marchandises_act_graph(self):
    data = anvil.server.call('vente_de_marchandises_actuel')
    fig = json.loads(data)
    self.plot_1.data = fig['data']
    self.plot_1.layout = fig['layout']

  def vente_de_marchandises_ant_graph(self):
    data = anvil.server.call('vente_de_marchandises_anterieurs')
    fig = json.loads(data)
    self.plot_2.data = fig['data']
    self.plot_2.layout = fig['layout']

  def production_vendue_biens_act_graph(self):
    data = anvil.server.call('production_vendue_de_biens_actuel')
    fig = json.loads(data)
    self.plot_3.data = fig['data']
    self.plot_3.layout = fig['layout']

  def production_vendue_biens_ant_graph(self):
    data = anvil.server.call('production_vendue_de_biens_anterieurs')
    fig = json.loads(data)
    self.plot_4.data = fig['data']
    self.plot_4.layout = fig['layout']

  def production_vendue_services_act_graph(self):
    data = anvil.server.call('production_vendue_de_services_actuel')
    fig = json.loads(data)
    self.plot_5.data = fig['data']
    self.plot_5.layout = fig['layout']

  def production_vendue_services_ant_graph(self):
    data = anvil.server.call('production_vendue_de_services_anterieurs')
    fig = json.loads(data)
    self.plot_6.data = fig['data']
    self.plot_6.layout = fig['layout']

  def chiffre_affaires_nets_act_graph(self):
    data = anvil.server.call('chiffre_affaires_nets_actuel')
    fig = json.loads(data)
    self.plot_7.data = fig['data']
    self.plot_7.layout = fig['layout']

  def chiffre_affaires_nets_ant_graph(self):
    data = anvil.server.call('chiffre_affaires_nets_anterieurs')
    fig = json.loads(data)
    self.plot_8.data = fig['data']
    self.plot_8.layout = fig['layout']
