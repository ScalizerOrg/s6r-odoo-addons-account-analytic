# Copyright 2026 Scalizer (<https://www.scalizer.fr>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0.html).

from odoo import fields, models


class HrEmployeePublic(models.Model):
    _inherit = "hr.employee.public"

    manual_distribution_id = fields.Many2one(
        comodel_name="account.analytic.distribution.manual",
        string="Manual Analytic Distribution",
        compute="_compute_manager_only_fields",
        help="Manual analytic distribution applied by default on the employee's "
        "expenses. Only visible to the employee's managers.",
    )

    def _get_manager_only_fields(self):
        """Expose the manual analytic distribution to the employee's managers.

        The field is restricted to ``hr.group_hr_user`` on ``hr.employee``, so
        it is mirrored here through the standard manager-only mechanism: it is
        computed from the private employee record and only filled in for users
        the employee reports to.

        :return: field names readable by the employee's managers
        :rtype: list
        """
        return super()._get_manager_only_fields() + ["manual_distribution_id"]
