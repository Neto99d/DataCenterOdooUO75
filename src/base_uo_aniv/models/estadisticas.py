from odoo import api, fields, models


class Estadisticas(models.Model):
    _name = 'estadisticas.estadisticas'
    _description = 'Estadisticas'

    name = fields.Char(
        string='Estadística sobre',
        required=True,
        default=lambda self: self._get_default_name(),
        copy=False
    )
    
    cantidad = fields.Integer(
        string='Cantidad',
    )
    
    @api.model
    def _get_default_name(self):
     return "Post " + str(self.env['estadisticas.estadisticas'].search_count(
            []))

    
