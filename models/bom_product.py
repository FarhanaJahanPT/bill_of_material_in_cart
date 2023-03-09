from ast import literal_eval

from odoo import models, fields, api


class ProductBom(models.TransientModel):
    _inherit = 'res.config.settings'

    bom_product = fields.Boolean(string='Product BOM')
    product_ids = fields.Many2many('product.template', string='Products')

    def set_values(self):
        res1 = super(ProductBom, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('bom_website.bom_product', self.bom_product),
        self.env['ir.config_parameter'].sudo().set_param('bom_website.product_ids', self.product_ids.ids)
        return res1

    @api.model
    def get_values(self):
        res = super(ProductBom, self).get_values()
        get_param = self.env['ir.config_parameter'].sudo().get_param
        values = self.env['ir.config_parameter'].sudo()
        product = values.get_param('bom_website.product_ids')
        res.update(
            bom_product=get_param('bom_website.bom_product'),

            product_ids=[(6, 0, literal_eval(product))] if product else False,)
        return res