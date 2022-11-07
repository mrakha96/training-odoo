# -*- coding: utf-8 -*-
# from odoo import http


# class Ppm15(http.Controller):
#     @http.route('/ppm15/ppm15/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ppm15/ppm15/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ppm15.listing', {
#             'root': '/ppm15/ppm15',
#             'objects': http.request.env['ppm15.ppm15'].search([]),
#         })

#     @http.route('/ppm15/ppm15/objects/<model("ppm15.ppm15"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ppm15.object', {
#             'object': obj
#         })
