# from odoo import fields,models
#
# class ResConfigSettings(models.TransientModel):
#    _inherit = 'res.config.settings'
#
#    is_gift_wrap=fields.Boolean(string="Gift Wrap",config_parameter='gift_wrap.is_gift_wrap')

from odoo import fields, models, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    is_gift_wrap = fields.Boolean(string="Gift Wrap", config_parameter='gift_wrap.is_gift_wrap')
    gift_wrap_product_id = fields.Many2one(
        'product.template',
        string="Gift Wrap Product",
        domain="[('gift_wrap', '=', True)]",
        config_parameter='gift_wrap.gift_wrap_product_id'
    )

    @api.depends('is_gift_wrap')
    def _compute_gift_wrap_products(self):
        for record in self:
            record.gift_wrap_product_ids = self.env['product.template'].search([('gift_wrap', '=', True)])
