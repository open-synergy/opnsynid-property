# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api
from datetime import datetime


class RentalProperty(models.Model):
    _name = "rental.property"
    _description = "Property Rental"
    _inherit = [
        "rental.common",
    ]

    @api.multi
    @api.depends(
        "type_id",
    )
    def _compute_policy(self):
        _super = super(RentalProperty, self)
        _super._compute_policy()

    @api.model
    def _default_type_id(self):
        return self.env.ref(
            "rental_property."
            "rental_property_type").id

    @api.multi
    @api.depends(
        "upfront_cost_ids",
        "upfront_cost_ids.amount_untaxed",
        "upfront_cost_ids.amount_tax",
        "upfront_cost_ids.amount_total",
    )
    def _compute_upfront_cost(self):
        _super = super(RentalProperty, self)
        _super._compute_upfront_cost()

    type_id = fields.Many2one(
        default=lambda self: self._default_type_id(),
    )
    detail_ids = fields.One2many(
        comodel_name="rental.property_detail",
    )
    upfront_cost_ids = fields.One2many(
        comodel_name="rental.property_upfront_cost",
    )

    @api.model
    def run_create_invoice(self):
        obj_schedule =\
            self.env["rental.property_detail_schedule"]
        date_now =\
            datetime.now().strftime("%Y-%m-%d")
        criteria = [
            ("date", "=", date_now)
        ]
        schedule_ids = obj_schedule.search(criteria)
        if schedule_ids:
            for schedule in schedule_ids:
                if schedule.rental_state == "open":
                    schedule._create_invoice()
                    schedule.write({
                        "state": "post",
                    })
