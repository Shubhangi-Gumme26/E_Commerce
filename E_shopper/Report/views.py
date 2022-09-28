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
from datetime import date, timedelta
import os
class PurchaseOrderModelViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def list(self, request):
        todays_date = datetime.date.today()                           # today date
        weekly = todays_date - datetime.timedelta(days=7)            # weekly date = 28-7=21
        monthly = todays_date - datetime.timedelta(days=30)          # monthly date = 28-30=
        quarterly = todays_date - datetime.timedelta(days=90)        # quarterly date
        yearly = todays_date - datetime.timedelta(days=365)          # yearly date

        while True:
            choice = input("Enter your choice : ")
            if choice == "today":                                               # today's report
                purorder = PurchaseOrder.objects.filter(date__gte=todays_date, date__lte=todays_date)
                queryset = purorder.prefetch_related("product")
                print("Purche order details are : ", queryset)
                serializer = PurchaseOrderSerializer(queryset, many=True)
                df = pd.DataFrame(serializer.data)
                print("pandas dataframe", df)
                # df.to_csv(f"{settings.BASE_DIR}/static/VendorPurchesReport/{uuid.uuid4()}.csv", encoding='UTF-8', index=False)
                df.to_csv(f"{settings.BASE_DIR}/static/VendorPurchesReport/{datetime.date.today()}.csv", encoding='UTF-8', index=False)
                return Response(status=status.HTTP_200_OK)
                break
            elif choice == "week":                                                   # weekly report
                purorder = PurchaseOrder.objects.filter(date__gte=weekly, date__lte=todays_date)
                print("weekly start date : ", weekly)
                print("weekly end date : ", todays_date)
                queryset = purorder.prefetch_related("product")
                print("Purche order details are : ", queryset)
                serializer = PurchaseOrderSerializer(queryset, many=True)
                df = pd.DataFrame(serializer.data)
                print("pandas dataframe", df)
                # df.to_csv(f"{settings.BASE_DIR}/static/VendorPurchesReport/{uuid.uuid4()}.csv", encoding='UTF-8', index=False)
                df.to_csv(f"{settings.BASE_DIR}/static/VendorPurchesReport/{datetime.date.today()}.csv", encoding='UTF-8', index=False)
                return Response(status=status.HTTP_200_OK)
                break
            elif choice == "month":                                                 # monthly report
                purorder = PurchaseOrder.objects.filter(date__gte=monthly, date__lte=todays_date)
                print("month start date : ", monthly)
                print("month end date : ", todays_date)
                queryset = purorder.prefetch_related("product")
                print("Purche order details are : ", queryset)
                serializer = PurchaseOrderSerializer(queryset, many=True)
                df = pd.DataFrame(serializer.data)
                print("pandas dataframe", df)
                # df.to_csv(f"{settings.BASE_DIR}/static/VendorPurchesReport/{uuid.uuid4()}.csv", encoding='UTF-8', index=False)
                df.to_csv(f"{settings.BASE_DIR}/static/VendorPurchesReport/{datetime.date.today()}.csv", encoding='UTF-8', index=False)
                return Response(status=status.HTTP_200_OK)
                break
            elif choice == 'quarter':                                               # quarterly report
                purorder = PurchaseOrder.objects.filter(date__gte=quarterly, date__lte=todays_date)
                print("quarter start date : ", quarterly)
                print("quarter end date : ", todays_date)
                queryset = purorder.prefetch_related("product")
                print("Purche order details are : ", queryset)
                serializer = PurchaseOrderSerializer(queryset, many=True)
                df = pd.DataFrame(serializer.data)
                print("pandas dataframe", df)
                # df.to_csv(f"{settings.BASE_DIR}/static/VendorPurchesReport/{uuid.uuid4()}.csv", encoding='UTF-8', index=False)
                df.to_csv(f"{settings.BASE_DIR}/static/VendorPurchesReport/{datetime.date.today()}.csv", encoding='UTF-8', index=False)
                return Response(status=status.HTTP_200_OK)
                break
            elif choice == 'year':                                                  # yearly report
                purorder = PurchaseOrder.objects.filter(date__gte=yearly, date__lte=todays_date)
                print("yearly start date : ", yearly)
                print("yearly end date : ", todays_date)
                queryset = purorder.prefetch_related("product")
                print("Purche order details are : ", queryset)
                serializer = PurchaseOrderSerializer(queryset, many=True)
                df = pd.DataFrame(serializer.data)
                print("pandas dataframe", df)
                # df.to_csv(f"{settings.BASE_DIR}/static/VendorPurchesReport/{uuid.uuid4()}.csv", encoding='UTF-8', index=False)
                df.to_csv(f"{settings.BASE_DIR}/static/VendorPurchesReport/{datetime.date.today()}.csv", encoding='UTF-8', index=False)
                return Response(status=status.HTTP_200_OK)
                break
            elif choice == '':
                break





    # def list(self, request):
    #     # fromdate = request.get['sdate']                                  # "2022-09-27"
    #     # todate = request.get['edate']                                    # "2022-09-28"
    #     fromdate = "2022-09-27"
    #     todate = "2022-09-28"
    #     if fromdate:
    #         purorder = PurchaseOrder.objects.filter(date__gte=fromdate)
    #     if todate:
    #         purorder = PurchaseOrder.objects.filter(date__lte=todate)
    #     # purorder = PurchaseOrder.objects.filter(date__gte=fromdate, date__lte=todate)
    #     queryset = purorder.prefetch_related("product")
    #     print("Purche order details are : ", queryset)
    #     serializer = PurchaseOrderSerializer(queryset, many=True)
    #     df = pd.DataFrame(serializer.data)
    #     print("pandas dataframe", df)
    #     df.to_csv(f"{settings.BASE_DIR}/static/VendorPurchesReport/{uuid.uuid4()}.csv", encoding='UTF-8', index=False)
    #     # df.to_csv(f"{settings.BASE_DIR}/static/ExportProduct/{datetime.datetime.now()}.csv", encoding='UTF-8', index=False)
    #     return Response(status=status.HTTP_200_OK)

class PurchaseOrderDetailsModelViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrderDetails.objects.all()
    serializer_class = PurchaseOrderDetailsSerializer
