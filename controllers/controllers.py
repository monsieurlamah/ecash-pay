# -*- coding: utf-8 -*-
# from odoo import http


# class MPaie(http.Controller):
#     @http.route('/m_paie/m_paie', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/m_paie/m_paie/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('m_paie.listing', {
#             'root': '/m_paie/m_paie',
#             'objects': http.request.env['m_paie.m_paie'].search([]),
#         })

#     @http.route('/m_paie/m_paie/objects/<model("m_paie.m_paie"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('m_paie.object', {
#             'object': obj
#         })
