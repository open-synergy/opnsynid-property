# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class PropertyLand(models.Model):
    _name = "property.land"
    _description = "Land"

    name = fields.Char(
        string="Land",
        required=True,
        )
    building_ids = fields.One2many(
        string="Buildings",
        comodel_name="property.building",
        inverse_name="land_id",
        )
    note = fields.Text(
        string="Notes"
    )
    active = fields.Boolean(
        string="Active",
        default=True
    )
