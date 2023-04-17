from odoo import models, fields

class CrmTeam(models.Model):
    _inherit = 'crm.team'

    margin_check = fields.Boolean("Margin Check", default=False, help="Activate margin check in the sales order.")