# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Property Reservation - Common",
    "version": "8.0.1.0.0",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": False,
    "depends": [
        "mail",
        "property_base",
    ],
    "data": [
        "data/ir_sequence_data.xml",
        "security/ir.model.access.csv",
        "menu.xml",
        "views/property_reservation_type_views.xml",
        "views/property_reservation_common_views.xml",
    ],
}
