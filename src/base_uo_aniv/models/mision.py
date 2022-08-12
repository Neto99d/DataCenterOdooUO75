from odoo import api, fields, models


class Mision(models.Model):
    _name = 'mision.mision'
    _description = 'Mision'


    name = fields.Char(
        string='Misión',
        required=True,
        default=lambda self: self._get_default_name(),
        copy=False
    )
    
    contenido = fields.Text(
        string='Contenido',
    )
    
    @api.model
    def _get_default_name(self):
     return "Post " + str(self.env['mision.mision'].search_count(
            []))
    


    
