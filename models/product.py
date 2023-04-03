from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    min_price = fields.Float(
        string='Margen minimo',
        help='Margen minimo en %',
        default=0.0
    )

class ProductProduct(models.Model):
    _inherit = 'product.product'

    min_price = fields.Float(
        string='Margen minimo',
        help='Margen minimo en %',
        default=0.0,
        related='product_tmpl_id.min_price',
        store=True
    )