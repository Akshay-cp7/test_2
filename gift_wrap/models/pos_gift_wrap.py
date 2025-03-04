from odoo import fields,models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    gift_wrap=fields.Boolean(string="Is Gift wrap",default=False)



