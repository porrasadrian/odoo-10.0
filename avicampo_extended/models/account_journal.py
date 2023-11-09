# -*- coding: utf-8 -*-

from odoo import fields, models, api


class AccountJournal(models.Model):
    _inherit = "account.journal"

    ap_ar = fields.Boolean(string="Para AR y AP", help="Para usarlo en las facturas de cliente y facturas de compra")


class AccountPayment(models.Model):
    _inherit = "account.payment"

    @api.onchange('payment_type')
    def _onchange_payment_type(self):
        if not self.invoice_ids:
            # Set default partner type for the payment type
            if self.payment_type == 'inbound':
                self.partner_type = 'customer'
        # Set payment method domain
        domain = [('type', 'in', ('bank', 'cash'))]
        if self.invoice_ids and self.payment_type == 'inbound':
            domain.append(('ap_ar', '=', True))
            return {'domain': {'journal_id': domain}}




