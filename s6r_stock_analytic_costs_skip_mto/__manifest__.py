# Copyright 2026 Scalizer (<https://www.scalizer.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    "name": "Scalizer Stock Analytic Costs Skip MTO",
    "version": "20.0.1.0.0",
    "author": "Scalizer",
    "website": "https://www.scalizer.fr",
    "category": "Specific Modules/Scalizer",
    "summary": "Skip the analytic cost of MTO moves per operation type",
    "sequence": 0,
    "license": "LGPL-3",
    "depends": ["project_stock_account", "purchase_stock"],
    "complexity": "easy",
    "description": """
Add a Skip MTO Moves option on the operation types generating analytic costs.
When checked, the moves supplied on order (MTO) and the purchase receipts
feeding them do not create analytic entries: their analytic cost comes from
the vendor bill, so it would be counted twice.
    """,
    "qweb": [],
    "demo": [],
    "images": ["static/description/icon.png"],
    "data": [
        # Views
        "views/stock_picking_type_views.xml",
    ],
    "auto_install": False,
    "installable": True,
    "application": False,
}
