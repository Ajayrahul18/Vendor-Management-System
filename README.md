# Vendor-management-system

Developed a Vendor Management System using Django and Django REST Framework. 
This system will handle vendor profiles, track purchase orders, and calculate vendor performance
  metrics.

  Models.py:
  Created 3 class for 
  1. VendorDetails
     It will handle the Details of a vendor.
  2. Order
     It will handle the Order details.
  3. Performance
     It will handle the calculate performance matrics

While Implementing the urls and views used POSTMAN to check the API.
  
  URLS.py:
  1. ('new_vendor/', views.new_vendor, name="new_vendor"),
     In this the new_vendor is an 'POST' request to create a new user in the Data base.
  
  2. ('get_vendor/<str:pk>', views.get_vendor, name="get_vendor"),
     In this get_vendor we can get the vendor using the primary key using a 'GET' API

  3. ('get_vendors/', views.get_vendors, name="get_vendors"),
     In this get_vendors it will list the vendors that are stored in the database using a 'GET' API

  4. ('update_vendor/<str:pk>/', views.pdate_vendor, name="pdate_vendor")
     In this update_vendor we will update the vendor field used the primary key to locate the particular vendor.

  5. ('create_order/', views.create_order, name="create_order")
     In this we can create order that will store in the Order model in this the "PUT" API is used

  6. ('get_orders/', views.get_orders, name="get_orders")
     In this we get the orders that has been placed totaly using the "GET" request
     
  8. ('get_order/<str:pk>/', views.get_order, name="get_order")
     In this we get the particular order with its primary key using the "GET" request
     
  10. ('update_order/<str:pk>/', views.update_order, name="update_order")
      In this we can update the order that that has been already placed we get the particular order by primary key using the "GET" request
      
  12. ('delete_order/<str:pk>/', views.delete_order, name="delete_order")
      In this we Deleted the particular order by indicating it with its primary key using the "DELETE" API

      **Till know i have used the @api_view() decorator to sepcify the API that we are passing for easy under standing and easy readability**
    
In The performance API i have created by following the official documentation to show that i have also that we can built API specifically and commonly 
her we have used  generics.RetrieveAPIView.

  13. ('vendors/<int:vendor_id>/performance/', VendorPerformanceView.as_view(), name='vendor-performance')
      1. This view is designed to retrieve and display the performance data of a vendor.

      2. "get_object method": This method is responsible for retrieving the specific vendor's performance data. It overrides the default 'get_object' method
       provided by "generics.RetrieveAPIView". It extracts the "vendor ID" from the URL using the lookup_url_kwarg, retrieves the corresponding vendor instance
       using generics.get_object_or_404, and then returns the performance data associated with that vendor.

      3. "retrieve method": This method is responsible for handling the HTTP "GET" request to retrieve and return the performance data for the specified vendor.
      It uses the get_object method to get the performance data, then serializes the data using the specified serializer (VendorPerformanceSerializer),
      and finally returns the serialized data in the HTTP respons.




