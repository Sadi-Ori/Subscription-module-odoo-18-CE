{
    'name': 'Subscription Management',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Manage subscriptions for customers',
    'depends': ['base', 'sale'],
    'data': [
    'security/ir.model.access.csv',
    'views/subscription_views.xml',
    'data/models.xml',  # Add this file for model external ID
],
    'installable': True,
    'application': True,
}
