# Generated by Django 2.1 on 2018-11-03 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', null=True, verbose_name='更新时间')),
                ('name', models.CharField(help_text='客户名称', max_length=20, null=True, unique=True, verbose_name='客户名称')),
                ('tontact_phone', models.CharField(blank=True, help_text='联系电话', max_length=20, null=True, verbose_name='联系电话')),
                ('contact_name', models.CharField(blank=True, help_text='联系人', max_length=20, null=True, verbose_name='联系人')),
                ('address', models.CharField(blank=True, help_text='地址', max_length=20, null=True, verbose_name='地址')),
                ('desc', models.CharField(blank=True, help_text='描述', max_length=100, null=True, verbose_name='描述')),
            ],
            options={
                'verbose_name': '客户',
                'verbose_name_plural': '客户',
            },
        ),
        migrations.CreateModel(
            name='Depot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', null=True, verbose_name='更新时间')),
                ('name', models.CharField(help_text='仓库名称', max_length=60, null=True, unique=True, verbose_name='仓库名称')),
                ('type', models.CharField(choices=[('main', '总库'), ('branch', '分库')], default='main', help_text='仓库类型', max_length=20, verbose_name='仓库类型')),
                ('stock', models.IntegerField(default=0, help_text='库存', verbose_name='库存')),
                ('cubage', models.IntegerField(default=0, help_text='容量', verbose_name='容量')),
                ('desc', models.CharField(blank=True, help_text='描述', max_length=100, null=True, verbose_name='描述')),
            ],
            options={
                'verbose_name': '仓库',
                'verbose_name_plural': '仓库',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', null=True, verbose_name='更新时间')),
                ('name', models.CharField(help_text='商品名称', max_length=100, null=True, unique=True, verbose_name='商品名称')),
                ('short_name', models.CharField(help_text='商品简称', max_length=100, null=True, verbose_name='商品简称')),
                ('code', models.CharField(help_text='商品编码', max_length=100, null=True, unique=True, verbose_name='商品编码')),
                ('img', models.CharField(blank=True, help_text='商品图片', max_length=500, null=True, verbose_name='商品图片')),
                ('brand', models.CharField(blank=True, help_text='品牌', max_length=100, null=True, verbose_name='品牌')),
                ('in_price', models.DecimalField(decimal_places=2, default=0, help_text='商品进价', max_digits=10, verbose_name='商品进价')),
                ('sale_price', models.DecimalField(decimal_places=2, default=0, help_text='商品售价', max_digits=10, verbose_name='商品售价')),
                ('stock', models.IntegerField(default=0, help_text='库存', verbose_name='库存')),
                ('last_operate_type', models.CharField(choices=[('depot_in', '入库'), ('depot_out', '出库')], help_text='最近操作类型', max_length=20, null=True, verbose_name='最近操作类型')),
                ('last_operate_time', models.DateTimeField(blank=True, help_text='上次操作时间', null=True, verbose_name='上次操作时间')),
                ('last_price', models.DecimalField(decimal_places=2, default=0, help_text='上次价格', max_digits=10, verbose_name='上次价格')),
                ('unit', models.CharField(blank=True, help_text='单位', max_length=100, null=True, verbose_name='单位')),
                ('spec', models.CharField(blank=True, help_text='规格', max_length=100, null=True, verbose_name='规格')),
                ('desc', models.CharField(blank=True, help_text='描述', max_length=100, null=True, verbose_name='描述')),
                ('is_book', models.BooleanField(blank=True, default=False, help_text='是否预定', verbose_name='是否预定')),
                ('stock_status', models.IntegerField(default=1, help_text='库存状态', verbose_name='库存状态')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
            },
        ),
        migrations.CreateModel(
            name='GoodsRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', null=True, verbose_name='更新时间')),
                ('record_type', models.CharField(choices=[('depot_in', '入库'), ('depot_out', '出库')], default='depot_in', help_text='操作类型', max_length=20, verbose_name='记录类型')),
                ('count', models.IntegerField(default=0, help_text='数量', verbose_name='数量')),
                ('leave_count', models.IntegerField(default=0, help_text='出库数量', verbose_name='出库数量')),
                ('price', models.FloatField(blank=True, help_text='价格', null=True, verbose_name='价格')),
                ('unit', models.CharField(blank=True, help_text='单位', max_length=200, null=True, verbose_name='单位')),
                ('operator_account', models.CharField(help_text='操作员账号', max_length=20, null=True, verbose_name='操作员账号')),
                ('record_time', models.DateTimeField(blank=True, help_text='记录时间', null=True, verbose_name='记录时间')),
                ('record_source', models.CharField(blank=True, default='', help_text='操作来源', max_length=50, verbose_name='操作来源')),
                ('remarks', models.TextField(blank=True, default='', help_text='备注', verbose_name='备注')),
                ('amount', models.DecimalField(decimal_places=2, default=0, help_text='成本', max_digits=10, verbose_name='成本')),
                ('goods', models.ForeignKey(blank=True, help_text='商品', null=True, on_delete=django.db.models.deletion.PROTECT, to='new7.Goods', verbose_name='商品')),
            ],
            options={
                'verbose_name': '商品记录',
                'verbose_name_plural': '商品记录',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', null=True, verbose_name='更新时间')),
                ('invoice', models.CharField(help_text='票号', max_length=100, null=True, unique=True, verbose_name='票号')),
                ('order_unique', models.CharField(help_text='流水号', max_length=200, null=True, unique=True, verbose_name='流水号')),
                ('order_type', models.CharField(choices=[('depot_in', '入库'), ('depot_out', '出库')], help_text='订单类型', max_length=20, verbose_name='订单类型')),
                ('tontact_phone', models.CharField(blank=True, help_text='联系电话', max_length=20, null=True, verbose_name='联系电话')),
                ('operator', models.CharField(blank=True, help_text='经办人', max_length=200, null=True, verbose_name='经办人')),
                ('delivery_date', models.DateTimeField(blank=True, help_text='交货日期', null=True, verbose_name='交货日期')),
                ('deliver_type', models.CharField(blank=True, help_text='送货方式', max_length=200, null=True, verbose_name='送货方式')),
                ('deliver_money', models.CharField(blank=True, help_text='运费', max_length=200, null=True, verbose_name='运费')),
                ('deliver_address', models.CharField(blank=True, help_text='收货地址', max_length=200, null=True, verbose_name='收货地址')),
                ('status', models.CharField(blank=True, help_text='订单状态', max_length=200, null=True, verbose_name='订单状态')),
                ('total_price', models.DecimalField(decimal_places=2, default=0, help_text='总金额', max_digits=10, verbose_name='总金额')),
                ('total_count', models.IntegerField(default=0, help_text='总数量', verbose_name='总数量')),
                ('pay_type', models.CharField(blank=True, help_text='支付方式', max_length=200, null=True, verbose_name='支付方式')),
                ('pay_from', models.CharField(blank=True, help_text='支付来源', max_length=200, null=True, verbose_name='支付来源')),
                ('is_pay', models.CharField(blank=True, help_text='是否支付', max_length=10, null=True, verbose_name='是否支付')),
                ('remark', models.CharField(blank=True, help_text='备注', max_length=500, null=True, verbose_name='备注')),
                ('is_closed', models.BooleanField(blank=True, default=False, help_text='订单是否完成', verbose_name='订单是否完成')),
                ('flag', models.CharField(blank=True, help_text='订单有效标识', max_length=20, null=True, verbose_name='订单有效标识')),
                ('trade_no', models.CharField(blank=True, help_text='在线支付流水号', max_length=20, null=True, verbose_name='在线支付流水号')),
                ('is_refond', models.BooleanField(blank=True, default=False, help_text='是否退款', verbose_name='是否退款')),
                ('depot', models.ForeignKey(blank=True, help_text='仓库', null=True, on_delete=django.db.models.deletion.PROTECT, to='new7.Depot', verbose_name='仓库')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
            },
        ),
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', null=True, verbose_name='更新时间')),
                ('count', models.IntegerField(default=1, help_text='数量', verbose_name='数量')),
                ('price', models.DecimalField(decimal_places=2, default=0, help_text='价格', max_digits=10, verbose_name='价格')),
                ('unit', models.CharField(blank=True, help_text='单位', max_length=200, null=True, verbose_name='单位')),
                ('goods', models.ForeignKey(blank=True, help_text='商品', null=True, on_delete=django.db.models.deletion.PROTECT, to='new7.Goods', verbose_name='商品')),
                ('operate_depot', models.ForeignKey(blank=True, help_text='操作仓库', null=True, on_delete=django.db.models.deletion.PROTECT, to='new7.Depot', verbose_name='操作仓库')),
                ('order', models.ForeignKey(blank=True, help_text='订单', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='order_goods', to='new7.Order', verbose_name='订单')),
            ],
            options={
                'verbose_name': '订单商品',
                'verbose_name_plural': '订单商品',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', null=True, verbose_name='更新时间')),
                ('deleted', models.BooleanField(blank=True, default=False, help_text='是否已删除', verbose_name='是否已删除')),
                ('object_id', models.PositiveIntegerField()),
                ('role', models.CharField(choices=[('super_admin', '超级管理员'), ('admin', '管理员'), ('worker', '业务员'), ('warekeeper', '仓库管理员')], default='worker', help_text='角色', max_length=20, verbose_name='角色')),
                ('name', models.CharField(help_text='姓名', max_length=20, verbose_name='姓名')),
                ('gender', models.IntegerField(choices=[(1, '男'), (2, '女')], default=1, help_text='性别', verbose_name='性别')),
                ('birth', models.DateTimeField(blank=True, help_text='出生日期', null=True, verbose_name='出生日期')),
                ('code', models.CharField(help_text='员工编号', max_length=200, null=True, unique=True, verbose_name='员工编号')),
                ('phone', models.CharField(help_text='电话', max_length=20, verbose_name='电话')),
                ('phone_verified', models.BooleanField(blank=True, default=False, help_text='电话是否已验证', verbose_name='电话是否已验证')),
                ('address', models.CharField(blank=True, help_text='地址', max_length=20, null=True, verbose_name='地址')),
                ('salary', models.IntegerField(default=0, help_text='工资', verbose_name='工资')),
                ('desc', models.CharField(blank=True, help_text='描述', max_length=100, null=True, verbose_name='描述')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType')),
                ('depot', models.ForeignKey(blank=True, help_text='负责仓库', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='depot_keepers', to='new7.Depot', verbose_name='负责仓库')),
                ('user', models.OneToOneField(help_text='用户', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '个人信息',
                'verbose_name_plural': '个人信息',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', null=True, verbose_name='更新时间')),
                ('name', models.CharField(help_text='单位名称', max_length=20, null=True, unique=True, verbose_name='单位名称')),
                ('type', models.CharField(blank=True, choices=[('formal', '正规合作'), ('finance', '商铺合作'), ('stall', '摊贩合作')], default='a', help_text='供应商分类', max_length=20, verbose_name='供应商分类')),
                ('license_code', models.CharField(blank=True, help_text='执照编号', max_length=20, null=True, verbose_name='执照编号')),
                ('tontact_phone', models.CharField(blank=True, help_text='联系电话', max_length=20, null=True, verbose_name='联系电话')),
                ('contact_name', models.CharField(blank=True, help_text='联系人', max_length=20, null=True, verbose_name='联系人')),
                ('address', models.CharField(blank=True, help_text='公司地址', max_length=200, null=True, verbose_name='公司地址')),
                ('operator', models.CharField(blank=True, help_text='经办人', max_length=200, null=True, verbose_name='经办人')),
                ('operator_name', models.CharField(blank=True, help_text='经办人电话', max_length=200, null=True, verbose_name='经办人电话')),
                ('desc', models.CharField(blank=True, help_text='描述', max_length=200, null=True, verbose_name='描述')),
            ],
            options={
                'verbose_name': '供应商',
                'verbose_name_plural': '供应商',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='supplier',
            field=models.ForeignKey(blank=True, help_text='供应商', null=True, on_delete=django.db.models.deletion.PROTECT, to='new7.Supplier', verbose_name='供应商'),
        ),
        migrations.AddField(
            model_name='goodsrecord',
            name='order',
            field=models.ForeignKey(blank=True, help_text='所属订单', null=True, on_delete=django.db.models.deletion.PROTECT, to='new7.Order', verbose_name='所属订单'),
        ),
        migrations.AddField(
            model_name='goodsrecord',
            name='record_depot',
            field=models.ForeignKey(blank=True, help_text='操作仓库', null=True, on_delete=django.db.models.deletion.PROTECT, to='new7.Depot', verbose_name='操作仓库'),
        ),
        migrations.AddField(
            model_name='goods',
            name='last_operator',
            field=models.ForeignKey(blank=True, help_text='最近操作人', null=True, on_delete=django.db.models.deletion.PROTECT, to='new7.Profile', verbose_name='最近操作人'),
        ),
    ]
