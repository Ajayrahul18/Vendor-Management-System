from rest_framework import serializers
from .models import *

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorDetals
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
       model = VendorDetals
       fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
       model = VendorDetals
       fields = '__all__'

class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = '__all__'
