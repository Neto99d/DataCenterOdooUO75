from odoo import api, fields, models


class Info(models.Model):
  _name = 'info.info'
  _description = 'Info Model'

  name = fields.Char(string='Name')
