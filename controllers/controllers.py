# -*- coding: utf-8 -*-
# from odoo import http


# class GestionLocationMateriel(http.Controller):
#     @http.route('/gestion_location_materiel/gestion_location_materiel', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_location_materiel/gestion_location_materiel/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_location_materiel.listing', {
#             'root': '/gestion_location_materiel/gestion_location_materiel',
#             'objects': http.request.env['gestion_location_materiel.gestion_location_materiel'].search([]),
#         })

#     @http.route('/gestion_location_materiel/gestion_location_materiel/objects/<model("gestion_location_materiel.gestion_location_materiel"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_location_materiel.object', {
#             'object': obj
#         })

