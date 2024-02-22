from odoo import models, api

class ProjectProject(models.Model):
    _inherit = 'project.project'

    @api.model
    def _get_duplicate_followers(self):
        Param = self.env['ir.config_parameter'].sudo()
        return Param.get_param('duplicate_followers', '0') == '0'

    def copy(self, default=None):
        if default is None:
            default = {}
        if not self._get_duplicate_followers():
            default['message_follower_ids'] = False
        return super(ProjectProject, self).copy(default)

class ProjectTask(models.Model):
    _inherit = 'project.task'

    def copy(self, default=None):
        if default is None:
            default = {}
        if not self.env['project.project']._get_duplicate_followers():
            default['message_follower_ids'] = False
        return super(ProjectTask, self).copy(default)
