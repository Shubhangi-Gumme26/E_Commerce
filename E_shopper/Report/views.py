from django.shortcuts import render
from .models import PurchaseOrder, PurchaseOrderDetails
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from .serializers import PurchaseOrderSerializer, PurchaseOrderDetailsSerializer
from Inventory.models import Product


import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import uuid
import datetime
import os
class PurchaseOrderModelViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # authentication_classes = [JWTAuthentication]
    def list(self, request):
        # queryset = PurchaseOrder.objects.filter(date=datetime.datetime.now())
        fromdate = PurchaseOrder.objects.filter(date='stdate')         #need to change with html input enddate
        todate = PurchaseOrder.objects.filter(date='stdate')           #need to change with html input enddate
        queryset = Product.objects.filter(datetime__lte=fromdate,datetime__gte=todate)
        print("all Product data usinmg date : ", queryset)
        serializer = PurchaseOrderSerializer(queryset, many=True)
        df = pd.DataFrame(serializer.data)
        print("pandas dataframe", df)
        df.to_csv(f"{settings.BASE_DIR}/static/VendorReport/{uuid.uuid4()}.csv", encoding='UTF-8', index=False)
        # df.to_csv(f"{settings.BASE_DIR}/static/ExportProduct/{datetime.now()}.csv", encoding='UTF-8', index=False)
        return Response(status=status.HTTP_200_OK)

class PurchaseOrderDetailsModelViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrderDetails.objects.all()
    serializer_class = PurchaseOrderDetailsSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]