from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Vendor
from .serializers import VendorSerializer
# from .models import Vendor, PurchaseOrder
# from .serializers import VendorSerializer, PurchaseOrderSerializer




# Create your views here.
class VendorModelViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]



# class PurchaseOrderModelViewSet(viewsets.ModelViewSet):
#     queryset = PurchaseOrder.objects.all()
#     serializer_class = PurchaseOrderSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     authentication_classes = [JWTAuthentication]


