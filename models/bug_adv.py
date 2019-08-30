# -*- coding: utf-8 -*-

from odoo import models, fields, api

class bugAdvanced(models.Model):
    _inherit = 'bm.bug'
    #在进阶模型中新增一个所需的时间字段
    need_time=fields.Integer('所需时间（小时）')
    #为bm.bug类的name字段增加help属性
    name=fields.Char(help='简要描述发现的bug')