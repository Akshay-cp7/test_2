import json
from odoo import http
from odoo.http import request

class TestController(http.Controller):

    @http.route('/apis/test', type='http', auth='public', methods=['GET'], csrf=False)
    def test_api(self, **kwargs):
        response_data = {
            "status": "success",
            "message": "API is working!",
            "data": kwargs
        }
        return request.make_response(json.dumps(response_data), headers=[('Content-Type', 'application/json')])

# class Snippet(http.Controller):
#     @http.route('/get_total_studentscntr/apk1234', auth='public', type='http', methods=['GET'])
#     def get_total_students(self):
#         try:
#             # Fetch students data
#             students = request.env['fk.student'].sudo().search_read([], ['name', 'phone', 'roll_no'])
#             # Wrap the students data in a dictionary
#             response_data = {
#                 'students': students
#             }
#             return request.make_response(json.dumps(response_data), headers={'Content-Type': 'application/json'})
#         except Exception as e:
#             return request.make_response(json.dumps({'error': str(e)}), headers={'Content-Type': 'application/json'}, status=500)

# class Snippet(http.Controller):
#     @http.route('/get_total_facultycntr/apk1234', auth='public', type='http', methods=['GET'])
#     def get_total_faculty(self):
#         try:
#             # Fetch faculty data
#             faculty = request.env['fk.faculty'].sudo().search_read([], ['name', 'code'])
#             # Wrap the faculty data in a dictionary
#             response_data = {
#                 'faculty': faculty
#             }
#             return request.make_response(json.dumps(response_data), headers={'Content-Type': 'application/json'})
#         except Exception as e:
#             return request.make_response(json.dumps({'error': str(e)}), headers={'Content-Type': 'application/json'}, status=500)
