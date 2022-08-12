from odoo import api, fields, models


class RedesSociales(models.Model):
    _name = 'redesociales.redesociales'
    _description = 'Redes Sociales'

    name = fields.Char(
        string='Redes',
        required=True,
        default=lambda self: self._get_default_name(),
        copy=False
    )

    link_Facebook = fields.Char(
        string='Link Facebook',
    )

    link_Telegram = fields.Char(
        string='Link Telegram',
    )

    link_Twitter = fields.Char(
        string='Link Twitter',
    )

    link_Youtube = fields.Char(
        string='Link Youtube',
    )

    link_Linkedin = fields.Char(
        string='Link Linkedin',
    )

    link_Instagram = fields.Char(
        string='Link Instagram',
    )

    @api.model
    def _get_default_name(self):
     return "Post " + str(self.env['redesociales.redesociales'].search_count(
            []))