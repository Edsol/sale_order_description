# -*- coding: utf-8 -*-
# from odoo import http


# class SaleOrderDescription(http.Controller):
#     @http.route('/sale_order_description/sale_order_description/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_order_description/sale_order_description/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_order_description.listing', {
#             'root': '/sale_order_description/sale_order_description',
#             'objects': http.request.env['sale_order_description.sale_order_description'].search([]),
#         })

#     @http.route('/sale_order_description/sale_order_description/objects/<model("sale_order_description.sale_order_description"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_order_description.object', {
#             'object': obj
#         })
