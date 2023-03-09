from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo import http
from odoo.http import request

class WebsiteSale(WebsiteSale):

    @http.route('/shop/cart', type='http', auth='public', website=True)
    def cart(self, **kw):
        vals = super().cart(**kw)
        bom_product = eval(request.env['ir.config_parameter'].sudo().get_param(
                'bom_website.product_ids'))
        print(bom_product)
        vals.qcontext.update({
                   'products': bom_product
               })
        return vals



