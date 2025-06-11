# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'estate',
    'version': '1.0',
    'category': 'Real Estate',
    'summary': 'Manage real estate properties',
    'description':'Module for managing real estate properties and offers.',
    'depends': [
        'base'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml'
    ],
    'installable':True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',

}