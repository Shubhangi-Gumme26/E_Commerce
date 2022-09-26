from django.db import models
from django.db.models import CASCADE
# from E_shopper.Inventory import Product  # error

# Create your models here.
class Vendor(models.Model):
    v_id = models.AutoField(primary_key=True)
    v_name = models.CharField(max_length=100)
    v_phone = models.IntegerField(unique=True)
    v_email = models.EmailField(unique=True)
    v_address = models.CharField(max_length=255, null=True, blank=True)
    v_gst_no = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return f"{self.v_name}"


# class PurchaseOrder(models.Model):
#     po_id = models.AutoField(primary_key=True)
#     vendor = models.ForeignKey(Vendor, on_delete=CASCADE)
#     product = models.ForeignKey(Product, on_delete=CASCADE)
#     total_amount = models.FloatField(default=200000)
#
#     def __str__(self):
#         return f"Purches Order:{self.po_id}--- Product:{self.product}"
