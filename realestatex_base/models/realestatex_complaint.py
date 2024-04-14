# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class RealestatexComplaint(models.Model):
    _name = 'realestatex.complaint'
    _inherit = ['mail.thread']
    _description = 'RealEstateX Complaint'

    name = fields.Char(string='Tenant Name', required=True)
    email = fields.Char(string='Email', required=True)
    flat_address = fields.Char(string='Flat Address', required=True)
    complaint_type = fields.Selection([
        ('question', 'Question'),
        ('electrical_issue', 'Electrical Issue'),
        ('heating_issue', 'Heating Issue'),
        ('other_issue', 'Other Issue'),
    ], string='Complaint Type', required=True)
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company)
    description = fields.Text(string='Description', required=True)
    complaint_number = fields.Char(string='Complaint Number', readonly=True, default="New")
    stage = fields.Selection([
        ('new', 'New'),
        ('in_review', 'In Review'),
        ('in_progress', 'In Progress'),
        ('solved', 'Solved'),
        ('dropped', 'Dropped'),
    ], string='Stage', default='new')
    assigned_user_id = fields.Many2one('res.users', string='Assigned User')
    action_plan = fields.Html(string='Action Plan')

    @api.model_create_multi
    def create(self, vals_list):
        """ Assign a user to the complaint and create the complaint number """
        for vals in vals_list:
            vals['assigned_user_id'] = self.env['res.users'].search([], limit=1).id
            if 'complaint_number' not in vals or vals['complaint_number'] == _('New'):
                vals['complaint_number'] = self.env['ir.sequence'].next_by_code('realestatex.complaint') or _('New')
        return super().create(vals_list)

    def set_to_in_review_complaint(self):
        self.write({'stage': 'in_review'})

    def set_to_in_progress_complaint(self):
        self.write({'stage': 'in_progress'})

    def close_complaint(self):
        self.write({'stage': 'solved'})
        self.send_email_notification()

    def drop_complaint(self):
        self.write({'stage': 'dropped'})
        self.send_email_notification()

    def send_email_notification(self):
        template = self.env.ref('realestatex_base.email_template_complaint_closed')
        template.send_mail(self.id, force_send=True)

    def print_work_order(self):
        return self.env.ref('realestatex_base.action_work_order_report').report_action(self)
