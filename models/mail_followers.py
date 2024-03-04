from odoo import models, api, fields


class Followers(models.Model):
    _inherit = 'mail.followers'

    @api.model_create_multi
    def create(self, vals_list):
        if self._context.get('no_dup_followers', False):
            return False
        return super(Followers, self).create(vals_list)
