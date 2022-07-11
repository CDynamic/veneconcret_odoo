# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custom__crm(models.Model):
    _name = 'custom__crm.datosNacionales'
    _description = 'custom__crm.datosNacionales'

    name = fields.Char()
    fisrt_name = fields.Char()
    Document = fields.Integer()
    cedula = fields.Integer()

    
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
