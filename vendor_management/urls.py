from django.urls import path, include
from vendor_app.views import VendorListCreateView, VendorRetrieveUpdateDeleteView, PurchaseOrderListCreateView, PurchaseOrderRetrieveUpdateDeleteView

urlpatterns = [
    path('api/vendors/', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('api/vendors/<int:pk>/', VendorRetrieveUpdateDeleteView.as_view(), name='vendor-retrieve-update-delete'),
    path('api/purchase_orders/', PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('api/purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDeleteView.as_view(), name='purchase-order-retrieve-update-delete'),
    # Add other URLs as needed
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('vendor_management.urls')),
]


