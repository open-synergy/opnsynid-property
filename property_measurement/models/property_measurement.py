# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class PropertyMeasurement(models.Model):
    _name = "property.measurement"
    _inherit = [
        "measurement.common"
    ]
    _description = "Measurement for Property"

    @api.multi
    @api.depends(
        "type_id",
    )
    def _compute_policy(self):
        _super = super(PropertyMeasurement, self)
        _super._compute_policy()

    @api.model
    def _default_type_id(self):
        return self.env.ref(
            "property_measurement."
            "measurement_type_property").id

    object_id = fields.Many2one(
        string="Property",
        comodel_name="property.object",
    )
    type_id = fields.Many2one(
        default=lambda self: self._default_type_id(),
    )
    item_ids = fields.One2many(
        comodel_name="property.measurement_item",
    )
