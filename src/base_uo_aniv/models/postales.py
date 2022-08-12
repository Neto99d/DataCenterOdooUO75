from odoo import api, fields, models


class Postales(models.Model):
    _name = 'postales.postales'
    _description = 'Postales'



    name = fields.Char(
        string='Postales',
        required=True,
        default=lambda self: self._get_default_name(),
        copy=False
    )
    
    imagen = fields.Binary(string='Imagen', attachment=True)
    store_fname = fields.Char(string="File Name")
    
    @api.model
    def _get_default_name(self):
     return "Post " + str(self.env['postales.postales'].search_count(
            []))
