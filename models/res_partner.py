from odoo import fields, models


class InheritUtm(models.Model):
    _inherit = "res.partner"

    campaign_id = fields.Many2one('utm.campaign')
    medium_id = fields.Many2one('utm.medium')
    source_id = fields.Many2one('utm.source')
    referred = fields.Char(string='Referred')