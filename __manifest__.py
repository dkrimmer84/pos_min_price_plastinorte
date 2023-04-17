# Copyright Dominic Krimmer <https://www.dkrimmer.de>
# License MIT (https://opensource.org/licenses/MIT).
{
    'name': 'POS Minimum Price Plastinorte',
    'version': '12.0.1.0.0',
    'category': 'Point of Sale',
    'author': 'Dominic Krimmer',
    'website': 'https://www.dkrimmer.de',
    'license': 'AGPL-3',
    'summary': 'Prevent selling products below the minimum margin',
    'depends': ['sale', 'point_of_sale', 'crm'],
    'data': [
        'views/pos_min_price_plastinorte_views.xml',
        'views/assets.xml',
        'views/crm_team_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
