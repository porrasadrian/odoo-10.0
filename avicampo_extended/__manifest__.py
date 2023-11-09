##############################################################################
#
#
#
#
##############################################################################

{
    'name': 'Avicampo Extended',
    'version': '10.0',
    'category': '',
    'summary': "",
    'author': "Adrian Porras",
    'website': '',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'mail',
        'account',
        'account_cancel',
        'l10n_mx_einvoice_payment',
        'mrp',
        'account_period_and_fiscalyear',

    ],
     'data': [
         'security/security.xml',
         'views/account_period_form.xml',
         'views/account_payment.xml',
         'views/account_journal.xml',





     ],

    'installable': True,
}
