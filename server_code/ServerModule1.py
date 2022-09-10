import anvil.facebook.auth
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
from pandas import json_normalize
import io
from datetime import date, timedelta
from itertools import groupby, accumulate
import anvil.http
import urllib.parse
from urllib.request import urlopen
import json

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
  return app_tables.invoice.search(amount=q.not_(None))

@anvil.server.callable
def create_fig():
    df = px.data.tips()
    fig = px.pie(df, values='tip', names='day', color_discrete_sequence=px.colors.sequential.RdBu)
    return fig

@anvil.server.callable
def create_pie():
    all_records = app_tables.invoice.search()
    # For each row, pull out only the data we want to put into pandas
    dicts = [{'date': r['date'], 'fournisseurs': r['issuer'], 'Montants': r['amount']}
          for r in all_records]
    df = pd.DataFrame.from_dict(dicts)
    fig = px.pie(df, values='Montants', names='fournisseurs', color_discrete_sequence=px.colors.sequential.RdBu, hole=.3)
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

@anvil.server.callable
def map_chart():

  df = px.data.carshare()
  fig = px.scatter_mapbox(df, lat="centroid_lat", lon="centroid_lon", color="peak_hour", size="car_hours",
                    color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
                    mapbox_style="carto-positron")
  return fig
"""
@anvil.server.callable
def get_locations():
  api_key = "UEJNpy9I6ZsI3J8Dwd_SAOeqnYJvMvM0guqwd7sVkgc"
  root_url = "https://geocode.search.hereapi.com/v1/geocode?"
  show = "parsing"
  rows = {}
  for row in app_tables.invoice.search():
    row = dict(row)
    
    issuer = row['issuer']
    
    country = row['country']
    countries = {"country": country}
    
    city = row['city']
    cities = {"city": city}
    
    postalCode = row['postalCode']
    postalCodes = {"postalCode": postalCode}
    
    house_number = row['house_number']
    houses_numbers = {"houseNumber": house_number}
    
    address = row['address']
    addresses = {"street": address}
    
    encoded_country = urllib.parse.urlencode(countries)
    encoded_postalCode = urllib.parse.urlencode(postalCodes)
    encoded_house_number = urllib.parse.urlencode(houses_numbers)
    encoded_address = urllib.parse.urlencode(addresses)
    encoded_city = urllib.parse.urlencode(cities)
    
    params = str(encoded_country+";"+encoded_postalCode+";"+encoded_house_number+";"+encoded_address+";"+encoded_city)
    
    url = f"{root_url}&qq={params}&show={show}&apiKey={api_key}"
    responses = anvil.http.request(url, json=True)
    
    for response in responses :
      data = json_normalize(responses, 'items')
      df_flush = data.to_dict(orient="records")
    
    df = pd.DataFrame(df_flush)
    for d in df_flush:
      app_tables.locations.add_row(**d)
      #df = pd.DataFrame.append(data)
      #df = pd.read_json(data)
      #print(df)
"""
@anvil.server.callable
def issuer_map():
  all_records = app_tables.locations.search()
  dicts = [{'lat': r['position.lat'], 'lon': r['position.lng'], 'address.city': r['address.city'], 'address.countryName': r['address.countryName'], 'address.houseNumber': r['address.houseNumber'], 'address.street': r['address.street']}
          for r in all_records]
  df = pd.DataFrame.from_dict(dicts)
  fig = px.scatter_mapbox(df, lat="lat", lon="lon", hover_name='address.city', hover_data=["address.countryName","address.houseNumber","address.street"],
                                  color_discrete_sequence=["red"], zoom=10, height=200)
  fig1 = fig.update_layout(mapbox_style="carto-positron")
  fig2 = fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})     
  return fig2

@anvil.server.callable
def filled_area():
    all_records = app_tables.sig.search()
    # For each row, pull out only the data we want to put into pandas
    dicts = [{'années': r['Year'], 'EBE': r['EBE'], 'sig': r['Marge commerciale']}
          for r in all_records]
    df = pd.DataFrame.from_dict(dicts)
    fig = px.area(df, x="années", y="EBE", color="EBE", line_group="sig")
    return fig

@anvil.server.callable
def bar_chart():
    all_records = app_tables.sig.search()
    dicts = [{'années': r['Year'], 'EBE': r['EBE'], 'sig': r['Marge commerciale']}
          for r in all_records]
    df = pd.DataFrame.from_dict(dicts)
    fig = px.bar(df, x='années', y='EBE')
    return fig
  
@anvil.server.callable
def funnel_chart():
  fig = px.funnel_area(names=["Boutique","Site internet", "Salons", "Bouches à oreilles", "Syndicat des fleuristes"],
                      values=[5, 4, 3, 2, 1])
  return fig

@anvil.server.callable
def time_series_chart():
  df = px.data.stocks(indexed=True)-1
  fig = px.bar(df, x=df.index, y="GOOG")
  return fig

@anvil.server.callable
def profitabilité():
  rows = {}
  for row in app_tables.sig.search():
      row = dict(row)
      row['taux de profitabilité'] = row['Résultat_exercice'] / row['Chiffre_affaires']
      absolue = row['taux de profitabilité']
      relative = (f"{absolue:.0%}")
      
      return relative

@anvil.server.callable
def chiffre_affaires():
  rows = {}
  for row in app_tables.sig.search():
      row = dict(row)
      chiffre_affaires = row['Chiffre_affaires']
      
      return chiffre_affaires

@anvil.server.callable
def total_charges():
    all_records = app_tables.invoice.search()
    dicts = [{'amount_untaxed': r['amount_untaxed']}
          for r in all_records]
    df = pd.DataFrame.from_dict(dicts)
    df2 = df.sum()
    df3 = (df2.to_string(index=False))
    
    return df3
    
    
@anvil.server.callable
def total_charges_fixes():
    all_records = app_tables.invoice.search(fixe='true')
    dicts = [{'amount': r['amount']}
          for r in all_records]
    df = pd.DataFrame.from_dict(dicts)
    df2 = df.sum()
    df3 = (df2.to_string(index=False))
    
    return df3
    
@anvil.server.callable   
def total_charges_variables():
    all_records = app_tables.invoice.search(variable='true')
    dicts = [{'amount': r['amount']}
          for r in all_records]
    df = pd.DataFrame.from_dict(dicts)
    df2 = df.sum()
    df3 = (df2.to_string(index=False))
    
    return df3
      
@anvil.server.callable
def taux_de_marge_sur_coûts_variables():
  total_charges_variables = anvil.server.call('total_charges_variables')
  chiffre_affaires = anvil.server.call('chiffre_affaires')
  taux_de_marge_sur_coûts_variables = float(total_charges_variables) / float(chiffre_affaires)
  relative = (f"{taux_de_marge_sur_coûts_variables:.0%}")
  
  print(taux_de_marge_sur_coûts_variables)
  return taux_de_marge_sur_coûts_variables
  
@anvil.server.callable
def seuil_de_rentabilité():
  charges_fixes = anvil.server.call('total_charges_fixes')
  taux_de_marge_sur_coûts_variables = anvil.server.call('taux_de_marge_sur_coûts_variables')
  seuil_de_rentabilité = float(charges_fixes) / float(taux_de_marge_sur_coûts_variables)
  
  print(seuil_de_rentabilité)
  return seuil_de_rentabilité

@anvil.server.callable
def number_of_issuer():
  all_records = app_tables.invoice.search()
  dicts = [{'issuer': r['issuer']}
        for r in all_records]

  seen = set()
  new_l = []
  for d in dicts:
      t = tuple(d.items())
      if t not in seen:
          seen.add(t)
          new_l.append(d)
  
  df = pd.DataFrame.from_dict(new_l)
  df2 = len(df)
  
  return df2

@anvil.server.callable
def nombre_de_factures():
  all_records = app_tables.invoice.search()
  dicts = [{'invoice_number': r['invoice_number']}
        for r in all_records]
  df = pd.DataFrame.from_dict(dicts)
  df2 = len(df)
  
  return df2

@anvil.server.callable
def anomalies_factures():
  all_records = app_tables.invoice.search(q.any_of(amount=None, issuer=None, date=None))
  dicts = [{'invoice_number': r['invoice_number']}
        for r in all_records]
  df = pd.DataFrame.from_dict(dicts)
  df2 = len(df)

  return df2

@anvil.server.callable
def data_to_csv():
  data = app_tables.invoice.search()
  return data.to_csv()

#Diagramme circulaire des produits les plus vendus
@anvil.server.callable
def pie_product():
    all_records = app_tables.revenue.search()
    dicts = [{'date': r['date'], 'Produits': r['desc'], 'Montants': r['amount'], 'Quantité': r['quantity']}
          for r in all_records]
    df = pd.DataFrame.from_dict(dicts)
    fig = px.pie(df, values='Quantité', names='Produits', color_discrete_sequence=px.colors.sequential.RdBu, hole=.4)
    return fig

@anvil.server.callable
def add_siren_and_accounting_exercise(dict):
  app_tables.siren_and_accounting_exercise.add_row(**dict)

@anvil.server.callable
def get_siren():
  rows = {}
  for row in app_tables.siren_and_accounting_exercise.search(siren_query=q.all_of()):
      row = dict(row)
      siren_query = row['siren_query']
      return siren_query
  
@anvil.server.callable
def get_accounting_exercise():
  rows = {}
  for row in app_tables.siren_and_accounting_exercise.search(accounting_exercise_query=q.all_of()):
      row = dict(row)
      accounting_exercise = row['accounting_exercise_query']
      return accounting_exercise

@anvil.server.callable
def delete_siren_and_accounting_exercise():
  app_tables.siren_and_accounting_exercise.delete_all_rows()

@anvil.server.callable
def display_financial_statement():
  return app_tables.financial_statement.search()
  
@anvil.server.callable
def calculate_treasury():
  rows = {}
  for row in app_tables.financial_statement.search():
    row = dict(row)    
    date_cloture_exercice= row['date_cloture_exercice']
    
    Valeurs_mobilieres_de_placement_m1= row['Valeurs_mobilieres_de_placement_m1']
    if Valeurs_mobilieres_de_placement_m1 == None:
      Valeurs_mobilieres_de_placement_m1 = 0
      
    Disponibilites_m1= row['Disponibilites_m1']
    if Disponibilites_m1 == None:
      Disponibilites_m1 = 0
      
    Concours_bancaires_courants_et_soldes_crediteurs_de_banques_et_C_C_P_m1 = row['Concours_bancaires_courants_et_soldes_crediteurs_de_banques_et_C_C_P_m1']
    if Concours_bancaires_courants_et_soldes_crediteurs_de_banques_et_C_C_P_m1 == None:
      Concours_bancaires_courants_et_soldes_crediteurs_de_banques_et_C_C_P_m1 = 0
    
    treasury = float(Valeurs_mobilieres_de_placement_m1) + float(Disponibilites_m1) - float(Concours_bancaires_courants_et_soldes_crediteurs_de_banques_et_C_C_P_m1)
    df = treasury.to_dict(orient="records")
    for d in df:
      app_tables.financial_statement.add_row(**d)
    return treasury

@anvil.server.callable
def visualise_treasury():
  all_records = app_tables.financial_statement.search()
  dicts = [{'date_cloture_exercice': r['date_cloture_exercice'],
            'Valeurs_mobilieres_de_placement_m1': r['Valeurs_mobilieres_de_placement_m1'],
            'Disponibilites_m1': r['Disponibilites_m1'],
            'Concours_bancaires_courants_et_soldes_crediteurs_de_banques_et_C_C_P_m1': r['Concours_bancaires_courants_et_soldes_crediteurs_de_banques_et_C_C_P_m1'],
            'treasury': r['treasury']}
           for r in all_records]
  df = pd.DataFrame.from_dict(dicts)
  fig = px.area(df, x="date_cloture_exercice", y="treasury")
  return fig


    
  