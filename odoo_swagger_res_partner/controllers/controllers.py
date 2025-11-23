from odoo import http
from odoo.http import request

class SwaggerResPartnerController(http.Controller):

    @http.route('/odoo_swagger_res_partner', type='http', auth='public', website=True)
    def web_index(self, **kw):
        return request.redirect('/web/static/src/index.html')
