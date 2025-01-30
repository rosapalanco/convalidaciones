# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Alumno(models.Model):
    _name = 'convalidaciones.alumno'

    name = fields.Char(string="Nombre y apellidos")
    edad = fields.Integer(string="Edad")
    localidad = fields.Char(strings="Localidad")
    provincia = fields.Char(strings="Provincia")
    email = fields.Char(strings="Email")
    convalidacion_ids = fields.One2many('convalidaciones.convalidacion', 'alumno_id',  string="Convalidaciones del Alumno")



class Modulo(models.Model):
    _name = 'convalidaciones.modulo'

    name = fields.Char(string="Nombre")
    descripcion = fields.Text(string="Descripción")
    ciclo_ids = fields.Many2many('convalidaciones.ciclo')

class Convalidacion(models.Model):
    _name = 'convalidaciones.convalidacion'

    name = fields.Char()
    fecha_convalidacion = fields.Date(string="Fecha de la Convalidacion")
    modulo_id = fields.Many2one('convalidaciones.modulo', string="Modulo")
    alumno_id = fields.Many2one('convalidaciones.alumno', string="Alumno")


class Ciclo(models.Model):
    _name = 'convalidaciones.ciclo'

    name = fields.Char(string="Nombre")
    descripcion = fields.Text(string="descripcion")
    modulo_ids = fields.Many2many("convalidaciones.modulo")
