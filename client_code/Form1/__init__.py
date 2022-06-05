from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run when the form opens.
    self.temp_data = []
    self.build_revenue_graph()
    self.build_marketing_graph()
    
  def style_plot(self, plot):
    plot.layout = go.Layout(
                            # expand the graphs
                            margin=dict(
                                l=50, #left margin
                                r=50, #right margin
                                b=50, #bottom margin
                                t=50, #top margin
                            ),
                            font=dict(family='Noto Sans', size=10),
                            # Format x-axis
                            xaxis=dict(
                              zeroline=False,
                              tickfont=dict(
                                  family='Noto Sans',
                                  size=11,
                                  color='#808080'
                              ),
                            ),
                            # Format y-axis
                            yaxis=dict(
                                zeroline=False,
                                tickfont=dict(
                                    family='Noto Sans',
                                    size=11,
                                    color='#808080'
                                ),
                            )
                          ) 
  
  def build_revenue_graph(self):
    # Get the data from our server function, and store it as 'db_data'
    db_data = anvil.server.call('get_revenue')
    max_revenue = sorted(db_data, key=lambda x: x['amount'], reverse=True)[0]
    self.revenue_label.text = f"{max_revenue['date']:%d %b %Y}, {max_revenue['amount']:,}"
    
    # Create a Bar plot with this data, and change the colour of the markers
    self.plot_1.data = go.Bar(
      x = [x['date'] for x in db_data],
      y = [x['amount'] for x in db_data],
      marker=dict(color='#2196f3')
    )
    # Style the plot and add a plot title
    self.style_plot(self.plot_1)
    self.plot_1.layout.title = "REVENUE GROWTH"
  
    
  def build_marketing_graph(self):
    # We’re calling a function on your local machine from the web!
    # Get the data and store it as 'marketing_data'
    marketing_data = anvil.server.call('get_marketing_data')
    max_hits = sorted(marketing_data, key=lambda x: x['count'], reverse=True)[0]
    self.marketing_label.text = f"{max_hits['strategy']}, {max_hits['count']} hits"
    # Create a Line plot with this data, and change the colour of the line
    self.plot_3.data = go.Scatter(x = [x['strategy'] for x in marketing_data],
                                  y = [x['count'] for x in marketing_data],
                                  mode='lines+markers',
                                  line=dict(color='#2196f3'))
    # Style the plot and add a plot title
    self.style_plot(self.plot_3)
    self.plot_3.layout.title = "TEST 2"
    

