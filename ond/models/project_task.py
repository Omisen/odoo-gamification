from odoo import models, fields


class ProjectTask(models.Model):
    _inherit = 'project.task'

    # flag che impedisce di assegnare xp più volte sulla stessa task
    xp_awarded = fields.Boolean(
        string='XP awarded',
        default=False,
        readonly=True,
    )