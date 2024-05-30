{
    'name': 'Event Equipment Rental Management',
    'version': '1.0',
    'summary': 'Manage the rental of event equipment',
    'category': 'Event Management',
    'author': 'kawtar',
    'website': 'https://www.yourwebsite.com',
    'depends': ['base'],
    'data': [
        'views/category_view.xml',
        'views/equipment_view.xml',
        'views/customer_view.xml',
        'views/equipment_rental_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
