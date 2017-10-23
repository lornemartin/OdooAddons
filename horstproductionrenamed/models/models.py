# -*- coding: windows-1252 -*-

from odoo import models, fields, api

 class Product(models.Model):
	_name = 'horstproduction.product'
	
	name = fields.Char(string="Title")
	description = fields.Text()
	
 