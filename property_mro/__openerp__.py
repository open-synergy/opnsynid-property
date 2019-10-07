# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Property Integration With MRO",
    "version": "8.0.1.0.1",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "property_base",
        "mro_common",
    ],
    "data": [
        "data/ir_sequence_data.xml",
        "data/base_sequence_configurator_data.xml",
        "data/mro_operation_type_data.xml",
        "data/base_workflow_policy_data.xml",
        "data/base_cancel_reason_configurator_data.xml",
        # "views/property_object_views.xml",
        "views/mro_operation_property_views.xml",
        "views/mro_operation_maintenance_property_views.xml",
    ],
}
