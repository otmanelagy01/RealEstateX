# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class ComplaintController(http.Controller):

    @http.route('/complaint/submit', type='http', auth='public', website=True, csrf=False)
    def submit_complaint(self, **post):
        complaint = request.env['realestatex.complaint'].sudo().create(post)
        email_template = request.env.ref('realestatex_base.email_template_complaint')
        email_template.send_mail(complaint.id, force_send=True)
        return request.render('realestatex_base.complaint_thanks',
                              {'complaint_number': complaint.complaint_number})
