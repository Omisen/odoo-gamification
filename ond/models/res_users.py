from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    character_name = fields.Char(
        string='Character name',
    )
    character_class = fields.Selection(
        selection=[
            ('wizard',  'Wizard'),
            ('rogue',   'Rogue'),
            ('paladin', 'Paladin'),
            ('bard',    'Bard'),
            ('ranger',  'Ranger'),
        ],
        string='Class',
    )