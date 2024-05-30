from odoo import models, fields # type: ignore

class Category(models.Model):
    _name = 'event.equipment.category'
    _description = 'Equipment Category'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')

    def action_return_to_tree(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Equipment Categories',
            'res_model': 'event.equipment.category',
            'view_mode': 'tree',
            'target': 'current',
        }
