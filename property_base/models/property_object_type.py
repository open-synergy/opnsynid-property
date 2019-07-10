# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class PropertyObjectType(models.Model):
    _name = "property.object_type"
    _description = "Property Type"

    name = fields.Char(
        string="Property",
        required=True,
    )
    note = fields.Text(
        string="Notes"
    )
    active = fields.Boolean(
        string="Active",
        default=True
    )
