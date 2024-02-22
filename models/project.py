from odoo import models, api, fields

class Project(models.Model):
    _inherit = 'project.project'

    @api.model
    def _get_follower_notifications(self):
        return self.env['ir.config_parameter'].sudo().get_param('project_duplication_control.activate_follower_notifications', 'False')

    def copy(self, default=None):
        if default is None:
            default = {}
        if self._get_follower_notifications() == 'False':
            default['message_follower_ids'] = False
        return super(Project, self).copy(default)

class ProjectTask(models.Model):
    _inherit = 'project.task'

    def copy(self, default=None):
        if default is None:
            default = {}
        if self.env['project.project']._get_follower_notifications() == 'False':
            default['message_follower_ids'] = False
        return super(ProjectTask, self).copy(default)
