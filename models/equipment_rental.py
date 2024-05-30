from odoo import models, fields, api
from odoo.exceptions import ValidationError

class EquipmentRental(models.Model):
    _name = 'event.equipment.rental'
    _description = 'Equipment Rental'

    customer_id = fields.Many2one('event.customer', string='Customer', required=True)
    equipment_id = fields.Many2one('event.equipment', string='Equipment', required=True)
    rental_date = fields.Date(string='Rental Date', required=True, default=fields.Date.context_today)
    return_date = fields.Date(string='Return Date')
    quantity = fields.Integer(string='Quantity', required=True, default=1)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('returned', 'Returned'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft')

    @api.constrains('quantity')
    def _check_quantity(self):
        for record in self:
            if record.quantity < 1:
                raise ValidationError("Quantity must be at least 1.")

    @api.constrains('return_date')
    def _check_return_date(self):
        for record in self:
            if record.return_date and record.return_date < record.rental_date:
                raise ValidationError("Return Date cannot be before Rental Date.")
    
    def action_confirm(self):
        self.state = 'confirmed'
        return self._get_action_window()
    
    def action_draft(self):
        self.state = 'draft'
        return self._get_action_window()
    
    def action_returned(self):
        self.state = 'returned'
        return self._get_action_window()
    
    def action_cancel(self):
        self.state = 'cancelled'
        return self._get_action_window()
    
    def _get_action_window(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Equipment Rentals',
            'res_model': 'event.equipment.rental',
            'view_mode': 'tree,form',
            'target': 'current',
        }
