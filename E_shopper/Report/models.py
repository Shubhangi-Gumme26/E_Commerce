from django.db import models
from django.db.models import CASCADE


# Create your models here.
from Inventory.models import Product
from Vendor.models import Vendor


class PurchaseOrder(models.Model):
    po_id = models.AutoField(primary_key=True)
    vendor = models.ForeignKey(Vendor, on_delete=CASCADE, related_name='vendor_purchesorder_rel')
    product = models.ForeignKey(Product, on_delete=CASCADE, related_name='purchesorder_purdetails_rel')
    total_amount = models.FloatField(default=200000)
    datettime = models.DateField(auto_now=True)
    def __str__(self):
        return f"Purches Order:{self.po_id}--- Product:{self.product}"

#vendor invoice
class PurchaseOrderDetails(models.Model):
    v_invoice_id = models.AutoField(primary_key=True)
    vendor = models.ForeignKey(Vendor, on_delete=CASCADE, related_name='vendor_purdetails_rel')
    purchaseorder = models.ForeignKey(PurchaseOrder, on_delete=CASCADE, default=True, related_name='purchesorder_details_rel')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Purches Order:{self.po_id}--- Product:{self.product}"