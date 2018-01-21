# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class PropertyRoom(models.Model):
    _name = "property.room"
    _inherit = "property.object"
    _description = "Room"

    floor_id = fields.Many2one(
        string="Floor",
        comodel_name="property.floor",
        required=False,
        )
