# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class PropertyBuilding(models.Model):
    _name = "property.building"
    _description = "Building"

    name = fields.Char(
        string="Building",
        required=True,
        )
    land_id = fields.Many2one(
        string="Land",
        comodel_name="property.land",
        required=False,
        )
    floor_ids = fields.One2many(
        string="Floors",
        comodel_name="property.floor",
        inverse_name="building_id",
        )
    note = fields.Text(
        string="Notes"
    )
    active = fields.Boolean(
        string="Active",
        default=True
    )
