// Copyright (c) 2021, Sudarshan and contributors
// For license information, please see license.txt

frappe.ui.form.on('My Sales', {
	 refresh: function(frm) {
         frm.add_custom_button("My Purchase", ()=>{
			frappe.set_route("Form","My Purchases");
		 })
	 }
});
