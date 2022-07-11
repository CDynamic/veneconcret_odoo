# -*- coding: utf-8 -*-
# from odoo import http


# class CustomCrm(http.Controller):
#     @http.route('/custom__crm/custom__crm', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom__crm/custom__crm/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom__crm.listing', {
#             'root': '/custom__crm/custom__crm',
#             'objects': http.request.env['custom__crm.custom__crm'].search([]),
#         })

#     @http.route('/custom__crm/custom__crm/objects/<model("custom__crm.custom__crm"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom__crm.object', {
#             'object': obj
#         })
