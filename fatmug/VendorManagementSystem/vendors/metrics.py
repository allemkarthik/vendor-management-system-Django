from django.db.models import Avg, Count, F
from .models import PurchaseOrder, Vendor

def calculate_performance_metrics(vendor):
    
    completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
    total_completed_orders = completed_orders.count()
    on_time_delivery_count = completed_orders.filter(delivery_date__lte=F('acknowledgment_date')).count()
    on_time_delivery_rate = (on_time_delivery_count / total_completed_orders) * 100 if total_completed_orders > 0 else 0
    vendor.on_time_delivery_rate = on_time_delivery_rate

    
    quality_rating_avg = completed_orders.aggregate(quality_rating_avg=Avg('quality_rating'))['quality_rating_avg']
    vendor.quality_rating_avg = quality_rating_avg if quality_rating_avg else 0

    
    response_times = completed_orders.exclude(acknowledgment_date=None).annotate(
        response_time=F('acknowledgment_date') - F('issue_date')
    ).aggregate(avg_response_time=Avg('response_time'))
    vendor.average_response_time = response_times['avg_response_time'].total_seconds() if response_times['avg_response_time'] else 0

    
    total_orders = PurchaseOrder.objects.filter(vendor=vendor).count()
    fulfilled_orders_count = completed_orders.filter(status='completed').count()
    fulfillment_rate = (fulfilled_orders_count / total_orders) * 100 if total_orders > 0 else 0
    vendor.fulfillment_rate = fulfillment_rate

    
    vendor.save()