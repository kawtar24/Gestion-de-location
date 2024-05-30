from odoo import models, fields

class Customer(models.Model):
    _name = 'event.customer'
    _description = 'Customer'

    name = fields.Char(string='Customer Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')

    def action_return_to_tree(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Customers',
            'res_model': 'event.customer',
            'view_mode': 'tree',
            'target': 'current',
        }
