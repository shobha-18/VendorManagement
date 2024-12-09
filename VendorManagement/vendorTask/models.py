from django.db import models

class VendorDetails(models.Model):
    vendor_code = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    contact_details = models.CharField(max_length=100)
    on_time_delivery_rate = models.DecimalField(max_digits=15, decimal_places=7)
    quality_rating_avg = models.DecimalField(max_digits=15, decimal_places=7)
    average_response_time = models.DecimalField(max_digits=15, decimal_places=7)
    fulfillment_rate = models.DecimalField(max_digits=15, decimal_places=7)

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=255)
    vendor_code = models.ForeignKey(VendorDetails, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=100)
    quality_rating = models.DecimalField(max_digits=15, decimal_places=7)
    #rain=models.BooleanField(default=False)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField()

class VendorPerformance(models.Model):
    vendor_code = models.ForeignKey(VendorDetails, on_delete=models.CASCADE)         
    date = models.DateTimeField()
    on_time_delivery_rate = models.DecimalField(max_digits=15, decimal_places=7)
    quality_rating_avg = models.DecimalField(max_digits=15, decimal_places=7)
    average_response_time = models.DecimalField(max_digits=15, decimal_places=7)
    fulfillment_rate = models.DecimalField(max_digits=15, decimal_places=7)
