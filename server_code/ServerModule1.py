import anvil.http
import plotly.express as px
import pandas as pd
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

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
def create_line():
    data = app_tables.sig.search()
    dicts = [{'années': r['Year'], 'sig': r['Marge commerciale']}
          for r in data]
    df = pd.DataFrame.from_dict(dicts)
    fig = px.line(df, facet_col="années", facet_col_wrap=2)
    fig.add_hline(y=1, line_dash="dot",
                annotation_position="bottom right")
    return fig