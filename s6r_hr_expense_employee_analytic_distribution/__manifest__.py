# Copyright 2026 Scalizer (<https://www.scalizer.fr>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0.html).
{
    "name": "Scalizer HR Expense Employee Analytic Distribution",
    "version": "18.0.1.0.0",
    "author": "Scalizer",
    "website": "https://www.scalizer.fr",
    "summary": "Use manual analytic distribution set on employee on expense",
    "sequence": 0,
    "license": "AGPL-3",
    "depends": [
        "hr_expense",
        "s6r_hr_employee_analytic_distribution_manual",
    ],
    "category": "Generic Modules/Scalizer",
    "complexity": "easy",
    "qweb": [],
    "demo": [],
    "images": [],
    "data": [],
    "auto_install": False,
    "installable": True,
    "application": False,
}
