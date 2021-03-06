# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Mobile',
    'category': 'Mobile',
    'summary': 'Odoo Mobile Core module',
    'version': '1.0',
    'description': """
        This module provides the core of the Odoo Mobile App.
        """,
    'depends': ['web_settings_dashboard'],
    'qweb': ['static/src/xml/web_template.xml', 'static/src/xml/user_menu.xml'],
    'data': ['views/mobile_template.xml', 'views/views.xml'],
    'installable': True,
    'auto_install': True,
    'license': 'OEEL-1',
}
