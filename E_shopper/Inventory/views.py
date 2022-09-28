from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer, GSTSerializer, DiscountSerializer, ProductSerializer, ExcelFileUploadSerializer
from .models import Category, GST, Discount, Product
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.pagination import PageNumberPagination
from datetime import datetime



class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class GSTModelViewSet(viewsets.ModelViewSet):
    queryset = GST.objects.all()
    serializer_class = GSTSerializer



class DiscountModelViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer



class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['p_name']
    pagination_class = PageNumberPagination


import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import uuid
import os
# from django.utils import timezone
from .models import ExcelFileUpload
class ExportImportExcel(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        df = pd.DataFrame(serializer.data)
        print("pandas dataframe",df)
        df.to_csv(f"{settings.BASE_DIR}/static/ExportProduct/{uuid.uuid4()}.csv", encoding='UTF-8', index=False)
        # df.to_csv(f"{settings.BASE_DIR}/static/ExportProduct/{datetime.now()}.csv", encoding='UTF-8', index=False)
        return Response(status=status.HTTP_200_OK)
    def post(self, request):
        from Vendor.models import Vendor
        new_upload_file = request.FILES['files']
        print("file type is file : ", new_upload_file)
        exceled_upload_obj = ExcelFileUpload(excel_file_upload=new_upload_file)
        print("exceled_upload_obj file upload : ", exceled_upload_obj)
        df = pd.read_csv(f"{settings.BASE_DIR}/static/ImportProductPending/{exceled_upload_obj.excel_file_upload}", encoding='UTF-8')


        print("list od data", df.values.tolist())
        for i in df.values.tolist():

            # catdata = Category.objects.get(id)
            # for j in catdata:
            #     print("category id is :", j.id)
            print(i)
            print("Product id : ", i[0])
            print("Product name : ", i[1])
            print("Product Image : ", i[2])
            print("Product price : ", i[3])
            print("Product stock : ", i[4])
            print("Product unit : ", i[5])
            print("Product reorder level : ", i[6])
            print("Product category : ", i[7])
            print("Product vendor : ", i[8])
            print("Product discount : ", i[9])
            print("Product gst : ", i[10])
            print(Category.objects.get_or_create(cat_id=i[7]))
            print(Vendor.objects.get_or_create(v_id=i[8]))
            print(Discount.objects.get_or_create(discount_id=i[9]))
            print(GST.objects.get_or_create(gst_id=i[10]))
            prodata = Product.objects.create(
                                    p_id = i[0],
                                    p_name = i[1],
                                    p_img = i[2],
                                    p_price = i[3],
                                    product_stock=i[4],
                                    unit=i[5],
                                    reorder_level=i[6],
                                    category=Category.objects.get_or_create(cat_id=i[7]),
                                    vendor= Vendor.objects.get_or_create(v_id=i[8]),
                                    discount = Discount.objects.get_or_create(discount_id=i[9]),
                                    gst = GST.objects.get_or_create(gst_id=i[10]),
                                    )
            serializer = ProductSerializer(prodata, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



