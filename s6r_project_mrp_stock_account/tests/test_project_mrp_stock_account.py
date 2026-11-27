# Copyright 2026 Scalizer (<https://www.scalizer.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo.tests import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestProjectMrpStockAccount(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.warehouse = cls.env["stock.warehouse"].search([("company_id", "=", cls.env.company.id)], limit=1)
        cls.warehouse.manufacture_steps = "pbm"
        cls.warehouse.pbm_type_id.analytic_costs = True
        plan = cls.env["account.analytic.plan"].create({"name": "Plan"})
        cls.account = cls.env["account.analytic.account"].create({"name": "Account", "plan_id": plan.id})
        cls.project = cls.env["project.project"].create({"name": "Project", "account_id": cls.account.id})
        cls.component = cls.env["product.product"].create(
            {"name": "Component", "is_storable": True, "standard_price": 10}
        )
        cls.finished = cls.env["product.product"].create({"name": "Finished", "is_storable": True})
        cls.env["mrp.bom"].create(
            {
                "product_tmpl_id": cls.finished.product_tmpl_id.id,
                "bom_line_ids": [(0, 0, {"product_id": cls.component.id, "product_qty": 2})],
            }
        )
        cls.env["stock.quant"]._update_available_quantity(cls.component, cls.warehouse.lot_stock_id, 10)

    def _confirm_production(self, project):
        production = self.env["mrp.production"].create(
            {
                "product_id": self.finished.id,
                "product_qty": 1,
                "project_id": project.id,
            }
        )
        production.action_confirm()
        return production.picking_ids.filtered(lambda picking: picking.picking_type_id == self.warehouse.pbm_type_id)

    def test_component_picking_gets_production_project(self):
        picking = self._confirm_production(self.project)
        self.assertEqual(picking.project_id, self.project)

    def test_component_picking_without_project(self):
        picking = self._confirm_production(self.env["project.project"])
        self.assertFalse(picking.project_id)

    def test_component_picking_analytic_cost_is_negative(self):
        picking = self._confirm_production(self.project)
        picking.action_assign()
        picking.move_ids.picked = True
        picking.button_validate()
        lines = picking.move_ids.analytic_account_line_ids
        self.assertEqual(picking.state, "done")
        self.assertEqual(lines.mapped(self.account.plan_id._column_name()), self.account)
        self.assertAlmostEqual(sum(lines.mapped("amount")), -20)

    def test_component_picking_analytic_distribution_of_production(self):
        plan2 = self.env["account.analytic.plan"].create({"name": "Plan 2"})
        account2 = self.env["account.analytic.account"].create({"name": "Account 2", "plan_id": plan2.id})
        production = self.env["mrp.production"].create(
            {
                "product_id": self.finished.id,
                "product_qty": 1,
                "analytic_distribution": {str(self.account.id): 100, str(account2.id): 100},
            }
        )
        production.action_confirm()
        picking = production.picking_ids.filtered(lambda picking: picking.picking_type_id == self.warehouse.pbm_type_id)
        picking.action_assign()
        picking.move_ids.picked = True
        picking.button_validate()
        lines = picking.move_ids.analytic_account_line_ids
        self.assertEqual(lines.mapped(self.account.plan_id._column_name()), self.account)
        self.assertEqual(lines.mapped(plan2._column_name()), account2)

    def test_component_picking_production_location_analytic_cost(self):
        self.warehouse.pbm_loc_id.usage = "production"
        picking = self._confirm_production(self.project)
        picking.action_assign()
        picking.move_ids.picked = True
        picking.button_validate()
        lines = picking.move_ids.analytic_account_line_ids
        self.assertEqual(picking.state, "done")
        self.assertAlmostEqual(sum(lines.mapped("amount")), -20)
