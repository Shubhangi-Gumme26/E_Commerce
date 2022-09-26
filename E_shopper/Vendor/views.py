from rest_framework import viewsets
from .models import Vendor
from .serializers import VendorSerializer
# from .models import Vendor, PurchaseOrder
# from .serializers import VendorSerializer, PurchaseOrderSerializer




# Create your views here.
class VendorModelViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


# class PurchaseOrderModelViewSet(viewsets.ModelViewSet):
#     queryset = PurchaseOrder.objects.all()
#     serializer_class = PurchaseOrderSerializer

