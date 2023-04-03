{
    'name': 'POS Minimum Price Plastinorte',
    'version': '12.0.1.0.0',
    'category': 'Point of Sale',
    'author': 'Dominic',
    'website': 'https://www.dkrimmer.de',
    'license': 'AGPL-3',
    'summary': 'Prevent selling products below the minimum margin',
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_min_price_plastinorte_views.xml',
        'views/assets.xml',
    ],
    'qweb': [
        'static/src/xml/pos_min_price_plastinorte_templates.xml',
    ],
    'installable': True,
    'auto_install': False,
}

