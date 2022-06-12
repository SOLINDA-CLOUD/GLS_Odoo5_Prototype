from odoo import _, api, fields, models


# class PurchaseRequest(models.Model):
#     _inherit = 'purchase.request'
    


class PurchaseRequestLine(models.Model):
    _inherit = 'purchase.request.line'
    
    
    item_id = fields.Many2one('item.item', string='Item')
    qty_item = fields.Integer('Qty RAP',related='item_id.product_qty')
    reason_qty_different = fields.Text('Reason')