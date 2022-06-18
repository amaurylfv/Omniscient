import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import plotly.express as px
import pandas as pd
import io

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:

@anvil.server.callable
def get_revenue():
  return app_tables.revenue.search()

@anvil.server.callable
def get_sig(): # Table des SIG
  return app_tables.sig.search()

@anvil.server.callable
def get_invoice(): #Extraction des données des factures
  return app_tables.invoice.search()

@anvil.server.callable
def create_fig():
    df = px.data.tips()
    fig = px.pie(df, values='tip', names='day', color_discrete_sequence=px.colors.sequential.RdBu)
    return fig


