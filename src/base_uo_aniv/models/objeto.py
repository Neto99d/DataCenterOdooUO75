from odoo import api, fields, models


class Objeto(models.Model):
    _name = 'objeto.objeto'
    _description = 'Objeto'


    name = fields.Char(
        string='Objeto Social',
        required=True,
        default=lambda self: self._get_default_name(),
        copy=False
    )

    contenido = fields.Text(
        string='Contenido',
    )
    
    @api.model
    def _get_default_name(self):
     return "Post " + str(self.env['objeto.objeto'].search_count(
            []))
    
