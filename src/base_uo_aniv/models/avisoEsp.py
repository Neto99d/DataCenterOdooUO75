from odoo import api, fields, models


class Aviso(models.Model):
    _name = 'aviso.aviso'
    _description = 'Aviso Especial'

  

    name = fields.Char(
        string='Aviso Especial',
        required=True,
        default=lambda self: self._get_default_name(),
        copy=False
    )

    contenido = fields.Text(
        string='Contenido',
    )

    
    fecha = fields.Date(
        string='Fecha',
        default=fields.Date.context_today,
    )
    
    @api.model
    def _get_default_name(self):
     return "Post " + str(self.env['aviso.aviso'].search_count(
            []))