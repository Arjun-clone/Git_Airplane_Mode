# Copyright (c) 2025, Arjun  and contributors
# For license information, please see license.txt


# import frappe
from frappe.model.document import Document

# from frappe.model.mapper import get_mapped_doc
# from frappe.utils import nowdate, nowtime, get_fullname


class FlightPassenger(Document):
    def validate(doc):
        doc.full_name = f"{doc.first_name} {doc.last_name}"


