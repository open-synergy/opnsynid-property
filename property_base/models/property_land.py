# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class PropertyLand(models.Model):
    _name = "property.land"
    _inherit = "property.object"
    _description = "Land"

    building_ids = fields.One2many(
        string="Buildings",
        comodel_name="property.building",
        inverse_name="land_id",
        )
