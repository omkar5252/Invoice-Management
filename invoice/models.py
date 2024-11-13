from django.db import models

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20, unique=True)
    customer_name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.invoice_number

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, related_name="details", on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.FloatField(default=0)
    line_total = models.FloatField(default=0)
    
    def save(self, *args, **kwargs):
        self.line_total = round(self.quantity * self.price, 2)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.description} - {self.invoice.invoice_number}"