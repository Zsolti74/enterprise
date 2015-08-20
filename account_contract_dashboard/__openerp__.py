# -*- coding: utf-8 -*-

{
    'name': 'Account Contract Dashboard',
    'version': '1.0',
    'depends': ['sale_contract', 'account_asset'],  # TODO: add account_deferred_revenue when splitted
    'author': 'Odoo S.A.',
    'description': """
Accounting Contract Dashboard
========================
It adds dashboards to :
1) Analyse the recurrent revenue and other metrics for contracts
2) Analyse the contracts modifications by salesman and compute their value.
    """,
    'website': 'https://www.odoo.com/page/accounting',
    'category': 'Accounting & Finance',
    'data': [
        'views/account_contract_dashboard_report_view.xml',
        'templates/assets.xml',
    ],
    'demo': [
        'demo/account_contract_dashboard_demo.xml',
    ],
    'qweb': [
        "static/src/xml/account_contract_dashboard.xml",
    ],
    'installable': True,
    'application': False,
}