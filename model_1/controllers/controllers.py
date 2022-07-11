# -*- coding: utf-8 -*-
# from odoo import http


# class Model1(http.Controller):
#     @http.route('/model_1/model_1', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/model_1/model_1/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('model_1.listing', {
#             'root': '/model_1/model_1',
#             'objects': http.request.env['model_1.model_1'].search([]),
#         })

#     @http.route('/model_1/model_1/objects/<model("model_1.model_1"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('model_1.object', {
#             'object': obj
#         })
