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
def map_chart():
  import plotly.express as px
  df = px.data.carshare()
  fig = px.scatter_mapbox(df, lat="centroid_lat", lon="centroid_lon", color="peak_hour", size="car_hours",
                    color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
                    mapbox_style="carto-positron")
  return fig