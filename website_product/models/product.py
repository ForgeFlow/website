# Copyright 2018 Eficent Business and IT Consulting Services S.L.
#   (http://www.eficent.com)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo import api, fields, models
from odoo.addons.http_routing.models.ir_http import slug
from odoo.tools.translate import html_translate


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    website_description = fields.Html('Description for the website',
                                      sanitize_attributes=False,
                                      translate=html_translate)

    @api.multi
    def _compute_website_url(self):
        # If the product cannot be sold, then use the new form view.
        # Otherwise, use the defult URL from website_sale, which will
        # redirect the user to the shop.
        for product in self.filtered(
                lambda p: not p.sale_ok and p.website_published):
            if product.sale_ok:
                continue
            product.website_url = "/product/%s" % slug(product)
