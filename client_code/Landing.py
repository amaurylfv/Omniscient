from ._anvil_designer import LandingTemplate
from anvil import *
import anvil.facebook.auth
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import date, timedelta
from itertools import groupby, accumulate

class Landing(LandingTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form11', my_parameter="an_argument") #Import facture

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1', my_parameter="an_argument") #Tableau de bord

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form13', my_parameter="an_argument") #Page d'aide

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    media_object = app_files.guide_utilisateur_pdf
    anvil.media.download(media_object)

    

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Form0', my_parameter="an_argument") #Login Page





