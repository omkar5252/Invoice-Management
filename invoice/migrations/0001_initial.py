# Generated by Django 5.0.9 on 2024-11-13 06:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(max_length=20, unique=True)),
                ('customer_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField(default=0)),
                ('line_total', models.FloatField(default=0)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='invoice.invoice')),
            ],
        ),
    ]