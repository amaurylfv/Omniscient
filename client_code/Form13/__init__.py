from ._anvil_designer import Form13Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form13(Form13Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    while not anvil.users.login_with_form():
      pass
    
    self.my_users = anvil.server.call('get_users')

    # Any code you write here will run when the form opens.
    
    for row in self.my_users.search():
      ud = UsersDisplay(row)
      self.linear_panel_1.add_component(ud)
      
  def add_btn_click(self, **event_args):
    row = self.my_users.add_row(description=self.text_box_1, done=False)
    ud = UsersDisplay(row)
    self.linear_panel_1.add_component(ud)
    self.text_box_1 = ""

    self.