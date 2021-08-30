# Copyright (c) 2021, Sudarshan and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class MySales(Document):
	
	def before_save(self):
		flag=0
		if frappe.db.exists("Company Stocks",{"stock_item":self.item_name}):
			old_qty=frappe.db.get_value("Company Stocks",{"stock_item":self.item_name},"stock_left")
			if old_qty>0:
				new_qty=self.qty
				if new_qty<=old_qty:
					new_qty-=old_qty
					frappe.db.set_value("Company Stocks",{"stock_item":self.item_name},"stock_left",abs(new_qty))
					self.sellamt()
					self.sell()
					self.soldgain()
				else:
					frappe.throw("Insufficient Stock,Reduce the order or Cancel")

			else:
				frappe.throw("No stock left ,Purchase this item or Cancel this sale")

		else:
			frappe.throw("No stock left ,Purchase this item or Cancel this sale")
	def sell(self):
		frappe.msgprint("You have Sold Successfully!!!")
	def sellamt(self):
		itemprice=frappe.db.get_value("Items",{"item_name":self.item_name},"price")
		self.price_per_unit=itemprice*(110/100)
		old_amt= (itemprice*(110/100)) * self.qty
		
		self.selling_amount=old_amt
	def soldgain(self):
		cp=frappe.db.get_value("My Purchases",{"item_name":self.item_name},"buying_amount")
		profit=abs(self.selling_amount-cp)
		frappe.db.set_value("Company Stocks",{"stock_item":self.item_name},"profit",profit)