# -*- coding: utf-8 -*-

#rooms.py

from odoo import models, fields, api

class rooms(models.Model):
    _name = 'hotel.guests'
    _description = 'guest master list'
    _order = 'lastname,firstname,middlename'

    lastname = fields.Char("Last Name")
    firstname = fields.Char("First Name")
    middlename = fields.Char("Middle Name")
    address_streetno  = fields.Char("Street & No.")       
    address_area  = fields.Char("Area, Unit, Bldg., Brgy.")
    address_city  = fields.Char("Address/City/Town")
    address_province  = fields.Char("Address/Province/State")
    zipcode = fields.Char("ZIP Code")
    contactno = fields.Char("Contact No.")
    email = fields.Char("Email")
    gender = fields.Selection([('FEMALE','Female'),('MALE','Male')],string="Gender")
    birthdate = fields.Date("Birth Date")
    photo = fields.Image("Photo")
    
    name = fields.Char(string='Guest Name', compute='_compute_name')
    @api.depends('lastname','firstname','middlename')
    def _compute_name(self):
        for rec in self:
            rec.name=f"{rec.lastname}, {rec.firstname} {rec.middlename}"