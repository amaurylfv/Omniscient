import anvil.http
import plotly.express as px
import pandas as pd
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

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
def show_pie_product():
   json.loads(resp)[‘data’]

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
def map_chart():
  import plotly.express as px
  df = px.data.carshare()
  fig = px.scatter_mapbox(df, lat="centroid_lat", lon="centroid_lon", color="peak_hour", size="car_hours",
                    color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
                    mapbox_style="carto-positron")
  return fig