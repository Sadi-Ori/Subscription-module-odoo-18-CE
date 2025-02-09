# my_subscription_module/models/subscription.py
from odoo import models, fields

class Subscription(models.Model):
    _name = 'subscription.subscription'
    _description = 'Subscription Management'

    name = fields.Char('Subscription Name', required=True)
    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    start_date = fields.Date('Start Date', required=True)
    end_date = fields.Date('End Date', required=True)
    subscription_type = fields.Selection([
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('annual', 'Annual'),
    ], string='Subscription Type', required=True)
    amount = fields.Float('Subscription Amount', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('expired', 'Expired'),
    ], string='Status', default='draft')

    def activate_subscription(self):
        self.state = 'active'

    def expire_subscription(self):
        self.state = 'expired'

    def cancel_subscription(self):
        self.state = 'draft'
