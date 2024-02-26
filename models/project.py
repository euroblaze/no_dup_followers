from odoo import models, api, fields


class ProjectProject(models.Model):
    _inherit = 'project.project'

    def copy(self, default=None):
        no_dup_followers = self.env['ir.config_parameter'].sudo().get_param('no_dup_followers.no_duplicating_followers_project', False)
        if not no_dup_followers:
            return super(ProjectProject, self).copy(default)
        project = super(ProjectProject, self).copy(default)
        self.env['mail.followers'].search([('res_model', '=', 'project.project'), ('res_id', '=', project.id)]).unlink()
        all_tasks = self.env['project.task'].with_context(active_test=False).search([('project_id', '=', project.id)], order='parent_id')
        for task in all_tasks:
            self.env['mail.followers'].search([('res_model', '=', 'project.task'), ('res_id', '=', task.id)]).unlink()
        return project


class ProjectTask(models.Model):
    _inherit = 'project.task'

    def copy(self, default=None):
        no_dup_followers = self.env['ir.config_parameter'].sudo().get_param('no_dup_followers.no_duplicating_followers_project', False)
        if not no_dup_followers:
            return super(ProjectTask, self).copy(default)
        task = super(ProjectTask, self).copy(default)
        self.env['mail.followers'].search([('res_model', '=', 'project.task'), ('res_id', '=', task.id)]).unlink()
        return task
