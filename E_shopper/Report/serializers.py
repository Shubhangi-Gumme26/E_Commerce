from rest_framework import serializers
from .models import PurchaseOrder, PurchaseOrderDetails
from Vendor.serializers import VendorSerializer
from Inventory.serializers import ProductSerializer

class PurchaseOrderSerializer(serializers.ModelSerializer):
    vendor_purchesorder_rel = VendorSerializer(read_only=True)
    product_purchesorder_rel = ProductSerializer(read_only=True)
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
    def create(self, validated_data):
        return PurchaseOrder.objects.create(**validated_data)


class PurchaseOrderDetailsSerializer(serializers.ModelSerializer):
    vendor_purdetails_rel = VendorSerializer(read_only=True)
    purchesorder_purdetails_rel = PurchaseOrderSerializer(read_only=True)
    class Meta:
        model = PurchaseOrderDetails
        fields = '__all__'
    def create(self, validated_data):
        return PurchaseOrderDetails.objects.create(**validated_data)