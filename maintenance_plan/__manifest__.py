# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Maintenance Plan",
    "summary": "Extends preventive maintenance planning",
    "version": "14.0.1.6.3",
    "author": "Camptocamp SA, ForgeFlow, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "category": "Maintenance",
    "website": "https://github.com/OCA/maintenance",
    "images": [],
    "depends": ["base_maintenance"],
    "data": [
        "security/ir.model.access.csv",
        "security/maintenance_security.xml",
        "views/maintenance_kind_views.xml",
        "views/maintenance_plan_views.xml",
        "views/maintenance_equipment_views.xml",
        "views/report_maintenance_request.xml",
    ],
    "external_dependencies": {"python": ["dateutil"]},
    "demo": ["data/demo_maintenance_plan.xml"],
    "post_init_hook": "post_init_hook",
    "installable": True,
}
