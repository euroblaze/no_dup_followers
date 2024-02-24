from odoo import models, api, fields


class ProjectProject(models.Model):
    _inherit = 'project.project'

    def copy(self, default=None):
        no_dup_followers = self.env['ir.config_parameter'].sudo().get_param('no_dup_followers.no_duplicating_followers_project', False)
        if not no_dup_followers:
            return super(ProjectProject, self).copy(default)
        res = super(ProjectProject, self).copy(default)
        for rec in res:
            self.env['mail.followers'].search([('res_model', '=', 'project.project'), ('res_id', '=', rec.id)]).unlink()
        return res


class ProjectTask(models.Model):
    _inherit = 'project.task'

    def copy(self, default=None):
        no_dup_followers = self.env['ir.config_parameter'].sudo().get_param('no_dup_followers.no_duplicating_followers_project', False)
        if not no_dup_followers:
            return super(ProjectTask, self).copy(default)
        res = super(ProjectTask, self).copy(default)
        for rec in res:
            self.env['mail.followers'].search([('res_model', '=', 'project.task'), ('res_id', '=', rec.id)]).unlink()
        return res
