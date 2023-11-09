# -*- coding: utf-8 -*-
from odoo import models, fields,api,_

class AccountPeriod(models.Model):
    _name = 'account.period'
    _inherit = ['mail.thread','account.period']
    _description = 'Modification in the account.period model to add chatter and blacklist users'

    name = fields.Char(track_visibility='onchange')
    fiscalyear_id = fields.Many2one(track_visibility='onchange')
    date_start = fields.Date(track_visibility='onchange')
    date_stop = fields.Date(track_visibility='onchange')
    code = fields.Char(track_visibility='onchange')
    special = fields.Boolean(track_visibility='onchange')
    state = fields.Selection([
            ('draft','Open'),
            ('done', 'Closed'),
        ], string='Status')























