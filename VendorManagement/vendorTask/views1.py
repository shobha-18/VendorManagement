# from django.http import JsonResponse
# from rest_framework.parsers import JSONParser
# import pdb; pdb.set_trace()
# from django.db.models import F, FloatField, ExpressionWrapper
# from .models import VendorDetails,PurchaseOrder,VendorPerformance
# # def update_on_time_delivery_rate(request,vendor_code):
# #     completed_orders = PurchaseOrder.objects.filter(vendor_code=vendor_code, status='completed')
# #     on_time_orders = completed_orders.filter(delivery_date__gte=F('order_date'))
# #     return JsonResponse({'data': completed_orders})
# #     print(on_time_orders)
# #     if completed_orders.exists():
# #         vendor.on_time_delivery_rate = (on_time_orders.count() / completed_orders.count()) * 100
# #         vendor.save()
# #         return JsonResponse(vendor.on_time_delivery_rate)
# #     #return JsonResponse({'message': 'On-time delivery rate updated successfully.'})
# def update_on_time_delivery_rate(request, vendor_code):
#     completed_orders = PurchaseOrder.objects.filter(vendor_code=vendor_code, status='completed')
#     print(completed_orders)
#     on_time_orders = completed_orders.filter(delivery_date__gte=F('order_date'))
#     print(on_time_orders)

#     # Calculate the on-time delivery rate
#     if completed_orders.exists():
#         on_time_delivery_rate = (on_time_orders.count() / completed_orders.count()) * 1000
#         return JsonResponse({'on_time_delivery_rate': on_time_delivery_rate})
#     pdb.set_trace()

   ## else:
        #on_time_delivery_rate =   # Default value if no completed orders exist

    # Return the on-time delivery rate as JSON response
        #return JsonResponse({'on_time_delivery_rate': on_time_delivery_rate})

from django.http import JsonResponse
from rest_framework.parsers import JSONParser
import pdb
from django.db.models import F, FloatField, ExpressionWrapper
from .models import VendorDetails, PurchaseOrder, VendorPerformance

def update_on_time_delivery_rate(request, vendor_code):
    pdb.set_trace()  # Set a breakpoint at the start to inspect the request and vendor_code
    completed_orders = PurchaseOrder.objects.filter(vendor_code=vendor_code, status='completed')
    print(completed_orders)
    pdb.set_trace()  # Breakpoint to check the completed_orders queryset

    on_time_orders = completed_orders.filter(delivery_date__gte=F('order_date'))
    print(on_time_orders)
    pdb.set_trace()  # Breakpoint to check the on_time_orders queryset

    # Calculate the on-time delivery rate
    if completed_orders.exists():
        on_time_delivery_rate = (on_time_orders.count() / completed_orders.count())* 100
        pdb.set_trace()  # Breakpoint to inspect the calculated on_time_delivery_rate
        return JsonResponse({'on_time_delivery_rate': on_time_delivery_rate})

    return JsonResponse({'message': 'No completed orders found for this vendor.'})
def update_quality_rating_avg(request, vendor_code=0):
    quality_rated_orders = PurchaseOrder.objects.filter(vendor_code=vendor_code, quality_rating__isnull=False, status='completed')
    data= list(quality_rated_orders)
    return JsonResponse({'quality_rated_orders':data})
    #if quality_rated_orders.exists():
        #average_quality = quality_rated_orders.aggregate(models.Avg('quality_rating'))['quality_rating__avg']
        #vendor.quality_rating_avg = average_quality
        #vendor.save()

