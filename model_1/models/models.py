# -*- coding: utf-8 -*-

from pkg_resources import require
from odoo import models, fields, api


class visit(models.Model):
    _name = 'model_1.visit'
    _description = 'visit'

    name = fields.Char(string='nombre')
    last_name = fields.Many2one(string='Cliente', comodel_name="res.partner")
    date = fields.Datetime(string='Fecha')
    type = fields.Selection([('0', 'Venezolano'),('1','Extrangero'),('2','Gobernamental')], string='Tipo', required=True)
    done = fields.Boolean(string='Realizada',readonly=True)
    image = fields.Binary(string='Imagenes')
    def toggle_state(self):
        self.done = not self.done
    
# class documentacion():
#     _name = 'model_1.documentacion'