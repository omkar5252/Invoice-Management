from django.urls import path, include
from rest_framework.routers import DefaultRouter
from invoice.api.views import InvoiceViewSet

router = DefaultRouter()
router.register('invoice', InvoiceViewSet, basename='invoice')

urlpatterns = [
    path('', include(router.urls)),
]