# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class gestion_location_materiel(models.Model):
#     _name = 'gestion_location_materiel.gestion_location_materiel'
#     _description = 'gestion_location_materiel.gestion_location_materiel'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

