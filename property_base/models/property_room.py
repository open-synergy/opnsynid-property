# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class PropertyRoom(models.Model):
    _name = "property.room"
    _description = "Room"

    name = fields.Char(
        string="Room",
        required=True,
        )
    floor_id = fields.Many2one(
        string="Floor",
        comodel_name="property.floor",
        required=False,
        )
    note = fields.Text(
        string="Notes"
    )
    active = fields.Boolean(
        string="Active",
        default=True
    )
