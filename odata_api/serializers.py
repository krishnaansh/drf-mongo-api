from odata_api.models import Products, Customers
# from rest_framework import serializers
from rest_framework_mongoengine import serializers

class ProductsSerializers(serializers.DocumentSerializer):
    
    class Meta:
        model = Products
        fields = '__all__'