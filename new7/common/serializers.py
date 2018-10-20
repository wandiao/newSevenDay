#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from new7 import models
from django.db.transaction import atomic


from . import mixins

class ProfileSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = models.Profile
    fields = (
      'id',
      'user',
      'phone',
      'name',
      'code',
      'gender',
      'address',
      'salary',
      'depot',
      'role',
      'birth',
      'desc',
      'phone_verified',
    )

ProfileDetailSerializer = ProfileSerializer

class ProfileCreateSerializer(
    mixins.OnePhonePerOneProfileMixin,
    serializers.ModelSerializer
):
    class Meta:
        model = models.Profile
        read_only_fields = (
            'id',
            'user',
            'phone_verified',
        )
        fields = read_only_fields + (
            'phone',
            'name',
            'code',
            'role',
            'depot',
            'gender',
            'address',
            'salary',
            'birth',
            'desc',
        )

    def validate(self, data):
        phone = data.get('phone')
        if 'role' in data:
          role = data['role']
          if role == 'warekeeper':
            if 'depot' not in data.keys():
                raise serializers.ValidationError('没有指定库房')
        
        if models.Profile.objects.filter(
            phone=phone,
            deleted=False,
        ):
            raise serializers.ValidationError(u'该手机号已经存在，不能创建')
        return data


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        read_only_fields = (
            'id',
            'user',
            'phone_verified',
        )
        fields = read_only_fields + (
            'phone',
            'name',
            'role',
            'code',
            'depot',
            'gender',
            'address',
            'salary',
            'birth',
            'desc',
        )

    def validate_phone(self, value):
        if models.Profile.objects.filter(phone=value, deleted=False).exclude(id=self.instance.id):
            raise serializers.ValidationError(u'该手机号已经存在')
        return value

class GoodsSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Goods
    fields = (
      'id',
      'name',
      'short_name',
      'code',
      'img',
      'brand',
      'in_price',
      'sale_price',
      'stock',
      'unit',
      'spec',
      'desc',
      'is_book',
    )

class GoodsRecordSerializer(serializers.ModelSerializer):
  goods_name = serializers.CharField(
    source='goods.name',
    read_only=True
  )
  record_depot_name = serializers.CharField(
    source='record_depot.name',
    read_only=True
  )
  class Meta:
    model = models.GoodsRecord
    fields = (
      'goods',
      'goods_name',
      'count',
      'unit',
      'price',
      'record_type',
      'record_depot',
      'record_depot_name',
      'record_time',
      'record_source',
      'operator_account',
      'remarks',
    )

class OrderGoodsListSerializer(serializers.Serializer):
  goods_id = serializers.CharField(
    max_length=20,
    help_text=u'商品id',
  )
  count = serializers.IntegerField(
    required=True,
    help_text=u'数量',
  )

class OrderGoodsSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.OrderGoods
    fields = (
      'order',
      'goods',
      'count',
    )

class OrderGoodsDetailSerializer(serializers.ModelSerializer):
  goods = GoodsSerializer(
    many=False,
    help_text=u'订单商品',
    read_only=True
  )
  class Meta:
    model = models.OrderGoods
    fields = (
      'order',
      'goods',
      'count',
    )


class OrderSerializer(serializers.ModelSerializer):
  supplier_name = serializers.CharField(
    source='supplier.name',
    read_only=True
  )
  order_goods = OrderGoodsDetailSerializer(
    many=True,
    help_text=u'订单商品',
    read_only=True
  )
  class Meta:
    model = models.Order
    fields = (
      'id',
      'invoice',
      'order_unique',
      'supplier',
      'supplier_name',
      'tontact_phone',
      'operator',
      'delivery_date',
      'deliver_type',
      'deliver_money',
      'deliver_address',
      'status',
      'pay_type',
      'pay_from',
      'is_pay',
      'is_closed',
      'flag',
      'trade_no',
      'is_refond',
      'depot',
      'code',
      'brand',
      'specification',
      'unit',
      'price',
      'total_price',
      'production_date',
      'expired_date',
      'remark',
      'order_goods',
    )

class OrderCreateSerializer(serializers.ModelSerializer):
  goods_info = OrderGoodsListSerializer(
        many=True,
        help_text=u'商品信息列表',
        required=False,
    )
  class Meta:
    model = models.Order
    fields = (
      'id',
      'invoice',
      'order_unique',
      'supplier',
      'tontact_phone',
      'operator',
      'delivery_date',
      'deliver_type',
      'deliver_money',
      'deliver_address',
      'status',
      'pay_type',
      'pay_from',
      'is_pay',
      'is_closed',
      'flag',
      'trade_no',
      'is_refond',
      'depot',
      'code',
      'brand',
      'specification',
      'unit',
      'price',
      'total_price',
      'production_date',
      'expired_date',
      'remark',
      'goods_info',
    )
  @atomic
  def create(self, validate_data):
      goods_info = validate_data.pop('goods_info')
      instance = models.Order.objects.create(**validate_data)
      return instance

class SupplierSerializer(serializers.ModelSerializer):
  class Meta:
    model = models.Supplier
    fields = (
      'id',
      'name',
      'type',
      'contact_name',
      'tontact_phone',
      'address',
      'operator',
      'operator_name',
      'license_code',
      'desc',
    )

class ClientSeralizer(serializers.ModelSerializer):
  class Meta:
    model = models.Client
    fields = (
      'id',
      'name',
      'contact_name',
      'tontact_phone',
      'address',
      'desc',      
    )

class DepotSerializer(serializers.ModelSerializer):
  depot_keepers = ProfileSerializer(
    many=True,
    read_only=True,
    help_text=u'库管员'
  )
  class Meta:
    model = models.Depot
    fields = (
      'id',
      'name',
      'type',
      'stock',
      'cubage',
      'desc',
      'depot_keepers',
    )