# Copyright 2026 Scalizer (<https://www.scalizer.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import models


class AccountAnalyticAccount(models.Model):
    _inherit = "account.analytic.account"

    def _perform_analytic_distribution(self, distribution, amount, unit_amount, lines, obj, additive=False):
        """Book the analytic amount of the component pickings as a cost.

        The standard only negates the amount of the outgoing valued moves: the
        internal moves picking components for a manufacturing order would
        otherwise be booked as an income.
        """
        if obj._name == "stock.move" and obj._is_production_component_picking():
            amount = -amount
        return super()._perform_analytic_distribution(distribution, amount, unit_amount, lines, obj, additive=additive)
