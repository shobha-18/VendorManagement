# Generated by Django 3.2 on 2024-05-14 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendorTask', '0003_auto_20240514_0706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='po_number',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='vendordetails',
            name='vendor_code',
            field=models.CharField(max_length=255),
        ),
    ]
