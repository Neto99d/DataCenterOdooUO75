from odoo import api, fields, models


class Vision(models.Model):
    _name = 'vision.vision'
    _description = 'Vision'

    name = fields.Char(
        string='Visión',
        required=True,
        default=lambda self: self._get_default_name(),
        copy=False
    )

    contenido = fields.Text(
        string='Contenido',
    )

    @api.model
    def _get_default_name(self):
        return "Post " + str(self.env['vision.vision'].search_count(
               []))
