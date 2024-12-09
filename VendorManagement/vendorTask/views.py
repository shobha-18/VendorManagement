from django.http import JsonResponse
from rest_framework.parsers import JSONParser
#from django.views.decorators.csrf import csrf_exempt
from .models import VendorDetails,PurchaseOrder,VendorPerformance
from .serializers import VendorDetailsSerializer,PurchaseOrderSerializer,VendorPerformanceSerializer
def vendorAPI(request):
    if request.method == 'GET':
        vendor_data1=VendorDetails.objects.all()
        vendor_serializers1 = VendorDetailsSerializer(vendor_data1,many=True)
        return JsonResponse(vendor_serializers1.data,safe=False)
    
    elif request.method == 'POST':
        vendor_data1 = JSONParser().parse(request)
        vendor_serializer = VendorDetailsSerializer(data=vendor_data1)
        if vendor_serializer.is_valid():
            vendor_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        else:
            # Handle the case where the serializer is not valid
            errors = vendor_serializer.errors
            return JsonResponse(errors, status=400)
def vendordetailsAPI(request, id=0):
    if request.method == 'GET':
        vendor_data=VendorDetails.objects.get(id="vendor_code")
        vendor_serializers = VendorDetailsSerializer(vendor_data,many=False)
        return JsonResponse(vendor_serializers.data,safe=False)
    elif request.method == 'PUT':
        vendor_data = JSONParser().parse(request)
        try:
            vendor_instance = VendorDetails.objects.get(id=id)
        except VendorDetails.DoesNotExist:
            return JsonResponse({"error": "Vendor not found"}, status=404)

    # Update the instance with the provided data
        vendor_serializer = VendorDetailsSerializer(vendor_instance, data=vendor_data)
        if vendor_serializer.is_valid():
           vendor_serializer.save()
           return JsonResponse("Updated successfully", safe=False)
        return JsonResponse(vendor_serializer.errors, status=400)

    elif request.method == 'DELETE':
        vendor_data = JSONParser().parse(request)
        try:
           vendor_test = VendorDetails.objects.get(id=id)
        except VendorDetails.DoesNotExist:
           return JsonResponse({"data1:page doesnot exist"}, status=404)
        vendor_test.delete()
        return JsonResponse({"data":"Delete success"}, safe=True)


def PurchaseOrderAPI(request):
    if request.method == 'GET':
        purchase_orders = PurchaseOrder.objects.all()
        purchase_orders_serializers = PurchaseOrderSerializer(purchase_orders, many=True)
        return JsonResponse(purchase_orders_serializers.data, safe=False)
    
    elif request.method == 'POST':
        purchase_order_data = JSONParser().parse(request)
        purchase_order_serializers = PurchaseOrderSerializer(data=purchase_order_data)
        if purchase_order_serializers.is_valid():
            purchase_order_serializers.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse(purchase_order_serializers.errors, status=400)
def PurchaseAPI(request, po_number=0):
    if request.method == 'GET':
      purchase_orders = PurchaseOrder.objects.filter(po_number=po_number).first()
      #data = {
            #'po_number': PurchaseOrder.po_number
      #}
      purchseorder_serializers = PurchaseOrderSerializer(purchase_orders, many=False)
      return JsonResponse(purchseorder_serializers.data, safe=False)

    elif request.method == "PUT":
       purchase_order_data = JSONParser().parse(request)
       try:
        # Accessing 'po_number' from purchase_order_data
          purchase_order = PurchaseOrder.objects.filter(po_number=po_number).first()
       except PurchaseOrder.DoesNotExist:
          return JsonResponse("Purchase order does not exist", status=404)
    
       purchase_order_serializer = PurchaseOrderSerializer(purchase_order, data=purchase_order_data)
       if purchase_order_serializer.is_valid():
          purchase_order_serializer.save()
          return JsonResponse("Updated successfully", safe=False)
       return JsonResponse(purchase_order_serializer.errors, status=400)

    
    elif request.method == "DELETE":
        try:
            purchase_order = PurchaseOrder.objects.get(id=id)
        except PurchaseOrder.DoesNotExist:
            return JsonResponse("Purchase order does not exist", status=404)
        
        purchase_order.delete()
        return JsonResponse("Deleted successfully", safe=False)

        
def VendorPerformanceAPI(request, id=0):
    if request.method == 'GET':
        # Retrieve all vendor performances
        vendorPerformances = VendorPerformance.objects.all()
        vendorPerformances_serializers = VendorPerformanceSerializer(vendorPerformances, many=True)
        return JsonResponse(vendorPerformances_serializers.data, safe=False)
    
    elif request.method == 'POST':
        # Create a new vendor performance entry
        vendorPerformance_data = JSONParser().parse(request)
        vendorPerformance_serializers = VendorPerformanceSerializer(data=vendorPerformance_data)
        if vendorPerformance_serializers.is_valid():
            vendorPerformance_serializers.save()
            return JsonResponse("Added successfully", safe=False, status=201)  # 201 Created
        return JsonResponse(vendorPerformance_serializers.errors, status=400)
    
    elif request.method == "PUT":
        # Update an existing vendor performance entry
        vendorPerformance_data = JSONParser().parse(request)
        try:
            vendorPerformance = VendorPerformance.objects.get(vendor_code=vendorPerformance_data['vendor_code'])
        except VendorPerformance.DoesNotExist:
            return JsonResponse("Vendor performance does not exist", status=404)
        
        vendorPerformance_serializers = VendorPerformanceSerializer(vendorPerformance, data=vendorPerformance_data)
        if vendorPerformance_serializers.is_valid():
            vendorPerformance_serializers.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse(vendorPerformance_serializers.errors, status=400)
    
    elif request.method == "DELETE":
        # Delete a vendor performance entry
        try:
            vendor_performance = VendorPerformance.objects.get(vendor_code=id)
        except VendorPerformance.DoesNotExist:
            return JsonResponse("Vendor performance does not exist", status=404)
        
        vendor_performance.delete()
        return JsonResponse("Deleted successfully", safe=False)
          
        




      