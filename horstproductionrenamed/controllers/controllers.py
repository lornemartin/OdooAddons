# -*- coding: utf-8 -*-
from odoo import http

# class Horstproduction(http.Controller):
#     @http.route('/horstproduction/horstproduction/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/horstproduction/horstproduction/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('horstproduction.listing', {
#             'root': '/horstproduction/horstproduction',
#             'objects': http.request.env['horstproduction.horstproduction'].search([]),
#         })

#     @http.route('/horstproduction/horstproduction/objects/<model("horstproduction.horstproduction"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('horstproduction.object', {
#             'object': obj
#         })