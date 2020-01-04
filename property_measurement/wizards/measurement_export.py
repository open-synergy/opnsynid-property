# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models


class PropertyMeasurementExport(models.TransientModel):
    _name = "property.measurement.export"
    _inherit = ["measurement.export"]
    _description = "Property Measurement Export"
