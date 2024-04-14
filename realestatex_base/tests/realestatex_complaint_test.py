from odoo.tests.common import TransactionCase
from odoo.exceptions import AccessError

class TestRealestatexComplaint(TransactionCase):

    def setUp(self):
        super().setUp()
        self.user = self.env.ref('base.user_admin')
        self.complaint_vals = {
            'name': 'Otman El agy',
            'email': 'otmanelagy1@gmail.com',
            'flat_address': '123 Main St',
            'complaint_type': 'question',
            'description': 'is This is a test complaint ?',
        }

    def test_create_complaint(self):
        complaint = self.env['realestatex.complaint'].create(self.complaint_vals)
        self.assertEqual(complaint.assigned_user_id, self.user, "User not assigned correctly")
        self.assertNotEqual(complaint.complaint_number, 'New', "Complaint number not generated")

    def test_change_stage(self):
        complaint = self.env['realestatex.complaint'].create(self.complaint_vals)
        with self.assertRaises(AccessError):
            complaint.set_to_in_review_complaint()

        self.env['realestatex.complaint'].write({'stage': 'in_review'})

        self.assertEqual(complaint.stage, 'in_review', "Stage not changed correctly")
