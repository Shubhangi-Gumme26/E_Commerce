from django.contrib import admin
from .models import Vendor
# from .models import Vendor, PurchaseOrder



# Register your models here.
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['v_id', 'v_name', 'v_phone', 'v_email', 'v_address', 'v_gst_no']
    list_filter = ['v_email']
    search_fields = ['v_id', 'v_name', 'v_phone', 'v_email', 'v_address', 'v_gst_no']
# admin.site.register(Vendor, VendorAdmin)



# @admin.register(PurchaseOrder)
# class PurchaseOrderAdmin(admin.ModelAdmin):
#     list_display = ['po_id', 'vender_id', 'p_id']
#     list_filter = ['po_id', 'vender_id', 'p_id']
#     search_fields = ['po_id', 'vender_id', 'p_id']

