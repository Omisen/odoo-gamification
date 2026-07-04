{
    'name': 'Odoo & Dragons',
    'summary': 'Gamification system with D&D theme for Odoo teams',
    'description': """
Odoo & Dragons (OND)
====================
A full-immersion D&D-themed gamification layer for Odoo.

Turns tickets, tasks and deals into quests.
Turns your team into a party of adventurers.
Turns your pipeline into a dungeon to conquer.

Features
--------
- Character creation with class selection (Wizard, Rogue, Paladin, Bard, Ranger)
- XP system built on top of native Odoo gamification
- Quest board mapped to Helpdesk, CRM and Project records
- Dungeon seasons with a Boss record and party HP
- OWL dashboard with dark corporate minimal UI
- Activity feed, streak tracking, badge integration
    """,

    'author': 'Koratyn',
    'website': 'https://www.koratyn.it',
    'license': 'LGPL-3',

    'category': 'Gamification',
    'version': '18.0.1.0.0',

    'depends': [
        'base',
        'base_automation',
        'gamification',
        'project',
        'mail',
        'web',
    ],

    'data': [
        # Security
        

        # Data
        'data/automation_xp.xml',

        # Views
        'views/res_users_views.xml',
    ],

    'assets': {
        'web.assets_backend': [
            
        ],
    },

    'demo': [
        
    ],

    'images': ['static/description/banner.png'],

    'installable': True,
    'application': True,
    'auto_install': False,
}