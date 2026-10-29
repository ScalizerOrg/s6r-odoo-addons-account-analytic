# Copyright 2026 Scalizer (<https://www.scalizer.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import models


class StockMove(models.Model):
    _inherit = "stock.move"

    def _is_analytic_cost_from_vendor_bill(self):
        """Tell whether the analytic cost of the move comes from a vendor bill.

        This is the case of a move supplied on order (MTO) and of the purchase
        receipt feeding such a move.

        :return: True if no analytic entry must be created for the move
        :rtype: bool
        """
        self.ensure_one()
        if self.procure_method == "make_to_order":
            return True
        return bool(
            self.purchase_line_id
            and self.move_dest_ids.filtered(
                lambda move: move.procure_method == "make_to_order"
            )
        )

    def _create_analytic_move(self):
        moves = self.filtered(
            lambda move: not (
                move.picking_type_id.analytic_costs_skip_mto
                and move._is_analytic_cost_from_vendor_bill()
            )
        )
        return super(StockMove, moves)._create_analytic_move()
