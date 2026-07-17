# Copyright 2026 Scalizer (<https://www.scalizer.fr>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0.html).

from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    manual_distribution_id = fields.Many2one(
        comodel_name="account.analytic.distribution.manual",
        string="Manual Analytic Distribution",
        domain="['|', ('company_id', '=', company_id), ('company_id', '=', False)]",
        help="Manual analytic distribution applied by default on the employee's "
        "expenses.",
    )
