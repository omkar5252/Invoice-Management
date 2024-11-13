from rest_framework import viewsets
from invoice.models import Invoice
from invoice.api.serializers import InvoiceSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer