# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from datetime import timedelta, datetime, date
from odoo.exceptions import UserError, ValidationError


class SekolahSiswa(models.Model):
     _name = 'sekolah.siswa'
     _inherit = ['mail.thread', 'mail.activity.mixin']
     _description = 'siswa sekolah'

     def get_year(self):
          return fields.Date.today() + relativedelta(years=-15)

     @api.model
     def create(self, vals):
        vals['nis'] = self.env['ir.sequence'].next_by_code('sekolah.siswa')
        return super(SekolahSiswa, self).create(vals)

     nis = fields.Char(string='NIS', readonly=True, default=101, tracking=True)
     name = fields.Char(string='Nama Siswa', required=True, tracking=True)
     jns_kelamin = fields.Selection([('male', 'Laki-laki'), ('female', 'Perempuan')], string='Jenis Kelamin', required=True, help='Jenis Kelamin', tracking=True)
     tgl_lahir = fields.Date(string="Tanggal Lahir", default=get_year, tracking=True)
     tgl_now = fields.Date(string="Tanggal Now", default=fields.Date.context_today, tracking=True)
     agama = fields.Char(string='Agama', tracking=True)
     nm_ayah = fields.Char(string='Nama Ayah', tracking=True)
     nm_ibu = fields.Char(string='Nama Ibu', tracking=True)
     usia = fields.Integer(string="Usia", help='Usia', tracking=True)
     alamat = fields.Text(string='Alamat', tracking=True)
     kelas_id = fields.Many2one('sekolah.kelas', string='Kelas', required=True, ondelete='cascade', tracking=True)

     @api.onchange('tgl_lahir', 'tgl_now','usia')
     def calculate_date(self):
        if self.tgl_lahir and self.tgl_now:
            d1=datetime.strptime(str(self.tgl_lahir),'%Y-%m-%d') 
            d2=datetime.strptime(str(self.tgl_now),'%Y-%m-%d')
            d3=relativedelta(d2, d1)
            self.usia = str(d3.years)

class SekolahGuru(models.Model):
     _name = 'sekolah.guru'
     _inherit = ['mail.thread', 'mail.activity.mixin']
     _description = 'guru sekolah'

     def _default_mapel(self):
        return self.env['sekolah.mapel'].browse(self._context.get('active_ids'))

     nip = fields.Char(string='NIP', readonly=True, default=150, tracking=True)
     name = fields.Char(string='Nama Guru', required=True, tracking=True)
     jns_kelamin = fields.Selection([('male', 'Laki-laki'), ('female', 'Perempuan')], string='Jenis Kelamin', required=True, help='Jenis Kelamin', tracking=True)
     mapel_line = fields.One2many('sekolah.mapel', 'guru_id', string='Mata Pelajaran', tracking=True)
#     mata_pelajaran = fields.Many2many('sekolah.mapel', 'name', 'jurusan', tracking=True)
#     mapel_id = fields.Many2one('sekolah.mapel', string='Mata Pelajaran')
#     mata_pelajaran = fields.Many2one('sekolah.mapel', string='Mata Pelajaran', required=True, tracking=True)
#     jurusan = fields.Char(string="Jurusan", related='mapel.jurusan', tracking=True)
#     guru_ids = fields.Many2many('sekolah.guru', string='Guru', tracking=True)
#     mapel_ids = fields.Many2many('sekolah.mapel', string="Mata Pelajaran", default=_default_mapel, tracking=True)
     usia = fields.Integer(string="Usia", help='Usia', default=25, tracking=True)
     no_telp = fields.Char(string='Telepon', tracking=True)
     alamat = fields.Text(string='Alamat', tracking=True)

     def tambah_mapel(self):
        for sekolah in self.mapel_ids:
            sekolah.name |= self.name

     @api.model
     def create(self, vals):
        vals['nip'] = self.env['ir.sequence'].next_by_code('sekolah.guru')
        return super(SekolahGuru, self).create(vals)

class SekolahMapel(models.Model):
     _name = 'sekolah.mapel'
     _inherit = ['mail.thread', 'mail.activity.mixin']
     _description = 'mata pelajaran sekolah'

     name = fields.Char(string='Mata Pelajaran', required=True, tracking=True)
     jurusan = fields.Char(string='Jurusan', required=True, tracking=True)
     guru_id = fields.Many2one('sekolah.guru', string='Guru Mata Pelajaran', required=True, ondelete='cascade')
     pelajaran = fields.Many2many('sekolah.guru', 'mata_pelajaran', 'jurusan', tracking=True)
#     guru = fields.Many2many('sekolah.guru', 'name', tracking=True)
#     mapel_id = fields.Many2one('sekolah.guru', string='Mata Pelajaran', required=True, ondelete='cascade', tracking=True)
#     mapel = fields.Many2one('sekolah.mapel', string='Mata Pelajaran', required=True, tracking=True)
#     autojurusan = fields.Char(string="Jurusan", related='mapel.jurusan', tracking=True)

     _sql_constraints = [
          ('mapel_unique', 'unique(name, jurusan)', 'Mata Pelajaran sudah ada!')
     ]

class SekolahKelas(models.Model):
     _name = 'sekolah.kelas'
     _inherit = ['mail.thread', 'mail.activity.mixin']
     _description = 'Kelas sekolah'

     name = fields.Char(string='Nama Kelas', required=True, tracking=True)
#     nm_siswa = fields.Many2one('sekolah.siswa', string='Nama Siswa', required=True, tracking=True)
#     siswa = fields.Many2many('sekolah.siswa', 'nis', 'name', string='Siswa', tracking=True)
     wali_kelas = fields.Many2one('sekolah.guru', string='Wali Kelas', required=True, tracking=True)
     siswa_line = fields.One2many('sekolah.siswa', 'kelas_id', string='Siswa', tracking=True)

     _sql_constraints = [
          ('kelas_unique', 'unique(name)', 'Kelas sudah ada!')
     ]
     
class SekolahJadwal(models.Model):
     _name = 'sekolah.jadwal'
     _inherit = ['mail.thread', 'mail.activity.mixin']
     _description = 'Jadwal sekolah'

     name = fields.Many2one('sekolah.kelas', string='Kelas', required=True, tracking=True)
     hari = fields.Selection([('monday', 'Senin'),
      ('tuesday', 'Selasa'),
      ('wednesday', 'Rabu'),
      ('thurday', 'Kamis'),
      ('friday', 'Jumat')],
       string='Hari', required=True, help='Hari Kelas', tracking=True)
     start = fields.Float(string='Jam Mulai', tracking=True)
     end = fields.Float(string='Jam Selesai', tracking=True)
     mapel = fields.Many2one('sekolah.mapel', string='Mata Pelajaran', required=True, tracking=True)
     autojurusan = fields.Char(string="Jurusan", related='mapel.jurusan', readonly=True, tracking=True)
     autoguru = fields.Many2one(string="Guru", related='mapel.guru_id', readonly=True, tracking=True)
#     autoguru = fields.Char(string="Guru", related='mapel.guru_id', tracking=True)

     _sql_constraints = [
          ('cne_unique', 'unique(name, hari, mapel)', 'Jadwal sudah ada!')
     ]

     @api.constrains('start', 'end')
     def check_jam(self):
        for r in self:
            if r.start >= r.end: 
                raise ValidationError("Input Jam Salah")

#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
