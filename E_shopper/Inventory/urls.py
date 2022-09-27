from django.urls import path
from .views import ExportImportExcel

urlpatterns = [
    path('import_export/', ExportImportExcel.as_view(), name='import_export_excel_url'),
]