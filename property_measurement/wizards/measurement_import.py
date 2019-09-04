# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models


class PropertyMeasurementImport(models.TransientModel):
    _name = "property.measurement.import"
    _inherit = ["measurement.import"]
    _description = "Property Measurement Import"

    @api.multi
    def _get_obj_item_name(self):
        self.ensure_one()
        model = "property.measurement_item"
        return model
