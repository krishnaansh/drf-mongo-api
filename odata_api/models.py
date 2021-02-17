from django.db import models
from mongoengine import *

# Create your models here.
Available_Size = ('S', 'M', 'L', 'XL', 'XXL')
Available_Color = ('WH','BL','GN')

class Products(Document):
    product_id = IntField(required=True)
    sku = StringField(max_length=200, required=True)
    idgku = StringField(max_length=200, required=True)
    vendor_product_id = IntField(required=True)
    product_name = StringField(max_length=200, required=True)
    product_description = StringField(max_length=200, required=True)
    # supplier_id = ReferenceField('Suppliers', reverse_delete_rule=CASCADE)
    category_id = IntField(required=True)
    quantity_per_unit = IntField(required=True)
    unit_price = FloatField(min_value=0,precision=5)
    msrp = StringField(max_length=200, required=True)
    available_size = StringField(max_length=3, choices=Available_Size)
    available_color = StringField(max_length=3, choices=Available_Color)
    size = StringField(max_length=200, required=True)
    color = StringField(max_length=200, required=True)
    discount = DecimalField()
    unit_weight = IntField(required=True)
    unit_in_stock = IntField(required=True)
    unit_or_order = IntField(required=True)
    reorder_level = StringField(max_length=200, required=True)
    product_availble = BooleanField(default=False)
    discount_availble = StringField(max_length=200, required=True)
    current_order = StringField(max_length=200, required=True)
    picture = ImageField()
    ranking = IntField(required=True)
    note = StringField(max_length=200, required=True)
    

class Customers(Document):
    customer_id = IntField(required=True)
    first_name = StringField(max_length=200, required=True)
    last_name = StringField(max_length=200, required=True)
    # class = StringField(max_length=200, required=True)
    room = StringField(max_length=200, required=True)
    building = StringField(max_length=200, required=True)
    address1 = StringField(max_length=200, required=True)
    address2 = StringField(max_length=200, required=True)
    city = StringField(max_length=200, required=True)
    state = StringField(max_length=200, required=True)
    postalcode = StringField(max_length=200, required=True)
    country = StringField(max_length=200, required=True)
    phone = StringField(max_length=10, required=True)
    email = EmailField(required=True)
    voice_mail = StringField(max_length=200, required=True)
    password = StringField(max_length=200, required=True)
    
    