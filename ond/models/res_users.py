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
        compute='_compute_xp_progression',
    )
    
    character_xp_progress = fields.Float(
        string='Progress',
        compute='_compute_xp_progression',
        help='Percentage of XP progress toward next level (0-100)',
    )
 
    # update con logica a curva esponenziale        
    @api.depends('character_level', 'character_xp')
    def _compute_xp_progression(self):
        for user in self:
            
            # exp per raggiungere il livello successivo
            xp_needed   = (user.character_level ** 2) * 100
            # exp a inizio livello
            xp_prev     = ((user.character_level - 1) ** 2) * 100
            # exp guadagnati all interno del livello attuale
            xp_in_level = user.character_xp - xp_prev
            # intervallo totale exp livello attuale
            xp_range    = xp_needed - xp_prev
            
            user.character_xp_next_level = xp_needed
            if xp_range > 0:
                user.character_xp_progress = min(round(xp_in_level / xp_range * 100, 1), 100.0)
            else:
                user.character_xp_progress = 0.0