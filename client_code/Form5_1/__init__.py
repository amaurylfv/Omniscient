from ._anvil_designer import Form5_1Template
from anvil import *
import anvil.facebook.auth
import plotly.graph_objects as go
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import json

from ..Form5_1_1 import Form5_1_1
from ..Form5_1_2 import Form5_1_2

class Form5_1(Form5_1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.intermediate_operating_filled_area_chart()
    self.build_structure_graph_2()
    self.build_structure_graph_3()
    self.build_structure_graph_4()
    self.build_structure_graph_5()
    self.build_structure_graph_6()

    # Any code you write here will run when the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form1', my_parameter="an_argument") #Accueil 

  def button_2_click(self, **event_args):
    open_form('Form5', my_parameter="an_argument") #Retour

  def button_1_click(self, **event_args):
    open_form('Form5_1_1', my_parameter="an_argument") #SIG

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
                                  color='#03071E'
                              ),
                            ),
                            # Format y-axis
                            yaxis=dict(
                                zeroline=False,
                                tickfont=dict(
                                    family='Noto Sans',
                                    size=11,
                                    color='#03071E'
                                ),
                            )
                          ) 
    
  def intermediate_operating_filled_area_chart(self):
    # Get the data from our server function, and store it as 'db_data'
    data = anvil.server.call('intermediate_operating_filled_area_graph')
    fig = json.loads(data)
    self.plot_1.data = fig['data']
    self.plot_1.layout = fig['layout']
    
    #max_marge = sorted(db, key=lambda x: x['Marge commerciale'], reverse=True)[0]
    #self.label_1.text = f"{max_marge['Marge commerciale']:,}"
    
  def build_structure_graph_2(self):
    # Get the data from our server function, and store it as 'db_data'
    db = anvil.server.call('get_sig')
      
      # Create a Bar plot with this data, and change the colour of the markers
    self.plot_2.data = go.Bar(
      x = [x['Year'] for x in db],
      y = [x["Production_exercice"] for x in db],
      marker=dict(color='#219EBC')
    )
    
    max_production = sorted(db, key=lambda x: x["Production_exercice"], reverse=True)[0]
    self.label_2.text = f"{max_production['Production_exercice']:,}"
    
    # Style the plot and add a plot title
    self.style_plot(self.plot_2)
    self.plot_2.layout.title = "Evolution de la Production de l'exercice"

  def build_structure_graph_3(self):
    # Get the data from our server function, and store it as 'db_data'
    db = anvil.server.call('get_sig')
      
      # Create a Bar plot with this data, and change the colour of the markers
    self.plot_3.data = go.Bar(
      x = [x['Year'] for x in db],
      y = [x['Marge commerciale'] for x in db],
      marker=dict(color='#D62828')
    )
    
    max_VA = sorted(db, key=lambda x: x['Valeur ajoutée'], reverse=True)[0]
    self.label_3.text = f"{max_VA['Valeur ajoutée']:,}"
    
    # Style the plot and add a plot title
    self.style_plot(self.plot_3)
    self.plot_3.layout.title = "Evolution de la Production de l'exercice"

  def build_structure_graph_4(self):
    # Get the data from our server function, and store it as 'db_data'
    db = anvil.server.call('get_sig')
      
      # Create a Bar plot with this data, and change the colour of the markers
    self.plot_4.data = go.Bar(
      x = [x['Year'] for x in db],
      y = [x["Valeur ajoutée"] for x in db],
      marker=dict(color='#003049')
    )
    
    max_EBE = sorted(db, key=lambda x: x['EBE'], reverse=True)[0]
    self.label_4.text = f"{max_EBE['EBE']:,}"    
    
    # Style the plot and add a plot title
    self.style_plot(self.plot_4)
    self.plot_4.layout.title = "Evolution de la valeur ajoutée"
    
  def build_structure_graph_5(self):
    # Get the data from our server function, and store it as 'db_data'
    db = anvil.server.call('get_sig')
      
      # Create a Bar plot with this data, and change the colour of the markers
    self.plot_5.data = go.Bar(
      x = [x['Year'] for x in db],
      y = [x["EBE"] for x in db],
      marker=dict(color='#F77F00')
    )
    
    max_Résultat_exploitation = sorted(db, key=lambda x: x["Résultat_exploitation"], reverse=True)[0]
    self.label_5.text = f"{max_Résultat_exploitation['Résultat_exploitation']:,}"      
    
    # Style the plot and add a plot title
    self.style_plot(self.plot_5)
    self.plot_5.layout.title = "Evolution de l'EBE"
    
  def build_structure_graph_6(self):
    # Get the data from our server function, and store it as 'db_data'
    db = anvil.server.call('get_sig')
      
      # Create a Bar plot with this data, and change the colour of the markers
    self.plot_6.data = go.Scatter(x = [x['Year'] for x in db],
                                  y = [x["Résultat_exploitation"] for x in db],
                                  mode='lines+markers',
                                  line=dict(color='#EAE2B7'))
    
    max_RCAI = sorted(db, key=lambda x: x['Résultat courant avant impôt'], reverse=True)[0]
    self.label_6.text = f"{max_RCAI['Résultat courant avant impôt']:,}"  
    
    # Style the plot and add a plot title
    self.style_plot(self.plot_6)
    self.plot_6.layout.title = "Evolution du Résultat d'exploitation"
    
    max_Résultat_exceptionnel = sorted(db, key=lambda x: x['Résultat exceptionnel'], reverse=True)[0]
    self.label_7.text = f"{max_Résultat_exceptionnel['Résultat exceptionnel']:,}"  

    max_Résultat_exercice = sorted(db, key=lambda x: x['Résultat_exercice'], reverse=True)[0]
    self.label_8.text = f"{max_Résultat_exercice['Résultat_exercice']:,}"      
    
  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form5_1_2', my_parameter="an_argument")

