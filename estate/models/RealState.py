# -*- coding: utf-8 -*-
# Tutorial: https://www.odoo.com/documentation/18.0/es/developer/tutorials/server_framework_101/03_basicmodel.html

from odoo import fields, models
from datetime import timedelta
import datetime

class RealState(models.Model):
    _name = "estate.property"
    _description = "Real state table"
    _order = "sequence"

    name              = fields.Char     ('Real estate'       ,required=True , translate=True)
    description       = fields.Text     ('Description'       ,required=True , translate=True)
    postcode          = fields.Char     ('Zip code'          ,required=False)
    date_availability = fields.Date     ('Date availability' ,required=False, default =datetime.datetime.now() + timedelta(days=90),copy=False)
    expected_price    = fields.Float    ('Expected price'    ,required=True)
    selling_price     = fields.Float    ('Selling price'     ,required=False, readonly=True,copy=False)
    bedrooms          = fields.Integer  ('Bedrooms'          ,required=False, default=2)
    living_area       = fields.Integer  ('Living area'       ,required=False)
    facades           = fields.Integer  ('Facades'           ,required=False)
    garage            = fields.Boolean  ('Garage'            ,required=False)
    garden            = fields.Boolean  ('Garden'            ,required=False)
    garden_area       = fields.Integer  ('Garden Area'       ,required=False)
    garden_orientation= fields.Selection(
        string='Garden orientation',
        selection=[('north', 'North'), ('south', 'South'),
                   ('east' , 'East') , ('west' , 'West' )],
        help="Garden orientation is used to know the orientation of de garden." )       
    state             = fields.Selection(
        string='State of property',
        selection=[('new', 'New'), ('offerr', 'Offer Received'),
                   ('offera' , 'Offer Accepted') , ('sold' , 'Sold' ), ('cancelled' , 'Cancelled' )],
        help="state of property is used to allow or deny acciones according selected value." )

    active = fields.Boolean('Active', default=True)
    sequence = fields.Integer('Sequence', default=10)
