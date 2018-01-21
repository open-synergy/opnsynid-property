# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class PropertyFloor(models.Model):
    _name = "property.floor"
    _inherit = "property.object"
    _description = "Floor"

    building_id = fields.Many2one(
        string="Building",
        comodel_name="property.building",
        required=False,
        )
    room_ids = fields.One2many(
        string="Rooms",
        comodel_name="property.room",
        inverse_name="floor_id",
        )
