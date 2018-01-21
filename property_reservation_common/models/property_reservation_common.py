# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api
from openerp.tools.translate import _
from openerp.exceptions import Warning as UserError


class PropertyReservationCommon(models.AbstractModel):
    _name = "property.reservation_common"
    _inherit = ["mail.thread"]
    _description = "Property Reservation Common Class"

    @api.model
    def _default_company_id(self):
        return self.env.user.company_id.id

    name = fields.Char(
        string="# Reservation",
        required=True,
        default="/",
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
        default=lambda self: self._default_company_id(),
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    type_id = fields.Many2one(
        string="Reservation Type",
        required=True,
        comodel_name="property.reservation_type",
    )
    property_id = fields.Many2one(
        string="Property",
        comodel_name="property.object",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    date_order = fields.Datetime(
        string="Date Order",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    date_start = fields.Datetime(
        string="Date Start",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    date_end = fields.Datetime(
        string="Date End",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    partner_id = fields.Many2one(
        string="Partner",
        comodel_name="res.partner",
        required=True,
        readonly=True,
        states={
            "draft": [
                ("readonly", False),
            ],
        },
    )
    note = fields.Text(
        string="Note",
    )
    state = fields.Selection(
        string="State",
        selection=[
            ("draft", "Draft"),
            ("confirm", "Waiting for Approval"),
            ("approve", "Ready to Process"),
            ("start", "Start"),
            ("finish", "Finish"),
            ("cancel", "Cancelled"),
        ],
        default="draft",
        required=True,
        readonly=True,
    )

    @api.model
    def create(self, values):
        values = self._prepare_create_data(values)
        _super = super(PropertyReservationCommon, self)
        return _super.create(values)

    @api.multi
    def button_confirm(self):
        for reservation in self:
            reservation.write(self._prepare_confirm_data())

    @api.multi
    def button_approve(self):
        for reservation in self:
            reservation.write(self._prepare_approve_data())

    @api.multi
    def button_start(self):
        for reservation in self:
            reservation.write(self._prepare_start_data())

    @api.multi
    def button_finish(self):
        for reservation in self:
            reservation.write(self._prepare_finish_data())

    @api.multi
    def button_cancel(self):
        for reservation in self:
            reservation.write(self._prepare_cancel_data())

    @api.multi
    def button_restart(self):
        for reservation in self:
            reservation.write(self._prepare_restart_data())

    @api.model
    def _prepare_create_data(self, values):
        name = values.get("name", False)
        if name == "/" or not name:
            values["name"] = self._create_sequence(
                values["type_id"])

        return values

    @api.multi
    def _prepare_confirm_data(self):
        self.ensure_one()
        result = {
            "state": "confirm",
        }
        return result

    @api.multi
    def _prepare_approve_data(self):
        self.ensure_one()
        result = {
            "state": "approve",
        }
        return result

    @api.multi
    def _prepare_start_data(self):
        self.ensure_one()
        result = {
            "state": "start",
        }
        return result

    @api.multi
    def _prepare_finish_data(self):
        self.ensure_one()
        result = {
            "state": "finish",
        }
        return result

    @api.multi
    def _prepare_cancel_data(self):
        self.ensure_one()
        result = {
            "state": "cancel",
        }
        return result

    @api.multi
    def _prepare_restart_data(self):
        self.ensure_one()
        result = {
            "state": "draft",
        }
        return result

    @api.model
    def _create_sequence(self, type_id):
        sequence_id = self._get_sequence_id(
            type_id)
        sequence = self.env["ir.sequence"].\
            next_by_id(sequence_id)
        return sequence

    @api.model
    def _get_sequence_id(self, type_id):
        sequence = self.env["property.reservation_type"].\
            browse(type_id)[0].sequence_id

        if not sequence:
            try:
                sequence = self.env.ref(
                    "property_reservation_common.sequence_reservation")
            except:
                err_msg = _("No sequence defined")
                raise UserError(err_msg)
        return sequence.id
