# Copyright 2026 Scalizer (<https://www.scalizer.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    "name": "Scalizer Project MRP Stock Account",
    "version": "20.0.1.0.0",
    "author": "Scalizer",
    "website": "https://www.scalizer.fr",
    "category": "Specific Modules/Scalizer",
    "summary": "Analytic costs on the component pickings of manufacturing orders",
    "sequence": 0,
    "license": "LGPL-3",
    "depends": ["project_mrp", "project_stock_account"],
    "complexity": "easy",
    "description": """
Generate the analytic costs of the component pickings (multi-step
manufacturing) on the project of the manufacturing order:
- the picking feeding a manufacturing order gets the project of this order;
- the analytic cost of its moves is booked as a cost (negative amount).
    """,
    "qweb": [],
    "demo": [],
    "images": ["static/description/icon.png"],
    "data": [],
    "auto_install": False,
    "installable": True,
    "application": False,
}
