# Generated by Django 4.1.1 on 2022-09-25 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0004_remove_product_total_am'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelFileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excelupload', models.FileField(upload_to='ImportedProduct')),
            ],
        ),
    ]
