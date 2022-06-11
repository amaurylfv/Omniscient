#Import des diverses librairies
from ._anvil_designer import Form1Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
import anvil.google.auth
from anvil.tables import app_tables

#Import des pages de navigation de la nav-bar
from ..Form2 import Form2
from ..Form3 import Form3
from ..Form4 import Form4
from ..Form5 import Form5
from ..Form6 import Form6
from ..Form7 import Form7
from ..Form8 import Form8
from ..Form9 import Form9
from ..Form10 import Form10
from ..Form11 import Form11


class Form1(Form1Template):

  
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run when the form opens.
    self.temp_data = []
    self.build_revenue_graph()
    self.build_marketing_graph()

    email_addr = anvil.google.auth.login()
    print(f"User logged in as {email_addr}")
    
#boutons qui permettent la navigation entre les rubriques (Marketing, Finance, etc.)
  def button_1_click(self, **event_args):
    open_form('Form2', my_parameter="an_argument") #Marketing
    
  def button_2_click(self, **event_args):
    open_form('Form3', my_parameter="an_argument") #Comptabilité
    
  def button_3_click(self, **event_args):
    open_form('Form4', my_parameter="an_argument") #Gestion
    
  def button_4_click(self, **event_args):
    open_form('Form5', my_parameter="an_argument") #Finance
    
  def button_5_click(self, **event_args):
    open_form('Form6', my_parameter="an_argument") #Audit
    
  def button_6_click(self, **event_args):
    open_form('Form7', my_parameter="an_argument") #Juridique
    
  def button_7_click(self, **event_args):
    open_form('Form8', my_parameter="an_argument") #Fiscalité
    
  def button_8_click(self, **event_args):
    open_form('Form9', my_parameter="an_argument") #Social
    
  def button_9_click(self, **event_args):
    open_form('Form10', my_parameter="an_argument") #Données
    
  def button_10_click(self, **event_args):
    open_form('Form11', my_parameter="an_argument") #Paramètres IA

    
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
      marker=dict(color='#F7DC6F')
    )
    # Style the plot and add a plot title
    self.style_plot(self.plot_1)
    self.plot_1.layout.title = "Chiffre d'affaires mensuel"
  
    
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
                                  line=dict(color='#F0B27A'))
    # Style the plot and add a plot title
    self.style_plot(self.plot_3)
    self.plot_3.layout.title = "Impact des campagnes"
        







