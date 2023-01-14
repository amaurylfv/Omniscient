from ._anvil_designer import Form11Template
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..Form11_1 import Form11_1
from ..Form11_2 import Form11_2

class Form11(Form11Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def button_2_click(self, **event_args):
    open_form('Form1', my_parameter="an_argument") #Accueil

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form11_1', my_parameter="an_argument")

  def file_loader_1_change(self, file, **event_args):
    # Upload the selected file into a Server Module
    c = FileLoader()
    invoice_data = anvil.server.call('get_invoice_data', file)
    
    c.clear()    

    text = anvil.server.call('get_invoice_data',self.file_loader_1.text)
    self.data_row_panel_1.text = text
    
  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form11_2', my_parameter="an_argument")

  def file_loader_5_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    c = FileLoader()
    bank_data = anvil.server.call('load_excel_bank_statement', file)
    
    c.clear()    

    text = anvil.server.call('load_excel_bank_statement',self.file_loader_5.text)
    self.data_row_panel_5.text = text

  def file_loader_4_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    c = FileLoader()
    sales_data = anvil.server.call('load_excel_file_sales', file)
    
    c.clear()    

    text = anvil.server.call('load_excel_file_sales',self.file_loader_4.text)
    self.data_row_panel_4.text = text

  def file_loader_3_change(self, file, **event_args):
    # Upload the selected file into a Server Module
    c = FileLoader()
    bank_data = anvil.server.call('bank_statement_data_to_csv', file)
    
    c.clear()    

    text = anvil.server.call('bank_statement_data_to_csv',self.file_loader_3.text)
    self.data_row_panel_3.text = text



    





