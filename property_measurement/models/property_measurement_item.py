# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class PropertyMeasurementItem(models.Model):
    _name = "property.measurement_item"
    _inherit = [
        "measurement.item_common"
    ]
    _description = "Measurement for Property"

    @api.multi
    @api.depends(
        "item_type_id",
    )
    def _compute_allowed_qualitative_option_ids(self):
        _super = super(PropertyMeasurementItem, self)
        _super._compute_allowed_qualitative_option_ids()

    measurement_id = fields.Many2one(
        comodel_name="property.measurement",
        required=True,
        ondelete="cascade",
    )
    allowed_qualitative_option_ids = fields.Many2many(
        compute="_compute_allowed_qualitative_option_ids",
        store=False,
    )
