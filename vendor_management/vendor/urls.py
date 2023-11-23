from django.urls import path
from . import views
from .views import VendorPerformanceView


urlpatterns = [
    path('new_vendor/', views.new_vendor, name="new_vendor"),
    path('get_vendor/<str:pk>/', views.get_vendor, name="get_vendor"),
    path('get_vendors/', views.get_vendors, name="get_vendors"),
    path('update_vendor/<str:pk>/', views.update_vendor, name="update_vendor"),
    path('create_order/', views.create_order, name="create_order"),
    path('get_orders/', views.get_orders, name="get_orders"),
    path('get_order/<str:pk>/', views.get_order, name="get_order"),
    path('update_order/<str:pk>/', views.update_order, name="update_order"),
    path('delete_order/<str:pk>/', views.delete_order, name="delete_order"),
    path('api/vendors/<int:vendor_id>/performance/', VendorPerformanceView.as_view(), name='vendor-performance'),
    ]