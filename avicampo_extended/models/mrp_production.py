# -*- coding: utf-8 -*-
from odoo import models, fields,api
from odoo.exceptions import UserError, ValidationError

class MrpProduction(models.Model):
    _inherit = 'mrp.production'
    _description = 'Inheritance of the mrp production model'



    @api.constrains('product_qty')
    def _product_qty(self):
        for r in self:
            if r.product_qty > 30000 and self.env.user.has_group('avicampo_extended.fabricacion_group_inherit'):
                raise UserError('No puedes Fabricar mas de 30 mil Kilos')

