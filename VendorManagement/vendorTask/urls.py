from django.urls import re_path,path
from . import views,views1  # Import views module

urlpatterns = [
    #re_path(r'^vendor$', views.vendordetailsAPI, name='vendordetailsAPI'),
    re_path(r'^purchaseOrder$',views.PurchaseOrderAPI,name='PurchaseOrderAPI'),
    re_path(r'^vendorPerformance$',views.VendorPerformanceAPI,name='VendorPerformanceAPI'),
    path('vendorPerformance/<int:id>/', views.VendorPerformanceAPI, name='VendorPerformanceAPI_detail'),
    path('purchaseOrder/<str:po_number>/',views.PurchaseAPI,name='PurchaseOrderAPI_details'),
    path('vendor/<int:id>/', views.vendordetailsAPI, name='vendordetailsAPI_details'),
    path('venor/',views.vendorAPI,name='vendordetailsAPI_detail'),
    path('delivery/<str:vendor_code>/',views1.update_on_time_delivery_rate, name='update_on_time_delivery_details'),
    path('deliverydata/',views1.update_quality_rating_avg,name='update_quality_rating_avg_details')
]
