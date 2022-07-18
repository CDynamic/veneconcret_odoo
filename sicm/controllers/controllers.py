# -*- coding: utf-8 -*-
from odoo import http
import requests
from bs4 import BeautifulSoup
from odoo.http import Response
import json

class scrapinTest(http.Controller):
    @http.route('/test')
    def scrape(self,**kw):
        header = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
        sicm = requests.Session()
        html = sicm.get('http://www.sicm.gob.ve/inicio.php?ms=',headers=header).content
        soup = BeautifulSoup(html,'html.parser')
        # print(soup)
        print(soup.find(id="img_cap").text)
        # req ={

        #     'login': 'admin',
        #     'password': '123456',
        #     'rt_admin_captcha': 2,
        #     'btn_login': 'Entrar',
        #     'log': 'true'
        # }
        # sicm.post('http://www.sicm.gob.ve/inicio.php?ms=',req)
        html = sicm.get('http://www.sicm.gob.ve/inicio.php?ms=').content
        return html

    @http.route('/sicm/objects/<model("account.move"):obj>', auth='public')
    def object(self, obj, **kw):
        print(obj)
        return Response({
            'object': obj
        }, content_type='application/json;charset=utf-8', status=200)
    #     return http.request.render('sicm.listing', {
    #         'object': obj
    #     }