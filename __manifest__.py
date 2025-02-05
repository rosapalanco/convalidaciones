# -*- coding: utf-8 -*-
{
    'name': "convalidaciones",

    'summary': """
        Ejemplo que nos permite gestionar las convalidaciones de un instituto.
        """,

    'description': """
        Aqui la descripcion mas larga del modulo
    """,

    'author': "Rosa",
    'website': "https://ieslamarisma.net/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # Las vistas que utilizara
    'data': [
        # 'security/ir.model.access.csv',
        'views/alumnos.xml',
        'views/modulos.xml',
        'views/convalidaciones.xml',
        'views/ciclos.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
