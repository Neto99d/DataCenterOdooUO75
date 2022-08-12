from odoo import api, fields, models


class Reseña(models.Model):
    _name = 'resena.resena'
    _description = 'Reseña'

    name = fields.Char(
        string='Reseña',
        required=1,
        default=lambda self: self._get_default_name(),
        copy=False
    )

    contenido = fields.Text(
        string='Contenido',
    )

    @api.model
    def _get_default_name(self):
     return "Post " + str(self.env['resena.resena'].search_count(
            []))