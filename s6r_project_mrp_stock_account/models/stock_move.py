# Copyright 2026 Scalizer (<https://www.scalizer.fr>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import models
from odoo.fields import Domain


class StockMove(models.Model):
    _inherit = "stock.move"

    def _is_production_component_picking(self):
        """Tell whether the move picks components for a manufacturing order.

        Such an internal move (e.g. Stock -> Pre-Production) feeds the
        component moves of a manufacturing order.

        :return: True if the move feeds a manufacturing order component move
        :rtype: bool
        """
        self.ensure_one()
        return bool(self.move_dest_ids.raw_material_production_id) and not self._is_out()

    def _get_production_component_distribution(self):
        """Return the analytic distribution of the manufacturing order fed by the move.

        :return: the distribution (all analytic plans) of the order, empty if none
        :rtype: dict
        """
        self.ensure_one()
        production = self.move_dest_ids.raw_material_production_id
        if len(production) == 1 and not self._is_out():
            return production.analytic_distribution or {}
        return {}

    def _get_analytic_distribution(self):
        """Use the analytic distribution of the manufacturing order (all plans)."""
        return self._get_production_component_distribution() or super()._get_analytic_distribution()

    def _get_valid_moves_domain(self):
        """Also generate the analytic entries of the component moves without project."""
        domain = super()._get_valid_moves_domain()
        return Domain.OR([[("move_dest_ids.raw_material_production_id.analytic_distribution", "!=", False)], domain])

    def _get_new_picking_values(self):
        """Set the project of the manufacturing order on its component picking.

        :return: the values to create the picking
        :rtype: dict
        """
        values = super()._get_new_picking_values()
        project = self.move_dest_ids.raw_material_production_id.project_id
        if not values.get("project_id") and len(project) == 1:
            values["project_id"] = project.id
        return values
