# -*- coding: utf-8 -*-

from odoo import api, fields, models


class TrainingCourse(models.Model):
     _name = 'training.course'
     _description = 'Training Kursus'

     name = fields.Char(string='Judul', required=True)
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
     description = fields.Text(string='Keterangan')
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
