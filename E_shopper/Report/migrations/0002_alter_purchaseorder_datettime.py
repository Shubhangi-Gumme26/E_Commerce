# Generated by Django 4.1.1 on 2022-09-27 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Report', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='datettime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
