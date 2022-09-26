from django.core import validators
from django.db import models
from django.db.models import CASCADE
from Vendor.models import Vendor


# Create your models here.
class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=100, unique=True)
    cat_desc = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return f"{self.cat_name}"


class GST(models.Model):
    gst_id = models.AutoField(primary_key=True)
    # category = models.ForeignKey(Category, on_delete=CASCADE, unique=True, related_name='category_gst_rel')
    category = models.ForeignKey(Category, on_delete=CASCADE, related_name='category_gst_rel')
    igst = models.IntegerField(validators=[validators.MinValueValidator(1),validators.MaxValueValidator(100)])
    hsn_code = models.IntegerField(unique=True)
    def __str__(self):
        return f"{self.hsn_code} --> {self.igst}% --> {self.category}"
    class Meta:
        verbose_name_plural = 'GST'


class Discount(models.Model):
    discount_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    desc = models.CharField(max_length=255)
    discount = models.FloatField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    def __str__(self):
        return f"{self.product_name} -->{self.discount}"


class Product(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=CASCADE, related_name='category_product_rel')
    p_img = models.ImageField(upload_to='product', null=True, blank=True)
    p_price = models.IntegerField()
    vendor = models.ForeignKey(Vendor, on_delete=CASCADE, related_name='vendor_product_rel')
    product_stock = models.FloatField()
    unit = models.CharField(max_length=100)
    reorder_level = models.FloatField()
    discount = models.ForeignKey(Discount, on_delete=CASCADE, null=True, blank=True, related_name='discount_product_rel')
    gst = models.ForeignKey(GST, on_delete=CASCADE, related_name='gst_product_rel')
    datetime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.p_name}"

class ExcelFileUpload(models.Model):
    excel_file_upload = models.FileField(upload_to='static/ImportedProduct')

