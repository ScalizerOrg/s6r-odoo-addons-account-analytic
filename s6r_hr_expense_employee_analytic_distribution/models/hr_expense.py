# Copyright 2026 Scalizer (<https://www.scalizer.fr>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0.html).

from odoo import api, models


class HrExpense(models.Model):
    _inherit = "hr.expense"

    @api.depends(
        "product_id",
        "account_id",
        "employee_id",
        "employee_id.manual_distribution_id",
    )
    def _compute_analytic_distribution(self):
        """Give priority to the employee's manual analytic distribution.

        The standard computation applies the automatic distribution models
        (product, account prefix, ...). When the employee has a manual
        distribution configured, it overrides the result of those rules.
        Without a manual distribution on the employee, the standard result
        is kept.

        The employee field is restricted to ``hr.group_hr_user``, so it is read
        with ``sudo()`` to let regular users encode their own expenses.
        """
        super()._compute_analytic_distribution()
        for expense in self:
            manual_distribution = expense.employee_id.sudo().manual_distribution_id
            if manual_distribution:
                expense.manual_distribution_id = manual_distribution.id
                expense.analytic_distribution = (
                    manual_distribution.analytic_distribution or False
                )
