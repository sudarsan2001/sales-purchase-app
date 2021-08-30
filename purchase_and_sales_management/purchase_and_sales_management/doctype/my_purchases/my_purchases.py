# Copyright (c) 2021, Sudarshan and contributors
# For license information, please see license.txt
from __future__ import unicode_literals

import frappe
from frappe.model.document import Document

class MyPurchases(Document):
      def before_save(self):
          if frappe.db.exists("Company Stocks",{'stock_item':self.item_name}):
              old_qty = frappe.db.get_value("Company Stocks",{'stock_item':self.item_name},"stock_left")
              new_qty = self.qty
              new_qty += old_qty
              frappe.db.set_value("Company Stocks",{'stock_item':self.item_name},"stock_left",new_qty)
          else:
              new_stock=frappe.new_doc("Company Stocks")
              new_stock.stock_item=self.item_name
              new_stock.stock_left=self.qty
              new_stock.save()
          
          self.puramt()
          self.purprint()
          #self.gain()
          
      def purprint(self):
          frappe.msgprint("You have Purchased Successfully!!!")
      def puramt(self):
          itemprice=frappe.db.get_value("Items",{"item_name":self.item_name},"price")
          self.price_per_unit=itemprice
          self.buying_amount= itemprice * self.qty
      def gain(self):
          frappe.db.set_value("Company Stocks",{"stock_item":self.item_name},"profit",self.amount)


      
          

          
	
