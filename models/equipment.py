from odoo import models, fields

class Equipment(models.Model):
    _name = 'event.equipment'
    _description = 'Event Equipment'

    name = fields.Char(string='Equipment Name', required=True)
    description = fields.Text(string='Description')
    quantity = fields.Integer(string='Quantity', required=True)
    category_id = fields.Many2one('event.equipment.category', string='Category', required=True)
    image = fields.Binary(string='Image')

    def action_save_and_close(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Equipment',
            'res_model': 'event.equipment',
            'view_mode': 'kanban,form',
            'target': 'current',
        }
