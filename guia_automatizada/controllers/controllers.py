# -*- coding: utf-8 -*-
from odoo import http
from suds.client import Client

# soap_msg = '''<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
# ..... some soap message
# </soap:Envelope>'''

# client = Client('https://soap_url_of_WSDL?WSDL')
# message = client.factory.create('Message')
# clientheader = client.factory.create('ClientHeader')
# # Add required details in HEADER as per WSDL rule
# clientheader.user = 'test' # credentials / token keys
# clientheader.SendAttempt = '0'
# message.ClientHeader = clientheader
# res_resp = client.service.ProcessMsg(message)
