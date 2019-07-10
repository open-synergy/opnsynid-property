# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class MroOperationProperty(models.Model):
    _name = "mro.operation_property"
    _inherit = [
        "mro.operation_common"
    ]
    _description = "MRO Operation for Property"

    @api.multi
    @api.depends(
        "type_id",
    )
    def _compute_policy(self):
        _super = super(MroOperationProperty, self)
        _super._compute_policy()

    @api.model
    def _default_type_id(self):
        return self.env.ref(
            "property_mro."
            "mro_operation_type_property").id

    mro_object_id = fields.Many2one(
        string="Property",
        comodel_name="property.object",
    )
    type_id = fields.Many2one(
        default=lambda self: self._default_type_id(),
    )
    maintenance_ids = fields.One2many(
        comodel_name="mro.operation_maintenance_property",
    )

    @api.multi
    def action_open_mro_maintenance(self):
        self.ensure_one()
        return self._get_mro_maintenance_waction(
            "property_mro.mro_operation_maintenance_property_action")
