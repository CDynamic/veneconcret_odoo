# -*- coding: utf-8 -*-
# from odoo import http


# class Sicm(http.Controller):
#     @http.route('/sicm/sicm', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sicm/sicm/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sicm.listing', {
#             'root': '/sicm/sicm',
#             'objects': http.request.env['sicm.sicm'].search([]),
#         })

#     @http.route('/sicm/sicm/objects/<model("sicm.sicm"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sicm.object', {
#             'object': obj
#         })
