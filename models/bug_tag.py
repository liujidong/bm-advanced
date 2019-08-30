# -*- coding: utf-8 -*-

from odoo import models, fields, api

class bugTag(models.Model):
    _name='bm.bug.tag'
    _description = 'bug标识'

    name=fields.Char('名称')