# Copyright (c) 2025, Arjun  and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document


# class AirplaneTicket(Document):
# 	pass


#import frappe
from frappe.model.document import Document

class AirplaneTicket(Document):
    def validate(self):
        self.remove_duplicate_addons()
        self.calculate_total_amount()

    def calculate_total_amount(self):
        total_addon_amount = sum([addon.amount or 0 for addon in self.add_ons])
        self.total_amount = (self.flight_price or 0) + total_addon_amount

    def remove_duplicate_addons(self):
        seen = set()
        unique_add_ons = []
        for addon in self.add_ons:
            if addon.item not in seen:
                seen.add(addon.item)
                unique_add_ons.append(addon)
        
        # Replace the child table with unique entries
        self.set("add_ons", unique_add_ons)
        
        print("hai")
