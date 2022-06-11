from ._anvil_designer import Form13Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.google.auth



class Form13(Form13Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
   

    # Any code you write here will run when the form opens.

    email_addr = anvil.google.auth.login()
    print(f"User logged in as {email_addr}")