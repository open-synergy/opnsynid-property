# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class PropertyObject(models.Model):
    _name = "property.object"
    _inherit = [
        "property.object",
        "mro.object_common",
    ]

    operation_ids = fields.One2many(
        comodel_name="mro.operation_property",
    )
    maintenance_ids = fields.One2many(
        comodel_name="mro.operation_maintenance_property",
    )

    @api.multi
    def action_open_mro_operation(self):
        self.ensure_one()
        return self._get_mro_operation_waction(
            "property_mro.mro_operation_property_action"
        )

    @api.multi
    def action_open_mro_maintenance(self):
        self.ensure_one()
        return self._get_mro_operation_waction(
            "property_mro.mro_operation_maintenance_property_action"
        )
