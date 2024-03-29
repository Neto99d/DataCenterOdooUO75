from odoo import api, fields, models
from odoo.modules import get_module_resource
import base64

class Multimedia(models.Model):
    _name = 'multimedia.multimedia'
    _description = 'Multimedia'

    name = fields.Char(
        string='Título',
        required=True,
        default=lambda self: self._get_default_name(),
        copy=False
    )

    contenido = fields.Text(
        string='Enlace directo al video',
    )

    imagen = fields.Binary(string='Imagen', attachment=True, default=lambda self: self._get_default_image())
    store_fname = fields.Char(string="File Name")
    
    @api.model
    def _get_default_name(self):
     return "Post " + str(self.env['multimedia.multimedia'].search_count(
            []))
            
    def _get_default_image(self):
     image_path = get_module_resource('base_uo_aniv', 'static/src/img', 'placeholder.png')
     return base64.b64encode(open(image_path, 'rb').read()) 
