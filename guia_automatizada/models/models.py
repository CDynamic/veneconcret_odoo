# -*- coding: utf-8 -*-

from suds.client import Client
from odoo import models, fields, api


class modelCMCredentials(models.Model):
    _name = 'guia_automatizada.credentials'

    code_sicm = fields.Char(string='Código SICM')
    code_segurity= fields.Char(string='Código Seguridad')
    

    

class guíasMovilización(models.Model):
    # cod_seguridad, sicm_destino, bultos, documentos
    _name = 'guia_automatizada.guias'

    cod_seguridad = fields.Char(string= 'Numero de la Guia')
    created = fields.Datetime(string= 'Fecha de creacion') 
    updated = fields.Datetime(string= 'Fecha de Actualizacion') 


class guíasMovilización(models.Model):
    _inherit = 'account.move'
    generarGuia = fields.Boolean(string='Guia de Movilizacion', readonly=False)

    

# class GenerateGuia(models.Model):
    

#     x = Client
#     x = x('http://www.sicm.gob.ve/sicm.php?wsdl')
#     age = x.service.guia_status('IzUkZ/bpFc835/6j0F+xUAGYZ32sCFripj1pfpxtTE2dmxPdFnF5iZ5ti9CYAZ0Hp08WHrWF+291Zoy4rJko8M', '26752403')
#     print(age)