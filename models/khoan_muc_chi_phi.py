from odoo import models, fields, api

class DanhMucChiPhi(models.Model):
    _name = 'khoan.muc.chi.phi'  # Tên model tiếng Việt không dấu
    _description = 'Khoản Mục Chi Phí'  # Tên hiển thị tiếng Việt trong giao diện

    ma = fields.Char(string="Mã", required=True)
    ten = fields.Char(string="Tên", required=True)
    thuoc = fields.Selection([
        ('cong_tac_phi', 'Công tác phí'),
        ('khac', 'Khác'),
    ], string="Thuộc", required=True, default='cong_tac_phi')
    dien_giai = fields.Text(string="Diễn giải")

    @api.model
    def action_save(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Danh mục chi phí',
            'view_mode': 'tree,form',
            'res_model': 'danh.muc.chi.phi',
        }

    @api.model
    def action_save_and_new(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Thêm mới',
            'view_mode': 'form',
            'res_model': 'danh.muc.chi.phi',
            'target': 'new',
        }

    @api.model
    def action_cancel(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Danh mục chi phí',
            'view_mode': 'tree,form',
            'res_model': 'danh.muc.chi.phi',
        }
