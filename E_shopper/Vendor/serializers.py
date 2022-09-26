from rest_framework import serializers
from .models import Vendor
# from .models import Vendor, PurchaseOrder


class VendorSerializer(serializers.ModelSerializer):
    vendor_product_rel = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Vendor
        # fields = '__all__'
        fields = ['v_id', 'v_name', 'v_phone','v_email', 'v_address', 'v_gst_no', 'vendor_product_rel']


# class PurchaseOrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PurchaseOrder
#         fields = '__all__'