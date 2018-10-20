# coding:utf-8

from django.db import models

from .base import BaseModel

class Goods(BaseModel):
    '''
    商品
    '''
    name = models.CharField(
        u'商品名称',
        max_length=100,
        null=True,
        unique=True,
        help_text=u'商品名称',
    )

    short_name = models.CharField(
        u'商品简称',
        max_length=100,
        null=True,
        blank=True,
        help_text=u'商品简称',
    )

    code = models.CharField(
        u'商品编码',
        null=True,
        unique=True,
        max_length=100,
        help_text=u'商品编码',
    )


    img = models.CharField(
        u'商品图片',
        max_length=500,
        null=True,
        blank=True,
        help_text=u'商品图片',
    )
    brand = models.CharField(
        u'品牌',
        max_length=100,
        null=True,
        blank=True,
        help_text=u'品牌',
    )
    in_price = models.CharField(
        u'商品进价',
        max_length=100,
        null=True,
        blank=True,
        help_text=u'商品进价',
    )
    sale_price = models.CharField(
        u'商品售价',
        max_length=100,
        null=True,
        blank=True,
        help_text=u'商品售价',
    )

    stock = models.IntegerField(
      u'库存',
      default=0,
      help_text=u'库存'
    )

    unit = models.CharField(
        u'单位',
        max_length=100,
        null=True,
        blank=True,
        help_text=u'单位',
    )

    spec = models.CharField(
        u'规格',
        max_length=100,
        null=True,
        blank=True,
        help_text=u'规格',
    )

    desc = models.CharField(
        u'描述',
        max_length=100,
        null=True,
        blank=True,
        help_text=u'描述',
    )

    is_book = models.BooleanField(
        u'是否预定',
        default=False,
        blank=True,
        help_text=u'是否预定',
    )


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = u'商品'
        verbose_name_plural = verbose_name


class GoodsRecord(BaseModel):
    '''
    商品操作
    '''

    OPERATE_TYPE = (
        ('depot_in', u'入库'),
        ('depot_out', u'出库'),
    )
    goods =  models.ForeignKey(
        'new7.Goods',
        verbose_name=u'商品',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        help_text=u'商品',
    )

    record_type = models.CharField(
        u'记录类型',
        default='main',
        max_length=20,
        choices=OPERATE_TYPE,
        help_text=u'操作类型',
    )

    count = models.IntegerField(
      u'数量',
      default=0,
      help_text=u'数量'
    )

    price = models.FloatField(
        u'价格',
        blank=True,
        null=True,
        help_text=u'价格',
    )

    unit = models.CharField(
        u'单位',
        max_length=200,
        null=True,
        blank=True,
        help_text=u'单位',
    )

    operator_account = models.CharField(
        u'操作员账号',
        max_length=20,
        null=True,
        help_text=u'操作员账号',
    )

    record_time = models.DateTimeField(
        u'记录时间',
        blank=True,
        null=True,
        help_text=u'记录时间',
    )

    record_source = models.CharField(
        u'操作来源',
        max_length=50,
        blank=True,
        default='',
        help_text=u'操作来源',
    )

    record_depot = models.ForeignKey(
        'new7.Depot',
        verbose_name=u'操作仓库',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        help_text=u'操作仓库',
    )

    remarks = models.TextField(
        u'备注',
        blank=True,
        default='',
        help_text=u'备注',
    )

    
