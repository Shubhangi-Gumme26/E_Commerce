from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer, GSTSerializer, DiscountSerializer, ProductSerializer, ExcelFileUploadSerializer
from .models import Category, GST, Discount, Product
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.pagination import PageNumberPagination


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = []
    # authentication_classes = [JWTAuthentication]


class GSTModelViewSet(viewsets.ModelViewSet):
    queryset = GST.objects.all()
    serializer_class = GSTSerializer
    # permission_classes = []
    # authentication_classes = [JWTAuthentication]

class DiscountModelViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    # permission_classes = []
    # authentication_classes = [JWTAuthentication]

class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = []
    # authentication_classes = [JWTAuthentication]
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
import datetime


from .models import ExcelFileUpload
class ExportImportExcel(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        df = pd.DataFrame(serializer.data)
        # {uuid.uuid4()}.csv
        df.to_csv(f"{settings.BASE_DIR}/static/ExportProduct/{datetime.datetime.now()}.csv", encoding='UTF-8', index=False)
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        exceled_upload_obj = ExcelFileUpload(excel_file_upload=request.FILES['files'])
        print("exceled_upload_obj file upload : ", exceled_upload_obj)

        df = pd.read_csv(f"{settings.BASE_DIR}/static/ImportProductPending/{exceled_upload_obj.excel_file_upload}", encoding='UTF-8')

        ########### create customer instance
        print("list od data", df.values.tolist())
        for i in df.values.tolist():
            print(i)
            print("Product id : ", i[0])
            print("Product name : ", i[1])
            print("Product Image : ", i[2])
            print("Product price : ", i[3])
            print("Product stock : ", i[4])
            print("Product unit : ", i[5])
            print("Product reorder level : ", i[6])
            print("Product datetime : ", i[7])
            print("Product category : ", i[8])
            print("Product vendor : ", i[9])
            print("Product discount : ", i[10])
            print("Product gst : ", i[11])
            prodata = Product(
                    p_id = i[0],
                    p_name = i[1],
                    p_img=i[2],
                    p_price=i[3],
                    product_stock=i[4],
                    unit=i[5],
                    reorder_level=i[6],
                    datetime = i[7],
                    category = i[8],
                    vendor = i[9],
                    discount = i[10],
                    gst = i[11],
                                    )
            prodata.save()
            print(prodata)
        return Response(status=status.HTTP_200_OK)
