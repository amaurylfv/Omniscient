import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import plotly.graph_objects as go
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

@anvil.server.callable
def create_pie():
    all_records = app_tables.sig.search()
    # For each row, pull out only the data we want to put into pandas
    dicts = [{'années': r['Year'], 'EBE': r['EBE'], 'sig': r['Marge commerciale']}
          for r in all_records]
    df = pd.DataFrame.from_dict(dicts)
    fig = px.pie(df, values='sig', names='années', color_discrete_sequence=px.colors.sequential.RdBu, hole=.3)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig

@anvil.server.callable
def create_line():
    data = app_tables.sig.search()
    dicts = [{'années': r['Year'], 'sig': r['Marge commerciale']}
          for r in data]
    df = pd.DataFrame.from_dict(dicts)
    fig = px.line(df, facet_col="années", facet_col_wrap=2)
    fig.add_hline(y=1, line_dash="dot",
                annotation_position="bottom right")
    return fig
  
@anvil.server.callable
def create_gantt_chart():
  df = pd.DataFrame([
      dict(Task="Recherche financement", Start='2022-01-01', Finish='2022-02-28', Resource="Elodie"),
      dict(Task="Mise en production", Start='2022-03-05', Finish='2022-04-15', Resource="Rebwar"),
      dict(Task="Campagne de pub", Start='2022-02-20', Finish='2022-05-30', Resource="Virginie")
  ])
  
  fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Resource")
  fig.update_yaxes(autorange="reversed")
  return fig
  
  
@anvil.server.callable
def create_histogram():
  df = px.data.tips()
  fig = px.histogram(df, x="total_bill", y="tip", color="sex", facet_row="time", facet_col="day",
        category_orders={"day": ["Thur", "Fri", "Sat", "Sun"], "time": ["Lunch", "Dinner"]})
  return fig
