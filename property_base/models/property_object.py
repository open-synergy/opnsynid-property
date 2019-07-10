# -*- coding: utf-8 -*-
# Copyright 2018-2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields


class PropertyObject(models.Model):
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
    parent_id = fields.Many2one(
        string="Parent Property",
        comodel_name="property.object",
    )
    partner_id = fields.Many2one(
        string="Owner",
        comodel_name="res.partner",
    )
    type_id = fields.Many2one(
        string="Type",
        comodel_name="property.object_type",
    )
