from rest_framework import serializers
from .models import Category, GST, Discount, Product


class CategorySerializer(serializers.ModelSerializer):
    category_product_rel = serializers.StringRelatedField(many=True, read_only=True)
    category_gst_rel = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'
        fields = ['cat_id', 'cat_name', 'cat_desc', 'category_product_rel', 'category_gst_rel']
    def create(self, validated_data):
        return Category.objects.create(**validated_data)


class GSTSerializer(serializers.ModelSerializer):
    gst_product_rel = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = GST
        # fields = '__all__'
        fields = ['gst_id', 'category', 'igst', 'hsn_code', 'gst_product_rel']
    def create(self, validated_data):
        return GST.objects.create(**validated_data)


import datetime
class DiscountSerializer(serializers.ModelSerializer):
    discount_product_rel = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Discount
        # fields = '__all__'
        fields = ['discount_id', 'product_name', 'desc', 'discount', 'start_date', 'end_date', 'discount_product_rel']
    def create(self, validated_data):
        return Discount.objects.create(**validated_data)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['p_id', 'p_name', 'category', 'p_price', 'vendor', 'product_stock', 'unit', 'reorder_level', 'discount', 'gst', 'datetime']
    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    #logoc for check product_stock <= reorder_level
    def validate(self, data):
        ps = data.get('product_stock')
        print("product stock is : ", ps)
        ro = data.get('reorder_level')
        print("reorder level is : ", ro)
        remain_stock = ps - 2       # CustomerOrder.objects.get('quantity'), data=1000-2=98
        print(f"remain_stock is : {ps}-{2}={remain_stock}")
        if remain_stock <= ro:
            raise serializers.ValidationError(f"Reorder level reached, please increase quantity of same product")
        elif remain_stock == 0:
            raise serializers.ValidationError(f"No product available")
        return data




# for Import Export Excel file
from .models import ExcelFileUpload
class ExcelFileUploadSerializer(serializers.ModelSerializer):
    cat_product = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = ExcelFileUpload
        fields = '__all__'
        # For add data or Post()

    def create(self, validated_data):
        return ExcelFileUpload.objects.create(**validated_data)