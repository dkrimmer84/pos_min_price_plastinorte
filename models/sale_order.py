from odoo import models, fields, api, exceptions
import logging
_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.one
    def action_confirm(self):
        if self.team_id.margin_check:
            for line in self.order_line:
                min_price = line.product_id.min_price
                tax_factor = 1
                for tax in line.tax_id:
                    if tax.price_include:
                        tax_factor += tax.amount / 100

                if min_price and (line.price_unit < line.product_id.standard_price * (1 + min_price / 100) * tax_factor):
                    min_price_value = line.product_id.standard_price * (1 + min_price / 100) * tax_factor
                    
                    responsible_group = self.env.ref('sales_team.group_sale_manager')
                    user_in_responsible_group = responsible_group in self.env.user.groups_id

                    if not user_in_responsible_group:
                        raise exceptions.UserError(
                            "El precio $%s para %s está por debajo del mínimo permitido. "
                            "El Precio mínimo es $%s. Por favor, corrija el precio antes de continuar." % (
                                round(line.price_unit, 2),
                                line.product_id.name,
                                round(min_price_value, 2)
                            )
                        )
                    else:
                        _logger.info("Margin check bypassed for user: %s, product: %s", self.env.user.login, line.product_id.name)
        return super(SaleOrder, self).action_confirm()