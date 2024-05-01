

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def clean(self):
      
        if not 0 <= self.on_time_delivery_rate <= 100:
            raise ValidationError("On-time delivery rate must be between 0 and 100.")
        if not 0 <= self.quality_rating_avg <= 5:  # Assuming quality ratings are on a scale of 0 to 5
            raise ValidationError("Quality rating average must be between 0 and 5.")
        if self.average_response_time < 0:
            raise ValidationError("Average response time cannot be negative.")
        if not 0 <= self.fulfillment_rate <= 100:
            raise ValidationError("Fulfillment rate must be between 0 and 100.")

class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled')
    ]

    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='purchase_orders')
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField(default=timezone.now)  
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def clean(self):
      
        if self.acknowledgment_date and self.acknowledgment_date < self.issue_date:
            raise ValidationError("Acknowledgment date cannot be before issue date.")

    def save(self, *args, **kwargs):
        self.full_clean() 
        super().save(*args, **kwargs)