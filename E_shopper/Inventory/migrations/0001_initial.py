# Generated by Django 4.1.1 on 2022-09-24 18:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Vendor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('cat_name', models.CharField(max_length=100, unique=True)),
                ('cat_desc', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('discount_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=255)),
                ('discount', models.FloatField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='GST',
            fields=[
                ('gst_id', models.AutoField(primary_key=True, serialize=False)),
                ('igst', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('hsn_code', models.IntegerField(unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.category', unique=True)),
            ],
            options={
                'verbose_name_plural': 'GST',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_name', models.CharField(max_length=100, unique=True)),
                ('p_img', models.ImageField(upload_to='product')),
                ('p_price', models.FloatField()),
                ('product_stock', models.FloatField()),
                ('unit', models.CharField(max_length=100)),
                ('reorder_level', models.FloatField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat_product', to='Inventory.category')),
                ('discount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Inventory.discount')),
                ('gst', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.gst')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vendor.vendor')),
            ],
        ),
    ]
