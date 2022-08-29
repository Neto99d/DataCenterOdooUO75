
# -*- coding: utf-8 -*-
###############################################################################
#
#
#
#    Copyright (c) All rights reserved:
#        (c) 2022  TM_FULLNAME
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses
#
#    Odoo and OpenERP is trademark of Odoo S.A.
#
###############################################################################
{
    'name': 'INFOCOM',
    'summary': 'Datos para App android de la Universidad de Oriente, Aniversario 75.',
    'version': '2.0',

    'description': """
Datos para App android UO Aniversario 75.
==============================================


    """,

    'author': 'Ernesto Duvalón Hernández',
    'maintainer': 'Universidad de Oriente',

    'license': 'AGPL-3',

    'depends': [
        'base',
        'restful'
    ],
    'data': [
        'security/access.xml',
        'views/menu.xml',
        'views/campaña.xml',
        'views/efemerides.xml',
        'views/estadisticas.xml',
        'views/honoriscausa.xml',
        'views/identidad.xml',
        'views/mision.xml',
        'views/multimedia.xml',
        'views/objeto.xml',
        'views/patrimonio.xml',
        'views/postales.xml',
        'views/profeEmerito.xml',
        'views/pteFeu.xml',
        'views/rectores.xml',
        'views/reseña.xml',
        'views/vision.xml',
        'views/redesSociales.xml',
        'views/aviso.xml',
        'views/info.xml'
    ],

    'installable': True,
    'application': True
}
