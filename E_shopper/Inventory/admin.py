from django.contrib import admin
from .models import Category, GST, Discount, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cat_id', 'cat_name', 'cat_desc']
    list_filter = ['cat_name']
    search_fields = ['cat_id', 'cat_name', 'cat_desc']
# admin.site.register(Category, CategoryAdmin)


@admin.register(GST)
class GSTAdmin(admin.ModelAdmin):
    list_display = ['gst_id', 'category', 'igst', 'hsn_code']
    list_filter = ['category']
    search_fields = ['gst_id', 'category', 'igst', 'hsn_code']
# admin.site.register(GST, GSTAdmin)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['discount_id', 'product_name', 'desc', 'discount', 'start_date', 'end_date']
    list_filter = ['product_name', 'discount']
    search_fields = ['discount_id', 'product_name', 'desc', 'discount', 'start_date', 'end_date']
# admin.site.register(Discount, DiscountAdmin)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['p_id','p_name','category','gst','reorder_level','vendor','unit','p_price','product_stock','discount', 'datetime']
    list_filter = ['reorder_level','p_name','category','vendor']
    search_fields = ['p_id','p_name','category','p_price','vendor','product_stock','unit','reorder_level','discount','gst']
# admin.site.register(Product, ProductAdmin)


