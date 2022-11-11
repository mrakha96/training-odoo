from odoo import api, fields, models
 
 
#class SekolahWizard(models.TransientModel):
#    _name = 'sekolah.wizard'
#    _description = 'Sekolah Wizard'
#  
#    def _default_mapel(self):
#        return self.env['sekolah.mapel'].browse(self._context.get('active_ids'))
      
#    mapel_id = fields.Many2one('sekolah.mapel', string="Mata Pelajaran", default=_default_mapel)
#    guru_ids = fields.Many2many('sekolah.guru', string='Guru')
#    mapel_ids = fields.Many2many('sekolah.mapel', string="Sesi", default=_default_mapel)

#    def tambah_mapel(self):
#        for sesi in self.mapel_ids:
#            sesi.guru_ids |= self.guru_ids
     
#    def tambah_guru(self):
#        self.mapel_id.guru_ids |= self.guru_ids