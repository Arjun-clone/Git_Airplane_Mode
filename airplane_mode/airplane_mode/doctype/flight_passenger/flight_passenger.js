// Copyright (c) 2025, Arjun  and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Flight Passenger", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Flight Passenger', {
    before_save: function(frm) {
        frm.set_value("full_name", frm.doc.first_name + " " + frm.doc.last_name);
    }
});