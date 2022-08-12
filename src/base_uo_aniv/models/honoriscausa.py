from odoo import api, fields, models
from odoo.modules import get_module_resource
import base64

class HonorCausa(models.Model):
    _name = 'honorcausa.honorcausa'
    _description = 'Honoris Causa'

    name = fields.Char(
        string='Honoris Causa',
        required=True,
        default=lambda self: self._get_default_name(),
        copy=False
    )

    contenido = fields.Text(
        string='Contenido',
    )

    imagen = fields.Binary(string='Imagen', attachment=True, default=lambda self: self._get_default_image())
    store_fname = fields.Char(string="File Name")
    
    @api.model
    def _get_default_name(self):
     return "Post " + str(self.env['honorcausa.honorcausa'].search_count(
            []))
            
    def _get_default_image(self):
     image_path = get_module_resource('base_uo_aniv', 'static/src/img', 'placeholder.png')
     return base64.b64encode(open(image_path, 'rb').read()) 
    