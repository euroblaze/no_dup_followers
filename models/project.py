from odoo import models, api, fields
from odoo.tools.misc import clean_context


class ProjectProject(models.Model):
    _inherit = 'project.project'

    def copy(self, default=None):
        no_dup_followers = self.env['ir.config_parameter'].sudo().get_param('no_dup_followers.no_duplicating_followers_project', False)
        if no_dup_followers:
            self = self.with_context(no_dup_followers=True)
        return super(ProjectProject, self).copy(default)


class ProjectTask(models.Model):
    _inherit = 'project.task'

    def copy(self, default=None):
        no_dup_followers = self.env['ir.config_parameter'].sudo().get_param('no_dup_followers.no_duplicating_followers_project', False)
        if no_dup_followers:
            self = self.with_context(no_dup_followers=True)
        return super(ProjectTask, self).copy(default)

