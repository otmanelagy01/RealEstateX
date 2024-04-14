# -*- coding: utf-8 -*-
{
    'name': "RealEstateX Complaint",

    'summary': "RealEstateX Complaint module for The complaint management",

    'description': """
RealEstateX Complaint module for The complaint management
    """,

    'author': "RealEstateX, otman EL AGY",
    # 'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/17.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '17.0',
    "license": 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/email_template_complaint.xml',
        'data/sequence.xml',
        'data/email_template_complaint_closed.xml',
        'reports/work_order_report.xml',
        'views/complaint_templates.xml',
        'views/complaint_success_page_templates.xml',
        'views/realestatex_complaint.xml',
        'views/complaint_menu.xml',
    ],
    # only loaded in demonstration mode
}

