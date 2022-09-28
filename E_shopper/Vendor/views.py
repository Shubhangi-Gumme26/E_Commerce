from rest_framework import viewsets
from .models import Vendor
from .serializers import VendorSerializer





# Create your views here.
class VendorModelViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer



