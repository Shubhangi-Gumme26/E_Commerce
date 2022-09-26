from django.urls import path
from .views import ExportImportExcel

urlpatterns = [
    path('ExportImportExcel/', ExportImportExcel.as_view, name='ExportImportExcel_url')
]