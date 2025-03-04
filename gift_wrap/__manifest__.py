{
    'name': 'Pos Gift Wrap',
    "author": "Mithun Mohan",
    'version': '18.0',
    'category': 'Point of Sale',
    'sequence': '1',
    'license': 'LGPL-3',
    'summary': 'Introduces a gift wrap feature',
    'depends': ['point_of_sale'],
    'data': [
        'views/res_config_settings_views.xml',
        'views/gift_wrap_views.xml',
    ],
    'assets':{
            'point_of_sale._assets_pos': [
                'gift_wrap/static/src/app/custom_button/custom_button.js',
                'gift_wrap/static/src/app/custom_button/custom_button.xml',
                'gift_wrap/static/src/app/custom_popup/custom_popup.js',
                'gift_wrap/static/src/app/custom_popup/custom_popup.xml',
        ],
    }
}