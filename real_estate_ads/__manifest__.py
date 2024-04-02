{
    "name": "Real Estate Ads",
    "version":"1.0",
    "website":"https//jameskamz.com",
    "author": "James",
    "description":"""
        Module to show available properties
    """,
    "category": "Sales",
    "depends":['base'],
    "data":[
        'security/ir.models.access.csv',
        'views/property_view.xml',
        'views/menu_items.xml'
    ],
    "installable":True,
    "application":True,
    "license":"LGPL-3"
}