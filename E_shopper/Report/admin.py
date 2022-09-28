from django.contrib import admin
from Report.models import PurchaseOrderDetails, PurchaseOrder

# Register your models here.
@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ['po_id', 'vendor', 'product', 'total_amount', 'date']
    list_filter = ['po_id', 'vendor', 'product', 'total_amount', 'date']
    search_fields = ['po_id', 'vendor', 'product', 'total_amount', 'date']
# admin.site.register(PurchaseOrder, PurchaseOrderAdmin)


@admin.register(PurchaseOrderDetails)
class PurchaseOrderDetailsAdmin(admin.ModelAdmin):
    list_display = ['v_invoice_id', 'vendor', 'purchaseorder', 'date']
    list_filter = ['v_invoice_id', 'vendor', 'purchaseorder', 'date']
    search_fields = ['v_invoice_id', 'vendor', 'purchaseorder', 'date']
# admin.site.register(PurchaseOrderDetails, PurchaseOrderDetailsAdmin)