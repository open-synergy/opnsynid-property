# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class PropertyRoom(models.AbstractModel):
    _name = "property.object"
    _description = "Common Class for Property Object"

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
