# Generated by Django 4.1.1 on 2022-09-27 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0002_purchaseorder'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PurchaseOrder',
        ),
    ]
