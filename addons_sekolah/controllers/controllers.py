# -*- coding: utf-8 -*-
# from odoo import http


# class AddonsSekolah(http.Controller):
#     @http.route('/addons_sekolah/addons_sekolah/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/addons_sekolah/addons_sekolah/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('addons_sekolah.listing', {
#             'root': '/addons_sekolah/addons_sekolah',
#             'objects': http.request.env['addons_sekolah.addons_sekolah'].search([]),
#         })

#     @http.route('/addons_sekolah/addons_sekolah/objects/<model("addons_sekolah.addons_sekolah"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('addons_sekolah.object', {
#             'object': obj
#         })
