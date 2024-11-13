from rest_framework import serializers
from invoice.models import Invoice, InvoiceDetail

class InvoiceDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = InvoiceDetail
        exclude = ['invoice']
        extra_kwargs = {
            'id': {'read_only': True},
            'line_total':{'read_only':True}
        }

    def validate_quantity(self, value):
        """Ensure quantity is a positive integer."""
        if value < 1:
            raise serializers.ValidationError("Quantity must be at least 1.")
        return value

class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(many=True, required=False)

    class Meta:
        model = Invoice
        fields = ['id', 'invoice_number', 'customer_name', 'date', 'details']
    
    def validate_details(self, value):
        """Ensure that each detail has the required fields."""
        if self.instance is None and not value:
            raise serializers.ValidationError("Invoice must have at least one detail.")

        for detail in value:
            if 'quantity' not in detail or 'price' not in detail:
                raise serializers.ValidationError("Each detail must include 'quantity' and 'price'.")
            if detail['quantity'] < 1:
                raise serializers.ValidationError("Quantity must be at least 1.")
        return value

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        invoice = Invoice.objects.create(**validated_data)
        for detail_data in details_data:
            InvoiceDetail.objects.create(invoice=invoice, **detail_data)
        return invoice
    
    def update(self, instance, validated_data):
        instance.invoice_number = validated_data.get('invoice_number', instance.invoice_number)
        instance.customer_name = validated_data.get('customer_name', instance.customer_name)
        instance.date = validated_data.get('date', instance.date)
        instance.save()

        if 'details' in validated_data:
            details_data = validated_data.pop('details')
            instance.details.all().delete()
            for detail_data in details_data:
                InvoiceDetail.objects.create(invoice=instance, **detail_data)

        return instance
