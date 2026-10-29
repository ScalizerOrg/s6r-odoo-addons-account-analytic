# Copyright 2026 Scalizer (<https://www.scalizer.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models


class StockPickingType(models.Model):
    _inherit = "stock.picking.type"

    analytic_costs_skip_mto = fields.Boolean(
        string="Skip MTO Moves",
        help="Do not generate analytic entries for the moves supplied on order "
        "(MTO) and for the purchase receipts feeding them: their analytic cost "
        "comes from the vendor bill.",
    )
