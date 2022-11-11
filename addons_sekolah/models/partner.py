from odoo import api, fields, models
 
class PartnerMapel(models.Model):
    _inherit = 'res.partner'
 
    instructor = fields.Boolean(string='Instruktur')
#    mapel_line = fields.One2many('sekolah.mapel', 'mapel_id', string='Mata Pelajaran', readonly=True)