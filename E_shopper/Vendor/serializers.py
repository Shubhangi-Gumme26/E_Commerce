from rest_framework import serializers, status
from .models import Vendor
# from .models import Vendor, PurchaseOrder
from rest_framework.response import Response


class VendorSerializer(serializers.ModelSerializer):
    vendor_product_rel = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Vendor
        # fields = '__all__'
        fields = ['v_id', 'v_name', 'v_phone','v_email', 'v_address', 'v_gst_no', 'vendor_product_rel']
    def create(self, validated_data):
        return Vendor.objects.create(**validated_data)
    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     self.perform_destroy(instance)
    #     return Response(status=status.HTTP_204_No_CONTENT)

# class PurchaseOrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PurchaseOrder
#         fields = '__all__'
#     def create(self, validated_data):
#         return PurchaseOrder.objects.create(**validated_data)