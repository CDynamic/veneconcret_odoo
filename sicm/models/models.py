# -*- coding: utf-8 -*-




from odoo import models, fields, api


class modelCMCredentials(models.Model):
    _name = 'sicm.credentials'

    username = fields.Char(string='Nombre De Usuario')
    password = fields.Char(string='contraseña')

    

class guíasMovilización(models.Model):
    _name = 'sicm.guias'

    guia = fields.Char(string= 'Numero de la Guia')
    created = fields.Datetime(string= 'Fecha de creacion') 
    updated = fields.Datetime(string= 'Fecha de Actualizacion') 

    

    