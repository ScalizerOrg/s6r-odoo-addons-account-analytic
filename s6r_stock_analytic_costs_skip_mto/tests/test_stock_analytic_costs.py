# Copyright 2026 Scalizer (<https://www.scalizer.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo.tests import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestStockAnalyticCosts(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product = cls.env["product.product"].create(
            {"name": "Product", "is_storable": True}
        )

    def _create_move(self, **values):
        return self.env["stock.move"].create(
            {
                "product_id": self.product.id,
                "product_uom_qty": 1,
                "location_id": self.env.ref("stock.stock_location_stock").id,
                "location_dest_id": self.env.ref("stock.stock_location_customers").id,
                **values,
            }
        )

    def test_make_to_stock_move_has_analytic_cost(self):
        move = self._create_move(procure_method="make_to_stock")
        self.assertFalse(move._is_analytic_cost_from_vendor_bill())

    def test_make_to_order_move_has_no_analytic_cost(self):
        move = self._create_move(procure_method="make_to_order")
        self.assertTrue(move._is_analytic_cost_from_vendor_bill())

    def test_skip_option_defaults_to_false(self):
        picking_type = self.env["stock.picking.type"].create(
            {"name": "Type", "code": "outgoing", "sequence_code": "T"}
        )
        self.assertFalse(picking_type.analytic_costs_skip_mto)
