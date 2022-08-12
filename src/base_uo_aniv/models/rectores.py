from odoo import api, fields, models
from odoo.modules import get_module_resource
import base64

class Rectores(models.Model):
    _name = 'rectores.rectores'
    _description = 'Rectores'

    name = fields.Char(
        string='Nombre',
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
        return "Post " + str(self.env['rectores.rectores'].search_count(
               []))
    def _get_default_image(self):
     image_path = get_module_resource('base_uo_aniv', 'static/src/img', 'user.png')
     return base64.b64encode(open(image_path, 'rb').read())