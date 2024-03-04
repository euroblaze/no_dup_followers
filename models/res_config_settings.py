from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    no_duplicating_followers_project = fields.Boolean(config_parameter='no_dup_followers.no_duplicating_followers_project')
