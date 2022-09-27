from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Inventory.views import CategoryModelViewSet, GSTModelViewSet, DiscountModelViewSet, ProductModelViewSet
from Vendor.views import VendorModelViewSet
# from Vendor.views import VendorModelViewSet, PurchaseOrderModelViewSet
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from Report.views import PurchaseOrderModelViewSet, PurchaseOrderDetailsModelViewSet


# for CategoryModelViewSet
router1 = DefaultRouter()
router1.register('', CategoryModelViewSet)

# for GSTModelViewSet
router2 = DefaultRouter()
router2.register('', GSTModelViewSet)

# for DiscountModelViewSet
router3 = DefaultRouter()
router3.register('', DiscountModelViewSet)

# for ProductModelViewSet
router4 = DefaultRouter()
router4.register('', ProductModelViewSet, basename='ProductModelViewSetbase')

# for VendorModelViewSet
router5 = DefaultRouter()
router5.register('', VendorModelViewSet)

# for PurchaseOrderModelViewSet
router6 = DefaultRouter()
router6.register('', PurchaseOrderModelViewSet)

# for PurchaseOrderDetailsModelViewSet
router7 = DefaultRouter()
router7.register('', PurchaseOrderDetailsModelViewSet)

# for ExcelFileUploadModelViewSet
# router7 = DefaultRouter()
# router7.register('', ExportImportExcelModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('category/', include(router1.urls)),
    path('gst/', include(router2.urls)),
    path('discount/', include(router3.urls)),
    path('product/', include(router4.urls)),

    path('vendor/', include(router5.urls)),

    path('purchaseorder/', include(router6.urls)),
    path('purchaseorder_details/', include(router7.urls)),

    # path('ExportImportExcel/', include(router7.urls)),
    path('importexporturl/', include('Inventory.urls')),

    #JWT Authentication urls
    path('api/token/', TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name ='token_refresh'),
]  +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
