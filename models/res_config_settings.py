from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    activate_follower_notifications_on_duplication = fields.Boolean(
        string='Activate Follower Notifications on Duplication',
        config_parameter='no_dup_followers.activate_follower_notifications_on_duplication',
    )
