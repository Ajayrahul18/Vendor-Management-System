from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import generics



# Vendor Profile Management

@api_view(['POST'])
def new_vendor(request):
    data = request.data

    user = SignUpSerializer(data=data)
    
    if user.is_valid():
        user = VendorDetals.objects.create(**data)
        res = SignUpSerializer(user, many=False)
        return Response({'message': res.data}, status=status.HTTP_201_CREATED)
    else:
        return Response(user.errors)
    


@api_view(['GET'])
def get_vendor(request, pk):
    
    user = get_object_or_404(VendorDetals, id=pk)
    serializer = UserSerializer(user, many=False)

    return Response({"Vendors": serializer.data})

@api_view(['GET'])
def get_vendors(request):
    vendors = VendorDetals.objects.all()
    serializer = UserSerializer(vendors, many = True)

    return Response({"Vendors": serializer.data})


@api_view(['PUT'])
def update_vendor(request, pk):
    vendor = get_object_or_404(VendorDetals, id=pk)

    vendor.name = request.data['name']
    vendor.contact_detail = request.data['contact_detail']
    vendor.addres = request.data['addres']
    vendor.vendor_code = request.data['vendor_code']
    vendor.on_time_delivery_rate = request.data['on_time_delivery_rate']
    vendor.quality_rating_average = request.data['quality_rating_average']
    vendor.average_response_time = request.data['average_response_time']
    vendor.fulfillment_rate = request.data['fulfillment_rate']

    vendor.save()

    serializer = VendorDetals(vendor, many=False)
    return Response({'Vendor': serializer.data})

@api_view(['DELETE'])
def delete_vendor(request, pk):
    vendor = get_object_or_404(VendorDetals, id=pk)

    vendor.delete()

    return Response({'details': 'Vendor deleted'})


#Purchase Order Tracking
@api_view(['POST'])
def create_order(request):
    data = request.data
    order_items = data['orderItems']

    if order_items and len(order_items) == 0:
        return Response({'error': 'No Order Items'})
    else:
        
        order = Order.objects.create(
            po_number = data['po_number'],
            vendor = data['vendor'],
            order_date = data['order_date'],
            item = data['item'],
            quantity = data['quantity'],
            status = data['status'],
        )

    order.save()

    serializer = OrderSerializer(order, many=False)
    return Response({'order': serializer.data})

@api_view(['GET'])
def get_orders(request):
    order = Order.objects.all()
    serializer = OrderSerializer(order, many=True)

    return Response({'Orders': serializer.data})


@api_view(['GET'])
def get_order(request, pk):
    order = get_object_or_404(Order, id=pk)
    serializer = OrderSerializer(order, many=False)

    return Response({'order': serializer.data})

@api_view(['PUT'])
def update_order(request, pk):
    order = get_object_or_404(Order, id=pk)
    
    order.po_number = request.data['po_number'],
    order.vendor = request.data['vendor'],
    order.order_date = request.data['order_date'],
    order.delivery_date = request.data['delivery_date'],
    order.item = request.data['item'],
    order.quantity = request.data['quantity'],
    order.status = request.data['status'],
    order.quantity_rating = request.data['quantity_rating'],
    order.issue_date = request.data['issue_date'],
    order.acknowledgment_date = request.data['acknowledgment_date'],

    order.save()

    serializer = OrderSerializer(order, many=False)
    return Response({'order': serializer.data})

@api_view(['DELETE'])
def delete_order(request, pk):
    order = get_object_or_404(Order, id=pk)
    order.delete()
    return Response({'details': 'Order Deleted'})

#Performance Evaluation

class VendorPerformanceView(generics.RetrieveAPIView):
    queryset = Performance.objects.all()
    serializer_class = VendorPerformanceSerializer
    lookup_url_kwarg = 'vendor_id'

    def get_object(self):
        vendor_id = self.kwargs.get(self.lookup_url_kwarg)
        vendor = generics.get_object_or_404(VendorDetals, id=vendor_id)
        return vendor.performance

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)