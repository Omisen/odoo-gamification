from odoo import models, fields, api


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
    character_level = fields.Integer(
        string='Level',
        default=1,
        readonly=True,
    )
    character_xp = fields.Integer(
        string='XP',
        default=0,
        readonly=True,
    )
    character_xp_next_level = fields.Integer(
        string='XP to next level',
        compute='_compute_xp_next_level',
    )
 
    # logica di _compute_xp_next_level per ora è semplicissima - livello × 100. Quindi livello 1 -> 100 XP, livello 5 -> 500 XP
    # update futuro con logica a curva esponenziale
    @api.depends('character_level')
    def _compute_xp_next_level(self):
        for user in self:
            user.character_xp_next_level = user.character_level * 100