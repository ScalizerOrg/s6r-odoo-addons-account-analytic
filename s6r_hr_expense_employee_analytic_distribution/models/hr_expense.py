# Copyright 2026 Scalizer (<https://www.scalizer.fr>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0.html).

from odoo import api, models


class HrExpense(models.Model):
    _inherit = "hr.expense"

    @api.onchange("employee_id")
    def _onchange_employee_id_manual_distribution(self):
        """Apply the employee's manual analytic distribution on the expense.

        When an employee is selected on an expense, default its analytic
        distribution from the ``manual_distribution_id`` configured on the
        employee. If no manual distribution is set on the employee, the
        analytic distribution is cleared.
        """
        for expense in self:
            manual_distribution = expense.employee_id.manual_distribution_id
            expense.manual_distribution_id = manual_distribution
            expense.analytic_distribution = (
                manual_distribution.analytic_distribution or False
            )
