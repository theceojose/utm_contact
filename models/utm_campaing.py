from odoo import fields, models


class UtmCampaign(models.Model):
    _inherit = "utm.campaign"

    related_contact_count = fields.Integer(string='Related contacts', compute='_compute_related_contact_count')

    def action_view_related_contacts(self):
        self.ensure_one()
        action = self.env.ref('base.action_partner_form').read()[0]
        action['domain'] = [('campaign_id', '=', self.id)]
        return action

    def _compute_related_contact_count(self):
        self.related_contact_count = self.env['res.partner'].search_count([('campaign_id', '=', self.id)])