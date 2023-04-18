from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    min_price = fields.Float(
        string='Margen minimo',
        help='Margen minimo en %',
        default=0.0
    )

    def_retal = fields.Float(
        string="Definicion Retal", 
        help="Definición de Retal en la medida configurado del producto. Hasta esta cantidad se ignora el margen minimo.",
        default=0.0)

class ProductProduct(models.Model):
    _inherit = 'product.product'

    min_price = fields.Float(
        string='Margen minimo',
        help='Margen minimo en %',
        default=0.0,
        related='product_tmpl_id.min_price',
        store=True
    )

class PosConfig(models.Model):
    _inherit = 'pos.config'

    check_margin = fields.Boolean(string='Check Margin', default=False)
