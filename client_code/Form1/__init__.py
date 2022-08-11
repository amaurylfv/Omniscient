#Import des diverses librairies
from ._anvil_designer import Form1Template
from anvil import *
import anvil.facebook.auth
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
from ..Form4_2 import Form4_2
from ..Form4_4 import Form4_4
from ..Form4_6 import Form4_6
from ..Form5 import Form5
from ..Form5_1 import Form5_1
from ..Form5_1_2 import Form5_1_2
from ..Form5_3 import Form5_3
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
    self.build_charges_graph()
    
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
                            font=dict(family='Source Code Pro', size=10),
                            # Format x-axis
                            xaxis=dict(
                              zeroline=False,
                              tickfont=dict(
                                  family='Source Code Pro',
                                  size=11,
                                  color='#808080'
                              ),
                            ),
                            # Format y-axis
                            yaxis=dict(
                                zeroline=False,
                                tickfont=dict(
                                    family='Source Code Pro',
                                    size=11,
                                    color='#808080'
                                ),
                            )
                          ) 
  
  def build_revenue_graph(self):
    # Get the data from our server function, and store it as 'db_data'
    db_data = anvil.server.call('get_sig')
    max_revenue = sorted(db_data, key=lambda x: x['Chiffre_affaires'], reverse=True)[0]
    self.label_1.text = f"{max_revenue['Chiffre_affaires']:,}"
    
    # Create a Bar plot with this data, and change the colour of the markers
    self.plot_1.data = go.Scatter(
      x = [x['Year'] for x in db_data],
      y = [x['Chiffre_affaires'] for x in db_data],
      fill=None,
      mode='lines',
      line_color='indigo',
    )
    
    self.style_plot(self.plot_1)
  
  def build_charges_graph(self):
    # Get the data from our server function, and store it as 'db_data'
    sum_charges = anvil.server.call('total_charges')
    self.label_2.text = sum_charges
        







